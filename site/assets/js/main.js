/* Bitcoin FilmFest — shared navigation and progressive page transitions.
   Same-origin links swap only the cinema screen; logo, menu, footer, bezel,
   and seats stay mounted. Full page navigation remains the fallback. */

(function () {
  'use strict';

  var nav = document.querySelector('[data-site-nav]');
  var navToggle = document.querySelector('[data-nav-toggle]');
  var navMenu = document.querySelector('[data-nav-menu]');
  var routeStatus = document.getElementById('route-status');
  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var navigating = false;

  function normalizePath(value) {
    var url = value instanceof URL ? value : new URL(value, window.location.href);
    var path = url.pathname.replace(/\/index\.html$/, '/');
    if (path !== '/' && !/\.[a-z0-9]+$/i.test(path) && !path.endsWith('/')) path += '/';
    return path;
  }

  function closeNavigation(options) {
    options = options || {};
    if (nav) nav.classList.remove('is-open');
    if (navToggle) navToggle.setAttribute('aria-expanded', 'false');
    document.querySelectorAll('[data-nav-group][open]').forEach(function (group) {
      group.removeAttribute('open');
    });
    if (options.restoreFocus && navToggle) navToggle.focus();
  }

  function setActiveNavigation(pathname) {
    var path = normalizePath(new URL(pathname, window.location.origin));
    var groupIsActive = {};

    document.querySelectorAll('[data-route]').forEach(function (link) {
      var route = normalizePath(new URL(link.getAttribute('data-route'), window.location.origin));
      var active = route === '/' ? path === '/' : path.indexOf(route) === 0;
      link.classList.toggle('active', active);
      if (active) {
        link.setAttribute('aria-current', 'page');
        var group = link.closest('[data-nav-group]');
        if (group) groupIsActive[group.getAttribute('data-nav-group')] = true;
      } else {
        link.removeAttribute('aria-current');
      }
    });

    document.querySelectorAll('[data-nav-group]').forEach(function (group) {
      var key = group.getAttribute('data-nav-group');
      var active = Boolean(groupIsActive[key]);
      var summary = group.querySelector('summary');
      group.classList.toggle('active', active);
      if (summary) {
        if (active) summary.setAttribute('aria-current', 'page');
        else summary.removeAttribute('aria-current');
      }
    });
  }

  function syncHead(nextDocument) {
    document.title = nextDocument.title;
    ['meta[name="description"]', 'meta[name="theme-color"]', 'link[rel="canonical"]'].forEach(function (selector) {
      var current = document.head.querySelector(selector);
      var next = nextDocument.head.querySelector(selector);
      if (!next) return;
      if (current) current.replaceWith(next.cloneNode(true));
      else document.head.appendChild(next.cloneNode(true));
    });
  }

  function syncCurrentLabel(nextDocument) {
    var label = document.querySelector('[data-nav-current-label]');
    var nextLabel = nextDocument.querySelector('[data-nav-current-label]');
    if (label && nextLabel) label.textContent = nextLabel.textContent;
  }

  function announceRoute(title) {
    if (!routeStatus) return;
    routeStatus.textContent = '';
    window.requestAnimationFrame(function () {
      routeStatus.textContent = title + ' loaded.';
    });
  }

  function focusMain(main) {
    if (!main) return;
    try {
      main.focus({ preventScroll: true });
    } catch (error) {
      main.focus();
    }
  }

  function shouldHandleLink(event, link) {
    if (!link || event.defaultPrevented || event.button !== 0) return false;
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return false;
    if (link.hasAttribute('download') || link.target) return false;

    var href = link.getAttribute('href');
    if (!href || href.charAt(0) === '#' || /^(mailto:|tel:|javascript:)/i.test(href)) return false;

    var url = new URL(link.href, window.location.href);
    if (url.origin !== window.location.origin) return false;
    if (url.pathname === window.location.pathname && url.search === window.location.search && url.hash) return false;
    return true;
  }

  async function navigate(url, options) {
    options = options || {};
    if (navigating) return;
    navigating = true;
    document.body.classList.add('is-navigating');
    closeNavigation();

    try {
      var response = await fetch(url.href, {
        headers: {
          'Accept': 'text/html',
          'X-Requested-With': 'BitcoinFilmFestTransition'
        }
      });
      if (!response.ok) throw new Error('Navigation returned ' + response.status);

      var markup = await response.text();
      var nextDocument = new DOMParser().parseFromString(markup, 'text/html');
      var nextMain = nextDocument.querySelector('[data-page-main]');
      if (!nextMain) throw new Error('Page screen missing');

      var applyPage = function () {
        var currentMain = document.querySelector('[data-page-main]');
        if (!currentMain) throw new Error('Current page screen missing');
        currentMain.replaceWith(nextMain);
        syncHead(nextDocument);
        syncCurrentLabel(nextDocument);
        document.body.setAttribute('data-current-route', normalizePath(url));
        setActiveNavigation(url.pathname);
        window.scrollTo({ top: 0, left: 0, behavior: 'auto' });
        focusMain(nextMain);
        document.dispatchEvent(new CustomEvent('bff:pagechange'));
      };

      if (document.startViewTransition && !prefersReduced.matches) {
        var transition = document.startViewTransition(applyPage);
        await transition.finished;
      } else {
        applyPage();
      }

      if (options.push !== false) history.pushState({ bff: true }, '', url.href);
      announceRoute(nextDocument.title);
    } catch (error) {
      window.location.assign(url.href);
      return;
    } finally {
      navigating = false;
      document.body.classList.remove('is-navigating');
    }
  }

  if (navToggle && nav) {
    navToggle.addEventListener('click', function () {
      var open = !nav.classList.contains('is-open');
      nav.classList.toggle('is-open', open);
      navToggle.setAttribute('aria-expanded', String(open));
    });
  }

  document.addEventListener('click', function (event) {
    var link = event.target.closest('a[href]');
    if (shouldHandleLink(event, link)) {
      event.preventDefault();
      navigate(new URL(link.href, window.location.href), { push: true });
      return;
    }

    if (nav && nav.classList.contains('is-open') && !event.target.closest('[data-site-nav]')) {
      closeNavigation();
    }
  });

  document.addEventListener('keydown', function (event) {
    if (event.key !== 'Escape') return;
    var hadOpenMenu = nav && nav.classList.contains('is-open');
    closeNavigation({ restoreFocus: hadOpenMenu });
  });

  window.addEventListener('popstate', function () {
    navigate(new URL(window.location.href), { push: false });
  });

  setActiveNavigation(window.location.pathname);
})();

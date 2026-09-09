/* Bitcoin FilmFest — end-credits auto-scroll.
   On the Credits page the roll moves steadily from the opening title through
   the full list like a film's closing credits. Any user scroll, wheel, touch,
   or keyboard input pauses it permanently for that visit — it never fights
   the reader. Respects prefers-reduced-motion and re-arms after soft navigation. */

(function () {
  'use strict';

  var prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  var playing = false;
  var rafId = null;
  var stopHandlersBound = false;
  var speedPxPerSec = 26;
  var lastTimestamp = null;
  var startDelayMs = 900;
  var pendingTimeout = null;

  function stop(roll) {
    playing = false;
    if (roll) roll.classList.remove('is-autoplaying');
    if (rafId) cancelAnimationFrame(rafId);
    rafId = null;
    if (stopHandlersBound) {
      ['wheel', 'touchstart', 'keydown', 'pointerdown'].forEach(function (type) {
        window.removeEventListener(type, stopFromEvent);
      });
      stopHandlersBound = false;
    }
  }

  function stopFromEvent() {
    stop(document.querySelector('[data-credits-roll]'));
  }

  function tick(roll, timestamp) {
    if (!playing) return;
    if (lastTimestamp === null) lastTimestamp = timestamp;
    var deltaSeconds = (timestamp - lastTimestamp) / 1000;
    lastTimestamp = timestamp;

    var scrollRoot = document.scrollingElement || document.documentElement;
    var atBottom = Math.ceil(window.scrollY + window.innerHeight) >= scrollRoot.scrollHeight - 4;
    if (atBottom) {
      stop(roll);
      return;
    }

    window.scrollBy(0, speedPxPerSec * deltaSeconds);
    rafId = requestAnimationFrame(function (nextTimestamp) {
      tick(roll, nextTimestamp);
    });
  }

  function start(roll) {
    if (playing) return;

    // Always begin the credits from the top, including after browser scroll restoration.
    window.scrollTo(0, 0);
    playing = true;
    roll.classList.add('is-autoplaying');
    lastTimestamp = null;
    rafId = requestAnimationFrame(function (timestamp) {
      tick(roll, timestamp);
    });
    stopHandlersBound = true;
    ['wheel', 'touchstart', 'keydown', 'pointerdown'].forEach(function (type) {
      window.addEventListener(type, stopFromEvent, { passive: true, once: true });
    });
  }

  function arm() {
    stop(document.querySelector('[data-credits-roll]'));
    if (pendingTimeout) window.clearTimeout(pendingTimeout);
    var roll = document.querySelector('[data-credits-roll]');
    if (!roll || prefersReduced.matches) return;
    pendingTimeout = window.setTimeout(function () {
      start(roll);
    }, startDelayMs);
  }

  document.addEventListener('bff:pagechange', arm);
  arm();
})();

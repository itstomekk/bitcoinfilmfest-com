/* Lightweight catalogue controls for the single-page Cinema hub. */
(function () {
  'use strict';

  var browser = document.querySelector('[data-cinema-browser]');
  if (!browser) return;

  var items = Array.prototype.slice.call(browser.querySelectorAll('[data-cinema-item]'));
  var search = browser.querySelector('[data-cinema-search]');
  var empty = browser.querySelector('[data-cinema-empty]');
  var count = browser.querySelector('[data-cinema-count]');
  var activeFilter = 'all';

  function update() {
    var query = (search.value || '').trim().toLowerCase();
    var visible = 0;

    items.forEach(function (item) {
      var matchesFilter = activeFilter === 'all'
        || item.dataset.kind === activeFilter
        || item.dataset.status === activeFilter;
      var matchesSearch = !query || item.dataset.search.toLowerCase().indexOf(query) !== -1;
      var show = matchesFilter && matchesSearch;
      item.hidden = !show;
      if (show) visible += 1;
    });

    if (count) count.textContent = visible + (visible === 1 ? ' title' : ' titles');
    if (empty) empty.hidden = visible !== 0;
  }

  browser.querySelectorAll('[data-cinema-filter]').forEach(function (button) {
    button.addEventListener('click', function () {
      activeFilter = button.dataset.cinemaFilter;
      browser.querySelectorAll('[data-cinema-filter]').forEach(function (peer) {
        peer.classList.toggle('is-active', peer === button);
      });
      update();
    });
  });

  if (search) search.addEventListener('input', update);
  update();
}());

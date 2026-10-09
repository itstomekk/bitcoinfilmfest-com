(function () {
  var note = document.querySelector('[data-redirect-home]');
  if (!note) return;
  var target = note.getAttribute('data-redirect-home') || '/';
  var left = parseInt(note.getAttribute('data-redirect-seconds'), 10) || 8;
  var count = note.querySelector('[data-redirect-count]');
  var timer = setInterval(function () {
    left -= 1;
    if (count) count.textContent = String(Math.max(left, 0));
    if (left <= 0) {
      clearInterval(timer);
      window.location.replace(target);
    }
  }, 1000);
})();

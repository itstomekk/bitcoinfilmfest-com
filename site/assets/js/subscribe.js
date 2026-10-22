/* Bitcoin FilmFest — FormSubmit subscription form
   AJAX keeps visitors on the BFF site. FormSubmit still forwards each
   submission to mails@bitcoinfilmfest.com after the form is activated once.
*/

(function () {
  document.querySelectorAll('form[data-subscribe]').forEach(function (form) {
    form.addEventListener('submit', function (event) {
      event.preventDefault();

      var button = form.querySelector('button[type="submit"]');
      var status = form.querySelector('[data-subscribe-status]');
      var originalLabel = button ? button.textContent : 'Subscribe';

      if (button) {
        button.disabled = true;
        button.textContent = 'Sending…';
      }
      if (status) status.textContent = 'Sending…';

      var blocklist = form.querySelector('input[name="_blacklist"]');
      var contact = form.querySelector('[name="contact"]');
      var next = form.querySelector('input[name="_next"]');
      if (blocklist && contact) {
        var value = contact.value.toLowerCase();
        var blocked = blocklist.value.split(',').some(function (phrase) {
          phrase = phrase.trim().toLowerCase();
          return phrase && value.indexOf(phrase) !== -1;
        });
        if (blocked) {
          if (next && next.value) window.location.href = next.value;
          return;
        }
      }

      fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      })
        .then(function (response) {
          return response.json().then(function (data) {
            if (!response.ok || data.success === false) {
              throw new Error(data.message || 'The form could not be sent.');
            }
            return data;
          });
        })
        .then(function () {
          if (next && next.value) window.location.href = next.value;
        })
        .catch(function (error) {
          if (button) {
            button.disabled = false;
            button.textContent = originalLabel;
          }
          if (status) {
            status.textContent = error.message || 'The form could not be sent. Please try again.';
          }
        });
    });
  });
})();

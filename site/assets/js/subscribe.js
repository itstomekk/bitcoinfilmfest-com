/* Bitcoin FilmFest — subscribe form (Nostr DM)
   Carried over from the /newpage/ build (2026-08): visitor enters an
   email OR npub; we don't have a live NIP-04 signer in a static site, so
   this version collects the value and gives the visitor a direct path —
   either a mailto: fallback or a copy-to-clipboard "DM me at <npub>"
   flow. Swap for a real backend / Mailchimp / DB later per Tomek's plan
   (keep Nostr DM concept now, revisit persistence later).

   Usage: <form data-subscribe>
            <input type="text" name="contact" placeholder="your e-mail or npub">
            <button type="submit">Subscribe</button>
          </form>
*/

(function () {
  var SITE_NPUB = document.body.getAttribute('data-nostr-npub');

  document.querySelectorAll('form[data-subscribe]').forEach(function (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var input = form.querySelector('input[name="contact"]');
      var value = (input && input.value || '').trim();
      var status = form.querySelector('[data-subscribe-status]');

      if (!value) {
        if (status) status.textContent = 'Enter your e-mail or npub first.';
        return;
      }

      var isNpub = value.toLowerCase().startsWith('npub1');
      var msg;

      if (isNpub) {
        msg = 'Thanks — follow/DM us and we’ll DM you back with updates.';
      } else {
        // Email path: mailto fallback until a real subscribe backend is wired up.
        var subject = encodeURIComponent('Bitcoin FilmFest — subscribe');
        var body = encodeURIComponent('Please add me to the BFF list: ' + value);
        window.location.href = 'mailto:hello@bitcoinfilmfest.com?subject=' + subject + '&body=' + body;
        msg = 'Opening your e-mail client to confirm...';
      }

      if (status) status.textContent = msg;
      form.reset();
    });
  });
})();

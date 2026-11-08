/* Bitcoin FilmFest — BFF'27 Lightning checkout
   Buying happens on this page: the visitor gets a Lightning invoice QR, pays, and the
   ticket QR appears here. Orders and tickets live in the bff-tickets Worker
   (projects/websites/bff-tickets/worker). Inactive unless a [data-bff27-buy] button
   carries data-api (set by site.bff27_tickets_api in _config.yml).
   All text from the API is written with textContent, never innerHTML.
*/

(function () {
  var buttons = Array.prototype.slice.call(document.querySelectorAll('[data-bff27-buy][data-api]'));
  if (!buttons.length) return;
  var api = buttons[0].getAttribute('data-api').replace(/\/$/, '');
  var type = null;
  var dialog = null;
  var pollTimer = null;

  function el(tag, attrs, children) {
    var node = document.createElement(tag);
    Object.keys(attrs || {}).forEach(function (key) {
      if (key === 'text') node.textContent = attrs[key];
      else node.setAttribute(key, attrs[key]);
    });
    (children || []).forEach(function (child) { if (child) node.appendChild(child); });
    return node;
  }
  function sats(n) { return Number(n).toLocaleString('en-US') + ' sats'; }
  function remember(url) {
    try {
      var list = JSON.parse(localStorage.getItem('bff27-tickets') || '[]');
      if (list.indexOf(url) === -1) list.push(url);
      localStorage.setItem('bff27-tickets', JSON.stringify(list.slice(-10)));
    } catch (e) {}
  }

  function setButtons(label, enabled) {
    buttons.forEach(function (b) {
      // A button may keep its own label when selling (data-label), e.g. the stub,
      // which already shows the price above it.
      b.textContent = enabled && b.dataset.label ? b.dataset.label : label;
      b.disabled = !enabled;
      b.classList.toggle('bff27-btn--soon', !enabled);
    });
  }

  fetch(api + '/api/types').then(function (r) { return r.json(); }).then(function (data) {
    type = (data.types || [])[0] || null;
    if (!type) { setButtons('Tickets coming soon', false); return; }
    if (!type.onSale) { setButtons(type.remaining === 0 ? 'Sold out' : 'Sales closed', false); return; }
    type.lightningAddress = data.lightningAddress;
    type.zaps = data.zaps;
    setButtons('Buy · ' + sats(type.priceSats), true);
  }).catch(function () { setButtons('Tickets coming soon', false); });

  function body() { return dialog.querySelector('.bff27-checkout-body'); }
  function show(nodes) {
    var b = body();
    while (b.firstChild) b.removeChild(b.firstChild);
    nodes.forEach(function (n) { if (n) b.appendChild(n); });
  }
  function close() {
    clearTimeout(pollTimer);
    if (dialog.open) dialog.close();
  }

  function openDialog() {
    if (!type) return;
    if (!dialog) {
      dialog = el('dialog', { 'class': 'bff27-checkout', 'aria-labelledby': 'bff27-checkout-title' }, [
        el('button', { type: 'button', 'class': 'bff27-checkout-close', 'aria-label': 'Close', text: '×' }),
        el('p', { 'class': 'bff27-section-label', text: 'BFF’27 · tickets' }),
        el('h2', { id: 'bff27-checkout-title', text: type.name }),
        el('div', { 'class': 'bff27-checkout-body', 'aria-live': 'polite' })
      ]);
      dialog.querySelector('.bff27-checkout-close').addEventListener('click', close);
      dialog.addEventListener('cancel', function () { clearTimeout(pollTimer); });
      document.body.appendChild(dialog);
    }
    showForm();
    dialog.showModal();
  }

  function showForm(error) {
    var qty = el('select', { name: 'qty', id: 'bff27-qty' }, [1, 2, 3, 4].map(function (n) {
      return el('option', { value: String(n), text: n + (n === 1 ? ' ticket' : ' tickets') + ' · ' + sats(n * type.priceSats) });
    }));
    var contact = el('input', { name: 'email', id: 'bff27-contact', type: 'email', required: 'required', autocomplete: 'email',
      inputmode: 'email', placeholder: 'you@example.com', maxlength: '254' });
    var npub = el('input', { name: 'npub', id: 'bff27-npub', type: 'text', autocomplete: 'off', spellcheck: 'false',
      placeholder: 'npub1…', maxlength: '80' });
    var submit = el('button', { type: 'submit', 'class': 'bff27-btn', text: 'Get Lightning invoice' });
    var form = el('form', { 'class': 'bff27-checkout-form' }, [
      el('label', { 'for': 'bff27-qty', text: 'How many' }), qty,
      el('label', { 'for': 'bff27-contact', text: 'E-mail' }), contact,
      el('label', { 'for': 'bff27-npub', text: 'npub (optional)' }), npub,
      el('p', { 'class': 'bff27-checkout-note', text: 'We use your e-mail only for your ticket and the festival. With an npub you also get the ticket as a Nostr DM.' }),
      error ? el('p', { 'class': 'bff27-checkout-error', role: 'alert', text: error }) : null,
      submit
    ]);
    form.addEventListener('submit', function (event) {
      event.preventDefault();
      var payload = { type: type.id, qty: Number(qty.value), email: contact.value.trim() };
      if (npub.value.trim()) payload.npub = npub.value.trim();
      submit.disabled = true;
      submit.textContent = 'Creating invoice…';
      fetch(api + '/api/orders', { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(payload) })
        .then(function (r) { return r.json(); })
        .then(function (order) { if (order.ok) showInvoice(order); else showForm(order.error || 'Something went wrong. Try again.'); })
        .catch(function () { showForm('Network error. Try again.'); });
    });
    var zap = type.zaps && type.lightningAddress
      ? el('p', { 'class': 'bff27-checkout-note', text: 'On Nostr? Zap ' + sats(type.priceSats) + ' per ticket to ' + type.lightningAddress + ' with your e-mail in the zap note.' })
      : null;
    show([form, zap]);
    contact.focus();
  }

  function showInvoice(order) {
    var copy = el('button', { type: 'button', 'class': 'bff27-btn bff27-btn--ghost', text: 'Copy invoice' });
    copy.addEventListener('click', function () {
      navigator.clipboard.writeText(order.paymentRequest).then(function () { copy.textContent = 'Copied'; });
    });
    var status = el('p', { 'class': 'bff27-checkout-status', text: 'Waiting for payment…' });
    show([
      el('p', { text: sats(order.amountSats) + ' · scan with any Lightning wallet.' }),
      el('img', { 'class': 'bff27-checkout-qr', src: order.invoiceQr, alt: 'Lightning invoice QR code', width: '260', height: '260' }),
      el('div', { 'class': 'bff27-checkout-actions' }, [
        el('a', { 'class': 'bff27-btn', href: 'lightning:' + order.paymentRequest, text: 'Open in wallet' }),
        copy
      ]),
      status,
      el('p', { 'class': 'bff27-checkout-note', text: 'The invoice is valid for 15 minutes. Keep this window open.' })
    ]);
    remember(order.ticketUrl);
    poll(order, status);
  }

  function poll(order, status) {
    clearTimeout(pollTimer);
    pollTimer = setTimeout(function () {
      fetch(api + '/api/orders/' + order.orderId).then(function (r) { return r.json(); }).then(function (o) {
        if (o.status === 'paid') showTickets(o);
        else if (o.status === 'expired') showForm('That invoice expired. Nothing was charged.');
        else poll(order, status);
      }).catch(function () { status.textContent = 'Checking…'; poll(order, status); });
    }, 2500);
  }

  function showTickets(order) {
    var nodes = [el('p', { 'class': 'bff27-checkout-status', text: 'Paid. See you in Warsaw.' })];
    order.tickets.forEach(function (t, i) {
      nodes.push(el('figure', { 'class': 'bff27-checkout-ticket' }, [
        el('img', { 'class': 'bff27-checkout-qr', src: t.qr, alt: 'Ticket QR code ' + (i + 1), width: '220', height: '220' }),
        el('figcaption', { text: 'Admit one · ' + (i + 1) + ' of ' + order.tickets.length })
      ]));
    });
    nodes.push(el('a', { 'class': 'bff27-btn', href: order.ticketUrl, target: '_blank', rel: 'noopener', text: 'Save your ticket page' }));
    nodes.push(el('p', { 'class': 'bff27-checkout-note', text: 'Bookmark that page and show the QR code at the door. Keep the link private.' }));
    show(nodes);
  }

  buttons.forEach(function (b) { b.addEventListener('click', openDialog); });
})();

/* Product routing and submission to the same-origin enquiry mail handler. */
(() => {
  const page = document.querySelector('.contact-page');
  if (!page) return;
  const select = page.querySelector('#product');
  const cards = Array.from(page.querySelectorAll('[data-contact-product]'));
  const company = page.querySelector('[data-contact-company]');
  const scope = page.querySelector('[data-contact-scope]');
  const form = page.querySelector('[data-contact-form]');
  const status = page.querySelector('[data-contact-status]');
  const send = page.querySelector('[data-contact-send]');
  if (!select || !cards.length || !company || !scope || !form || !status || !send) return;
  const products = new Map(cards.map(card => [card.dataset.contactProduct, card.dataset.company]));

  const choose = (product) => {
    if (!products.has(product)) return;
    select.value = product;
    cards.forEach(card => card.setAttribute('aria-pressed', String(card.dataset.contactProduct === product)));
    company.textContent = products.get(product);
    scope.textContent = product;
    status.textContent = '';
  };
  cards.forEach(card => card.addEventListener('click', () => choose(card.dataset.contactProduct)));
  select.addEventListener('change', () => choose(select.value));
  // Preserve incoming product links from Home and other pages, including file:// use.
  const requested = new URLSearchParams(window.location.search).get('product');
  choose(products.has(requested) ? requested : (products.has(select.value) ? select.value : cards[0].dataset.contactProduct));
  let submitting = false;
  form.addEventListener('submit', async event => {
    event.preventDefault();
    if (submitting || !form.reportValidity()) return;
    submitting = true;
    send.disabled = true;
    form.setAttribute('aria-busy', 'true');
    status.textContent = 'Sending your enquiry…';
    try {
      const response = await fetch(form.action, {
        method: 'POST',
        body: new FormData(form),
        headers: { Accept: 'application/json' }
      });
      const result = await response.json();
      if (!response.ok || result.success !== true) {
        throw new Error(result.message || 'Unable to send. Please try again or email jackie.jo@mdhichina.com.');
      }
      form.reset();
      choose(select.value);
      status.textContent = result.message;
    } catch (error) {
      status.textContent = error instanceof SyntaxError || error instanceof TypeError
        ? 'Unable to send online. Please email jackie.jo@mdhichina.com or try again later.'
        : error.message;
    } finally {
      submitting = false;
      send.disabled = false;
      form.removeAttribute('aria-busy');
    }
  });
  send.disabled = false;
})();

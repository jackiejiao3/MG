/* Local-only product routing. No network requests or data storage. */
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
  form.addEventListener('submit', event => {
    event.preventDefault();
    status.textContent = 'Your enquiry has not been sent. Online submission is not connected yet.';
  });
  send.disabled = false;
})();

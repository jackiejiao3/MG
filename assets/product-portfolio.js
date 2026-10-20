(() => {
  const links = [...document.querySelectorAll('.pp-product-nav a')];
  const sections = [...document.querySelectorAll('.pp-product')];
  if (!links.length || !('IntersectionObserver' in window)) return;
  const setCurrent = (id) => links.forEach((link) => {
    const current = link.hash === `#${id}`;
    link.classList.toggle('is-current', current);
    if (current) link.setAttribute('aria-current', 'location');
    else link.removeAttribute('aria-current');
  });
  const observer = new IntersectionObserver((entries) => {
    const visible = entries.filter((entry) => entry.isIntersecting)
      .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
    if (visible.length) setCurrent(visible[0].target.id);
  }, { rootMargin: '-20% 0px -50% 0px', threshold: 0 });
  sections.forEach((section) => observer.observe(section));
})();

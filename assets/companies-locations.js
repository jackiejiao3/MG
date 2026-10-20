document.querySelectorAll('[data-company-location]').forEach(link => {
  link.addEventListener('click', () => {
    const map = document.querySelector('[data-interactive-map]');
    const button = map?.querySelector('[data-map-select="' + link.dataset.companyLocation + '"]');
    button?.click();
  });
});

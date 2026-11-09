document.querySelectorAll('[data-company-location]').forEach(link => {
  link.addEventListener('click', () => {
    const map = document.querySelector('[data-interactive-map]');
    const button = map?.querySelector('[data-map-select="' + link.dataset.companyLocation + '"]');
    const directory = map?.querySelector('.map-directory-disclosure');
    if (directory) directory.open = true;
    button?.click();
  });
});

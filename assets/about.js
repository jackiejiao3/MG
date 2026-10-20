(() => {
  const root = document.querySelector('.about-page');
  if (!root) return;

  const history = {
    2010: {
      title: 'MDHI founded',
      copy: 'Modern Heavy Industries (Taicang) Co., Ltd. was founded and began delivering structural steel and industrial fabrication projects to international customers, establishing the quality and delivery discipline that underpins the network.'
    },
    2017: {
      title: 'MMEC founded',
      copy: 'Modern Modular Engineering & Construction Co., Ltd. is founded and the port-adjacent modular yard is built out, adding integrated-module capability to the network.'
    },
    2025: {
      title: 'MEEM manufacturing facility opens',
      copy: 'Modern Energy Equipment Manufacturing Co., Ltd. opens a dedicated plant for HRSG pressure parts and air-cooled heat exchangers, completing the current four-product-line network.'
    }
  };

  const buttons = [...root.querySelectorAll('[data-history]')];
  const title = root.querySelector('[data-history-title]');
  const copy = root.querySelector('[data-history-copy]');
  if (!buttons.length || !title || !copy) return;

  const selectYear = (button) => {
    const item = history[button.dataset.history];
    if (!item) return;

    buttons.forEach((candidate) => {
      const selected = candidate === button;
      candidate.classList.toggle('is-active', selected);
      candidate.setAttribute('aria-selected', String(selected));
    });
    title.textContent = item.title;
    copy.textContent = item.copy;
  };

  buttons.forEach((button, index) => {
    button.addEventListener('click', () => selectYear(button));
    button.addEventListener('keydown', (event) => {
      if (!['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'Home', 'End'].includes(event.key)) return;
      event.preventDefault();
      let nextIndex = index;
      if (event.key === 'ArrowLeft' || event.key === 'ArrowUp') nextIndex = (index - 1 + buttons.length) % buttons.length;
      if (event.key === 'ArrowRight' || event.key === 'ArrowDown') nextIndex = (index + 1) % buttons.length;
      if (event.key === 'Home') nextIndex = 0;
      if (event.key === 'End') nextIndex = buttons.length - 1;
      buttons[nextIndex].focus();
      selectYear(buttons[nextIndex]);
    });
  });
})();

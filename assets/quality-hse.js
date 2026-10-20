(() => {
  const stepButtons = [...document.querySelectorAll('[data-qh-step]')];
  const panels = [...document.querySelectorAll('[data-qh-panel]')];
  const tablist = document.querySelector('.qh-process-navigation');
  if (tablist && stepButtons.length && panels.length) {
    tablist.setAttribute('role', 'tablist');
    tablist.setAttribute('aria-orientation', matchMedia('(max-width:760px)').matches ? 'horizontal' : 'vertical');
    const selectStep = (button, moveFocus = false) => {
      stepButtons.forEach((item) => {
        const active = item === button;
        item.setAttribute('role', 'tab');
        item.setAttribute('aria-selected', String(active));
        item.tabIndex = active ? 0 : -1;
      });
      panels.forEach((panel) => {
        panel.setAttribute('role', 'tabpanel');
        panel.tabIndex = 0;
        panel.hidden = panel.dataset.qhPanel !== button.dataset.qhStep;
      });
      if (moveFocus) button.focus();
    };
    selectStep(stepButtons[0]);
    stepButtons.forEach((button, index) => {
      button.addEventListener('click', () => selectStep(button));
      button.addEventListener('keydown', (event) => {
        let next;
        if (['ArrowRight','ArrowDown'].includes(event.key)) next = (index + 1) % stepButtons.length;
        if (['ArrowLeft','ArrowUp'].includes(event.key)) next = (index - 1 + stepButtons.length) % stepButtons.length;
        if (event.key === 'Home') next = 0;
        if (event.key === 'End') next = stepButtons.length - 1;
        if (next !== undefined) { event.preventDefault(); selectStep(stepButtons[next], true); }
      });
    });
    matchMedia('(max-width:760px)').addEventListener('change', (event) => tablist.setAttribute('aria-orientation', event.matches ? 'horizontal' : 'vertical'));
  }
})();

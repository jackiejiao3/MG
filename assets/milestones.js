(() => {
  const root = document.querySelector('[data-milestone-ruler]');
  if (!root) return;
  const track = root.querySelector('.mr-track');
  const scroller = root.querySelector('.mr-track-scroll');
  const tabs = [...root.querySelectorAll('[data-milestone-index]')];
  const panels = [...root.querySelectorAll('.mr-panel')];
  const previous = root.querySelector('[data-milestone-prev]');
  const next = root.querySelector('[data-milestone-next]');
  const close = root.querySelector('.mr-popup-close');
  let current = tabs.length - 1;
  let isOpen = false;
  const hashIndex = panels.findIndex(panel => '#' + panel.id === location.hash);
  if (hashIndex >= 0) current = hashIndex;
  track.setAttribute('role', 'tablist');
  function position() {
    if (!isOpen) return;
    const bounds = root.getBoundingClientRect();
    const tab = tabs[current].getBoundingClientRect();
    const width = Math.min(350, bounds.width - 40);
    const left = Math.max(20, Math.min(bounds.width - width - 20, tab.left - bounds.left + tab.width / 2 - width / 2));
    root.style.setProperty('--milestone-popup-left', left + 'px');
    root.style.setProperty('--milestone-popup-top', (tab.top - bounds.top + 184) + 'px');
  }
  function select(index, open = true) {
    current = index;
    isOpen = open;
    root.style.setProperty('--milestone-progress', String(index / Math.max(1, tabs.length - 1)));
    root.classList.toggle('mr-pop-open', open);
    tabs.forEach((tab, i) => {
      tab.setAttribute('aria-selected', String(i === index));
      tab.tabIndex = i === index ? 0 : -1;
      panels[i].hidden = i !== index || !open;
    });
    previous.disabled = index === 0;
    next.disabled = index === tabs.length - 1;
    close.hidden = !open;
    scroller.scrollLeft = Math.max(0, tabs[index].offsetLeft - scroller.clientWidth / 2 + tabs[index].offsetWidth / 2);
    position();
  }
  function dismiss(focus = false) {
    isOpen = false;
    root.classList.remove('mr-pop-open');
    panels.forEach(panel => { panel.hidden = true; });
    close.hidden = true;
    if (focus) tabs[current].focus();
  }
  tabs.forEach((tab, index) => {
    tab.setAttribute('role', 'tab');
    tab.setAttribute('aria-controls', panels[index].id);
    panels[index].setAttribute('role', 'tabpanel');
    tab.addEventListener('click', event => {
      event.preventDefault();
      if (isOpen && current === index) dismiss();
      else select(index);
    });
    tab.addEventListener('keydown', event => {
      let target;
      if (event.key === 'ArrowLeft') target = Math.max(0, index - 1);
      if (event.key === 'ArrowRight') target = Math.min(tabs.length - 1, index + 1);
      if (event.key === 'Home') target = 0;
      if (event.key === 'End') target = tabs.length - 1;
      if (target !== undefined) { event.preventDefault(); select(target); tabs[target].focus(); }
    });
  });
  previous.addEventListener('click', () => select(Math.max(0, current - 1)));
  next.addEventListener('click', () => select(Math.min(tabs.length - 1, current + 1)));
  close.addEventListener('click', () => dismiss(true));
  document.addEventListener('keydown', event => { if (event.key === 'Escape' && isOpen) dismiss(true); });
  document.addEventListener('click', event => { if (isOpen && !root.contains(event.target)) dismiss(); });
  scroller.addEventListener('scroll', position, { passive: true });
  window.addEventListener('resize', position);
  root.classList.add('mr-enhanced');
  root.querySelector('.mr-controls').hidden = false;
  root.querySelector('.mr-help').hidden = false;
  select(current, hashIndex >= 0);
})();

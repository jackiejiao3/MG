(() => {
  const root = document.querySelector('[data-milestone-ruler]');
  if (!root) return;
  const track = root.querySelector('.mr-track');
  const tabs = [...root.querySelectorAll('[data-milestone-index]')];
  const panels = [...root.querySelectorAll('.mr-panel')];
  const controls = root.querySelector('.mr-controls');
  const previous = root.querySelector('[data-milestone-prev]');
  const next = root.querySelector('[data-milestone-next]');
  let current = tabs.length - 1;
  const hashIndex = panels.findIndex(panel => '#' + panel.id === location.hash);
  if (hashIndex >= 0) current = hashIndex;
  track.setAttribute('role', 'tablist');
  tabs.forEach((tab, index) => {
    tab.setAttribute('role', 'tab');
    tab.setAttribute('aria-controls', panels[index].id);
    panels[index].setAttribute('role', 'tabpanel');
    tab.addEventListener('click', event => { event.preventDefault(); select(index); });
    tab.addEventListener('keydown', event => {
      let target;
      if (event.key === 'ArrowLeft') target = Math.max(0, index - 1);
      if (event.key === 'ArrowRight') target = Math.min(tabs.length - 1, index + 1);
      if (event.key === 'Home') target = 0;
      if (event.key === 'End') target = tabs.length - 1;
      if (target !== undefined) { event.preventDefault(); select(target); tabs[target].focus(); }
    });
  });
  function select(index) {
    current = index;
    tabs.forEach((tab, i) => {
      tab.setAttribute('aria-selected', String(i === index));
      tab.tabIndex = i === index ? 0 : -1;
      panels[i].hidden = i !== index;
    });
    previous.disabled = index === 0;
    next.disabled = index === tabs.length - 1;
    const scroller = root.querySelector('.mr-track-scroll');
    const tab = tabs[index];
    scroller.scrollLeft = Math.max(0, tab.offsetLeft - scroller.clientWidth / 2 + tab.offsetWidth / 2);
  }
  previous.addEventListener('click', () => select(Math.max(0, current - 1)));
  next.addEventListener('click', () => select(Math.min(tabs.length - 1, current + 1)));
  root.classList.add('mr-enhanced');
  controls.hidden = false;
  root.querySelector('.mr-help').hidden = false;
  select(current);
})();

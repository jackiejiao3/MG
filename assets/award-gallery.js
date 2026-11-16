document.querySelectorAll('.ma-award-detail .award-card__media').forEach((media, group) => {
  const photos = Array.from(media.querySelectorAll('a')).filter(a => a.querySelector('img'));
  if (photos.length < 2) return;
  const region = document.createElement('section');
  region.className = 'award-carousel';
  region.setAttribute('aria-label', 'Award photographs');
  region.setAttribute('aria-roledescription', 'carousel');
  const track = document.createElement('div');
  track.className = 'award-carousel__track';
  track.id = 'award-photos-' + group;
  track.tabIndex = 0;
  track.setAttribute('aria-label', 'Photographs. Swipe or use left and right arrow keys.');
  photos.forEach((photo, i) => {
    const slide = document.createElement('div');
    slide.className = 'award-carousel__slide';
    slide.setAttribute('role', 'group');
    slide.setAttribute('aria-roledescription', 'slide');
    slide.setAttribute('aria-label', (i + 1) + ' of ' + photos.length);
    slide.append(photo);
    track.append(slide);
  });
  const controls = document.createElement('div');
  controls.className = 'award-carousel__controls';
  const prev = document.createElement('button');
  const next = document.createElement('button');
  prev.type = next.type = 'button';
  prev.textContent = '←'; next.textContent = '→';
  prev.setAttribute('aria-label', 'Previous photograph');
  next.setAttribute('aria-label', 'Next photograph');
  prev.setAttribute('aria-controls', track.id); next.setAttribute('aria-controls', track.id);
  const count = document.createElement('span');
  count.setAttribute('role', 'status');
  count.setAttribute('aria-live', 'polite');
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
  let current = 0;
  function update() {
    current = Math.max(0, Math.min(photos.length - 1, Math.round(track.scrollLeft / (track.clientWidth || 1))));
    count.textContent = (current + 1) + ' / ' + photos.length;
    prev.disabled = current === 0; next.disabled = current === photos.length - 1;
  }
  function go(index) {
    track.scrollTo({ left: Math.max(0, Math.min(photos.length - 1, index)) * track.clientWidth, behavior: reduced.matches ? 'auto' : 'smooth' });
  }
  prev.addEventListener('click', () => go(current - 1));
  next.addEventListener('click', () => go(current + 1));
  track.addEventListener('keydown', e => {
    if (e.key !== 'ArrowLeft' && e.key !== 'ArrowRight') return;
    e.preventDefault(); go(current + (e.key === 'ArrowLeft' ? -1 : 1));
  });
  track.addEventListener('scroll', update, { passive: true });
  controls.append(prev, count, next);
  region.append(track, controls);
  media.replaceChildren(region);
  if (window.ResizeObserver) new ResizeObserver(() => {
    track.scrollTo({left: current * track.clientWidth, behavior: 'instant'});
    update();
  }).observe(track);
  update();
});

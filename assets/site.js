(() => {
  const header = document.querySelector('.site-header');
  const toggle = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#primary-nav');

  if (!header || !toggle || !nav) return;

  const setOpen = (open) => {
    document.body.classList.toggle('menu-open', open);
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  };

  toggle.addEventListener('click', () => {
    setOpen(!document.body.classList.contains('menu-open'));
  });

  nav.addEventListener('click', (event) => {
    if (event.target.closest('a')) setOpen(false);
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') setOpen(false);
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 900) setOpen(false);
  });
})();

(() => {
  const productSelect = document.querySelector('#product');
  if (!productSelect) return;

  const requestedProduct = new URLSearchParams(window.location.search).get('product');
  const validProducts = Array.from(productSelect.options, (option) => option.value);
  if (requestedProduct && validProducts.includes(requestedProduct)) {
    productSelect.value = requestedProduct;
  }

  document.querySelectorAll('[data-product]').forEach((link) => {
    link.addEventListener('click', () => {
      productSelect.value = link.dataset.product;
    });
  });
})();

(() => {
  document.querySelectorAll('[data-interactive-map]').forEach((map) => {
    const get = (selector) => map.querySelector(selector);
    const all = (selector) => Array.from(map.querySelectorAll(selector));
    const viewport = get('.map-viewport');
    const canvas = get('.map-canvas');
    if (!viewport || !canvas) return;
    const scaleControl = get('[data-map-scale]');
    const scaleMeasure = get('[data-map-scale-measure]');
    const scaleValue = get('[data-map-scale-value]');
    const mapWidthKm = Number(map.dataset.mapWidthKm);
    const markers = all('.map-hotspot');
    const filters = all('[data-map-filter]');
    const cards = all('[data-map-card]');
    const locationButtons = all('[data-map-select]');
    const distanceRows = all('[data-distance-row]');
    const selectedDistances = get('[data-selected-distances]');
    const otherDistances = get('[data-other-distances]');
    const picker = get('[data-map-location-select]');
    let selectedId = 'mdhi';
    let scale = 1, offsetX = 0, offsetY = 0;
    let fitWidth = 0, fitHeight = 0, baseLeft = 0, baseTop = 0;
    let pointerId = null, dragStartX = 0, dragStartY = 0, dragOriginX = 0, dragOriginY = 0;
    const clamp = (value, min, max) => Math.min(max, Math.max(min, value));
    const ids = (value) => (value || '').split(' ').filter(Boolean);
    const updateScaleBar = () => {
      if (!scaleControl || !scaleMeasure || !scaleValue) return;
      if (!Number.isFinite(mapWidthKm) || mapWidthKm <= 0 || fitWidth <= 0) {
        scaleControl.hidden = true;
        return;
      }
      // The ruler stays in screen space; the base artwork scales underneath it.
      const pixelsPerKm = fitWidth * scale / mapWidthKm;
      const targetWidth = Math.min(132, Math.max(120, viewport.clientWidth * .3));
      const targetKm = targetWidth / pixelsPerKm;
      const magnitude = 10 ** Math.floor(Math.log10(targetKm));
      const fraction = targetKm / magnitude;
      const distanceKm = (fraction >= 5 ? 5 : fraction >= 2.5 ? 2.5 : fraction >= 2 ? 2 : 1) * magnitude;
      const distanceText = distanceKm >= 1
        ? `${Number(distanceKm.toPrecision(3))} km`
        : `${Math.round(distanceKm * 1000)} m`;
      scaleMeasure.style.width = `${distanceKm * pixelsPerKm}px`;
      scaleValue.textContent = distanceText;
      scaleControl.setAttribute('aria-label', `Approximate straight-line scale: ${distanceText}. Not road distance.`);
      scaleControl.hidden = false;
    };
    const applyTransform = () => {
      const width = viewport.clientWidth, height = viewport.clientHeight;
      if (!width || !height) return;
      fitWidth = Math.min(width, height * 3420 / 2214);
      fitHeight = fitWidth * 2214 / 3420;
      baseLeft = (width - fitWidth) / 2;
      baseTop = (height - fitHeight) / 2;
      offsetX = clamp(offsetX, Math.min(0, width - baseLeft - fitWidth * scale), 0);
      offsetY = clamp(offsetY, Math.min(0, height - baseTop - fitHeight * scale), 0);
      canvas.style.width = `${fitWidth}px`;
      canvas.style.height = `${fitHeight}px`;
      canvas.style.left = `${baseLeft}px`;
      canvas.style.top = `${baseTop}px`;
      canvas.style.transform = `translate3d(${offsetX}px, ${offsetY}px, 0) scale(${scale})`;
      updateScaleBar();
    };
    const resetView = () => { scale = 1; offsetX = 0; offsetY = 0; applyTransform(); };
    const setScale = (next, x = viewport.clientWidth / 2, y = viewport.clientHeight / 2) => {
      const previous = scale;
      scale = clamp(next, 1, 2.6);
      const ratio = scale / previous;
      offsetX = x - baseLeft - (x - baseLeft - offsetX) * ratio;
      offsetY = y - baseTop - (y - baseTop - offsetY) * ratio;
      applyTransform();
    };
    const updateDistances = () => {
      const groupSites = map.dataset.mapLayer === 'site';
      let count = 0;
      let otherCount = 0;
      distanceRows.forEach((row) => {
        const from = ids(row.dataset.distanceFrom), to = ids(row.dataset.distanceTo);
        const allowed = groupSites === (row.dataset.groupSites === 'true');
        const relevant = from.includes(selectedId) || to.includes(selectedId);
        row.hidden = !allowed;
        row.querySelector('[data-distance-label]').textContent = !groupSites && relevant
          ? (from.includes(selectedId) ? row.dataset.distanceToLabel : row.dataset.distanceFromLabel)
          : row.dataset.distanceFullLabel;
        const primary = allowed && (groupSites || relevant);
        (primary ? selectedDistances : otherDistances).append(row);
        if (primary) count += 1;
        else if (allowed) otherCount += 1;
      });
      get('[data-distance-empty]').hidden = count !== 0;
      get('.map-other-distances').hidden = otherCount === 0;
      if (groupSites) get('[data-distance-heading]').textContent = 'Group-site distances';
    };
    const selectMarker = (marker) => {
      if (!marker || marker.hidden) return;
      selectedId = marker.dataset.mapId;
      get('.map-sidebar').scrollTop = 0;
      markers.forEach((item) => {
        const active = item === marker;
        item.classList.toggle('is-active', active);
        item.setAttribute('aria-pressed', String(active));
      });
      cards.forEach((card) => card.classList.toggle('is-active', card.dataset.mapCard === selectedId));
      locationButtons.forEach((button) => {
        const active = button.dataset.mapSelect === selectedId;
        button.classList.toggle('is-active', active);
        button.setAttribute('aria-pressed', String(active));
      });
      for (const field of ['kicker','code','title','chinese','address','copy']) {
        const key = `map${field[0].toUpperCase()}${field.slice(1)}`;
        get(`[data-map-detail-${field}]`).textContent = marker.dataset[key] || '';
      }
      get('[data-map-detail-chinese]').hidden = !marker.dataset.mapChinese;
      get('[data-map-address-block]').hidden = !marker.dataset.mapAddress;
      get('[data-map-detail-icon]').src = marker.querySelector('img').getAttribute('src');
      get('[data-distance-heading]').textContent = `Distances from ${marker.dataset.mapCode}`;
      if (picker) picker.value = marker.dataset.mapType === 'transport' ? selectedId : '';
      updateDistances();
    };
    markers.forEach((marker) => marker.addEventListener('click', () => selectMarker(marker)));
    locationButtons.forEach((button) => button.addEventListener('click', () => {
      const marker = markers.find((item) => item.dataset.mapId === button.dataset.mapSelect);
      if (!marker || marker.hidden) return;
      selectMarker(marker);
      resetView();
      if (!button.hasAttribute('data-map-chip')) {
        get('.map-workspace').scrollIntoView({ behavior: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'instant' : 'smooth', block: 'start' });
        marker.focus({ preventScroll: true });
      }
    }));
    picker?.addEventListener('change', () => {
      const marker = markers.find((item) => item.dataset.mapId === picker.value);
      if (marker) { selectMarker(marker); resetView(); }
    });
    const applyFilter = (selected, button) => {
      filters.forEach((filter) => {
        filter.classList.toggle('is-active', filter === button);
        filter.setAttribute('aria-pressed', String(filter === button));
      });
      [...markers, ...cards].forEach((item) => { item.hidden = selected !== 'all' && item.dataset.mapType !== selected; });
      get('[data-site-choices]').hidden = selected === 'transport';
      get('[data-transport-picker]').hidden = selected !== 'transport';
      all('[data-legend-type]').forEach((item) => { item.hidden = selected !== 'all' && item.dataset.legendType !== selected; });
      map.dataset.mapLayer = selected;
      const current = markers.find((marker) => marker.dataset.mapId === selectedId && !marker.hidden);
      selectMarker(current || markers.find((marker) => marker.dataset.mapId === 'mdhi' && !marker.hidden) || markers.find((marker) => !marker.hidden));
      resetView();
    };
    filters.forEach((filter) => filter.addEventListener('click', () => applyFilter(filter.dataset.mapFilter, filter)));
    get('[data-map-zoom-in]')?.addEventListener('click', () => setScale(scale + .3));
    get('[data-map-zoom-out]')?.addEventListener('click', () => setScale(scale - .3));
    get('[data-map-reset]')?.addEventListener('click', resetView);
    viewport.addEventListener('wheel', (event) => {
      event.preventDefault();
      const rect = viewport.getBoundingClientRect();
      setScale(scale + (event.deltaY < 0 ? .2 : -.2), event.clientX - rect.left, event.clientY - rect.top);
    }, { passive: false });
    viewport.addEventListener('dblclick', (event) => {
      if (event.target.closest('.map-hotspot, .map-controls')) return;
      const rect = viewport.getBoundingClientRect();
      setScale(scale + .4, event.clientX - rect.left, event.clientY - rect.top);
    });
    viewport.addEventListener('pointerdown', (event) => {
      if (event.target.closest('.map-hotspot, .map-controls') || event.button !== 0) return;
      pointerId = event.pointerId;
      dragStartX = event.clientX; dragStartY = event.clientY;
      dragOriginX = offsetX; dragOriginY = offsetY;
      viewport.classList.add('is-dragging');
      viewport.setPointerCapture?.(pointerId);
    });
    viewport.addEventListener('pointermove', (event) => {
      if (pointerId === null || event.pointerId !== pointerId) return;
      offsetX = dragOriginX + event.clientX - dragStartX;
      offsetY = dragOriginY + event.clientY - dragStartY;
      applyTransform();
    });
    const stopDragging = (event) => {
      if (event.pointerId !== pointerId) return;
      pointerId = null;
      viewport.classList.remove('is-dragging');
    };
    viewport.addEventListener('pointerup', stopDragging);
    viewport.addEventListener('pointercancel', stopDragging);
    viewport.addEventListener('lostpointercapture', stopDragging);
    viewport.addEventListener('keydown', (event) => {
      if (event.key === '+' || event.key === '=') setScale(scale + .3);
      else if (event.key === '-') setScale(scale - .3);
      else if (event.key === '0') resetView();
      else if (event.key === 'ArrowLeft') offsetX += 45;
      else if (event.key === 'ArrowRight') offsetX -= 45;
      else if (event.key === 'ArrowUp') offsetY += 45;
      else if (event.key === 'ArrowDown') offsetY -= 45;
      else return;
      event.preventDefault(); applyTransform();
    });
    window.addEventListener('resize', applyTransform);
    if (typeof ResizeObserver !== 'undefined') new ResizeObserver(applyTransform).observe(viewport);
    const initial = filters.find((filter) => filter.classList.contains('is-active')) || filters[0];
    if (initial) applyFilter(initial.dataset.mapFilter, initial);
    applyTransform();
  });
})();

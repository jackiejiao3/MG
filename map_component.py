"""Shared static-HTML network map. Source geography and icons remain unchanged."""
from html import escape
from map_locations import LOCATIONS, DISTANCES, location_description
from map_scale import reference_width_km


def render_map(depth, variant='full'):
    r = lambda p: '../' * depth + p
    loc = {item['id']: item for item in LOCATIONS}
    first = loc['mdhi']
    icon_path = lambda item: r(f'assets/images/map-pin-{item["icon"]}.svg')
    pins, cards, chips, options, selected_rows, other_rows = [], [], [], [], [], []
    for item in LOCATIONS:
        p = {k: escape(v) if isinstance(v, str) else v for k, v in item.items()}
        p['copy'] = escape(location_description(item))
        active = item['id'] == 'mdhi'
        pressed = str(active).lower()
        attrs = ' '.join(f'data-map-{key}="{p[value]}"' for key, value in [('id','id'),('type','kind'),('code','code'),('title','title'),('kicker','kicker'),('copy','copy'),('address','address'),('chinese','chinese')])
        pins.append(f'<button class="map-hotspot map-hotspot--{p["kind"]}{" is-active" if active else ""}" type="button" style="--x:{p["x"]}%;--y:{p["y"]}%;" {attrs} aria-label="Show details for {p["title"]}" aria-pressed="{pressed}"><img src="{icon_path(item)}" alt="" draggable="false"></button>')
        address = f'<address>{p["address"]}</address>' if p['address'] else ''
        chinese = f'<p class="map-location-chinese" lang="zh-CN">{p["chinese"]}</p>' if p['chinese'] else ''
        cards.append(f'<article class="map-location-card" data-map-card="{p["id"]}" data-map-type="{p["kind"]}"><img src="{icon_path(item)}" alt="" width="36" height="62"><div><span class="map-location-code">{p["code"]}</span><h4>{p["title"]}</h4>{chinese}{address}<p>{p["copy"]}</p><button type="button" data-map-select="{p["id"]}" aria-pressed="{pressed}">Locate on map ↗</button></div></article>')
        if item['kind'] == 'site':
            chips.append((item['id'], f'<button type="button" class="map-site-chip{" is-active" if active else ""}" data-map-select="{p["id"]}" data-map-chip aria-pressed="{pressed}">{"Shanghai" if p["id"] == "sh" else p["code"]}</button>'))
        else:
            options.append(f'<option value="{p["id"]}">{p["title"]}</option>')

    # Reference distances are shown in the sidebar only, never over the map.
    for distance in DISTANCES:
        d = distance
        from_ids, to_ids = ' '.join(d['start']), ' '.join(d['end'])
        relevant = not d.get('group_sites') and 'mdhi' in d['start'] + d['end']
        group_site = str(d.get('group_sites', False)).lower()
        distance_text = f'{d["km"]} km'
        full_label = escape(d['start_label'] + ' ↔ ' + d['end_label'])
        initial_label = escape(d['end_label'] if 'mdhi' in d['start'] else d['start_label']) if relevant else full_label
        row = f'<li data-distance-row="{d["id"]}" data-distance-from="{from_ids}" data-distance-to="{to_ids}" data-group-sites="{group_site}" data-distance-from-label="{escape(d["start_label"])}" data-distance-to-label="{escape(d["end_label"])}" data-distance-full-label="{full_label}"{" hidden" if d.get("group_sites") else ""}><span data-distance-label>{initial_label}</span><strong>{distance_text}</strong></li>'
        (selected_rows if relevant else other_rows).append(row)
    chips.sort(key=lambda pair: ['mdhi','mmec','meem','sh'].index(pair[0]))
    map_id = 'home-network-map' if variant == 'compact' else 'network-map'
    legend = ''.join(f'<span data-legend-type="{kind}"><img src="{r(f"assets/images/map-pin-{icon}.svg")}" alt="">{label}</span>' for kind,icon,label in [('site','mdhi','Factories'),('site','office','Shanghai office'),('transport','port','Ports'),('transport','airport','Airports'),('transport','rail','Rail')])
    return f'''<div class="interactive-map interactive-map--{variant} interactive-map--sidebar" id="{map_id}" data-interactive-map data-map-width-km="{reference_width_km()}">
      <div class="interactive-map-toolbar"><strong>Sites &amp; transport</strong><div class="map-filters" aria-label="Map layers"><button type="button" data-map-filter="site" aria-pressed="false">Group sites</button><button class="is-active" type="button" data-map-filter="all" aria-pressed="true">Sites + transport</button><button type="button" data-map-filter="transport" aria-pressed="false">Transport only</button></div></div>
      <div class="map-workspace">
        <aside class="map-sidebar" aria-label="Selected location and distances">
          <p class="map-sidebar-eyebrow">Select a location</p><div class="map-site-choices" data-site-choices>{''.join(chip for _,chip in chips)}</div>
          <label class="map-transport-picker" data-transport-picker><span>Transport hubs</span><select data-map-location-select aria-label="Choose a transport hub"><option value="">Choose a transport hub…</option>{''.join(options)}</select></label>
          <div class="map-detail" aria-live="polite" aria-atomic="true"><div class="map-detail-heading"><img data-map-detail-icon src="{icon_path(first)}" width="42" height="70" alt=""><div><span data-map-detail-kicker>{escape(first['kicker'])}</span><h3 data-map-detail-code>MDHI</h3></div></div><h4 data-map-detail-title>{escape(first['title'])}</h4><p data-map-detail-chinese lang="zh-CN">{first['chinese']}</p><div class="map-address-block" data-map-address-block><span class="map-sidebar-eyebrow">Address</span><address data-map-detail-address>{first['address']}</address></div><p data-map-detail-copy>{first['copy']}</p></div>
          <section class="map-distance-summary" aria-label="Distance information"><h4 class="map-sidebar-eyebrow" data-distance-heading>Distances from MDHI</h4><ul data-selected-distances>{''.join(selected_rows)}</ul><p class="map-distance-empty" data-distance-empty hidden>No distance is specified for this location in the source map.</p><details class="map-other-distances" open><summary>Other network links</summary><ul data-other-distances>{''.join(other_rows)}</ul></details></section>
        </aside>
        <div class="map-stage"><div class="map-viewport" tabindex="0" aria-label="Interactive map. Drag to move; use plus and minus to zoom; select a marker for details on the left."><div class="map-canvas"><img src="{r('assets/images/modern-group-map-base.webp')}" alt="Regional map of the Modern Group network" width="3420" height="2214" draggable="false"><img class="map-city-labels" src="{r('assets/images/map-city-labels.svg')}" alt="Shanghai 上海, Taicang 太仓, Suzhou 苏州, Wuxi 无锡 and Zhangjiagang 张家港市" width="3420" height="2214" draggable="false">{''.join(pins)}</div><div class="map-scale" data-map-scale role="img" aria-label="Approximate straight-line scale" hidden><span class="map-scale-caption">Approx.</span><div class="map-scale-measure" data-map-scale-measure><div class="map-scale-numbers"><span>0</span><span data-map-scale-value></span></div><span class="map-scale-rule" aria-hidden="true"></span></div></div><div class="map-controls" aria-label="Map zoom controls"><button type="button" data-map-zoom-in aria-label="Zoom in">+</button><button type="button" data-map-zoom-out aria-label="Zoom out">−</button><button type="button" data-map-reset aria-label="Reset map view">↺</button></div><div class="map-legend">{legend}</div></div><p class="map-route-note">Approximate straight-line scale, calibrated from airport landmarks. Not for navigation or road-distance measurement. Reference distances remain in the location panel.</p></div>
      </div>
      <details class="map-directory-disclosure"><summary>View all location names and addresses</summary><div class="map-location-directory" aria-label="Locations in the selected map layer">{''.join(cards)}</div></details>
    </div>'''

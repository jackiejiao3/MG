import os

def svg(title, subtitle, w=1200, h=800, dark=True):
    bg = "#202326" if dark else "#f6f2e8"
    fg = "#bda16d"
    sub = "#aeb2b4" if dark else "#625e57"
    rect = "#292d30" if dark else "#e9e1d2"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <rect width="{w}" height="{h}" fill="{bg}"/>
  <rect x="{w*0.08:.0f}" y="{h*0.22:.0f}" width="{w*0.84:.0f}" height="{h*0.56:.0f}" rx="4" fill="{rect}" stroke="{fg}" stroke-width="2" stroke-dasharray="12 10"/>
  <text x="{w/2}" y="{h*0.48:.0f}" font-family="Georgia, serif" font-size="42" fill="{fg}" text-anchor="middle" font-weight="400">{title}</text>
  <text x="{w/2}" y="{h*0.56:.0f}" font-family="ui-sans-serif, system-ui, sans-serif" font-size="18" fill="{sub}" text-anchor="middle">{subtitle}</text>
</svg>'''

images = {
    "hero-home.svg": ("Modern Group Manufacturing Network", "Envisioned: Aerial view of the connected MDHI, MMEC and MEEM production bases near the Yangtze River"),
    "mdhi-facility.svg": ("MDHI Facility", "Envisioned: Bird's-eye view of the MDHI structural-steel fabrication shop in Taicang Port Development Zone"),
    "mmec-facility.svg": ("MMEC Facility", "Envisioned: Aerial view of the MMEC modular assembly yard and Zhangjiagang port load-out area"),
    "meem-facility.svg": ("MEEM Facility", "Envisioned: Bird's-eye view of the MEEM HRSG and ACHE manufacturing plant in Zhangjiagang"),
    "location-map.svg": ("Location Map", "Envisioned: Map showing Taicang, Zhangjiagang and Shanghai with port and logistics markers"),
    "structural-steel.svg": ("Structural Steel", "Envisioned: Large structural steel columns and trusses during fabrication"),
    "modular-plant.svg": ("Modular Plant", "Envisioned: Integrated process module under assembly in the modular yard"),
    "hrsg.svg": ("HRSG Pressure Parts", "Envisioned: Finned tubes and harp assemblies for a heat recovery steam generator"),
    "ache.svg": ("Air-Cooled Heat Exchanger", "Envisioned: Air-cooled heat exchanger bundle with finned tubes and fan deck"),
}

for name, (t, s) in images.items():
    path = os.path.join(os.path.dirname(__file__), name)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg(t, s))
    print("wrote", path)

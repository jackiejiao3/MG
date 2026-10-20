"""Product portfolio content. Replace gallery slots and enrich product records here."""
from html import escape


PRODUCTS = (
    {
        "id": "structural-steel", "name": "Structural Steel", "short": "Steel structures",
        "theme": "steel", "company": "MDHI + MMEC", "companies": ("MDHI", "MMEC"),
        "image": "pp-b2b-product-structural-steel-cargo-enhanced.webp", "alt": "Fabricated structural steel components stacked in a ship cargo hold",
        "headline": "The framework behind ambitious builds.",
        "description": "Project-specific structural steel fabrication for buildings, infrastructure and industrial facilities, supported by two specialist manufacturing bases.",
        "scope": ("Columns & beams", "Complex steel structures", "Industrial steelwork"),
        "applications": ("Buildings & infrastructure", "Power plants", "Mining", "Oil & gas"),
        "detail": "Typical scope includes detailing, procurement, fabrication, coatings, assembly and delivery. The responsible operating company confirms the scope for each enquiry.",
        "slots": (
            {"label": "Connections & fabrication detail", "image": "pp-b2b-structural-steel-fabrication.webp", "alt": "Welding and connection details of a structural steel assembly in the fabrication workshop", "caption": "Connections & fabrication detail"},
            {"label": "Assembly & delivery", "image": "pp-b2b-structural-steel-delivery.webp", "alt": "Structural steel components with protective wrapping and securing straps ready for delivery", "caption": "Assembly & delivery"},
        ),
        "technical": "Material grades · member dimensions · fabrication tolerances",
    },
    {
        "id": "modular-plants", "name": "Modular Plants", "short": "Modular Plants",
        "theme": "modular", "company": "MMEC", "companies": ("MMEC",),
        "image": "pp-b2b-product-modular-plants-layer3.webp", "alt": "Modular plant equipment",
        "headline": "Bring more of the plant together.",
        "description": "Integrated modules, process units and modular plant packages manufactured through MMEC’s assembly and port-oriented delivery platform.",
        "scope": ("Process modules", "Plant skids", "Pipe racks & utilities"),
        "applications": ("Process industries", "Oil & gas", "Energy facilities", "Modular construction"),
        "detail": "Manufacturing scope can include structural fabrication, pipe spools, module assembly, blasting and coating, SPMT transport and port load-out. MMEC confirms the package boundary for each enquiry.",
        "slots": (
            {"label": "Module assembly & integration", "image": "pp-b2b-modular-plants-assembly-integration.webp", "alt": "Module assembly & integration", "caption": "Module assembly & integration"},
            {"label": "Transport & port load-out", "image": "pp-b2b-modular-plants-port-loadout.webp", "alt": "Transport & port load-out", "caption": "Transport & port load-out"},
        ),
        "technical": "Module dimensions · package scope · transport requirements",
    },
    {
        "id": "hrsg-pressure-parts", "name": "HRSG Pressure Parts", "short": "Pressure-part assemblies",
        "theme": "hrsg", "company": "MEEM", "companies": ("MEEM",),
        "image": "pp-b2b-product-hrsg-pressure-parts.webp", "alt": "HRSG pressure-part header assembly in a fabrication workshop",
        "headline": "Purpose-built for heat recovery.",
        "description": "Dedicated manufacture of pressure-part components and assemblies for heat recovery steam generator applications, delivered by MEEM.",
        "scope": ("Finned tubes & headers", "Manifolds & harps", "Pressure-part modules"),
        "applications": ("Combined-cycle power", "Cogeneration", "Industrial heat recovery"),
        "detail": "The product line covers pressure-part components and assemblies for HRSG applications. Material requirements, design conditions, inspection scope and certification requirements are confirmed directly with MEEM.",
        "slots": (
            {"label": "Tube & header detail", "image": "pp-b2b-hrsg-tube-header-detail.webp", "alt": "Tube & header detail", "caption": "Tube & header detail"},
            {"label": "Workshop & assembly", "image": "pp-b2b-hrsg-workshop-assembly.webp", "alt": "Workshop & assembly", "caption": "Workshop & assembly"},
        ),
        "technical": "Materials · design conditions · inspection requirements",
    },
    {
        "id": "air-cooled-heat-exchangers", "name": "Air-Cooled Heat Exchangers", "short": "Air-Cooled Heat Exchangers",
        "theme": "ache", "company": "MEEM", "companies": ("MEEM",),
        "image": "pp-b2b-product-air-cooled-heat-exchangers-default.webp", "alt": "Air-cooled heat exchanger manufactured by MEEM",
        "headline": "Equipment for demanding cooling duties.",
        "description": "Specialized fabrication of air-cooled heat exchanger equipment for energy and process applications, supported by MEEM’s manufacturing facility.",
        "scope": ("Heat exchanger bundles", "Air-cooled equipment", "ACHE assemblies"),
        "applications": ("Process cooling", "Power generation", "Energy facilities"),
        "detail": "MEEM is the responsible operating company for this product line. Equipment configuration, materials, thermal duty and inspection requirements are reviewed against the customer’s specification.",
        "slots": (
            {"label": "Assembly hall", "image": "air-cooled-heat-exchanger-assembly-hall.webp", "alt": "Air-cooled heat exchanger assemblies in the MEEM manufacturing hall", "caption": "Assembly hall"},
            {"label": "Modular air-cooled heat exchanger", "image": "modular-air-cooled-heat-exchanger.webp", "alt": "Front view of a modular air-cooled heat exchanger assembly", "caption": "Modular air-cooled heat exchanger"},
        ),
        "technical": "Equipment configuration · thermal duty · material requirements",
    },
)


def gallery_slot(slot):
    if slot["image"]:
        return f'''<figure class="pp-gallery-item"><img src="../assets/images/{escape(slot['image'])}" alt="{escape(slot['alt'])}" loading="lazy" decoding="async"><figcaption>{escape(slot['caption'] or slot['label'])}</figcaption></figure>'''
    return f'''<figure class="pp-placeholder"><span class="pp-image-symbol" aria-hidden="true"><svg viewBox="0 0 48 48" fill="none"><rect x="7" y="9" width="34" height="30" rx="2"/><circle cx="17" cy="19" r="3"/><path d="m9 35 11-10 7 6 6-8 7 12"/></svg></span><figcaption><strong>{escape(slot['label'])}</strong><span>Image to come</span></figcaption></figure>'''


def render_portfolio(page):
    mosaic = "".join(f'''<a class="pp-mosaic-tile pp-theme-{p['theme']}" href="#{p['id']}" aria-label="Explore {escape(p['name'])}"><img src="../assets/images/{p['image']}" alt="{escape(p['alt'])}" width="1600" height="1000" decoding="async"><span><b>{i:02d}</b>{escape(p['short'])}<em aria-hidden="true">↗</em></span></a>''' for i, p in enumerate(PRODUCTS, 1))
    nav = "".join(f'''<a href="#{p['id']}" class="pp-theme-{p['theme']}"><span>{i:02d}</span>{escape(p['name'])}<b aria-hidden="true">↓</b></a>''' for i, p in enumerate(PRODUCTS, 1))
    content = f'''<a class="pp-skip" href="#product-lines">Skip to product lines</a>
<section class="pp-hero"><div class="pp-width pp-hero-grid"><div class="pp-hero-copy"><p class="pp-kicker">Modern Group / Product Portfolio</p><h1>Four product lines.<br><em>Built around<br>your requirements.</em></h1><p class="pp-intro">Structural steel, integrated modules and energy equipment. Explore the scope. Find the right manufacturing company.</p><a class="pp-button pp-button-gold" href="#product-lines">Explore the portfolio <span aria-hidden="true">↓</span></a><div class="pp-hero-note"><span>04 <small>Product lines</small></span><span>03 <small>Operating companies</small></span></div></div><div class="pp-mosaic">{mosaic}<p>Specialist manufacturing. A connected network.</p></div></div></section>
<nav class="pp-product-nav" aria-label="Product lines"><div class="pp-width">{nav}</div></nav>
<section class="pp-overview pp-width" id="product-lines" aria-labelledby="pp-overview-title"><div><p class="pp-kicker">01 / Explore our scope</p><h2 id="pp-overview-title">Different capabilities.<br>Clear responsibility.</h2></div><p>Each product line connects to the operating company with the relevant facility and manufacturing scope. That company confirms your requirements and takes responsibility for quotation, contract and delivery.</p></section>'''
    for i, p in enumerate(PRODUCTS, 1):
        tags = "".join(f"<li>{escape(x)}</li>" for x in p["applications"])
        scope = "".join(f'<li><span aria-hidden="true">↗</span>{escape(x)}</li>' for x in p["scope"])
        profiles = "".join(f'<a href="../{company.lower()}/index.html">{company} profile <span aria-hidden="true">↗</span></a>' for company in p["companies"])
        gallery = "".join(gallery_slot(slot) for slot in p["slots"])
        content += f'''
<section class="pp-product pp-theme-{p['theme']}" id="{p['id']}" aria-labelledby="{p['id']}-title"><div class="pp-width"><div class="pp-product-heading"><div class="pp-product-index"><span>{i:02d}</span><p>Product line / {escape(p['company'])}</p></div><h2 id="{p['id']}-title">{escape(p['name'])}</h2><a class="pp-top-link" href="#product-lines" aria-label="Back to all product lines">All products ↑</a></div><div class="pp-product-layout"><div class="pp-product-visuals"><figure class="pp-main-image"><img src="../assets/images/{p['image']}" alt="{escape(p['alt'])}" width="1600" height="1000" loading="lazy" decoding="async"><figcaption><span>{escape(p['short'])}</span><b>{escape(p['company'])}</b></figcaption></figure><div class="pp-gallery">{gallery}</div></div><div class="pp-product-copy"><p class="pp-kicker">{escape(p['company'])} / Manufacturing scope</p><h3>{escape(p['headline'])}</h3><p class="pp-description">{escape(p['description'])}</p><div class="pp-scope"><h4>Scope at a glance</h4><ul>{scope}</ul></div><div class="pp-applications"><h4>Typical applications</h4><ul>{tags}</ul></div><details class="pp-details"><summary>Explore the manufacturing scope <span aria-hidden="true">+</span></summary><p>{escape(p['detail'])}</p></details><div class="pp-product-actions"><a class="pp-button" href="../contact/index.html?product={p['name'].replace(' ', '%20')}">Discuss your requirements <span aria-hidden="true">↗</span></a><div class="pp-profile-links">{profiles}</div></div></div></div></div></section>'''
    content += '''
<section class="pp-route"><div class="pp-width"><div class="pp-route-heading"><p class="pp-kicker">02 / The next step</p><h2>From your requirement<br>to the right manufacturer.</h2><p>A clear starting point for your enquiry.</p></div><ol class="pp-route-steps"><li><span>01</span><h3>Define the requirement</h3><p>Share the product type, application, destination and available drawings or specifications.</p></li><li><span>02</span><h3>Connect to the company</h3><p>We route your enquiry to the operating company with the relevant manufacturing scope.</p></li><li><span>03</span><h3>Confirm the scope</h3><p>The responsible company reviews the requirements, delivery scope and commercial proposal.</p></li></ol><div class="pp-route-bottom"><p>Not sure where to start? Send us a brief description of your requirement.</p><a class="pp-button pp-button-gold" href="../contact/index.html">Start an enquiry <span aria-hidden="true">↗</span></a></div></div></section>'''
    return page("Product Portfolio | Modern Group", 1, "Product Portfolio", "", "", "", content,
                "Explore structural steel, modular plants, HRSG pressure parts and air-cooled heat exchangers across the Modern Group manufacturing network.")

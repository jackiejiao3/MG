import os, html

BASE = os.path.dirname(os.path.abspath(__file__))

def rel(path_from_page, depth):
    return ("../" * depth) + path_from_page

def header(title, depth, active=None):
    r = lambda p: rel(p, depth)
    nav = [
        ("Home", r("index.html")),
        ("About", r("about/index.html")),
        ("Companies & Locations", r("companies-locations/index.html")),
        ("Product Portfolio", r("product-portfolio/index.html")),
        ("Quality & HSE", r("quality-hse/index.html")),
        ("Contact", r("contact/index.html")),
    ]
    links = "".join(f'<a class="{"active-nav" if active==label else ""}" href="{href}">{label}</a>' for label, href in nav)
    return f'''<header class="site-header {'inner-header' if depth else ''}"><a class="brand" href="{r('index.html')}" aria-label="Modern Group home"><span class="brand-surface"><img src="{r('assets/images/logo-white.webp')}" alt="Modern Group" width="598" height="115"></span></a><button class="menu-toggle" type="button" aria-label="Open navigation" aria-controls="primary-nav" aria-expanded="false"><span></span><span></span><span></span></button><nav id="primary-nav" aria-label="Primary navigation">{links}</nav><div class="header-tools"><a class="header-cta" href="{r('contact/index.html')}">Start an enquiry</a></div></header>'''

def footer(depth):
    r = lambda p: rel(p, depth)
    return f'''<footer><div class="footer-brand"><span class="brand-surface"><img src="{r('assets/images/logo-white.webp')}" alt="Modern Group" width="598" height="115"></span></div><p>Modern Group is a commercial brand and is not a separate incorporated legal entity. Contracts, certifications and legal obligations are held by the relevant operating company.</p><div><a href="{r('legal-notice/index.html')}">Legal</a><a href="{r('privacy/index.html')}">Privacy</a></div></footer>'''

def page(title, depth, active, hero_title, hero_sub, hero_img, content, desc=""):
    r = lambda p: rel(p, depth)
    body_class = "home" if depth == 0 else "inner"
    page_assets = ""
    if active == "Home":
        page_assets = '<link rel="stylesheet" href="assets/home.css">'
    if active == "About":
        body_class += " about-page"
        page_assets = f'''\n  <link rel="stylesheet" href="{r('assets/about.css?v=hero-original-5')}">'''
    if active == "Product Portfolio":
        body_class += " portfolio-page"
        page_assets = f'''
  <link rel="stylesheet" href="{r('assets/product-portfolio.css')}">
  <script defer src="{r('assets/product-portfolio.js')}"></script>'''
    if active == "Companies & Locations":
        body_class += " companies-page"
        page_assets = '<link rel="stylesheet" href="../assets/companies-locations.css"><script defer src="../assets/companies-locations.js"></script>'
    if active == "Quality & HSE":
        body_class += " quality-page"
        page_assets = f'''
  <link rel="stylesheet" href="{r('assets/quality-hse.css')}">
  <script defer src="{r('assets/quality-hse.js')}"></script>'''
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>{html.escape(title)}</title>
  <meta name="description" content="{html.escape(desc)}">
  <link rel="icon" href="{r('assets/images/favicon.ico')}">
  <link rel="stylesheet" href="{r('assets/styles.css')}">
  <script defer src="{r('assets/site.js')}"></script>{page_assets}
</head>
<body class="{body_class}">
{header(title.split(' | ')[0], depth, active)}
<main>
{content}
</main>
{footer(depth)}
</body>
</html>'''

def inner_hero(title, subtitle, img_path, depth):
    r = lambda p: rel(p, depth)
    return f'''<section class="inner-hero"><img class="inner-hero-bg" src="{r(img_path)}" alt=""><div class="inner-hero-content"><div class="breadcrumb">Modern Group · {html.escape(title)}</div><p class="eyebrow">Specialized manufacturing network</p><h1>{html.escape(title)}</h1><p>{html.escape(subtitle)}</p></div></section>'''

def interactive_map(depth, variant="full"):
    from map_component import render_map
    return render_map(depth, variant)

# ---------- Pages ----------

def how_we_work():
    steps = [
        ('01', 'work-route.svg', 'Route by scope',
         'We identify the product line and connect the enquiry with the relevant operating company.'),
        ('02', 'work-responsibility.svg', 'Clarify responsibility',
         'Proposals, contracts and project obligations are issued by the company undertaking the work.'),
        ('03', 'work-coordinate.svg', 'Coordinate where useful',
         'When a project crosses capabilities, the companies can coordinate communication across the network.'),
    ]
    cards = ''.join(
        f'<article><div class="principle-card-top"><span>{number}</span>'
        f'<img class="principle-icon" src="assets/images/{icon}" alt="" aria-hidden="true" width="72" height="72" loading="lazy" decoding="async"></div>'
        f'<h3>{title}</h3><p>{copy}</p></article>'
        for number, icon, title, copy in steps
    )
    return f'''<section class="principles section-shell section-muted principles--illustrated" id="how-we-work" aria-labelledby="how-we-work-title"><div class="section-heading"><div class="section-label"><span>05</span> How we work</div><h2 id="how-we-work-title">One point of entry. The right company takes responsibility.</h2></div><div class="principle-grid">{cards}</div></section>'''


def home():
    r = lambda p: rel(p, 0)
    content = f'''<section class="hero hero--group" id="top" aria-labelledby="group-title">
  <img class="hero-bg" src="assets/images/hero-blueprint-v2.webp" alt="Engineering blueprint illustrating Modern Group manufacturing capabilities" fetchpriority="high">
  <div class="hero-overlay"></div>
  <div class="hero-content">
    <p class="eyebrow">Three specialist companies. One Modern Group.</p>
    <h1 id="group-title">MODERN GROUP</h1>
    <p class="hero-copy">Modern Group is an integrated manufacturing group specializing in structural steel, modular plants, air-cooled heat exchangers and HRSG systems.</p>
    <ul class="hero-company-signature" aria-label="Companies in the Modern Group network">
      <li><a href="mdhi/index.html"><strong>MDHI</strong><span>Modern Heavy Industries Co., Ltd.</span></a></li>
      <li><a href="mmec/index.html"><strong>MMEC</strong><span>Modern Modular Engineering &amp; Construction Co., Ltd.</span></a></li>
      <li><a href="meem/index.html"><strong>MEEM</strong><span>Modern Energy Equipment Manufacturing Co., Ltd.</span></a></li>
    </ul>
    <div class="hero-actions"><a class="button button-gold" href="#about">Discover our network <span aria-hidden="true">↓</span></a><a class="button button-ghost" href="product-portfolio/index.html">Explore our capabilities</a></div>
  </div>
  <a class="scroll-cue" href="#about">Discover the network <span aria-hidden="true">↓</span></a>
</section>
<section class="network-overview section-shell" id="about" aria-labelledby="network-title">
  <div class="section-label"><span>01</span> The network</div>
  <div class="network-heading">
    <h2 id="network-title">One group identity.<br>Three connected companies.</h2>
    <p class="network-lead">Shared leadership. Complementary capabilities. Clear responsibility.</p>
    <p>Modern Group is the shared commercial identity of MDHI, MMEC and MEEM.</p>
  </div>
  <div class="network-relationship" aria-label="Modern Group connects three operating companies under shared executive leadership">
    <div class="network-brand"><img src="assets/images/logo-white.webp" alt="Modern Group" width="598" height="115" loading="lazy"><p>Shared commercial identity</p></div>
    <div class="network-company-headings">
      <a href="mdhi/index.html"><h3>MDHI</h3><p>Modern Heavy Industries</p></a>
      <a href="mmec/index.html"><h3>MMEC</h3><p>Modern Modular Engineering &amp; Construction</p></a>
      <a href="meem/index.html"><h3>MEEM</h3><p>Modern Energy Equipment Manufacturing</p></a>
    </div>
    <div class="network-shared-leadership"><span class="network-shared-symbol" aria-hidden="true">↔</span><div><h4>Shared executive leadership</h4><p>Led by the same executive team</p></div></div>
    <div class="network-scope-grid">
      <div><p class="network-fact-label">Manufacturing base</p><p class="network-base">Taicang, Jiangsu</p><div class="network-focus"><p class="network-fact-label">Specialist focus</p><p>Structural Steel</p></div></div>
      <div><p class="network-fact-label">Manufacturing base</p><p class="network-base">Zhangjiagang, Jiangsu</p><div class="network-focus"><p class="network-fact-label">Specialist focus</p><p>Structural Steel<br>Modular Plants</p></div></div>
      <div><p class="network-fact-label">Manufacturing base</p><p class="network-base">Zhangjiagang, Jiangsu</p><div class="network-focus"><p class="network-fact-label">Specialist focus</p><p>HRSG Pressure Parts<br>Air-Cooled Heat Exchangers</p></div></div>
    </div>
    <div class="network-mobile-companies">
      <article><h3><a href="mdhi/index.html">MDHI <span aria-hidden="true">↗</span></a></h3><p class="network-mobile-name">Modern Heavy Industries</p><dl><div><dt>Manufacturing base</dt><dd>Taicang, Jiangsu</dd></div><div><dt>Specialist focus</dt><dd>Structural Steel</dd></div></dl></article>
      <article><h3><a href="mmec/index.html">MMEC <span aria-hidden="true">↗</span></a></h3><p class="network-mobile-name">Modern Modular Engineering &amp; Construction</p><dl><div><dt>Manufacturing base</dt><dd>Zhangjiagang, Jiangsu</dd></div><div><dt>Specialist focus</dt><dd>Structural Steel · Modular Plants</dd></div></dl></article>
      <article><h3><a href="meem/index.html">MEEM <span aria-hidden="true">↗</span></a></h3><p class="network-mobile-name">Modern Energy Equipment Manufacturing</p><dl><div><dt>Manufacturing base</dt><dd>Zhangjiagang, Jiangsu</dd></div><div><dt>Specialist focus</dt><dd>HRSG Pressure Parts · Air-Cooled Heat Exchangers</dd></div></dl></article>
    </div>
  </div>
  <div class="network-accountability"><div><h3>Connected at group level. Accountable at company level.</h3><p>Contracts, certifications and project delivery remain with the relevant operating company.</p></div><a href="#companies">Explore our companies <span aria-hidden="true">↗</span></a></div>
</section>
<section class="facility-network section-shell" id="companies"><div class="split-heading"><div><div class="section-label"><span>02</span> Our companies</div><h2>Three manufacturing bases. Clear responsibility by company.</h2></div><p>Purpose-built facilities in Taicang and Zhangjiagang align specialist production with port-oriented logistics.</p></div><div class="facility-grid"><a class="facility-card" href="{r('mdhi/index.html')}"><div class="facility-photo"><img src="{r('assets/images/mdhi_birdview.webp')}" alt="Aerial view of MDHI manufacturing base"><span>01</span></div><div class="facility-info"><p class="company-code">MDHI · TAICANG</p><h3>Modern Heavy Industries (Taicang) Co., Ltd.</h3><p class="company-role">Structural Steel</p><span class="card-link">Explore MDHI <b>→</b></span></div></a><a class="facility-card" href="{r('mmec/index.html')}"><div class="facility-photo"><img src="{r('assets/images/mmec_birdview.webp')}" alt="Aerial view of MMEC manufacturing base"><span>02</span></div><div class="facility-info"><p class="company-code">MMEC · ZHANGJIAGANG</p><h3>Modern Modular Engineering &amp; Construction Co., Ltd.</h3><p class="company-role">Structural Steel · Modular Plants</p><span class="card-link">Explore MMEC <b>→</b></span></div></a><a class="facility-card" href="{r('meem/index.html')}"><div class="facility-photo"><img src="{r('assets/images/meem_birdview.webp')}" alt="Aerial view of MEEM manufacturing base"><span>03</span></div><div class="facility-info"><p class="company-code">MEEM · ZHANGJIAGANG</p><h3>Modern Energy Equipment Manufacturing Co., Ltd.</h3><p class="company-role">HRSG Pressure Parts · ACHE</p><span class="card-link">Explore MEEM <b>→</b></span></div></a></div></section>
<section class="portfolio section-shell section-soft" id="capabilities"><div class="portfolio-header"><div><div class="section-label"><span>03</span> Product portfolio</div><p class="eyebrow dark">A clear route to the right manufacturer</p><h2>Four focused product lines.</h2><p>Every enquiry is directed to the operating company with the relevant manufacturing scope.</p></div><aside class="portfolio-assurance"><span>Routing principle</span><p>Every product line is owned by a legal entity that can quote, contract, certify and deliver.</p></aside></div><div class="product-list"><article class="product-card"><div class="product-media"><img src="assets/images/home-structural-steel-frame-1600.webp" srcset="assets/images/home-structural-steel-frame-800.webp 800w, assets/images/home-structural-steel-frame-1600.webp 1600w, assets/images/home-structural-steel-frame-2000.webp 2000w" sizes="(max-width: 700px) 100vw, (max-width: 1050px) 310px, 390px" alt="Multi-level structural steel frame during preassembly at the fabrication yard" width="1600" height="628" loading="lazy" decoding="async"><span>01</span></div><div class="product-card-body"><div><h3>Structural Steel</h3><p>Two specialized fabrication bases supporting project-specific structural steel requirements.</p></div><strong>MDHI + MMEC</strong><a href="product-portfolio/index.html" aria-label="Explore Structural Steel in the product portfolio">Explore product portfolio <b>→</b></a></div></article><article class="product-card"><div class="product-media"><img src="assets/images/product-modular-plants-layer3.webp" alt="Modular plant equipment" width="1600" height="1000" loading="lazy" decoding="async"><span>02</span></div><div class="product-card-body"><div><h3>Modular Plants</h3><p>A focused manufacturing platform for integrated modules and modular plant delivery.</p></div><strong>MMEC</strong><a href="product-portfolio/index.html" aria-label="Explore Modular Plants in the product portfolio">Explore product portfolio <b>→</b></a></div></article><article class="product-card"><div class="product-media"><img src="assets/images/product-hrsg-pressure-parts.webp" alt="HRSG pressure-part header assembly in a fabrication workshop" width="1600" height="1000" loading="lazy" decoding="async"><span>03</span></div><div class="product-card-body"><div><h3>HRSG Pressure Parts</h3><p>Dedicated manufacture of pressure-part assemblies for heat recovery steam generator applications.</p></div><strong>MEEM</strong><a href="product-portfolio/index.html" aria-label="Explore HRSG Pressure Parts in the product portfolio">Explore product portfolio <b>→</b></a></div></article><article class="product-card"><div class="product-media"><img src="assets/images/home-air-heater-approved.webp" alt="Air heater equipment in the manufacturing workshop" width="1440" height="1080" loading="lazy" decoding="async"><span>04</span></div><div class="product-card-body"><div><h3>Air-Cooled Heat Exchangers</h3><p>Specialized fabrication of air-cooled heat exchanger equipment for energy and process projects.</p></div><strong>MEEM</strong><a href="product-portfolio/index.html" aria-label="Explore Air-Cooled Heat Exchangers in the product portfolio">Explore product portfolio <b>→</b></a></div></article></div></section>
<section class="locations section-shell locations-map-section" id="locations"><div class="location-copy"><div class="section-label"><span>04</span> Locations</div><p class="eyebrow dark">Shanghai · Taicang · Zhangjiagang</p><h2>Manufacturing access shaped by ports and industry.</h2><p>MDHI operates in Taicang Port Development Zone. MMEC and MEEM are located in Zhangjiagang near Gangxin Port, with engineering and commercial coordination supported from Shanghai.</p><div class="map-key"><span>3 manufacturing bases</span><span>1 engineering center</span><span>Yangtze River logistics</span></div></div>{interactive_map(0, "compact")}</section>
{how_we_work()}
<section class="contact-section" id="contact"><div class="section-shell"><div><p class="eyebrow">Start with Modern Group</p><h2>Tell us what you need to manufacture.</h2><p>Choose one of the four product lines. We will route your enquiry to the operating company with the relevant manufacturing responsibility.</p></div><div class="contact-links"><a href="{r('contact/index.html?product=Structural%20Steel#enquiry-form')}"><b>Structural Steel</b><span>MDHI + MMEC →</span></a><a href="{r('contact/index.html?product=Modular%20Plants#enquiry-form')}"><b>Modular Plants</b><span>MMEC →</span></a><a href="{r('contact/index.html?product=HRSG%20Pressure%20Parts#enquiry-form')}"><b>HRSG Pressure Parts</b><span>MEEM →</span></a><a href="{r('contact/index.html?product=Air-Cooled%20Heat%20Exchangers#enquiry-form')}"><b>Air-Cooled Heat Exchangers</b><span>MEEM →</span></a></div></div></section>'''
    return page("Modern Group | Specialized Manufacturing Network", 0, "Home", "", "", "", content, "Modern Group connects MDHI, MMEC and MEEM across four focused manufacturing product lines.")

def about():
    from about_page import render_about
    return render_about(page)


def companies_locations():
    from companies_locations import render_companies
    return render_companies(page, interactive_map)


def profile(slug, code, legal, role, location, desc, scope, facts, img, image_alt):
    depth = 1
    r = lambda p: rel(p, depth)
    hero_title = f"{code}"
    hero_sub = f"{legal} — {role}."
    content = inner_hero(hero_title, hero_sub, f"assets/images/{img}", depth)
    visuals = f'<div class="profile-image profile-image--manufacturing"><img src="{r(f"assets/images/{img}")}" alt="{html.escape(image_alt)}" loading="lazy" decoding="async"><span class="profile-image-label">{code} · {location}</span></div>'
    content += f'''<section class="content-shell company-profile"><div class="profile-visuals">{visuals}</div><div class="prose"><p class="eyebrow dark">Operating company</p><h2>{legal}</h2><p>{desc}</p><div class="profile-facts">'''
    for k, v in facts:
        content += f'<div><span>{k}</span><strong>{v}</strong></div>'
    content += f'''</div><h3>Core manufacturing scope</h3><p>{scope}</p><a class="button button-gold profile-cta" href="{official_url(code)}" target="_blank" rel="noopener">Visit {code} website ↗</a></div></section>'''
    return page(f"{code} | Modern Group", depth, None, "", "", "", content, f"{legal} — {role}.").replace("assets/styles.css", "assets/styles.css?v=company-photos-1")

def official_url(code):
    return {"MDHI":"https://mdhiglobal.com","MMEC":"https://mmecglobal.com","MEEM":"https://m-energy.com"}[code]

def mdhi_profile():
    facts = [("Legal name","Modern Heavy Industries (Taicang) Co., Ltd."),("Address","169 Longjiang Road, Taicang Port Development Zone, Taicang, Jiangsu 215433, China"),("Scope","Structural Steel"),("Website","mdhiglobal.com")]
    desc = "MDHI is the group’s specialist structural-steel fabricator in Taicang, serving demanding international projects with CNC high-accuracy production, project coordination and port-oriented delivery."
    scope = "Structural steel fabrication for buildings, infrastructure, power, mining, oil & gas and industrial projects. Capabilities include detailing, procurement, column-and-beam fabrication, complex steel structures, mechanical plate-work, conveyors, coatings, assembly and logistics."
    return profile("mdhi", "MDHI", "Modern Heavy Industries (Taicang) Co., Ltd.", "Structural Steel", "Taicang, Jiangsu", desc, scope, facts, "mdhi-robotic-welding-refined.webp", "Robotic welding of a large structural steel assembly at the MDHI workshop")

def mmec_profile():
    facts = [("Legal name","Modern Modular Engineering & Construction Co., Ltd."),("Address","2669 Yanjiang Road, Daxin Town, Zhangjiagang, Jiangsu, China"),("Scope","Structural Steel · Modular Plants"),("Website","mmecglobal.com")]
    desc = "MMEC is the group’s modular engineering and construction platform in Zhangjiagang. It combines a 77,000 m² covered workshop with a 166,000 m² modular yard adjacent to Gangxin Port."
    scope = "Heavy structural steel fabrication, modular plant and process module manufacturing, pipe spool fabrication, blasting and coating, logistics coordination, SPMT and port load-out."
    return profile("mmec", "MMEC", "Modern Modular Engineering & Construction Co., Ltd.", "Structural Steel · Modular Plants", "Zhangjiagang, Jiangsu", desc, scope, facts, "mmec-heavy-steel-assembly-refined.webp", "Large steel assemblies with access platforms during fabrication at MMEC")

def meem_profile():
    facts = [("Legal name","Modern Energy Equipment Manufacturing Co., Ltd."),("Address","1 Duanshan Road, Deji Subdistrict, Zhangjiagang, Jiangsu 215635, China"),("Scope","HRSG Pressure Parts · ACHE"),("Website","m-energy.com")]
    desc = "MEEM is the group’s newest manufacturing facility, dedicated to energy equipment for power generation and process industries. It brings 15+ years of sector experience into a purpose-built Zhangjiagang plant."
    scope = "Heat recovery steam generator (HRSG) pressure parts including finned tubes, headers, manifolds, harps and modules; air-cooled heat exchangers (ACHE); ASME pressure vessels; and modular structures for energy projects."
    return profile("meem", "MEEM", "Modern Energy Equipment Manufacturing Co., Ltd.", "HRSG Pressure Parts · ACHE", "Zhangjiagang, Jiangsu", desc, scope, facts, "mdhi-large-module-delivery-clean.webp", "Large fabricated module on an SPMT transporter in a manufacturing workshop")

def product_portfolio():
    from product_portfolio import render_portfolio
    return render_portfolio(page)

def quality_hse():
    from quality_hse import render_quality
    return render_quality(page)

def contact():
    from contact_page import render_contact
    return render_contact(page)

def legal_notice():
    content = inner_hero("Legal Notice", "How the Modern Group brand relates to MDHI, MMEC and MEEM.", "assets/images/mdhi_birdview.webp", 1)
    content += '''<section class="content-shell"><div class="legal-body"><h2>Brand and entity status</h2><p>“Modern Group” is a commercial brand used to present the connected manufacturing network of MDHI, MMEC and MEEM. It is not a separate incorporated legal entity.</p><h2>Operating companies</h2><p>Commercial enquiries and quotations may be coordinated across the network. Contracts, certifications, project execution, warranties and legal obligations remain with the relevant operating company. The three operating companies are:</p><ul><li><strong>Modern Heavy Industries (Taicang) Co., Ltd.</strong> — 169 Longjiang Road, Taicang Port Development Zone, Taicang, Jiangsu 215433, China</li><li><strong>Modern Modular Engineering &amp; Construction Co., Ltd.</strong> — 2669 Yanjiang Road, Daxin Town, Zhangjiagang, Jiangsu, China</li><li><strong>Modern Energy Equipment Manufacturing Co., Ltd.</strong> — 1 Duanshan Road, Deji Subdistrict, Zhangjiagang, Jiangsu 215635, China</li></ul><h2>Website information</h2><p>This site provides group-level orientation. Technical, contractual or certification information should be confirmed directly with the operating company responsible for the relevant product or project.</p><h2>Intellectual property</h2><p>All content on this site is provided for informational purposes. Trademarks, logos and product names belong to their respective owners.</p><h2>Limitation of liability</h2><p>Modern Group (as a brand) accepts no liability for decisions made on the basis of information published on this site. Always rely on the official documentation issued by the relevant operating company.</p></div></section>'''
    return page("Legal Notice | Modern Group", 1, None, "", "", "", content, "How the Modern Group brand relates to MDHI, MMEC and MEEM.")

def privacy():
    content = inner_hero("Privacy", "A concise statement for this informational corporate website.", "assets/images/mmec_birdview.webp", 1)
    content += '''<section class="content-shell"><div class="legal-body"><h2>Information collected</h2><p>This website does not provide an account system. The contact form collects your name, email address, selected product line, project region and message, and sends them by email to jackie.jo@mdhichina.com to handle your enquiry. Enquiries are not saved in a website database. The server uses a temporary, hashed network identifier to limit repeated submissions; email records and hosting logs may be retained.</p><h2>Data use</h2><p>Any personal data submitted through contact forms or emails is used solely to respond to your enquiry and to route it to the relevant operating company. Data is not used for unrelated marketing without your consent.</p><h2>Retention</h2><p>Enquiry records are retained only as long as necessary to handle the request and satisfy applicable business or legal record-keeping requirements, typically for the duration of the related commercial relationship plus any statutory period.</p><h2>External links</h2><p>Company websites linked from this site (mdhiglobal.com, mmecglobal.com, m-energy.com) apply their own privacy policies and data practices.</p><h2>Server logs and analytics</h2><p>The hosting provider may process standard technical logs. Any analytics or cookie tools introduced before launch should be disclosed here and configured in accordance with applicable law.</p><h2>Contact</h2><p>For privacy questions related to a specific enquiry, please contact the operating company to which your enquiry was directed. For questions about this website, use the contact form or write to the site administrator.</p><h2>Cookies</h2><p>This site does not currently use non-essential cookies. If cookies or similar technologies are added, a cookie banner and detailed cookie notice should be implemented.</p></div></section>'''
    return page("Privacy | Modern Group", 1, None, "", "", "", content, "A concise statement for this informational corporate website.")

# ---------- Write files ----------

pages = {
    "index.html": home(),
    "about/index.html": about(),
    "companies-locations/index.html": companies_locations(),
    "mdhi/index.html": mdhi_profile(),
    "mmec/index.html": mmec_profile(),
    "meem/index.html": meem_profile(),
    "product-portfolio/index.html": product_portfolio(),
    "quality-hse/index.html": quality_hse(),
    "contact/index.html": contact(),
    "legal-notice/index.html": legal_notice(),
    "privacy/index.html": privacy(),
}

for path, html_content in pages.items():
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("wrote", full)

# Simple logo placeholder
logo_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 48" width="64" height="48">
  <rect width="64" height="48" fill="#202326"/>
  <polygon points="10,38 20,10 32,30 44,10 54,38" fill="none" stroke="#bda16d" stroke-width="3"/>
</svg>'''
with open(os.path.join(BASE, "assets/images/logo.svg"), "w", encoding="utf-8") as f:
    f.write(logo_svg)
print("wrote logo.svg")

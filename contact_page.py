"""Illustrated Contact page; preserves the site's shared header and footer."""

from html import escape


PRODUCTS = (
    ("Structural Steel", "MDHI + MMEC", "contact-structural-steel.webp",
     "Long-span fabricated steel truss with diagonal bracing and an integrated walkway",
     "Project-specific steelwork for buildings, infrastructure and industrial facilities."),
    ("Modular Plants", "MMEC", "contact-modular-plants.webp",
     "Large three-level integrated process plant module",
     "Integrated modules, process modules, skids and port-oriented modular delivery."),
    ("HRSG Pressure Parts", "MEEM", "contact-hrsg.webp",
     "Complete installed HRSG, shown as an application illustration for pressure parts",
     "Headers, finned tubes, harps, manifolds and pressure-part assemblies."),
    ("Air-Cooled Heat Exchangers", "MEEM", "contact-ache.webp",
     "Multi-fan air-cooled heat exchanger array on a tall cross-braced support structure",
     "Air-cooled heat exchanger equipment for energy and process projects."),
)


def render_contact(page):
    cards = []
    for number, (name, company, image, description, scope) in enumerate(PRODUCTS, 1):
        selected = "true" if number == 1 else "false"
        cards.append(f'''<button class="contact-product" type="button" data-contact-product="{escape(name)}" data-company="{escape(company)}" aria-pressed="{selected}" aria-controls="enquiry-destination">
  <span class="contact-product-media"><img src="../assets/images/{image}" alt="{escape(description)}" width="960" height="640" decoding="async"><span class="contact-product-number" aria-hidden="true">{number:02d}</span></span>
  <span class="contact-product-copy"><span class="contact-product-title">{escape(name)}</span><span class="contact-product-description">{escape(scope)}</span><span class="contact-product-route"><span>{escape(company)}</span><span class="contact-product-check" aria-hidden="true">✓</span></span></span>
</button>''')
    options = "".join(f'<option value="{escape(name)}">{escape(name)}</option>' for name, *_ in PRODUCTS)
    content = f'''<section class="contact-hero" aria-labelledby="contact-title">
  <div class="contact-width"><div class="contact-hero-copy"><p class="contact-kicker">Modern Group · Contact</p><h1 id="contact-title">Contact &amp; Enquiries</h1><p>Start with the product scope. We will direct you to the relevant operating company.</p></div>
  </div>
</section>
<section class="contact-routing contact-width" aria-labelledby="routing-title">
  <div class="section-label"><span>01</span> Enquiry routing</div><h2 id="routing-title">Start with what you need to manufacture.</h2>
  <div class="contact-products" role="group" aria-label="Choose your product line">{''.join(cards)}</div>
</section>
<section class="contact-enquiry contact-width" id="enquiry-form" aria-labelledby="enquiry-title">
  <div class="contact-enquiry-heading"><div class="section-label"><span>02</span> Send an enquiry</div><h2 id="enquiry-title">Tell us about your project.</h2></div>
  <div class="contact-enquiry-layout">
    <aside class="contact-destination" aria-label="Enquiry responsibility">
      <img class="contact-destination-icon" src="../assets/images/work-route.svg" width="38" height="38" alt="">
      <p class="contact-kicker">Relevant operating company</p>
      <div id="enquiry-destination" aria-live="polite" aria-atomic="true"><h3 data-contact-company>MDHI + MMEC</h3><p class="contact-scope" data-contact-scope>Structural Steel</p>
        <div class="contact-company-emails" aria-labelledby="relevant-emails-title">
          <h4 id="relevant-emails-title">Enquiry emails for this product</h4>
          <dl>
            <div data-contact-email-company="MDHI"><dt>MDHI</dt><dd><a href="mailto:info@mdhiglobal.com">info@mdhiglobal.com</a></dd></div>
            <div data-contact-email-company="MMEC"><dt>MMEC</dt><dd><a href="mailto:build@mmecglobal.com">build@mmecglobal.com</a></dd></div>
            <div data-contact-email-company="MEEM" hidden><dt>MEEM</dt><dd><a href="mailto:info@m-energy.com">info@m-energy.com</a></dd></div>
          </dl>
          <noscript><p><a href="#company-emails">View all company enquiry emails</a></p></noscript>
        </div>
      </div>
      <div class="contact-responsibility"><h4><img src="../assets/images/work-responsibility.svg" width="22" height="22" alt="">Clear responsibility</h4><p>Commercial enquiries and quotations may be coordinated across the network. Contracts and project obligations remain with the responsible operating company.</p></div>
    </aside>
    <form class="contact-enquiry-form" data-contact-form action="send-enquiry.php" method="post" aria-label="Project enquiry" aria-describedby="contact-form-notice">
      <div hidden aria-hidden="true"><label for="website">Leave this field empty</label><input type="text" id="website" name="website" tabindex="-1" autocomplete="off"></div>
      <div class="contact-fields">
        <div class="contact-field"><label for="name">Name</label><input type="text" id="name" name="name" placeholder="Your name" autocomplete="name" required></div>
        <div class="contact-field"><label for="email">Email</label><input type="email" id="email" name="email" placeholder="you@company.com" autocomplete="email" required></div>
        <div class="contact-field"><label for="product">Product line</label><select id="product" name="product">{options}</select></div>
        <div class="contact-field"><label for="region">Project region</label><input type="text" id="region" name="region" placeholder="Country / region"></div>
        <div class="contact-field contact-field-wide"><label for="message">Message</label><textarea id="message" name="message" rows="5" placeholder="Tell us about your project requirements"></textarea></div>
      </div>
      <button type="submit" class="contact-send" data-contact-send>Send enquiry <span aria-hidden="true">→</span></button>
      <p class="contact-form-notice" id="contact-form-notice">All product enquiries are sent to <a href="mailto:jackie.jo@mdhichina.com">jackie.jo@mdhichina.com</a>.</p>
      <p class="contact-form-status" data-contact-status role="status" aria-live="polite"></p>
      <noscript><p class="contact-form-notice">You can submit this form without JavaScript. All enquiries go to jackie.jo@mdhichina.com.</p></noscript>
    </form>
  </div>
</section>
<section class="contact-email-directory contact-width" id="company-emails" aria-labelledby="company-emails-title">
  <div class="section-label"><span>03</span> Company enquiry emails</div>
  <h2 id="company-emails-title">Contact our companies directly.</h2>
  <div class="contact-email-grid">
    <article><h3>MDHI</h3><p>Modern Heavy Industries</p><a href="mailto:info@mdhiglobal.com">info@mdhiglobal.com <span aria-hidden="true">↗</span></a></article>
    <article><h3>MMEC</h3><p>Modern Modular Engineering &amp; Construction</p><a href="mailto:build@mmecglobal.com">build@mmecglobal.com <span aria-hidden="true">↗</span></a></article>
    <article><h3>MEEM</h3><p>Modern Energy Equipment Manufacturing</p><a href="mailto:info@m-energy.com">info@m-energy.com <span aria-hidden="true">↗</span></a></article>
  </div>
</section>'''
    result = page("Contact & Enquiries | Modern Group", 1, "Contact", "", "", "", content,
                  "Start with the product scope. We will direct you to the relevant operating company.")
    result = result.replace('<body class="inner">', '<body class="inner contact-page">')
    result = result.replace('</head>', '  <link rel="stylesheet" href="../assets/contact.css?v=20261023-routing">\n  <script defer src="../assets/contact.js?v=20261023-routing"></script>\n</head>')
    return result

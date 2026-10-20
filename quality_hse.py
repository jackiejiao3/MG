"""Quality & HSE management principles; no company document section."""
from html import escape

STEPS = (
    ("governance", "Set responsibility", "Bring responsibility into daily work.",
     "Clear responsibilities and coordination across quality, technical, production and HSE teams connect responsible manufacturing, environmental protection and employee well-being with everyday decisions.",
     ("Clear responsibilities", "Cross-functional coordination", "Continual improvement"), "Governance and responsibility"),
    ("risk", "Assess the risks", "Identify hazards. Define the controls.",
     "Identify workplace hazards, assess occupational health and safety risks and define practical controls. Risk-based planning helps teams prepare for routine work and unexpected situations.",
     ("Hazard identification", "Health and safety risk assessment", "Control measures"), "Risk assessment and control"),
    ("monitoring", "Monitor conditions", "Look closely at the working environment.",
     "Workplace monitoring focuses on chemical hazards and physical factors, while environmental monitoring considers water discharge, emissions and noise. Occupational health surveillance helps identify concerns and supports appropriate action.",
     ("Workplace chemical and physical factors", "Water, emissions and noise", "Occupational health examinations"), "Workplace and environmental monitoring"),
    ("improvement", "Improve operations", "Reduce errors, waste and resource use.",
     "Efficient engineering, careful procurement and resource-conscious production help reduce errors and manufacturing waste. Improvement priorities include energy-efficient equipment, emission control and tracking water use.",
     ("Efficient engineering", "Resource-efficient equipment", "Waste and emission reduction"), "Operational improvement"),
)

COMPANIES = (
    ("MDHI", "Structural steel fabrication", "mdhi"),
    ("MMEC", "Structural steel & modular plants", "mmec"),
    ("MEEM", "HRSG pressure parts & air-cooled equipment", "meem"),
)

ICONS = {
    "safety": '<path d="M9 31v-6a15 15 0 0 1 30 0v6M6 31h36v7H6zM24 9v17M14 14v8M34 14v8"/>',
    "improve": '<path d="M37 17a15 15 0 0 0-25-4l-5 5m0-9v9h9M11 31a15 15 0 0 0 25 4l5-5m0 9v-9h-9"/><path d="m18 24 4 4 8-9"/>',
    "environment": '<path d="M12 35C2 17 25 9 40 8c0 18-5 31-20 31M9 41l22-22M19 31l-1-10M25 25l10 1"/>',
}

# Replace None with an image filename in assets/images when photography is available.
PHOTOS = {"quality": "quality-hse-workplace-improvement.webp", "safety": "quality-hse-protect-people.webp", "improve": "quality-hse-prepare-train-respond.webp", "environment": "quality-hse-resources.webp"}


def photo_slot(key, label):
    if PHOTOS[key]:
        return f'<figure class="qh-photo"><img src="../assets/images/{escape(PHOTOS[key])}" alt="{escape(label)}" loading="lazy"><figcaption>{escape(label)}</figcaption></figure>'
    return f'''<figure class="qh-photo-placeholder"><svg viewBox="0 0 48 48" fill="none" aria-hidden="true"><rect x="7" y="9" width="34" height="30" rx="2"/><circle cx="17" cy="19" r="3"/><path d="m9 35 11-10 7 6 6-8 7 12"/></svg><figcaption><strong>{escape(label)}</strong><span>Photography to come</span></figcaption></figure>'''


def render_quality(page):
    company_links = ''.join(f'<a href="../{slug}/index.html">{code} <span aria-hidden="true">↗</span></a>' for code, _, slug in COMPANIES)
    content = f'''<a class="qh-skip" href="#quality-process">Skip to quality and HSE content</a>
<section class="qh-hero"><div class="qh-width qh-hero-grid"><div class="qh-hero-copy"><p class="qh-kicker">Modern Group / Quality &amp; HSE</p><h1>Quality &amp; HSE.<br><em>Care in<br>every detail.</em></h1><p class="qh-lead">Quality, people and the environment are connected. Clear responsibility, practical risk controls and continual improvement guide the way we work.</p><a class="qh-button qh-button-dark" href="#quality-process">Explore our approach <span aria-hidden="true">↓</span></a><p class="qh-hero-footnote">Quality · Health &amp; Safety · Environment</p></div><div class="qh-hero-visual"><img src="../assets/images/quality-hse-safety-training.webp" srcset="../assets/images/quality-hse-safety-training-800.webp 800w, ../assets/images/quality-hse-safety-training.webp 1586w" sizes="(max-width:760px) calc(100vw - 62px), (max-width:1536px) 43vw, 630px" alt="Safety officer briefing helmeted workers in a factory yard" width="1586" height="992" decoding="async" fetchpriority="high"><span class="qh-photo-label">Safety training / Workplace awareness</span><div class="qh-visual-caption"><span aria-hidden="true">Q</span><p>Shared principles.<br><em>Company-level accountability.</em></p></div></div></div><nav class="qh-width qh-pillar-nav" aria-label="Quality and HSE sections"><a href="#quality-process"><span>01 / Quality</span><strong>Responsible operations.</strong><b aria-hidden="true">↘</b></a><a href="#hse-principles"><span>02 / Health, safety &amp; environment</span><strong>Care in how we work.</strong><b aria-hidden="true">↘</b></a></nav></section>
<aside class="qh-accountability qh-width" aria-label="Responsibility"><div><span class="qh-small-mark" aria-hidden="true">↗</span><p><strong>One shared identity. Clear responsibility.</strong> Shared principles guide the network. Project-level quality and HSE responsibility remains with the company undertaking the work.</p></div><div class="qh-company-links">{company_links}</div></aside>
<section class="qh-quality qh-width" id="quality-process" aria-labelledby="quality-heading"><div class="qh-section-heading"><div><p class="qh-kicker">01 / Quality &amp; responsible operations</p><h2 id="quality-heading">Responsible operations.<br><em>A practical management approach.</em></h2></div><p>Clear responsibilities, risk assessment, workplace monitoring and continual improvement provide a practical framework for responsible manufacturing.</p></div><div class="qh-process"><div class="qh-process-navigation" aria-label="Quality process steps">'''
    for i, (key, title, *_rest) in enumerate(STEPS, 1):
        content += f'<button type="button" id="step-{key}" data-qh-step="{key}" aria-controls="panel-{key}"><span>{i:02d}</span><strong>{escape(title)}</strong><b aria-hidden="true">↗</b></button>'
    content += '</div><div class="qh-process-content">'
    for i, (key, title, headline, copy, records, topic) in enumerate(STEPS, 1):
        items = ''.join(f'<li><span aria-hidden="true">✓</span>{escape(record)}</li>' for record in records)
        content += f'''<article class="qh-process-panel" id="panel-{key}" data-qh-panel="{key}" aria-labelledby="step-{key}"><p class="qh-panel-eyebrow">Step {i:02d} / {escape(topic)}</p><h3>{escape(headline)}</h3><p>{escape(copy)}</p><div class="qh-records"><h4>Management priorities</h4><ul>{items}</ul></div></article>'''
    content += f'''</div></div><div class="qh-quality-bottom">{photo_slot('quality', 'Manufacturing & workplace improvement')}<div class="qh-quality-note"><p class="qh-kicker">Improve the way work is done</p><h3>Efficiency with responsibility.</h3><p>Efficient engineering, careful procurement and improved equipment support fewer errors, less manufacturing waste and more responsible resource use.</p><a href="../contact/index.html">Discuss your requirements <span aria-hidden="true">↗</span></a></div></div></section>
<section class="qh-hse" id="hse-principles" aria-labelledby="hse-heading"><div class="qh-width"><div class="qh-section-heading"><div><p class="qh-kicker">02 / Health, safety &amp; environment</p><h2 id="hse-heading">Care beyond<br><em>the finished product.</em></h2></div><p>Protecting people starts with understanding workplace risks. Training, emergency preparedness and responsible resource use support safer, more sustainable operations.</p></div><div class="qh-hse-grid">'''
    hse = (
        ("safety", "01", "Protect people.", "Occupational health & safety", "Preventing harm is the priority. Risk assessment, occupational health surveillance and monitoring of workplace hazards help protect employees throughout daily operations.", ("Harm prevention", "Occupational health", "Workplace monitoring"), "People & safe working practices"),
        ("improve", "02", "Prepare. Train. Respond.", "Training & emergency preparedness", "Training in workshop and fire safety, environmental incidents and spill response helps teams understand their responsibilities. Practical preparation and clear response plans support effective action when an emergency occurs.", ("Workshop & fire safety", "Emergency preparedness", "Spill response"), "Safety training & team communication"),
        ("environment", "03", "Use resources wisely.", "Environmental protection", "Use energy and water efficiently, control emissions and reduce manufacturing waste. Recycling, material reuse and responsible handling of hazardous waste help limit the environmental impact of operations.", ("Energy efficiency", "Emission reduction", "Waste treatment"), "Environmental practices on site"),
    )
    for key, number, headline, topic, copy, tags, photo in hse:
        tag_markup = ''.join(f'<li>{escape(tag)}</li>' for tag in tags)
        content += f'''<article class="qh-hse-card qh-{key}"><div class="qh-hse-card-top"><svg viewBox="0 0 48 48" fill="none" aria-hidden="true">{ICONS[key]}</svg><span>{number}</span></div><p class="qh-kicker">{topic}</p><h3>{headline}</h3><p class="qh-hse-copy">{copy}</p><ul>{tag_markup}</ul>{photo_slot(key, photo)}</article>'''
    content += '''</div></div></section>
<section class="qh-contact"><div class="qh-width qh-contact-layout"><div><p class="qh-kicker">Connect with the responsible company</p><h2>Have a quality or HSE question?</h2><p>Tell us about your quality, workplace safety or environmental requirements. We will connect you with the responsible operating company.</p></div><a class="qh-button qh-button-gold" href="../contact/index.html">Start a conversation <span aria-hidden="true">↗</span></a></div></section>'''
    return page("Quality & HSE | Modern Group", 1, "Quality & HSE", "", "", "", content,
                "Our approach to quality, health, safety and the environment: clear responsibility, risk assessment, occupational health and resource-efficient operations.")

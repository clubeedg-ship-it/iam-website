import os
import re

# Dynamically determine project root (parent of 'tools' directory)
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTIALS_DIR = os.path.join(ROOT_DIR, 'partials')

# Translation Dictionary for automated replacement in EN partials
TRANSLATIONS = {
    # Navigation
    '>Producten<': '>Products<',
    '>Interactieve Vloer<': '>Interactive Floor<',
    '>Interactieve Muur<': '>Interactive Wall<',
    '>Interactieve Zandbak<': '>Interactive Sandbox<',
    '>Interactieve Klimwand<': '>Interactive Climbing Wall<',
    '>Mobiele Vloer<': '>Mobile Floor<',
    '>Software & Maatwerk<': '>Software & Customization<',
    '>Mogelijkheden<': '>Applications<',
    '>Bouw een Park<': '>Build a Park<',
    '>3D Spellen<': '>3D Games<',
    '>Parken & Speelhallen<': '>Parks & Arcades<',
    '>Onderwijs<': '>Education<',
    '>Zorg & Revalidatie<': '>Care & Rehabilitation<',
    '>Over Ons<': '>About Us<',
    '>Over InterActiveMove<': '>About InterActiveMove<',
    '>Prijzen<': '>Prices<',
    '>Contact<': '>Contact<',
    
    # Common Buttons/Labels
    '>Ontdek onze producten<': '>Discover our products<',
    '>Meer info<': '>More info<',
    '>Bekijk Prijzen<': '>View Prices<',
    '>Offerte Aanvragen<': '>Request Quote<',
    '>Offerte aanvragen<': '>Request Quote<',
    '>Vraag brochure aan<': '>Request brochure<',
    '>Populair<': '>Popular<',
    '>Verstuur Bericht<': '>Send Message<',
    '>VERSTUUR BERICHT<': '>SEND MESSAGE<',
    
    # Footer / Common Headings
    '>Beweeg, Leer en Speel met InterActiveMove<': '>Move, Learn and Play with InterActiveMove<',
    '>Alle rechten voorbehouden<': '>All rights reserved<',
    '>Onze Producten<': '>Our Products<',
    '>Kenmerken<': '>Features<',
    '>Veelgestelde Vragen<': '>Frequently Asked Questions<',
    '>Neem contact op<': '>Contact us<',
    '>Praktische informatie<': '>Practical information<',
    '>Quick Links<': '>Quick Links<',
    '>Onze Missie<': '>Our Mission<',
    '>Onze Visie<': '>Our Vision<',
    
    # Contact Form Placeholders
    'placeholder="Naam"': 'placeholder="Name"',
    'aria-label="Naam"': 'aria-label="Name"',
    'placeholder="Bedrijf / Organisatie"': 'placeholder="Company / Organization"',
    'aria-label="Bedrijf"': 'aria-label="Company"',
    'placeholder="Waar kunnen wij u mee helpen?"': 'placeholder="How can we help you?"',
    
    # Language Toggle Logic (Active Class)
    # We will handle toggle active state programmatically or by regex substitution specific to the button
}

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

def process_file(file_path):
    filename = os.path.basename(file_path)
    rel_path = os.path.relpath(file_path, ROOT_DIR)
    
    if 'partials' in rel_path or filename == 'index.html':
        return # Skip index.html (already done) and existing partials
    
    print(f"Processing {rel_path}...")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find the main content blocks
    # We look for header, mobile-nav, main, footer
    # Because valid HTML order is usually this. 
    # But files might have global canvas before header.
    
    # Strategy: Capture everything between <body> and <script... that is NOT the canvas>
    # Better: Identify the start of <header> and the end of <footer>.
    
    header_start = content.find('<header>')
    footer_end = content.find('</footer>') + 9
    
    if header_start == -1 or footer_end == 8:
        print(f"  Skipping {rel_path}: Could not find <header> or <footer>")
        return

    # Also include mobile nav if it exists outside header/footer (it does in 3d-spellen.html)
    # It usually comes after header.
    # Actually, we want to grab the range from <header> to <footer> inclusive.
    # And verify if there is a <div class="mobile-nav"> outside?
    # In 3d-spellen (Step 863):
    # <header>...</header>
    # <div class="mobile-nav" id="mobileNav">...</div>
    # <main>...</main>
    # <footer>...</footer>
    
    # So we should capture from <header> to <footer>.
    body_content = content[header_start:footer_end]
    
    # START PARTIALS GENERATION
    
    # 1. NL Partial
    # We need to construct the relative path for partials
    # e.g. products/interactieve-vloer.html -> partials/products/interactieve-vloer-nl.html
    partial_rel_path = os.path.join('partials', os.path.dirname(rel_path), filename.replace('.html', '-nl.html'))
    partial_abs_path = os.path.join(ROOT_DIR, partial_rel_path)
    
    ensure_dir(partial_abs_path)
    
    with open(partial_abs_path, 'w', encoding='utf-8') as f:
        f.write(body_content)
    print(f"  Created NL partial: {partial_rel_path}")

    # 2. EN Partial
    en_content = body_content
    for nl, en in TRANSLATIONS.items():
        en_content = en_content.replace(nl, en)
    
    # Fix Language Toggle in EN Partial
    # NL Button: remove active. EN Button: add active.
    # Pattern: <button class="lang-btn active">NL</button> ... <button class="lang-btn">EN</button>
    # Target: <button class="lang-btn">NL</button> ... <button class="lang-btn active">EN</button>
    en_content = re.sub(r'class="lang-btn active">NL<', 'class="lang-btn">NL<', en_content)
    en_content = re.sub(r'class="lang-btn">EN<', 'class="lang-btn active">EN<', en_content)
    
    # Also update HTMX attributes in partial buttons (Wait, the original files don't have HTMX attributes yet!)
    # I need to ADD HTMX attributes to the partials.
    
    # Add HTMX to NL Partial
    # We need to compute the path to the OTHER partial.
    # If we are in `products/interactieve-vloer.html`, the partial path we load is `../partials/products/interactieve-vloer-en.html`?
    # NO. 
    # If the USER is at `products/interactieve-vloer.html`, the browser URL is `products/interactieve-vloer.html`.
    # To load `partials/products/interactieve-vloer-en.html`, the path relative to document is `../partials/products/interactieve-vloer-en.html`.
    
    # Calculate depth
    depth = rel_path.count(os.sep)
    prefix = '../' * depth + 'partials/'
    if depth > 0:
        # e.g. products/foo.html -> depth 1. prefix = '../partials/'
        # partial path relative to partial folder is products/foo-en.html
        # Joined: ../partials/products/foo-en.html. Correct.
        pass
    else:
        # index.html -> depth 0. prefix = 'partials/'
        pass
        
    en_partial_target = f"{prefix}{os.path.dirname(rel_path)}/{filename.replace('.html', '-en.html')}".replace('//', '/').lstrip('/')
    nl_partial_target = f"{prefix}{os.path.dirname(rel_path)}/{filename.replace('.html', '-nl.html')}".replace('//', '/').lstrip('/')
    
    def add_htmx_to_buttons(text, my_lang):
        # Find NL button
        # <button class="lang-btn( active)?">NL</button>
        # We want to add hx-get, hx-target, hx-swap, hx-push-url
        
        # NL Button
        nl_attrs = f' hx-get="{nl_partial_target}" hx-target="#page-wrapper" hx-swap="innerHTML" hx-push-url="?lang=nl"'
        text = re.sub(r'(<button class="lang-btn(?: active)?")>NL</button>', r'\1' + nl_attrs + '>NL</button>', text)
        
        # EN Button
        en_attrs = f' hx-get="{en_partial_target}" hx-target="#page-wrapper" hx-swap="innerHTML" hx-push-url="?lang=en"'
        text = re.sub(r'(<button class="lang-btn(?: active)?")>EN</button>', r'\1' + en_attrs + '>EN</button>', text)
        
        return text

    # Rewrite NL Partial with HTMX
    with open(partial_abs_path, 'r', encoding='utf-8') as f:
        nl_content_saved = f.read()
    
    nl_content_final = add_htmx_to_buttons(nl_content_saved, 'nl')
    with open(partial_abs_path, 'w', encoding='utf-8') as f:
        f.write(nl_content_final)

    # Rewrite EN Partial with HTMX
    en_content_final = add_htmx_to_buttons(en_content, 'en')
    
    partial_en_rel_path = os.path.join('partials', os.path.dirname(rel_path), filename.replace('.html', '-en.html'))
    partial_en_abs_path = os.path.join(ROOT_DIR, partial_en_rel_path)
    
    with open(partial_en_abs_path, 'w', encoding='utf-8') as f:
        f.write(en_content_final)
    print(f"  Created EN partial: {partial_en_rel_path}")
    
    # 3. Modify Original File
    # We replace the body_content with <div id="page-wrapper">{body_content}</div>
    # AND add the script.
    
    new_page_content = content.replace(body_content, f'<div id="page-wrapper">\n{nl_content_final}\n</div>')
    
    # Add Script if not present
    script_code = f"""
    <script>
        // Check URL on load
        document.addEventListener('DOMContentLoaded', () => {{
            const params = new URLSearchParams(window.location.search);
            const lang = params.get('lang');
            if (lang === 'en') {{
                htmx.ajax('GET', '{en_partial_target}', '#page-wrapper');
            }}
        }});
    </script>
    """
    
    if 'DOMContentLoaded' not in new_page_content:
        # Insert before </body>
        new_page_content = new_page_content.replace('</body>', f'{script_code}\n</body>')
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_page_content)
    print(f"  Updated original file: {rel_path}")


def main():
    for root, dirs, files in os.walk(ROOT_DIR):
        for file in files:
            if file.endswith('.html'):
                process_file(os.path.join(root, file))

if __name__ == '__main__':
    main()

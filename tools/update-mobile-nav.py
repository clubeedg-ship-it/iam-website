#!/usr/bin/env python3
"""Replace flat mobile-nav with dropdown version across all HTML files."""
import re, glob, os

ROOT_MOBILE_NAV = '''        <div class="mobile-nav" id="mobileNav">
            <a href="index.html" onclick="closeMobileNav()">Home</a>
            <div class="mobile-dropdown">
                <button class="mobile-dropdown-toggle" onclick="toggleMobileDropdown(this)">
                    Producten <svg class="mobile-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
                </button>
                <div class="mobile-dropdown-items">
                    <a href="products/interactieve-vloer.html">Interactieve Vloer</a>
                    <a href="products/interactieve-muur.html">Interactieve Muur</a>
                    <a href="products/interactieve-zandbak.html">Interactieve Zandbak</a>
                    <a href="products/interactieve-klimwand.html">Interactieve Klimwand</a>
                    <a href="products/mobiele-vloer.html">Mobiele Vloer</a>
                    <a href="products/software-maatwerk.html">Software &amp; Maatwerk</a>
                </div>
            </div>
            <div class="mobile-dropdown">
                <button class="mobile-dropdown-toggle" onclick="toggleMobileDropdown(this)">
                    Mogelijkheden <svg class="mobile-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
                </button>
                <div class="mobile-dropdown-items">
                    <a href="bouw-een-park.html">Bouw een Park</a>
                    <a href="3d-spellen.html">3D Spellen</a>
                    <a href="parken-speelhallen.html">Parken &amp; Speelhallen</a>
                    <a href="onderwijs.html">Onderwijs</a>
                    <a href="zorg-revalidatie.html">Zorg &amp; Revalidatie</a>
                </div>
            </div>
            <div class="mobile-dropdown">
                <button class="mobile-dropdown-toggle" onclick="toggleMobileDropdown(this)">
                    Over Ons <svg class="mobile-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
                </button>
                <div class="mobile-dropdown-items">
                    <a href="over-ons.html">Over InterActiveMove</a>
                    <a href="prijzen.html">Prijzen</a>
                    <a href="index.html#contact" onclick="closeMobileNav()">Contact</a>
                </div>
            </div>
            <a href="blog.html">Blog</a>
            <a href="index.html#contact" onclick="closeMobileNav()">Contact</a>
        </div>'''

# For product pages (prefix ../)
PRODUCT_MOBILE_NAV = ROOT_MOBILE_NAV.replace('href="products/', 'href="../products/').replace('href="index.html', 'href="../index.html').replace('href="bouw-een-park.html', 'href="../bouw-een-park.html').replace('href="3d-spellen.html', 'href="../3d-spellen.html').replace('href="parken-speelhallen.html', 'href="../parken-speelhallen.html').replace('href="onderwijs.html', 'href="../onderwijs.html').replace('href="zorg-revalidatie.html', 'href="../zorg-revalidatie.html').replace('href="over-ons.html', 'href="../over-ons.html').replace('href="prijzen.html', 'href="../prijzen.html').replace('href="blog.html', 'href="../blog.html')

# JS to inject if not present
TOGGLE_JS = '''
        function toggleMobileDropdown(btn) {
            const dropdown = btn.parentElement;
            dropdown.classList.toggle('open');
        }'''

def replace_mobile_nav(filepath, nav_html):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Match the mobile-nav div (from opening to closing)
    pattern = r'<div class="mobile-nav" id="mobileNav">.*?</div>\s*(?=\n\s*<main|\n\s*<div|\n\s*$)'
    match = re.search(pattern, content, re.DOTALL)
    if not match:
        # Try simpler pattern
        pattern = r'(<div class="mobile-nav" id="mobileNav">)(.*?)(</div>)\s*\n'
        # Find start and count divs to find matching close
        start = content.find('<div class="mobile-nav" id="mobileNav">')
        if start == -1:
            print(f"  SKIP (no mobile-nav): {filepath}")
            return False
        
        # Find the matching closing div
        depth = 0
        i = start
        while i < len(content):
            if content[i:i+4] == '<div':
                depth += 1
            elif content[i:i+6] == '</div>':
                depth -= 1
                if depth == 0:
                    end = i + 6
                    break
            i += 1
        else:
            print(f"  SKIP (no matching close): {filepath}")
            return False
        
        old = content[start:end]
        content = content[:start] + nav_html + content[end:]
    else:
        content = content[:match.start()] + nav_html + content[match.end():]
    
    # Add toggleMobileDropdown if not present
    if 'toggleMobileDropdown' not in content or 'function toggleMobileDropdown' not in content:
        # Add it after closeMobileNav function
        insert_point = content.find('function closeMobileNav')
        if insert_point != -1:
            # Find the closing brace of closeMobileNav
            brace_count = 0
            i = content.index('{', insert_point)
            while i < len(content):
                if content[i] == '{': brace_count += 1
                elif content[i] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        content = content[:i+1] + TOGGLE_JS + content[i+1:]
                        break
                i += 1
    
    with open(filepath, 'w') as f:
        f.write(content)
    print(f"  OK: {filepath}")
    return True

os.chdir('/home/adminuser/iam-website')

# Root-level pages (skip index.html which is already done)
root_files = glob.glob('*.html')
for f in sorted(root_files):
    if f in ('index.html', 'blog.html'):
        continue
    replace_mobile_nav(f, ROOT_MOBILE_NAV)

# Product pages
product_files = glob.glob('products/*.html')
for f in sorted(product_files):
    replace_mobile_nav(f, PRODUCT_MOBILE_NAV)

# Partials with mobile nav
partial_files = glob.glob('partials/*.html') + glob.glob('partials/**/*.html', recursive=True)
for f in sorted(partial_files):
    with open(f) as fh:
        if 'mobile-nav' in fh.read():
            # Partials are swapped into root context
            replace_mobile_nav(f, ROOT_MOBILE_NAV)

print("\nDone!")

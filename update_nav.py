#!/usr/bin/env python3
"""Add 2-in-1 Vloer & Muur as first item in Products dropdown across all HTML files."""
import os
import re
import glob

ROOT = '/tmp/iam-2in1-nav'

def get_all_html_files():
    files = []
    # Root level
    for f in glob.glob(os.path.join(ROOT, '*.html')):
        files.append(f)
    # Products
    for f in glob.glob(os.path.join(ROOT, 'products', '*.html')):
        files.append(f)
    # Partials root
    for f in glob.glob(os.path.join(ROOT, 'partials', '*.html')):
        files.append(f)
    # Partials products
    for f in glob.glob(os.path.join(ROOT, 'partials', 'products', '*.html')):
        files.append(f)
    return files

def is_english(filepath):
    """Check if file is English version."""
    basename = os.path.basename(filepath)
    return basename.endswith('-en.html')

def is_in_products_dir(filepath):
    """Check if file is in products/ or partials/products/ directory."""
    rel = os.path.relpath(filepath, ROOT)
    return rel.startswith('products/') or rel.startswith('partials/products/')

def is_product_shell(filepath):
    """Check if file is a product shell (products/*.html, NOT partials)."""
    rel = os.path.relpath(filepath, ROOT)
    return rel.startswith('products/') and not rel.startswith('partials/')

def add_desktop_nav(content, filepath):
    """Add 2-in-1 as first item in desktop Products dropdown."""
    en = is_english(filepath)
    in_products = is_in_products_dir(filepath)

    label = "2-in-1 Floor & Wall" if en else "2-in-1 Vloer & Muur"

    if in_products:
        href = "2-in-1-vloer-muur.html"
    else:
        href = "products/2-in-1-vloer-muur.html"

    new_link = f'<a href="{href}">{label}</a>'

    # Find the Products/Producten dropdown-menu and insert before the first <a> inside it
    # Pattern: button with Producten/Products, then dropdown-menu div, then first <a>
    # We need to insert after <div class="dropdown-menu"> and before the first <a>

    # Match the dropdown-menu after Producten/Products button
    pattern = r'(<button class="nav-link">Producte?n?s?</button>\s*<div class="dropdown-menu">\s*)'

    def replacer(m):
        existing = m.group(1)
        # Get the indentation of the first <a> that follows
        # Find what comes after in the original content
        pos = m.end()
        # Look at the next line to get indentation
        remaining = content[pos:]
        indent_match = re.match(r'(\s*)<a ', remaining)
        indent = indent_match.group(1) if indent_match else '                    '
        return existing + indent + new_link + '\n'

    result = re.sub(pattern, replacer, content, count=1)
    return result

def add_mobile_nav(content, filepath):
    """Add 2-in-1 as first item in mobile Products dropdown."""
    en = is_english(filepath)
    is_prod_shell = is_product_shell(filepath)
    in_products = is_in_products_dir(filepath)

    label_escaped = "2-in-1 Floor &amp; Wall" if en else "2-in-1 Vloer &amp; Muur"
    label_plain = "2-in-1 Floor & Wall" if en else "2-in-1 Vloer & Muur"

    # Determine href based on mobile nav patterns in the file
    # Product shells use ../products/ prefix for mobile
    # Product partials use products/ prefix for mobile (matching existing pattern)
    # Root files use products/ prefix for mobile
    if is_prod_shell:
        href = "../products/2-in-1-vloer-muur.html"
    else:
        href = "products/2-in-1-vloer-muur.html"

    new_link = f'<a href="{href}">{label_escaped}</a>'

    # Find mobile-dropdown-items after Producten/Products toggle
    pattern = r'(Producte?n?s?\s*<svg class="mobile-chevron".*?</svg>\s*</button>\s*<div class="mobile-dropdown-items">\s*)'

    def replacer(m):
        existing = m.group(1)
        pos = m.end()
        remaining = content[pos:]
        indent_match = re.match(r'(\s*)<a ', remaining)
        indent = indent_match.group(1) if indent_match else '                    '
        return existing + indent + new_link + '\n'

    result = re.sub(pattern, replacer, content, count=1, flags=re.DOTALL)
    return result

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already has 2-in-1
    if '2-in-1' in content:
        print(f"  SKIP (already has 2-in-1): {os.path.relpath(filepath, ROOT)}")
        return False

    original = content

    # Add to desktop nav
    content = add_desktop_nav(content, filepath)

    # Add to mobile nav
    content = add_mobile_nav(content, filepath)

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  UPDATED: {os.path.relpath(filepath, ROOT)}")
        return True
    else:
        print(f"  NO CHANGE: {os.path.relpath(filepath, ROOT)}")
        return False

def main():
    files = get_all_html_files()
    print(f"Found {len(files)} HTML files")

    updated = 0
    for f in sorted(files):
        if process_file(f):
            updated += 1

    print(f"\nUpdated {updated} files")

if __name__ == '__main__':
    main()

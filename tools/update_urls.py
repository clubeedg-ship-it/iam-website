import os
import re

# Define the mapping (old_href -> new_clean_url)
# We search for both versions: with and without leading /
# and handle the .html extension.

mapping = {
    r'over-ons\.html': '/about',
    r'prijzen\.html': '/pricing',
    r'blog\.html': '/blog',
    r'onderwijs\.html': '/education',
    r'zorg-revalidatie\.html': '/healthcare',
    r'parken-speelhallen\.html': '/entertainment',
    r'bouw-een-park\.html': '/build-a-park',
    r'3d-spellen\.html': '/3d-games',
    r'maak-je-spel\.html': '/create-your-game',
    r'word-partner\.html': '/partner',
    r'privacybeleid\.html': '/privacy',
    r'cookiebeleid\.html': '/cookies',
    r'toegankelijkheid\.html': '/accessibility',
    r'index\.html': '/',
    r'products/2-in-1-vloer-muur\.html': '/products/2-in-1-floor-wall',
    r'products/interactieve-vloer\.html': '/products/interactive-floor',
    r'products/interactieve-muur\.html': '/products/interactive-wall',
    r'products/interactieve-zandbak\.html': '/products/interactive-sandbox',
    r'products/interactieve-klimwand\.html': '/products/interactive-climbing-wall',
    r'products/mobiele-vloer\.html': '/products/mobile-floor',
    r'products/software-maatwerk\.html': '/products/software',
    r'products/interactieve-tekeningen\.html': '/products/interactive-drawings',
    r'2-in-1-vloer-muur\.html': '/products/2-in-1-floor-wall',
    r'interactieve-vloer\.html': '/products/interactive-floor',
    r'interactieve-muur\.html': '/products/interactive-wall',
    r'interactieve-zandbak\.html': '/products/interactive-sandbox',
    r'interactieve-klimwand\.html': '/products/interactive-climbing-wall',
    r'mobiele-vloer\.html': '/products/mobile-floor',
    r'software-maatwerk\.html': '/products/software',
    r'interactieve-tekeningen\.html': '/products/interactive-drawings',
}

# Directories to process
directories = [
    '/home/adminuser/iam-website',
    '/home/adminuser/iam-website/products',
    '/home/adminuser/iam-website/partials',
    '/home/adminuser/iam-website/partials/products',
    '/home/adminuser/iam-website/js'
]

def update_content(content, is_in_products_dir=False):
    # Update href="path" and href="/path"
    for old, new in mapping.items():
        # Sitemap loc update: <loc>https://interactivemove.nl/over-ons.html</loc> -> <loc>https://interactivemove.nl/about</loc>
        content = re.sub(f'<loc>https://interactivemove.nl/{old}</loc>', f'<loc>https://interactivemove.nl{new}</loc>', content)

        # Handle index.html specially to avoid replacing sub-parts of words
        if old == r'index\.html':
            pattern_href = r'href="(\.\./)?index\.html"'
            content = re.sub(pattern_href, 'href="/"', content)
            pattern_js = r'[\'"](\.\./)?index\.html[\'"]'
            content = re.sub(pattern_js, '"/"', content)
            continue

        # For relative paths starting with ../
        if is_in_products_dir:
            # href="../over-ons.html" -> href="/about"
            content = re.sub(f'href="\.\./{old}"', f'href="{new}"', content)
            # action="../over-ons.html" -> action="/about"
            content = re.sub(f'action="\.\./{old}"', f'action="{new}"', content)
            # JS: '../over-ons.html' -> '/about'
            content = re.sub(f'\'\.\./{old}\'', f'\'{new}\'', content)
            content = re.sub(f'"\.\./{old}"', f'"{new}"', content)

        # Standard relative and absolute paths
        content = re.sub(f'href="{old}"', f'href="{new}"', content)
        content = re.sub(f'href="/{old}"', f'href="{new}"', content)
        content = re.sub(f'action="{old}"', f'action="{new}"', content)
        content = re.sub(f'action="/{old}"', f'action="{new}"', content)
        content = re.sub(f'\'{old}\'', f'\'{new}\'', content)
        content = re.sub(f'"{old}"', f'"{new}"', content)
        
    return content

for directory in directories:
    is_in_products_dir = directory.endswith('/products')
    for filename in os.listdir(directory):
        if filename.endswith('.html') or filename.endswith('.js') or filename == 'sitemap.xml':
            filepath = os.path.join(directory, filename)
            if os.path.isfile(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = update_content(content, is_in_products_dir)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated {filepath}")

print("Update complete.")

#!/usr/bin/env python3
"""Generate all 22 shell pages from template."""
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

TEMPLATE = r'''<!DOCTYPE html>
<html lang="nl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>%%PAGE_TITLE%%</title>
    <meta name="description" content="%%PAGE_DESCRIPTION%%">
    <link rel="icon" href="%%BASE_PATH%%media/icon.png" type="image/png">
    <link rel="stylesheet" href="%%BASE_PATH%%styles.css">
    <script src="/js/htmx.min.js"></script>
    <!-- Google Tag Manager -->
    <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','GTM-KPX78C22');</script>
</head>
<body data-page="%%PAGE_SLUG%%" data-base="%%BASE_PATH%%" data-section="%%SECTION%%">
    <!-- Google Tag Manager (noscript) -->
    <noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-KPX78C22" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    
    <a href="#main-content" class="skip-link">Ga naar inhoud</a>
    
    <div id="global-canvas-container">
        <canvas id="projector-canvas"></canvas>
    </div>
    
    <div id="page-wrapper">
        <!-- NAV (permanent, bilingual) -->
        <header>
            <a href="%%BASE_PATH%%index.html"><img src="%%BASE_PATH%%media/logo-final.png" alt="InterActiveMove" class="logo-img"></a>
            <nav>
                <ul class="nav-menu">
                    <li class="nav-item dropdown">
                        <button class="nav-link"><span class="lang-nl">Producten</span><span class="lang-en">Products</span></button>
                        <div class="dropdown-menu">
                            <a href="%%BASE_PATH%%products/2-in-1-vloer-muur.html">2-in-1 Vloer &amp; Muur</a>
                            <a href="%%BASE_PATH%%products/interactieve-vloer.html">Interactieve Vloer</a>
                            <a href="%%BASE_PATH%%products/interactieve-muur.html">Interactieve Muur</a>
                            <a href="%%BASE_PATH%%products/interactieve-zandbak.html">Interactieve Zandbak</a>
                            <a href="%%BASE_PATH%%products/interactieve-klimwand.html">Interactieve Klimwand</a>
                            <a href="%%BASE_PATH%%products/mobiele-vloer.html">Mobiele Vloer</a>
                            <a href="%%BASE_PATH%%products/software-maatwerk.html">Software &amp; Maatwerk</a>
                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <button class="nav-link"><span class="lang-nl">Mogelijkheden</span><span class="lang-en">Solutions</span></button>
                        <div class="dropdown-menu">
                            <a href="%%BASE_PATH%%bouw-een-park.html"><span class="lang-nl">Bouw een Park</span><span class="lang-en">Build a Park</span></a>
                            <a href="%%BASE_PATH%%3d-spellen.html">3D <span class="lang-nl">Spellen</span><span class="lang-en">Games</span></a>
                            <a href="%%BASE_PATH%%parken-speelhallen.html"><span class="lang-nl">Parken &amp; Speelhallen</span><span class="lang-en">Parks &amp; Arcades</span></a>
                            <a href="%%BASE_PATH%%onderwijs.html"><span class="lang-nl">Onderwijs</span><span class="lang-en">Education</span></a>
                            <a href="%%BASE_PATH%%zorg-revalidatie.html"><span class="lang-nl">Zorg &amp; Revalidatie</span><span class="lang-en">Care &amp; Rehabilitation</span></a>
                        </div>
                    </li>
                    <li class="nav-item dropdown">
                        <button class="nav-link"><span class="lang-nl">Over Ons</span><span class="lang-en">About Us</span></button>
                        <div class="dropdown-menu">
                            <a href="%%BASE_PATH%%over-ons.html"><span class="lang-nl">Over InterActiveMove</span><span class="lang-en">About InterActiveMove</span></a>
                            <a href="%%BASE_PATH%%prijzen.html"><span class="lang-nl">Prijzen</span><span class="lang-en">Prices</span></a>
                            <a href="%%BASE_PATH%%index.html#contact">Contact</a>
                        </div>
                    </li>
                    <li class="nav-item">
                        <a href="%%BASE_PATH%%blog.html" class="nav-link">Blog</a>
                    </li>
                </ul>
                <div class="lang-toggle">
                    <button class="lang-btn active" data-lang="nl" onclick="switchLang('nl')">NL</button>
                    <span class="divider">|</span>
                    <button class="lang-btn" data-lang="en" onclick="switchLang('en')">EN</button>
                </div>
                <button class="hamburger" onclick="toggleMobileNav()" aria-label="Menu">
                    <span></span><span></span><span></span>
                </button>
                <a href="%%BASE_PATH%%index.html#contact" class="btn" style="padding: 0.5rem 1.5rem; font-size: 0.9rem; border-radius: 999px;">Contact</a>
            </nav>
        </header>

        <!-- Mobile Navigation Overlay -->
        <div class="mobile-nav" id="mobileNav">
            <a href="%%BASE_PATH%%index.html" onclick="closeMobileNav()">Home</a>
            <div class="mobile-dropdown">
                <button class="mobile-dropdown-toggle" onclick="toggleMobileDropdown(this)">
                    <span class="lang-nl">Producten</span><span class="lang-en">Products</span> <svg class="mobile-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
                </button>
                <div class="mobile-dropdown-items">
                    <a href="%%BASE_PATH%%products/2-in-1-vloer-muur.html">2-in-1 Vloer &amp; Muur</a>
                    <a href="%%BASE_PATH%%products/interactieve-vloer.html">Interactieve Vloer</a>
                    <a href="%%BASE_PATH%%products/interactieve-muur.html">Interactieve Muur</a>
                    <a href="%%BASE_PATH%%products/interactieve-zandbak.html">Interactieve Zandbak</a>
                    <a href="%%BASE_PATH%%products/interactieve-klimwand.html">Interactieve Klimwand</a>
                    <a href="%%BASE_PATH%%products/mobiele-vloer.html">Mobiele Vloer</a>
                    <a href="%%BASE_PATH%%products/software-maatwerk.html">Software &amp; Maatwerk</a>
                </div>
            </div>
            <div class="mobile-dropdown">
                <button class="mobile-dropdown-toggle" onclick="toggleMobileDropdown(this)">
                    <span class="lang-nl">Mogelijkheden</span><span class="lang-en">Solutions</span> <svg class="mobile-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
                </button>
                <div class="mobile-dropdown-items">
                    <a href="%%BASE_PATH%%bouw-een-park.html"><span class="lang-nl">Bouw een Park</span><span class="lang-en">Build a Park</span></a>
                    <a href="%%BASE_PATH%%3d-spellen.html">3D <span class="lang-nl">Spellen</span><span class="lang-en">Games</span></a>
                    <a href="%%BASE_PATH%%parken-speelhallen.html"><span class="lang-nl">Parken &amp; Speelhallen</span><span class="lang-en">Parks &amp; Arcades</span></a>
                    <a href="%%BASE_PATH%%onderwijs.html"><span class="lang-nl">Onderwijs</span><span class="lang-en">Education</span></a>
                    <a href="%%BASE_PATH%%zorg-revalidatie.html"><span class="lang-nl">Zorg &amp; Revalidatie</span><span class="lang-en">Care &amp; Rehabilitation</span></a>
                </div>
            </div>
            <div class="mobile-dropdown">
                <button class="mobile-dropdown-toggle" onclick="toggleMobileDropdown(this)">
                    <span class="lang-nl">Over Ons</span><span class="lang-en">About Us</span> <svg class="mobile-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M6 9l6 6 6-6"/></svg>
                </button>
                <div class="mobile-dropdown-items">
                    <a href="%%BASE_PATH%%over-ons.html"><span class="lang-nl">Over InterActiveMove</span><span class="lang-en">About InterActiveMove</span></a>
                    <a href="%%BASE_PATH%%prijzen.html"><span class="lang-nl">Prijzen</span><span class="lang-en">Prices</span></a>
                    <a href="%%BASE_PATH%%index.html#contact" onclick="closeMobileNav()">Contact</a>
                </div>
            </div>
            <a href="%%BASE_PATH%%blog.html">Blog</a>
            <a href="%%BASE_PATH%%index.html#contact" onclick="closeMobileNav()">Contact</a>
        </div>

        <!-- Content Area (swapped by HTMX on lang change) -->
        <main id="content-area">
            %%NL_CONTENT%%
        </main>
    </div>

    <script src="%%BASE_PATH%%projector.js"></script>
    <script src="/js/site.js"></script>
    <script src="/js/cookie-consent.js"></script>
    <script src="/js/contact-form.js"></script>
    <script type="text/javascript" id="hs-script-loader" async defer src="//js.hs-scripts.com/49291889.js"></script>
    <script src="%%BASE_PATH%%js/iam-knowledge-base.js"></script>
    <script src="%%BASE_PATH%%js/chat-config.js"></script>
    <script src="%%BASE_PATH%%js/chat-widget.js"></script>
</body>
</html>'''

PAGES = [
    # Root pages
    {"file": "index.html", "slug": "index", "title": "InterActiveMove | Interactieve oplossingen voor beweging, leren en spelen", "partial": "partials/index-nl.html", "base": "", "section": ""},
    {"file": "over-ons.html", "slug": "over-ons", "title": "Over Ons | InterActiveMove", "partial": "partials/over-ons-nl.html", "base": "", "section": ""},
    {"file": "prijzen.html", "slug": "prijzen", "title": "Prijzen | InterActiveMove", "partial": "partials/prijzen-nl.html", "base": "", "section": ""},
    {"file": "onderwijs.html", "slug": "onderwijs", "title": "Onderwijs | InterActiveMove", "partial": "partials/onderwijs-nl.html", "base": "", "section": ""},
    {"file": "3d-spellen.html", "slug": "3d-spellen", "title": "3D Spellen | InterActiveMove", "partial": "partials/3d-spellen-nl.html", "base": "", "section": ""},
    {"file": "bouw-een-park.html", "slug": "bouw-een-park", "title": "Bouw een Park | InterActiveMove", "partial": "partials/bouw-een-park-nl.html", "base": "", "section": ""},
    {"file": "parken-speelhallen.html", "slug": "parken-speelhallen", "title": "Parken & Speelhallen | InterActiveMove", "partial": "partials/parken-speelhallen-nl.html", "base": "", "section": ""},
    {"file": "zorg-revalidatie.html", "slug": "zorg-revalidatie", "title": "Zorg & Revalidatie | InterActiveMove", "partial": "partials/zorg-revalidatie-nl.html", "base": "", "section": ""},
    {"file": "maak-je-spel.html", "slug": "maak-je-spel", "title": "Maak je eigen spel | InterActiveMove", "partial": "partials/maak-je-spel-nl.html", "base": "", "section": ""},
    {"file": "word-partner.html", "slug": "word-partner", "title": "Word Partner | InterActiveMove", "partial": "partials/word-partner-nl.html", "base": "", "section": ""},
    {"file": "blog.html", "slug": "content", "title": "Blog | InterActiveMove", "partial": "partials/content-nl.html", "base": "", "section": ""},
    {"file": "cookiebeleid.html", "slug": "cookiebeleid", "title": "Cookiebeleid | InterActiveMove", "partial": "partials/cookiebeleid-nl.html", "base": "", "section": ""},
    {"file": "privacybeleid.html", "slug": "privacybeleid", "title": "Privacybeleid | InterActiveMove", "partial": "partials/privacybeleid-nl.html", "base": "", "section": ""},
    {"file": "toegankelijkheid.html", "slug": "toegankelijkheid", "title": "Toegankelijkheid | InterActiveMove", "partial": "partials/toegankelijkheid-nl.html", "base": "", "section": ""},
    # Product pages
    {"file": "products/2-in-1-vloer-muur.html", "slug": "2-in-1-vloer-muur", "title": "2-in-1 Interactieve Vloer & Muur | InterActiveMove", "partial": "partials/products/2-in-1-vloer-muur-nl.html", "base": "../", "section": "products"},
    {"file": "products/interactieve-vloer.html", "slug": "interactieve-vloer", "title": "Interactieve Vloer | InterActiveMove", "partial": "partials/products/interactieve-vloer-nl.html", "base": "../", "section": "products"},
    {"file": "products/interactieve-muur.html", "slug": "interactieve-muur", "title": "Interactieve Muur | InterActiveMove", "partial": "partials/products/interactieve-muur-nl.html", "base": "../", "section": "products"},
    {"file": "products/interactieve-zandbak.html", "slug": "interactieve-zandbak", "title": "Interactieve Zandbak | InterActiveMove", "partial": "partials/products/interactieve-zandbak-nl.html", "base": "../", "section": "products"},
    {"file": "products/interactieve-klimwand.html", "slug": "interactieve-klimwand", "title": "Interactieve Klimwand | InterActiveMove", "partial": "partials/products/interactieve-klimwand-nl.html", "base": "../", "section": "products"},
    {"file": "products/mobiele-vloer.html", "slug": "mobiele-vloer", "title": "Mobiele Vloer | InterActiveMove", "partial": "partials/products/mobiele-vloer-nl.html", "base": "../", "section": "products"},
    {"file": "products/software-maatwerk.html", "slug": "software-maatwerk", "title": "Software & Maatwerk | InterActiveMove", "partial": "partials/products/software-maatwerk-nl.html", "base": "../", "section": "products"},
    {"file": "products/interactieve-tekeningen.html", "slug": "interactieve-tekeningen", "title": "Interactieve Tekeningen | InterActiveMove", "partial": "partials/products/interactieve-tekeningen-nl.html", "base": "../", "section": "products"},
]

# Try to extract existing meta descriptions
import re

def get_existing_description(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        m = re.search(r'<meta\s+name="description"\s+content="([^"]*)"', content)
        if m:
            return m.group(1)
    except FileNotFoundError:
        pass
    return ""

for page in PAGES:
    desc = get_existing_description(page["file"])
    
    # Read partial
    try:
        with open(page["partial"], 'r', encoding='utf-8') as f:
            partial_content = f.read()
    except FileNotFoundError:
        print(f"WARNING: Partial not found: {page['partial']}")
        partial_content = "<!-- partial not found -->"
    
    html = TEMPLATE
    html = html.replace("%%PAGE_TITLE%%", page["title"])
    html = html.replace("%%PAGE_DESCRIPTION%%", desc)
    html = html.replace("%%PAGE_SLUG%%", page["slug"])
    html = html.replace("%%BASE_PATH%%", page["base"])
    html = html.replace("%%SECTION%%", page["section"])
    html = html.replace("%%NL_CONTENT%%", partial_content)
    
    with open(page["file"], 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✓ {page['file']}")

print(f"\nDone! Generated {len(PAGES)} shell pages.")

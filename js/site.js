// site.js — Unified JS for IAM website (nav, lang switching, reveals)

// === Mobile Navigation ===
function toggleMobileNav() {
    var nav = document.getElementById('mobileNav');
    if (nav) nav.classList.toggle('active');
}

function closeMobileNav() {
    var nav = document.getElementById('mobileNav');
    if (nav) nav.classList.remove('active');
}

function toggleMobileDropdown(btn) {
    if (btn && btn.parentElement) {
        btn.parentElement.classList.toggle('open');
    }
}

// === Language Switching ===
function switchLang(lang) {
    // 1. Save to localStorage
    localStorage.setItem('iam-lang', lang);

    // 2. Update URL param
    var url = new URL(window.location);
    url.searchParams.set('lang', lang);
    history.replaceState(null, '', url);

    // 3. Toggle active on lang buttons
    document.querySelectorAll('.lang-btn').forEach(function(btn) {
        btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    // 4. Set data-lang on <html>
    document.documentElement.setAttribute('data-lang', lang);

    // 5. Build partial path
    var body = document.body;
    var slug = body.getAttribute('data-page') || 'index';
    var basePath = body.getAttribute('data-base') || '';
    var section = body.getAttribute('data-section') || '';

    var partialPath;
    if (section === 'products') {
        partialPath = basePath + 'partials/products/' + slug + '-' + lang + '.html';
    } else {
        partialPath = basePath + 'partials/' + slug + '-' + lang + '.html';
    }

    // 6. Swap content via HTMX
    if (typeof htmx !== 'undefined') {
        htmx.ajax('GET', partialPath, '#content-area');
    }

    // 7. Close mobile nav
    closeMobileNav();
}

// === Reveal Observer ===
var revealObserver = new IntersectionObserver(function(entries) {
    entries.forEach(function(entry) {
        if (entry.isIntersecting) {
            entry.target.classList.add('revealed');
        }
    });
}, { threshold: 0.1 });

function observeRevealElements() {
    document.querySelectorAll('.section-reveal, .reveal, .reveal-fade-up, .reveal-fade-left, .reveal-fade-right, .reveal-scale').forEach(function(el) {
        if (!el.classList.contains('revealed')) {
            revealObserver.observe(el);
        }
    });
}

// === Init on DOMContentLoaded ===
document.addEventListener('DOMContentLoaded', function() {
    // Determine language
    var params = new URLSearchParams(window.location.search);
    var lang = params.get('lang') || localStorage.getItem('iam-lang') || 'nl';

    // Set initial state
    document.documentElement.setAttribute('data-lang', lang);
    localStorage.setItem('iam-lang', lang);

    // Update active lang button
    document.querySelectorAll('.lang-btn').forEach(function(btn) {
        btn.classList.toggle('active', btn.getAttribute('data-lang') === lang);
    });

    // If not default NL, swap to that language
    if (lang !== 'nl') {
        switchLang(lang);
    }

    // Init reveal observer
    observeRevealElements();
});

// === HTMX afterSwap hook ===
document.body.addEventListener('htmx:afterSwap', function() {
    setTimeout(observeRevealElements, 50);
});

// === Desktop dropdown close on outside click ===
document.addEventListener('click', function(e) {
    if (!e.target.closest('.nav-item.dropdown')) {
        document.querySelectorAll('.dropdown-menu').forEach(function(menu) {
            menu.style.display = '';
        });
    }
});

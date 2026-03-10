// Reveal animation observer - adds 'revealed' class when elements scroll into view
(function() {
    var observer = new IntersectionObserver(function(entries) {
        entries.forEach(function(entry) {
            if (entry.isIntersecting) {
                entry.target.classList.add('revealed');
            }
        });
    }, { threshold: 0.1 });

    function observeAll() {
        document.querySelectorAll('.section-reveal, .reveal, .reveal-fade-up, .reveal-fade-left, .reveal-fade-right, .reveal-scale').forEach(function(el) {
            if (!el.classList.contains('revealed')) {
                observer.observe(el);
            }
        });
    }

    // Run on load and after every HTMX swap (for partial loading)
    document.addEventListener('DOMContentLoaded', observeAll);
    document.body.addEventListener('htmx:afterSwap', function() {
        setTimeout(observeAll, 50);
    });
})();

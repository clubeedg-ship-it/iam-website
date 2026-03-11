// Blog carousel — loads posts from Ghost API into #blog-carousel
(function() {
    const GHOST_API = '/ghost/api/content';
    const GHOST_KEY = 'b8903092a7c9a8b54d7378f5a1';

    async function loadBlogCarousel() {
        try {
            const isEn = new URLSearchParams(window.location.search).get('lang') === 'en';
            const langFilter = isEn ? '&filter=tag:hash-en' : '&filter=tag:hash-nl';
            const res = await fetch(`${GHOST_API}/posts/?key=${GHOST_KEY}&include=tags&fields=id,title,slug,feature_image,custom_excerpt,excerpt,published_at&limit=6${langFilter}`);
            const data = await res.json();
            const carousel = document.getElementById('blog-carousel');
            if (!carousel) return;

            if (!data.posts || data.posts.length === 0) {
                var empty = document.getElementById('blog-carousel-empty');
                if (empty) empty.style.display = 'block';
                carousel.style.display = 'none';
                return;
            }

            carousel.innerHTML = data.posts.map(function(post) {
                var date = new Date(post.published_at).toLocaleDateString(isEn ? 'en-GB' : 'nl-NL', {
                    year: 'numeric', month: 'short', day: 'numeric'
                });
                var excerpt = post.custom_excerpt || post.excerpt || '';
                var tag = post.tags && post.tags[0] ? post.tags[0].name : 'Nieuws';
                var img = post.feature_image
                    ? '<img src="' + post.feature_image + '" alt="' + post.title + '" loading="lazy">'
                    : '<div class="card-placeholder"><svg width="48" height="48" viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zm-5-7l-3 3.72L9 13l-3 4h12l-4-5z"/></svg></div>';
                return '<a href="/blog?post=' + post.slug + '" class="blog-carousel-card">' +
                    img +
                    '<div class="card-body">' +
                    '<span class="card-tag">' + tag + '</span>' +
                    '<h3>' + post.title + '</h3>' +
                    '<p class="card-excerpt">' + excerpt.substring(0, 120) + (excerpt.length > 120 ? '...' : '') + '</p>' +
                    '<div class="card-meta">' +
                    '<span>' + date + '</span>' +
                    '<span class="read-more">' + (isEn ? 'Read more →' : 'Lees meer →') + '</span>' +
                    '</div></div></a>';
            }).join('');
        } catch (e) {
            var empty = document.getElementById('blog-carousel-empty');
            if (empty) empty.style.display = 'block';
        }
    }

    window.scrollBlogCarousel = function(dir) {
        var c = document.getElementById('blog-carousel');
        if (c) c.scrollBy({ left: dir * 360, behavior: 'smooth' });
    };

    document.addEventListener('DOMContentLoaded', loadBlogCarousel);
    document.body.addEventListener('htmx:afterSwap', loadBlogCarousel);
})();

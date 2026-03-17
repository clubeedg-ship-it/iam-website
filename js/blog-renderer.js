/**
 * Blog Renderer for InterActiveMove
 * Handles both List View and Single Post View with Groq-style clean layout
 */
(function() {
    function initBlog() {
        const app = document.getElementById('blog-app');
        if (!app) return;

        const params = new URLSearchParams(window.location.search);
        const postSlug = params.get('post');
        const currentLang = params.get('lang') || localStorage.getItem('iam-lang') || 'nl';
        const isEn = currentLang === 'en';

        // Translation helper
        const t = (obj, field) => obj[field + '_' + currentLang] || obj[field + '_nl'] || '';
        
        // Labels
        const labels = {
            blogTitle: isEn ? 'Blog' : 'Blog',
            readMore: isEn ? 'Read Blog' : 'Lees meer',
            backToBlog: isEn ? 'Back' : 'Terug',
            relatedPosts: isEn ? 'Related' : 'Gerelateerd',
            news: isEn ? 'Blog' : 'Blog',
            publishedOn: isEn ? 'Published on' : 'Gepubliceerd op'
        };

        if (postSlug) {
            renderSinglePost(app, postSlug, currentLang, labels, t);
        } else {
            renderBlogList(app, currentLang, labels, t);
        }
    }

    function formatDate(dateStr, lang) {
        const date = new Date(dateStr);
        const months = {
            nl: ['JAN', 'FEB', 'MRT', 'APR', 'MEI', 'JUN', 'JUL', 'AUG', 'SEP', 'OKT', 'NOV', 'DEC'],
            en: ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
        };
        const m = months[lang] || months.nl;
        return `${m[date.getMonth()]} ${date.getDate()}, ${date.getFullYear()}`;
    }

    function renderBlogList(container, lang, labels, t) {
        const posts = BLOG_LOCAL_DATA;
        if (!posts || posts.length === 0) return;

        // Select a random featured post
        const featuredIndex = Math.floor(Math.random() * posts.length);
        const featuredPost = posts[featuredIndex];
        const otherPosts = posts.filter((_, i) => i !== featuredIndex);

        let html = `
            <div class="blog-light-wrapper">
                <div class="blog-content-container">
                    <header class="blog-header">
                        <h1 class="blog-page-title">${labels.blogTitle}</h1>
                        <hr class="blog-title-sep">
                    </header>

                    <!-- Featured Post -->
                    <section class="featured-post-section">
                        ${renderFeaturedCard(featuredPost, lang, labels, t)}
                    </section>

                    <!-- Post Grid -->
                    <section class="posts-grid-section">
                        <div class="blog-posts-grid">
                            ${otherPosts.map(post => renderGridCard(post, lang, labels, t)).join('')}
                        </div>
                    </section>
                </div>
            </div>
        `;

        container.innerHTML = html;
        window.scrollTo(0, 0);
    }

    function renderFeaturedCard(post, lang, labels, t) {
        const title = t(post, 'title');
        const excerpt = t(post, 'excerpt').replace(/\[&hellip;\]/g, '...');
        const tag = post.tags && post.tags[0] ? (post.tags[0]['name_' + lang] || post.tags[0].name_nl) : labels.news;
        const langParam = lang === 'en' ? '&lang=en' : '';
        const url = `blog.html?post=${post.slug}${langParam}`;

        return `
            <div class="featured-card">
                <div class="featured-card-content">
                    <span class="featured-tag">${tag}</span>
                    <h2 class="featured-title">${title}</h2>
                    <p class="featured-excerpt">${excerpt.substring(0, 200)}${excerpt.length > 200 ? '...' : ''}</p>
                    <a href="${url}" class="featured-btn">${labels.readMore}</a>
                </div>
                <div class="featured-card-image">
                    <img src="${post.feature_image}" alt="${title}" loading="lazy">
                </div>
            </div>
        `;
    }

    function renderGridCard(post, lang, labels, t) {
        const title = t(post, 'title');
        const dateStr = formatDate(post.published_at, lang);
        const langParam = lang === 'en' ? '&lang=en' : '';
        const url = `blog.html?post=${post.slug}${langParam}`;

        return `
            <a href="${url}" class="grid-card">
                <div class="grid-card-date">${dateStr}</div>
                <div class="grid-card-image">
                    <img src="${post.feature_image}" alt="${title}" loading="lazy">
                </div>
                <h3 class="grid-card-title">${title}</h3>
            </a>
        `;
    }

    function renderSinglePost(container, slug, lang, labels, t) {
        const post = BLOG_LOCAL_DATA.find(p => p.slug === slug);

        if (!post) {
            container.innerHTML = `<div class="blog-light-wrapper"><div class="blog-content-container" style="padding: 10rem 0; text-align: center;"><h1>Post not found</h1><a href="blog.html" class="back-link">${labels.backToBlog}</a></div></div>`;
            return;
        }

        const title = t(post, 'title');
        const content = t(post, 'html');
        const dateStr = formatDate(post.published_at, lang);
        const tag = post.tags && post.tags[0] ? (post.tags[0]['name_' + lang] || post.tags[0].name_nl) : labels.news;
        const langParam = lang === 'en' ? '?lang=en' : '';

        let html = `
            <div class="blog-light-wrapper">
                <article class="blog-content-container single-post-view">
                    <a href="blog.html${langParam}" class="back-link-top">
                        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
                        ${labels.backToBlog}
                    </a>
                    
                    <header class="post-detail-header">
                        <div class="post-detail-date">${dateStr}</div>
                        <h1 class="post-detail-title">${title}</h1>
                    </header>

                    ${post.feature_image ? `<div class="post-detail-hero-img"><img src="${post.feature_image}" alt="${title}"></div>` : ''}

                    <div class="post-detail-content">
                        ${content}
                    </div>

                    ${renderRelatedGrid(post, lang, labels, t)}
                </article>
            </div>
        `;

        container.innerHTML = html;
        window.scrollTo(0, 0);
    }

    function renderRelatedGrid(currentPost, lang, labels, t) {
        const related = BLOG_LOCAL_DATA
            .filter(p => p.slug !== currentPost.slug)
            .slice(0, 4);

        if (related.length === 0) return '';

        return `
            <section class="related-section">
                <h2 class="related-title">${labels.relatedPosts}</h2>
                <div class="blog-posts-grid mini">
                    ${related.map(post => renderGridCard(post, lang, labels, t)).join('')}
                </div>
            </section>
        `;
    }

    // Initialize on load
    document.addEventListener('DOMContentLoaded', initBlog);
    window.addEventListener('popstate', initBlog);
    window.reRenderBlog = initBlog;

    const originalSwitchLang = window.switchLang;
    window.switchLang = function(lang) {
        if (originalSwitchLang) originalSwitchLang(lang);
        setTimeout(initBlog, 50);
    };
})();

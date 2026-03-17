/**
 * Blog Renderer for InterActiveMove
 * Handles both List View and Single Post View
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
            blogTitle: isEn ? 'Latest Articles' : 'Laatste Artikelen',
            readMore: isEn ? 'Read more →' : 'Lees meer →',
            backToBlog: isEn ? '← Back to blog' : '← Terug naar blog',
            relatedPosts: isEn ? 'Related Posts' : 'Gerelateerde Artikelen',
            news: isEn ? 'News' : 'Nieuws',
            publishedOn: isEn ? 'Published on' : 'Gepubliceerd op'
        };

        if (postSlug) {
            renderSinglePost(app, postSlug, currentLang, labels, t);
        } else {
            renderBlogList(app, currentLang, labels, t);
        }
    }

    function renderBlogList(container, lang, labels, t) {
        const isEn = lang === 'en';
        const posts = BLOG_LOCAL_DATA;

        let html = `
            <div class="blog-container container">
                <h1 class="industrial-label">${labels.blogTitle}</h1>
                <div class="blog-grid">
        `;

        posts.forEach(post => {
            const title = t(post, 'title');
            const excerpt = t(post, 'excerpt');
            const date = new Date(post.published_at).toLocaleDateString(isEn ? 'en-GB' : 'nl-NL', {
                year: 'numeric', month: 'long', day: 'numeric'
            });
            const tag = post.tags && post.tags[0] ? (post.tags[0]['name_' + lang] || post.tags[0].name_nl) : labels.news;
            
            const imgHtml = post.feature_image 
                ? `<img src="${post.feature_image}" alt="${title}" class="blog-card-img" loading="lazy">`
                : `<div class="blog-card-img" style="background: #111; display: flex; align-items: center; justify-content: center;">
                    <svg width="48" height="48" viewBox="0 0 24 24" fill="rgba(255,255,255,0.1)"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zm-5-7l-3 3.72L9 13l-3 4h12l-4-5z"/></svg>
                   </div>`;

            const langParam = lang === 'en' ? '&lang=en' : '';
            
            html += `
                <a href="blog.html?post=${post.slug}${langParam}" class="blog-card">
                    ${imgHtml}
                    <div class="blog-card-body">
                        <span class="blog-card-tag">${tag}</span>
                        <h3>${title}</h3>
                        <p>${excerpt.substring(0, 150)}${excerpt.length > 150 ? '...' : ''}</p>
                        <div class="blog-card-meta">
                            <span>${date}</span>
                            <span class="read-more-link">${labels.readMore}</span>
                        </div>
                    </div>
                </a>
            `;
        });

        html += `
                </div>
            </div>
        `;

        container.innerHTML = html;
        window.scrollTo(0, 0);
    }

    function renderSinglePost(container, slug, lang, labels, t) {
        const isEn = lang === 'en';
        const post = BLOG_LOCAL_DATA.find(p => p.slug === slug);

        if (!post) {
            container.innerHTML = `<div class="container" style="padding: 10rem 0; text-align: center;"><h1>Post not found</h1><a href="blog.html" class="back-link">${labels.backToBlog}</a></div>`;
            return;
        }

        const title = t(post, 'title');
        const content = t(post, 'html');
        const date = new Date(post.published_at).toLocaleDateString(isEn ? 'en-GB' : 'nl-NL', {
            year: 'numeric', month: 'long', day: 'numeric'
        });
        const tag = post.tags && post.tags[0] ? (post.tags[0]['name_' + lang] || post.tags[0].name_nl) : labels.news;
        const langParam = lang === 'en' ? '?lang=en' : '';

        let html = `
            <article class="post-container">
                <a href="blog.html${langParam}" class="back-link">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
                    ${labels.backToBlog}
                </a>
                
                <header class="post-header">
                    <span class="post-tag">${tag}</span>
                    <h1 class="post-title">${title}</h1>
                    <div class="post-meta">${labels.publishedOn} ${date}</div>
                </header>

                ${post.feature_image ? `<img src="${post.feature_image}" alt="${title}" class="post-feature-img">` : ''}

                <div class="post-content">
                    ${content}
                </div>

                ${renderRelatedPosts(post, lang, labels, t)}
            </article>
        `;

        container.innerHTML = html;
        window.scrollTo(0, 0);
    }

    function renderRelatedPosts(currentPost, lang, labels, t) {
        const isEn = lang === 'en';
        const currentTag = currentPost.tags && currentPost.tags[0] ? currentPost.tags[0].name_nl : null;
        
        const related = BLOG_LOCAL_DATA
            .filter(p => p.slug !== currentPost.slug)
            .filter(p => {
                if (!currentTag) return true;
                return p.tags && p.tags.some(tag => tag.name_nl === currentTag);
            })
            .slice(0, 3);

        if (related.length === 0) return '';

        let html = `
            <section class="related-posts">
                <h2 class="industrial-label" style="font-size: 1.5rem; margin-bottom: 2rem;">${labels.relatedPosts}</h2>
                <div class="blog-grid" style="grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));">
        `;

        related.forEach(post => {
            const title = t(post, 'title');
            const langParam = lang === 'en' ? '&lang=en' : '';
            const imgHtml = post.feature_image 
                ? `<img src="${post.feature_image}" alt="${title}" class="blog-card-img" style="height: 150px;">`
                : `<div class="blog-card-img" style="height: 150px; background: #111; display: flex; align-items: center; justify-content: center;">
                    <svg width="32" height="32" viewBox="0 0 24 24" fill="rgba(255,255,255,0.1)"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm0 16H5V5h14v14zm-5-7l-3 3.72L9 13l-3 4h12l-4-5z"/></svg>
                   </div>`;

            html += `
                <a href="blog.html?post=${post.slug}${langParam}" class="blog-card">
                    ${imgHtml}
                    <div class="blog-card-body" style="padding: 1rem;">
                        <h3 style="font-size: 1rem; margin-bottom: 0;">${title}</h3>
                    </div>
                </a>
            `;
        });

        html += `
                </div>
            </section>
        `;

        return html;
    }

    // Initialize on load
    document.addEventListener('DOMContentLoaded', initBlog);
    
    // Support language switching without reload if needed (htmx or custom)
    window.addEventListener('popstate', initBlog);
    
    // Expose for language switcher to trigger re-render
    window.reRenderBlog = initBlog;

    // Hook into existing switchLang if it exists
    const originalSwitchLang = window.switchLang;
    window.switchLang = function(lang) {
        if (originalSwitchLang) originalSwitchLang(lang);
        setTimeout(initBlog, 50); // Small delay to let localStorage update
    };
})();

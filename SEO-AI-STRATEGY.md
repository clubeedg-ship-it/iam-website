# SEO & AI Strategy for InterActiveMove.nl

> **Date:** March 2026 | **Site:** interactivemove.nl | **Stack:** Static HTML + HTMX + CSS
> **Market:** Dutch B2B — interactive projectors for education, healthcare, recreation

---

## Table of Contents

1. [Quick Wins (Week 1-2)](#1-quick-wins-week-1-2)
2. [Schema Markup & Structured Data](#2-schema-markup--structured-data)
3. [Technical SEO for HTMX Sites](#3-technical-seo-for-htmx-sites)
4. [Dutch Market SEO](#4-dutch-market-seo)
5. [AI-Powered Content Strategy](#5-ai-powered-content-strategy)
6. [Competitor Analysis & Gap Opportunities](#6-competitor-analysis--gap-opportunities)
7. [Content Calendar & Pillar Pages](#7-content-calendar--pillar-pages)
8. [Backlink Strategy](#8-backlink-strategy)
9. [Tools & Budget](#9-tools--budget)
10. [Implementation Roadmap](#10-implementation-roadmap)

---

## 1. Quick Wins (Week 1-2)

### 1.1 Add Schema Markup to All Pages (Impact: HIGH)

Currently NO structured data exists. This is the single biggest quick win.

**Product pages** — add `Product` schema to all 6 product pages:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Interactieve Vloer",
  "description": "De Interactieve Vloer van IAM reageert op beweging en maakt elke ruimte tot een speelwereld. Perfect voor scholen, BSO's en events.",
  "brand": {
    "@type": "Brand",
    "name": "InterActiveMove"
  },
  "category": "Interactive Projection Systems",
  "image": "https://interactivemove.nl/media/products/interactieve-vloer.webp",
  "offers": {
    "@type": "Offer",
    "url": "https://interactivemove.nl/products/interactieve-vloer.html",
    "priceCurrency": "EUR",
    "availability": "https://schema.org/InStock",
    "seller": {
      "@type": "Organization",
      "name": "InterActiveMove"
    }
  },
  "audience": {
    "@type": "Audience",
    "audienceType": "Schools, BSO, Healthcare facilities, Recreation parks"
  }
}
</script>
```

**Organization schema** — add to every page (put in a shared partial):

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "InterActiveMove",
  "alternateName": "IAM",
  "url": "https://interactivemove.nl",
  "logo": "https://interactivemove.nl/media/logo-final.png",
  "description": "Interactieve oplossingen voor beweging, leren en spelen in onderwijs, sport en zorg.",
  "address": {
    "@type": "PostalAddress",
    "addressCountry": "NL"
  },
  "sameAs": [],
  "contactPoint": {
    "@type": "ContactPoint",
    "contactType": "sales",
    "availableLanguage": ["Dutch", "English"]
  }
}
</script>
```

**Breadcrumb schema** — add to all inner pages:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://interactivemove.nl/" },
    { "@type": "ListItem", "position": 2, "name": "Producten", "item": "https://interactivemove.nl/products/" },
    { "@type": "ListItem", "position": 3, "name": "Interactieve Vloer", "item": "https://interactivemove.nl/products/interactieve-vloer.html" }
  ]
}
</script>
```

### 1.2 Fix Meta Tags (Impact: MEDIUM)

Add `og:` and `twitter:` meta tags to all pages:

```html
<meta property="og:type" content="website">
<meta property="og:title" content="Interactieve Vloer | InterActiveMove">
<meta property="og:description" content="De Interactieve Vloer reageert op beweging...">
<meta property="og:image" content="https://interactivemove.nl/media/og/interactieve-vloer.jpg">
<meta property="og:url" content="https://interactivemove.nl/products/interactieve-vloer.html">
<meta property="og:locale" content="nl_NL">
<meta name="twitter:card" content="summary_large_image">
```

### 1.3 Add `lastmod` to Sitemap (Impact: LOW-MEDIUM)

Current sitemap has no `<lastmod>`. Add it:

```xml
<url>
  <loc>https://interactivemove.nl/products/interactieve-vloer.html</loc>
  <lastmod>2026-03-06</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.9</priority>
</url>
```

### 1.4 Image Alt Text Audit (Impact: MEDIUM)

Ensure every `<img>` has descriptive Dutch alt text. Pattern:
- ❌ `alt="vloer"` 
- ✅ `alt="Kinderen spelen op een interactieve vloerprojectie in een basisschool"`

### 1.5 Create a Blog Section (Impact: HIGH, effort: MEDIUM)

Add `/blog/` — this is critical for long-tail keyword capture. Start with 5-10 articles. See Section 5.

---

## 2. Schema Markup & Structured Data

### 2.1 FAQ Schema (for "People Also Ask")

Add to product and industry pages:

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Wat kost een interactieve vloer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "De prijzen van een interactieve vloer beginnen vanaf €X.XXX. Neem contact op voor een offerte op maat."
      }
    },
    {
      "@type": "Question",
      "name": "Is een interactieve vloer geschikt voor scholen?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Ja, onze interactieve vloer wordt breed ingezet in het onderwijs. Van basisscholen tot speciaal onderwijs..."
      }
    },
    {
      "@type": "Question",
      "name": "Hoe werkt een interactieve muurprojectie?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Een interactieve muur gebruikt een projector met bewegingssensoren..."
      }
    }
  ]
}
</script>
```

### 2.2 Video Schema (when you add demo videos)

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "VideoObject",
  "name": "Interactieve Vloer Demo - Basisschool",
  "description": "Bekijk hoe kinderen spelen en leren met de interactieve vloer van IAM.",
  "thumbnailUrl": "https://interactivemove.nl/media/video-thumb-vloer.jpg",
  "uploadDate": "2026-03-01",
  "contentUrl": "https://www.youtube.com/watch?v=XXXXX",
  "embedUrl": "https://www.youtube.com/embed/XXXXX",
  "duration": "PT2M30S"
}
</script>
```

### 2.3 LocalBusiness Schema

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "name": "InterActiveMove",
  "url": "https://interactivemove.nl",
  "telephone": "+31-XX-XXXXXXX",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "...",
    "addressLocality": "...",
    "postalCode": "...",
    "addressCountry": "NL"
  },
  "geo": {
    "@type": "GeoCoordinates",
    "latitude": "52.XXX",
    "longitude": "4.XXX"
  },
  "openingHoursSpecification": {
    "@type": "OpeningHoursSpecification",
    "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday"],
    "opens": "09:00",
    "closes": "17:00"
  },
  "priceRange": "€€€"
}
</script>
```

---

## 3. Technical SEO for HTMX Sites

### 3.1 HTMX Crawlability (CRITICAL)

HTMX loads content via `hx-get` which Googlebot **can** process (it executes JS), but with caveats:

**Best practices:**
1. **Server-side render all critical content** — Don't rely on HTMX for initial page load of indexable content
2. **Use `hx-boost` carefully** — It's fine for navigation (enhances links), but ensure the full HTML page works without JS
3. **Ensure every HTMX partial also exists as a full page** — Google must be able to crawl the URL directly
4. **Test with `site:interactivemove.nl` in Google** to verify all pages are indexed
5. **Use Google Search Console's URL Inspection** to see rendered HTML

**Action:** Test each page with JavaScript disabled. If content disappears, it won't be indexed reliably.

### 3.2 Core Web Vitals

Current stack (static HTML + minimal JS) should score well. Verify with:

```bash
# Test with Lighthouse CLI
npx lighthouse https://interactivemove.nl --only-categories=performance,seo,accessibility --output=json
```

**Key optimizations:**
- **LCP (Largest Contentful Paint):** Preload hero images with `<link rel="preload" as="image" href="...">`
- **CLS (Cumulative Layout Shift):** Set explicit `width` and `height` on all images
- **FID/INP:** Minimal JS = minimal issue. Keep canvas animations non-blocking

### 3.3 Image Optimization

```html
<!-- Convert all images to WebP with fallback -->
<picture>
  <source srcset="/media/products/vloer-hero.webp" type="image/webp">
  <img src="/media/products/vloer-hero.jpg" 
       alt="Kinderen spelen op een interactieve vloerprojectie in een gymzaal"
       width="1200" height="675"
       loading="lazy"
       decoding="async">
</picture>
```

**Convert images in bulk:**
```bash
# Install cwebp
sudo apt install webp

# Convert all JPGs and PNGs
find media/ -name "*.jpg" -o -name "*.png" | while read f; do
  cwebp -q 80 "$f" -o "${f%.*}.webp"
done
```

### 3.4 Hreflang for NL/EN (when adding English)

Add to `<head>` of every page:

```html
<link rel="alternate" hreflang="nl" href="https://interactivemove.nl/products/interactieve-vloer.html">
<link rel="alternate" hreflang="en" href="https://interactivemove.nl/en/products/interactive-floor.html">
<link rel="alternate" hreflang="x-default" href="https://interactivemove.nl/products/interactieve-vloer.html">
```

**URL structure recommendation:** `/en/` prefix for English pages, Dutch as default.

### 3.5 Additional Technical Items

```html
<!-- Add canonical URLs to every page -->
<link rel="canonical" href="https://interactivemove.nl/products/interactieve-vloer.html">

<!-- Preconnect to external resources -->
<link rel="preconnect" href="https://fonts.googleapis.com">

<!-- DNS prefetch for analytics -->
<link rel="dns-prefetch" href="https://www.googletagmanager.com">
```

---

## 4. Dutch Market SEO

### 4.1 Target Keywords (Prioritized)

**High-intent product keywords (Priority 1):**
| Keyword | Est. Monthly Search | Difficulty | Page |
|---------|-------------------|------------|------|
| interactieve vloer | 500-1000 | Medium | /products/interactieve-vloer.html |
| interactieve muur | 200-500 | Medium | /products/interactieve-muur.html |
| interactieve zandbak | 100-300 | Low | /products/interactieve-zandbak.html |
| interactieve klimwand | 100-200 | Low | /products/interactieve-klimwand.html |
| interactieve vloerprojectie | 100-200 | Low | /products/interactieve-vloer.html |
| interactieve projectie | 200-500 | Medium | Homepage |

**Long-tail B2B keywords (Priority 2):**
| Keyword | Intent | Target Page |
|---------|--------|-------------|
| interactieve vloer school kopen | Transactional | Product + Onderwijs |
| interactieve speelvloer kinderopvang | Transactional | Product + Blog |
| bewegend leren basisschool | Informational | Blog |
| interactieve technologie onderwijs | Informational | Blog/Onderwijs |
| revalidatie interactief spel | Informational | Zorg page + Blog |
| interactieve muur kinderdagverblijf | Transactional | Product |
| prijs interactieve vloer | Transactional | Prijzen |
| interactieve projectie huren | Transactional | New page opportunity |
| speeltoestel indoor interactief | Transactional | Parken page |
| digitale speeltuin | Informational | Blog |

**Industry/sector keywords (Priority 3):**
| Keyword | Target Page |
|---------|-------------|
| BSO activiteiten interactief | Blog |
| gymzaal innovatie basisschool | Blog |
| sensorische stimulatie dementie | Zorg + Blog |
| motorische ontwikkeling kleuters | Blog |
| speciaal onderwijs hulpmiddelen | Blog |

### 4.2 On-Page Optimization Pattern

For each product page, ensure:

```
Title: [Product] Kopen | Interactieve [Type] voor Scholen & Zorg | IAM
H1: Interactieve [Product] — [Benefit]
H2s: Hoe werkt het? | Voor wie? | Specificaties | Veelgestelde vragen
Meta description: [Product] van InterActiveMove. [Key benefit]. Geschikt voor [audience]. ✓ Plug & play ✓ 500+ spellen ✓ Nederlandse support. Vraag een demo aan.
```

### 4.3 Google Business Profile

**Action items:**
1. Create/claim Google Business Profile for InterActiveMove
2. Category: "Educational Equipment Supplier" + "Playground Equipment Supplier"
3. Add all products as "Products" in GBP
4. Upload 20+ photos (installations, team, products in action)
5. Get Google Reviews from existing customers (aim for 10+ reviews)
6. Post weekly updates (new installations, blog posts)
7. Add service areas (heel Nederland / nationwide)

### 4.4 Dutch-Specific SEO Notes

- **Google.nl uses the same algorithm as google.com** — no special ranking factors
- **Dutch users search in Dutch** — prioritize Dutch content, add English later
- **B2B decision makers search differently:** terms like "kopen", "leverancier", "offerte", "prijs" indicate buying intent
- **Educational sector:** Decision makers are schoolbesturen, ICT-coördinatoren, directeuren — content should address their concerns (budget, ROI, subsidies)
- **Subsidies angle:** Create content about "subsidie interactief leren" — schools search for funding options

---

## 5. AI-Powered Content Strategy

### 5.1 Pillar Page Architecture

```
PILLAR: /interactieve-technologie-onderwijs/ (2000+ words)
├── CLUSTER: /blog/bewegend-leren-basisschool/
├── CLUSTER: /blog/interactieve-vloer-gymles/
├── CLUSTER: /blog/digitale-leermiddelen-speciaal-onderwijs/
├── CLUSTER: /blog/motorische-ontwikkeling-kleuters-technologie/
└── CLUSTER: /blog/subsidie-digitale-leermiddelen/

PILLAR: /interactieve-technologie-zorg/ (2000+ words)
├── CLUSTER: /blog/sensorische-stimulatie-dementie/
├── CLUSTER: /blog/revalidatie-gamification/
├── CLUSTER: /blog/interactief-spelen-verpleeghuis/
└── CLUSTER: /blog/bewegen-ouderen-technologie/

PILLAR: /interactieve-speelruimte/ (2000+ words)
├── CLUSTER: /blog/indoor-speeltuin-interactief/
├── CLUSTER: /blog/bso-activiteiten-innovatief/
├── CLUSTER: /blog/kinderopvang-interactieve-speelmuur/
└── CLUSTER: /blog/speelhal-attracties-2026/
```

### 5.2 Blog Post Templates (AI-Assisted)

Use Claude/ChatGPT to generate first drafts, then humanize:

**Template for educational blog posts:**
```markdown
Title: [Probleem/Vraag] — [Oplossing met IAM context]
Example: "Bewegend Leren op de Basisschool: 7 Praktische Ideeën voor de Gymzaal"

Structure:
1. Hook (problem/question teachers face)
2. Why it matters (research/stats)
3. Solutions (including but not limited to IAM products)
4. Practical implementation tips
5. Case study / example
6. CTA (vraag een demo aan)

Word count: 1200-1800 words
Internal links: 3-5 to relevant product/industry pages
```

### 5.3 Programmatic SEO Pages

Generate pages for specific use cases:

```
/oplossingen/interactieve-vloer-voor-basisscholen/
/oplossingen/interactieve-vloer-voor-bso/
/oplossingen/interactieve-vloer-voor-kinderopvang/
/oplossingen/interactieve-vloer-voor-revalidatie/
/oplossingen/interactieve-vloer-voor-speelhallen/
/oplossingen/interactieve-muur-voor-basisscholen/
/oplossingen/interactieve-muur-voor-verpleeghuizen/
... (product × sector matrix)
```

Each page: unique intro (200 words), shared specs, sector-specific benefits, relevant case study, FAQ.

**Generation script concept:**
```javascript
const products = ['interactieve-vloer', 'interactieve-muur', 'interactieve-zandbak', 'interactieve-klimwand'];
const sectors = ['basisscholen', 'bso', 'kinderopvang', 'revalidatie', 'speelhallen', 'verpleeghuizen', 'speciaal-onderwijs'];

// Generate with AI, review manually before publishing
for (const product of products) {
  for (const sector of sectors) {
    generatePage({ product, sector, template: 'solution-page' });
  }
}
```

### 5.4 Blog Publishing Cadence

- **Phase 1 (Month 1-2):** 2 posts/week (build foundation, 16 posts)
- **Phase 2 (Month 3-6):** 1 post/week (maintain freshness)
- **Phase 3 (Month 6+):** 2 posts/month + update existing content

**Content freshness signals:** Update key pages quarterly with new stats, case studies, or features. Change `lastmod` in sitemap.

### 5.5 Video SEO

1. Create YouTube channel "InterActiveMove"
2. Upload product demo videos (1-3 min each)
3. Embed on product pages with Video schema
4. Create "How it works" explainer series
5. Customer testimonial videos
6. Optimize YouTube titles/descriptions in Dutch
7. Add Dutch subtitles (auto-generate with Whisper, then edit)

---

## 6. Competitor Analysis & Gap Opportunities

### 6.1 Competitor Overview

| Competitor | Strengths | Weaknesses | Opportunity |
|-----------|-----------|------------|-------------|
| **EyeClick** (eyeclick.com) | Strong brand, "award-winning", global presence, EN content | No Dutch content, enterprise pricing focus | Win Dutch-language searches entirely |
| **Tovertafel/Tover** (tover.care) | Scientific backing, strong healthcare niche, multi-language | Narrow focus (dementia/care), premium pricing | Broader product range, education focus |
| **OMi** (omi.uk) | UK-based, education focus | Limited NL presence | Dutch market is underserved |
| **Lü Interactive** (lu.com) | Gym/school focus, immersive | No NL content | Target "interactieve gymzaal" keywords |

### 6.2 Content Gap Opportunities

**Keywords competitors rank for but IAM doesn't (yet):**
- "interactieve projectie kopen" → Create dedicated buying guide
- "interactieve speelvloer" → Optimize existing page or create new
- "beweegvloer" → Alternative term, create content
- "sensory room" / "snoezelen interactief" → Healthcare angle
- "gamification onderwijs" → Blog content opportunity
- "digitale speeltuin" → New page opportunity
- "interactieve attractie" → Parks/entertainment angle

### 6.3 Backlink Strategy

**Quick wins:**
1. **Dutch business directories:** KVK, Gouden Gids, Detelefoongids.nl
2. **Industry directories:** Onderwijsinnovatie.nl, Kinderopvangtotaal.nl
3. **Supplier listings:** Schoolleveranciers platforms

**Medium-term:**
4. **Guest posts** on Dutch education blogs (Wij-leren.nl, Kennisnet.nl)
5. **Case studies** with partner schools (they link to you)
6. **Press releases** to Dutch education media (Didactief, Van12tot18)
7. **Trade show presence** → links from event websites (NOT, Onderwijs & ICT)

**Long-term:**
8. **Create linkable assets:**
   - "Whitepaper: Interactief Leren in 2026" (gated content for leads)
   - Infographic: "Voordelen van Bewegend Leren" (shareable)
   - Free tool: "ROI Calculator voor Interactieve Technologie"
9. **University partnerships** — reach out to onderwijskunde departments
10. **HARO/Connectively** equivalent for Dutch media

---

## 7. Internal Linking Optimization

### 7.1 Current Issues

The site has a flat structure with limited cross-linking. Fix:

```
Every product page should link to:
├── Related products ("Bekijk ook: Interactieve Muur")
├── Relevant industry page ("Lees meer over inzet in het onderwijs")
├── Pricing page ("Bekijk onze prijzen")
└── Blog posts (when they exist)

Every industry page should link to:
├── All relevant products
├── Case studies
├── Pricing
└── Contact/demo request
```

### 7.2 Contextual Internal Links

Add in-content links naturally:

```html
<!-- In the onderwijs.html page -->
<p>Met de <a href="/products/interactieve-vloer.html">interactieve vloer</a> 
kunnen leerlingen op een speelse manier <a href="/blog/bewegend-leren-basisschool/">
bewegend leren</a> in de gymzaal. Combineer dit met onze 
<a href="/products/interactieve-muur.html">interactieve muur</a> voor een 
volledig interactief klaslokaal.</p>
```

### 7.3 Add "Related Products" Component

```html
<section class="related-products">
  <h2>Bekijk ook</h2>
  <div class="product-grid">
    <a href="/products/interactieve-muur.html" class="product-card">
      <img src="/media/products/muur-thumb.webp" alt="Interactieve Muur" width="300" height="200" loading="lazy">
      <h3>Interactieve Muur</h3>
      <p>Projecteer interactieve games op elke muur</p>
    </a>
    <!-- more cards -->
  </div>
</section>
```

---

## 8. Google Search Console & Analytics Setup

### 8.1 Essential Setup

1. **Google Search Console** — verify ownership, submit sitemap
2. **Google Analytics 4** — track conversions (demo requests, contact form fills)
3. **Microsoft Clarity** (free) — heatmaps, session recordings

### 8.2 Conversion Tracking

```html
<!-- GA4 event for demo request -->
<script>
document.querySelector('#demo-form').addEventListener('submit', function() {
  gtag('event', 'generate_lead', {
    'event_category': 'engagement',
    'event_label': 'demo_request',
    'value': 1
  });
});
</script>
```

---

## 9. Tools & Budget

### Free Tools
| Tool | Purpose |
|------|---------|
| Google Search Console | Indexing, search performance, errors |
| Google Analytics 4 | Traffic & conversion tracking |
| Google Business Profile | Local SEO |
| Microsoft Clarity | Heatmaps, user behavior |
| Google PageSpeed Insights | Core Web Vitals testing |
| Google Rich Results Test | Schema validation |
| Screaming Frog (free up to 500 URLs) | Technical SEO audit |
| AnswerThePublic (limited free) | Question-based keyword research |
| AlsoAsked.com | "People Also Ask" research |
| Claude/ChatGPT | Content drafting, keyword clustering |

### Affordable Paid Tools
| Tool | Cost | Purpose |
|------|------|---------|
| Ubersuggest | ~€30/mo | Keyword research, competitor analysis |
| SE Ranking | ~€40/mo | Rank tracking, site audit |
| Surfer SEO | ~€70/mo | NLP content optimization |
| Ahrefs Lite | ~€90/mo | Backlink analysis, keyword research |

**Recommended minimum stack:** Google tools (free) + Ubersuggest ($30/mo) + Claude for content = ~€30/mo

---

## 10. Implementation Roadmap

### Phase 1: Foundation (Weeks 1-4) — Quick Wins
- [ ] Add Organization + LocalBusiness schema to all pages
- [ ] Add Product schema to all 6 product pages
- [ ] Add Breadcrumb schema to all inner pages
- [ ] Add canonical URLs to all pages
- [ ] Add OG meta tags to all pages
- [ ] Audit and fix all image alt texts (Dutch, descriptive)
- [ ] Add `lastmod` to sitemap.xml
- [ ] Set up Google Search Console + submit sitemap
- [ ] Set up Google Analytics 4
- [ ] Claim Google Business Profile
- [ ] Convert images to WebP with fallback
- [ ] Add `width`/`height` to all images
- [ ] Add `loading="lazy"` to below-fold images
- [ ] Preload hero images
- **Expected impact:** 20-40% improvement in search visibility within 2-3 months

### Phase 2: Content Engine (Weeks 5-12)
- [ ] Create `/blog/` section
- [ ] Write 3 pillar pages (onderwijs, zorg, speelruimte)
- [ ] Publish 2 blog posts/week (AI-assisted)
- [ ] Add FAQ sections with schema to all product pages
- [ ] Add FAQ sections to industry pages
- [ ] Create 5 programmatic solution pages (product × sector)
- [ ] Implement internal linking strategy
- [ ] Add "Related Products" component
- [ ] Set up YouTube channel, upload first 3 demo videos
- [ ] Add Video schema where applicable
- **Expected impact:** 50-100% organic traffic increase over 6 months

### Phase 3: Authority Building (Months 4-6)
- [ ] Submit to 10 Dutch business/industry directories
- [ ] Reach out to 5 education blogs for guest posts
- [ ] Create 3 case studies with customer schools/facilities
- [ ] Create downloadable whitepaper (lead magnet)
- [ ] Launch "subsidie-gids" content (high-value for education buyers)
- [ ] Expand programmatic pages to full matrix (28 pages)
- [ ] Start collecting Google Reviews (target: 15+)
- **Expected impact:** Domain authority increase, backlink growth

### Phase 4: Scale & Optimize (Months 6-12)
- [ ] Add English (`/en/`) version with hreflang
- [ ] Implement hreflang tags across all pages
- [ ] A/B test meta titles/descriptions based on CTR data
- [ ] Update and expand existing content based on Search Console data
- [ ] Build ROI calculator tool (linkable asset)
- [ ] Explore Google Ads for high-intent keywords
- [ ] Monthly content audit and refresh cycle
- **Expected impact:** Sustained 10-20% month-over-month growth

---

## Appendix: AI Workflow for Content Creation

### Keyword Clustering with AI

Prompt template for Claude/ChatGPT:
```
Given these seed keywords for a Dutch B2B website selling interactive projectors 
for schools and healthcare:
[paste keyword list]

Group them into topic clusters. For each cluster, suggest:
1. A pillar page topic
2. 3-5 supporting blog post topics  
3. Primary keyword + secondary keywords for each
4. Search intent (informational/transactional/navigational)
5. Suggested word count
```

### NLP-Optimized Content with AI

Use this prompt to create content that satisfies Google's NLP understanding:

```
Write a 1500-word Dutch blog post about "[topic]" for a B2B audience 
(school directors, ICT coordinators, healthcare facility managers).

Requirements:
- Use semantic variations of the primary keyword naturally
- Include related entities (NLP entities Google would expect)
- Structure with H2/H3 headers using question-based headers where possible
- Include a FAQ section at the end (3-5 questions)
- Write in professional but accessible Dutch
- Include a clear CTA to request a demo
- Suggest internal links to: [list relevant pages]
```

### Content Quality Checklist (Before Publishing)
- [ ] Primary keyword in title, H1, first 100 words, meta description
- [ ] 3+ internal links to relevant pages
- [ ] 1+ external link to authoritative source
- [ ] All images have descriptive Dutch alt text
- [ ] FAQ section with schema markup
- [ ] Meta description under 155 characters, includes CTA
- [ ] Mobile-friendly formatting (short paragraphs, bullet lists)
- [ ] Unique content (not duplicate of other pages)

---

*This strategy was compiled March 2026. Review and update quarterly.*
*Note: Web search was unavailable during research — recommendations based on current SEO best practices and competitor site analysis.*

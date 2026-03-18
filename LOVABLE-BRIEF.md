# Lovable Brief — InterActiveMove Website Refactor

## Prompt for Lovable

---

Build a complete, production-ready website for **InterActiveMove** (interactivemove.nl) — a B2B company that sells interactive floor projectors, wall projectors, sandboxes, and climbing walls for schools, healthcare, and entertainment venues.

### Tech Stack
- React + TypeScript + Tailwind CSS
- React Router for client-side routing
- Fully static-exportable (no server-side logic — this will later be wrapped in Next.js with `output: 'export'`)
- shadcn/ui components where appropriate

### Design Direction — THIS IS THE SOUL OF THE SITE, DO NOT CHANGE

**The #1 signature element is the interactive particle background with frosted glass UI.** This is non-negotiable and must be implemented exactly:

#### Interactive Particle Background (Canvas)
- A **full-screen fixed canvas** behind all content (`position: fixed; z-index: -1; pointer-events: none`)
- Background color: `#f0f2f5` (light warm gray)
- **25 large floating particles** (15px–45px radius) that drift with Brownian motion
- **Particle colors** (industrial palette): `#d23234` (red), `#feba04` (golden amber), `#333333`, `#4d4d4d`, `#2a2a2a` (dark grays/blacks)
- **Mouse interaction**: particles are repelled from the cursor within a 300px radius (fluid physics feel)
- **Connection lines**: faint cyan lines (`rgba(0, 188, 212, 0.2)`) between particles within 200px of each other (constellation effect)
- **Trail effect**: semi-transparent fill (`rgba(240, 244, 248, 0.3)`) each frame instead of clearRect, creating soft motion trails
- Touch support (mobile)
- Canvas renders behind EVERYTHING — all page content sits on top

#### Frosted Glass UI Panels
- All content sections use **glassmorphism** — `backdrop-filter: blur(16px–24px)` with semi-transparent backgrounds
- Light glass panels: `rgba(255, 255, 255, 0.8)` with `backdrop-filter: blur(16px)` and subtle border `rgba(255, 255, 255, 0.4)`
- Dark glass panels: `rgba(29, 30, 34, 0.85)` with `backdrop-filter: blur(24px)`
- The particles are visible through the frosted glass, creating depth and movement
- Header: dark frosted glass (`backdrop-filter: blur(20px)`)
- Cards/sections float on glass over the particle background

#### Typography & Colors
- **Bold, Swiss-style typography** — tight letter-spacing (`-0.03em`), font-weight 800 for headings
- Font: system sans-serif stack
- Big type: h1 at 3.5rem, confident and bold
- Primary brand color: `#feba04` (golden amber — **DO NOT change this**)
- Danger/accent: `#d23234` (red)
- Dark background: `#1d1e22`
- Dark surface: `#2a2b30`
- Light background: `#ffffff`
- Light surface: `#f8f9fa`
- Canvas background: `#f0f2f5`
- Text: `#1d1e22` on light, `#f0f0f0` on dark
- Text muted: `#666666`

#### Overall Aesthetic
- Think **Apple product page meets Swiss industrial design**
- Generous whitespace, bold confident layout
- Responsive: mobile-first, perfect on phones
- Scroll animations (fade-in on scroll)
- The particle background + frosted glass is what makes this site unique — it simulates an interactive floor projector, which IS the product being sold

### Bilingual (NL/EN)
- Language toggle (NL | EN) in the nav bar
- Default language: Dutch (NL)
- Use a simple i18n context/hook pattern. All text content should come from a translations object so switching is instant (no page reload)
- URL does NOT change on language switch (same route, different display language)

### Navigation Structure

**Header (sticky, dark background):**
- Logo (left): InterActiveMove (use placeholder, we'll swap the real logo)
- Nav items:
  - **Producten / Products** (dropdown):
    - 2-in-1 Vloer & Muur / 2-in-1 Floor & Wall → `/products/2-in-1-floor-wall`
    - Interactieve Vloer / Interactive Floor → `/products/interactive-floor`
    - Interactieve Muur / Interactive Wall → `/products/interactive-wall`
    - Interactieve Zandbak / Interactive Sandbox → `/products/interactive-sandbox`
    - Interactieve Klimwand / Interactive Climbing Wall → `/products/interactive-climbing-wall`
    - Mobiele Vloer / Mobile Floor → `/products/mobile-floor`
    - Software & Maatwerk / Software & Customization → `/products/software`
  - **Mogelijkheden / Solutions** (dropdown):
    - Bouw een Park / Build a Park → `/build-a-park`
    - 3D Spellen / 3D Games → `/3d-games`
    - Parken & Speelhallen / Parks & Arcades → `/entertainment`
    - Onderwijs / Education → `/education`
    - Zorg & Revalidatie / Care & Rehabilitation → `/healthcare`
  - **Over Ons / About Us** (dropdown):
    - Over InterActiveMove / About InterActiveMove → `/about`
    - Prijzen / Prices → `/pricing`
    - Contact → `/#contact`
  - **Blog** → `/blog`
- Language toggle: NL | EN
- Hamburger menu on mobile
- CTA button: "Contact" (links to contact section)

### Pages

#### 1. Homepage (`/`)
- **Hero**: Full-width video background (placeholder dark gradient for now) with large headline, subtitle, and two CTAs ("Ontdek onze producten" + "Bekijk Demo")
- **Trust strip**: 4 stat counters (e.g. "100+ Spellen", "500+ Installaties", "15+ Landen", "2 Jaar Garantie")
- **Product showcase**: 6 product cards in a grid. Each card: image placeholder, product name, one-line description, "Meer info →" link. Products: Interactive Floor, Interactive Wall, Interactive Sandbox, Interactive Climbing Wall, Mobile Floor, 2-in-1 Floor & Wall
- **"Why InterActiveMove" section**: 4 feature cards with icons (Innovative Tech, Largest Projection, Plug & Play, Dutch Quality)
- **Use cases section**: 3 columns — Education, Healthcare, Entertainment. Each with icon, title, short description, CTA
- **Blog preview carousel**: Horizontal scroll of 3-6 blog post cards (image, date, title, excerpt). Data from a `blogPosts` array
- **Contact section** (`#contact`): Two-column. Left: heading + description + direct info (email: info@interactivemove.nl, phone: +31 6 2399 8934, address: Smitspol 15K, 3861RS Nijkerk). Right: contact form (name, email, phone, company, message, submit button)
- **Footer**: 4 columns (Brand + socials, Quick Links, Products, Contact info). Bottom bar with copyright + legal links

#### 2. Product Pages (`/products/:slug`)
Each product page follows the same template:

- **Product hero**: Two-column layout. Left: product image/video placeholder. Right: product name, subtitle, bullet list of key features, price note ("Op aanvraag" / "On request"), two CTAs (email + phone)
- **"Why this product" section**: 3 spec cards with SVG icons — key selling points
- **Technical specs**: Clean table or spec grid (dimensions, weight, projection size, lumens, resolution, etc.)
- **Use cases**: 3 cards (IAM Moving / IAM Learning / IAM Playing)
- **Video demo section**: Embedded YouTube video placeholder (16:9 aspect ratio)
- **FAQ accordion**: 5-6 Q&A items
- **CTA banner**: "Ready to transform your space?" with email + phone buttons

Products and their key specs:

**Interactive Floor**: 4K laser projector, 3x4m projection, 60+ games, ceiling mount
**Interactive Wall**: 4K laser projector, wall-mounted, multi-touch, 60+ games
**Interactive Sandbox**: AR sandbox, topographic projection, educational
**Interactive Climbing Wall**: Wall-mounted projector, climbing hold integration, gamified
**Mobile Floor**: Same as Interactive Floor but in a wheeled flightcase, 10-min setup
**2-in-1 Floor & Wall**: Combined system, switch between floor and wall mode
**Software & Customization**: Game editor, custom game development, content management

#### 3. Solutions Pages
Each follows a similar template:
- Hero with relevant background
- 3-4 benefit sections with alternating image/text layout
- Product recommendations for that sector
- Testimonial placeholder
- CTA

Pages: `/education`, `/healthcare`, `/entertainment`, `/build-a-park`, `/3d-games`

#### 4. Blog (`/blog`)
**List view** (default):
- Clean light background (#fafafa)
- Large "Blog" title with thin separator line
- **Featured post hero card**: randomly selected, text-left + image-right layout, "Read more" pill button
- **Post grid below**: 4 columns (desktop), 2 (tablet), 1 (mobile). Each card: date on top (monospace uppercase), image, title below. Minimal — no excerpts in grid

**Single post view** (`/blog/:slug`):
- Light background
- Back link at top
- Date, title, feature image
- Full article body (rendered HTML)
- Related posts grid at bottom (max 4)

Blog data source: import from a `blogPosts` array (we'll provide the real data). For now, create 3-4 placeholder posts with lorem ipsum.

#### 5. About (`/about`)
- Company story section
- Team/values section
- Partnership info
- Location/map placeholder

#### 6. Pricing (`/pricing`)
- Comparison table or tiered cards for different products
- "All prices on request" note
- CTA to contact

#### 7. Legal Pages
- `/privacy` — Privacy Policy (placeholder text)
- `/cookies` — Cookie Policy (placeholder text)
- `/accessibility` — Accessibility Statement (placeholder text)

### Components to Build (reusable)

```
Layout/
  Header (sticky, dark, bilingual nav + mobile hamburger)
  Footer (4-column, dark)
  LanguageToggle

UI/
  ProductCard (image, title, description, link)
  BlogCard (image, date, title, excerpt)
  SpecCard (icon, title, description)
  FAQAccordion (question, answer)
  ContactForm
  CTABanner
  TrustStrip (stats)
  VideoEmbed (YouTube iframe wrapper)
  
Pages/
  HomePage
  ProductPage (template, data-driven)
  SolutionPage (template, data-driven)
  BlogListPage
  BlogPostPage
  AboutPage
  PricingPage
  PrivacyPage
  CookiePage
  AccessibilityPage
```

### Data Architecture
All content should live in TypeScript data files (not hardcoded in components):

```typescript
// src/data/products.ts
export const products: Product[] = [...]

// src/data/blogPosts.ts  
export const blogPosts: BlogPost[] = [...]

// src/data/translations.ts
export const translations = { nl: {...}, en: {...} }
```

### Important Notes
- No backend. Everything is static/client-side
- No database. Blog posts are in a TS data file
- Forms: just use mailto: or a simple fetch to an API endpoint placeholder
- All images are placeholders (gradient boxes with text labels). We'll swap real assets later
- Cookie consent banner (GDPR) — simple banner at bottom with Accept/Decline
- SEO: each page should set document.title and meta description via a useEffect or helmet equivalent
- Performance: lazy load images, code-split routes
- The site must feel **finished and professional**, not like a template. Bold typography, confident spacing, polished micro-interactions

### Company Info (for footer, contact, etc.)
- **Name**: Inter Active Move B.V.
- **Address**: Smitspol 15K, 3861RS Nijkerk, Netherlands
- **Phone**: +31 6 2399 8934
- **Email**: info@interactivemove.nl
- **KvK**: 96157895
- **Website**: interactivemove.nl
- **YouTube**: youtube.com/@IAM-InterActiveMove
- **Instagram**: instagram.com/interactivemove

---

*This design will later be exported as static HTML via Next.js `output: 'export'` for SEO. Build components accordingly — no server-side dependencies.*

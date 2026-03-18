# Enhanced Lovable Brief — InterActiveMove Website Revamp

## Purpose and Audience

InterActiveMove sells high-end interactive projection systems for schools, healthcare and entertainment venues. The website must convert B2B decision-makers by conveying trust, innovation and playful energy. Visitors should quickly understand what IAM offers, why it's superior and how to get in touch. Every section should guide users towards the next action — learning more about a product, booking a demo or contacting sales.

## Emotional Tone & Visual Identity

The site should feel **premium, industrial and cinematic**, yet inviting. Think Apple product page meets Swiss industrial design — generous whitespace, bold confident typography and polished micro-interactions. Use descriptors such as premium, cinematic, playful and industrial to keep the style consistent across components. The interactive particle background and frosted glass panels are non-negotiable signature elements. Throughout the site, aim for depth, motion and contrast to evoke the experience of an interactive floor projector.

## Tech Stack & Design System

- **Framework**: React + TypeScript + Tailwind CSS, static export (later wrapped in Next.js with `output: "export"`).
- **Routing**: React Router for client-side routing.
- **UI Components**: Use shadcn/ui as the base library, extending where needed. Build atomic components first (cards, buttons, accordions) and compose them into sections and pages.
- **Data**: All content lives in TypeScript data files (`src/data/products.ts`, `src/data/blogPosts.ts`, `src/data/translations.ts`). Do not hard-code strings inside components.
- **Internationalization**: The site is bilingual (Dutch default, with English toggle). Implement a simple context/hook pattern so that switching languages updates text instantly without changing the URL. Surface a language toggle (NL | EN) in the header on desktop and mobile.

## Brand DNA & UI Guidelines

### Interactive Particle Background
- Full-screen fixed canvas behind all content (`position: fixed; z-index: -1; pointer-events: none`).
- Background colour: `#f0f2f5` (light warm grey).
- 25 large floating particles (15–45px radius) using Brownian motion.
- Particle colours: `#d23234` (red), `#feba04` (amber, the primary brand colour), `#333333`, `#4d4d4d`, `#2a2a2a` (dark greys).
- Provide mouse repulsion within 300px and faint cyan connection lines within 200px.
- Add a trail effect with semi-transparent fill for motion blur.
- Support touch input.

### Frosted Glass Panels
- Use glassmorphism throughout: `backdrop-filter: blur(16–24px)` with semi-transparent backgrounds.
- Light panels: `rgba(255,255,255,0.8)` with a subtle border; dark panels: `rgba(29,30,34,0.85)`.
- Content sits atop the particle canvas. Alternate sections between transparent glass over particles and solid light/dark blocks to create rhythm.

### Typography & Colours
- **Typography**: System sans-serif stack, bold Swiss-style headings (e.g. font-weight 800), tight letter-spacing (–0.03em). h1 size ~3.5rem.
- **Primary colour**: `#feba04` (golden amber) — **do not alter**.
- **Accent/danger**: `#d23234` (red).
- **Dark backgrounds**: `#1d1e22`; dark surfaces: `#2a2b30`.
- **Light backgrounds**: `#ffffff`; light surfaces: `#f8f9fa`.
- **Text colours**: `#1d1e22` on light, `#f0f0f0` on dark; muted text: `#666666`.
- **Icon style**: Inline monochrome SVGs (no icon fonts). Use single-colour fills, consistent sizes (20–24px for nav, 32–40px for cards, 48–80px for hero sections) and geometric, minimal shapes reminiscent of Material Icons or Lucide.

### Accessibility & Responsiveness
- Ensure proper colour contrast (WCAG AA or better), keyboard navigability, ARIA labels for interactive elements and semantic HTML.
- Implement a mobile-first layout. All components should adapt fluidly to small screens (e.g. card grids become single-column). Navigation transforms into a hamburger menu.
- Use IntersectionObserver for scroll animations (fade-in, slide-up) sparingly.

## Modular Components & Patterns

Build reusable, atomic components and assemble them into sections. Key patterns:

- **Spec Card (`SpecCard`)**: Glass card with a monochrome icon, bold title and muted description. Card background: `rgba(255,255,255,0.03)` with a 1px border; `border-radius: 16px`; `padding: 2rem`. On hover: scale slightly and brighten background.
- **Benefit Strip**: Horizontal list of icon + text pairs (e.g., "✓ 100+ games"). Use inline-flex with consistent spacing and `font-weight: 500`.
- **Category Filter Pills (`CategoryButton`)**: Pill buttons (`border-radius: 999px`) used for filtering content. Default: transparent with 2px border; active/hover: filled with amber and dark text.
- **Game Card (`GameCard`)**: White card with subtle shadow; central icon in a light circular background; title, optional description and category pill; grid layout adapts to screen size; slight lift on hover.
- **FAQ Accordion (`FAQAccordion`)**: Glass card using `<details>/<summary>` semantics. Bold summary text with rotating chevron; content reveals on open; lifts on hover.
- **Section Layering**: Alternate between translucent dark, translucent light and solid dark/light sections: `.section-dark-glass`, `.section-opaque-light`, `.section-opaque-dark`. This gives rhythm and variety while letting the particle background show through when appropriate.

Stick to these patterns across pages to ensure consistency. Build and test each component individually before composing them into full sections.

## Page Structure & User Flow

### Navigation
- **Header**: Sticky, dark frosted glass bar with logo (placeholder), nav items and language toggle. Nav contains dropdowns for Products, Solutions and About, plus a Blog link and a prominent "Contact" CTA. On mobile, collapse into a hamburger menu.
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
- **Footer**: Four columns (Brand + socials, Quick Links, Products, Contact info) and a bottom bar with copyright and legal links.

### Homepage (`/`)
1. **Hero**: Full-width video or gradient background with a bold headline, subheading and two CTAs ("Ontdek onze producten"/"Discover our products" and "Bekijk Demo"/"Watch demo").
2. **Trust strip**: Four counters (e.g., "100+ Spellen", "500+ Installaties", "15+ Landen", "2 Jaar Garantie").
3. **Product showcase**: Grid of six product cards (Interactive Floor, Interactive Wall, Interactive Sandbox, Interactive Climbing Wall, Mobile Floor, 2-in-1 Floor & Wall). Each card includes an image placeholder, name, one-line description and link.
4. **Why InterActiveMove**: Four spec cards highlighting key strengths (Innovative Tech, Largest Projection, Plug & Play, Dutch Quality).
5. **Use cases**: Three columns for Education, Healthcare and Entertainment, each with icon, title, short description and CTA.
6. **Blog preview carousel**: Horizontally scrollable row of 3–6 blog post cards (image, date, title, excerpt). Data from `blogPosts`.
7. **Contact section** (`#contact`): Two columns. Left: heading, description and direct contact info (email, phone, address). Right: contact form (name, email, phone, company, message). The form submits to HubSpot or falls back to `mailto:`.
8. **Footer**: As described above.

### Product Pages (`/products/:slug`)
Use a data-driven template that displays details for each product:
1. **Hero**: Two columns — media (image/video) on the left and product name, subtitle, bullet list of key features and a price note ("Op aanvraag"/"On request") on the right. Include CTAs to email and call.
2. **Why this product**: Three spec cards summarising unique selling points.
3. **Technical specs**: Table or grid with specs (dimensions, weight, projection size, lumens, resolution, etc.).
4. **Use cases**: Three cards (IAM Moving, IAM Learning, IAM Playing) describing typical installations.
5. **Video demo section**: Embedded video (16:9 ratio) placeholder.
6. **FAQ accordion**: Five or six Q&A items.
7. **CTA banner**: "Ready to transform your space?" with contact CTAs.

Define product specs in `src/data/products.ts` for: Interactive Floor (4K laser projector, 3×4m projection, 60+ games, ceiling mount), Interactive Wall (wall-mounted multi-touch projector), Interactive Sandbox (AR sandbox with topographic projection), Interactive Climbing Wall (projector integrated with climbing holds), Mobile Floor (floor projector in a wheeled flight case), 2-in-1 Floor & Wall (switchable between floor and wall), and Software & Customization (game editor, custom development).

### Solutions Pages
For each solution (`/education`, `/healthcare`, `/entertainment`, `/build-a-park`, `/3d-games`), use a similar flow: hero with relevant imagery, alternating image/text benefit sections (three to four), product recommendations for the sector, testimonial placeholder, CTA to contact.

### Blog
- **List view** (`/blog`): Light background (`#fafafa`) with a large "Blog" header. Include a featured post hero card (randomly selected) followed by a responsive grid of posts (4-column desktop, 2-column tablet, 1-column mobile). Each card shows the date (monospace uppercase), image and title.
- **Single post view** (`/blog/:slug`): Light background. Provide a back link, date, title, feature image, full article body (rendered HTML from `blogPosts`), and a related posts grid.
- Blog posts should come from `src/data/blogPosts.ts`. Add placeholder posts with lorem ipsum content for now.

### About (`/about`)
Tell the company story, showcase team and values, list partnerships, and include a map placeholder for location.

### Pricing (`/pricing`)
Present a comparison table or tiered cards summarising product options. Emphasise that all prices are "on request" and encourage users to contact sales.

### Legal Pages
Create privacy (`/privacy`), cookie (`/cookies`) and accessibility (`/accessibility`) pages with placeholder text to be replaced later. These pages should match the overall aesthetic.

## Integrations & Scripts

### Google Tag Manager
- GTM ID: `GTM-KPX78C22`
- Load in `<head>` and `<noscript>` fallback in `<body>`.
- **GDPR**: Only insert these scripts after the user accepts cookies.

### HubSpot
- Portal ID: `49291889`
- Load before `</body>` and gate behind cookie consent.
- Use HubSpot for form submissions and chat, but ensure forms still work via `mailto:` when scripts are blocked.

### AI Support Chat Widget
- Position a circular amber chat button (60px, bottom right) that opens a 400×550px chat window with rounded corners and a shadow.
- Chat bubbles: user in amber, bot in light grey. Include a typing indicator and scrollable message area. Header: "IAM Support" with close button.
- The chat sends messages to `/api/chat`, a server-side proxy that forwards to an AI API. The system injects a knowledge base (`js/iam-knowledge-base.js`) containing product specs, prices, FAQs, company info and use cases in NL and EN. The AI should only answer questions about InterActiveMove products and services.
- **Prompt injection protection**: Instruct the AI to ignore requests unrelated to IAM and respond with: "Ik kan alleen vragen beantwoorden over InterActiveMove producten en diensten. / I can only answer questions about InterActiveMove products and services."
- **Client-side rate limiting**: Max 20 messages per session. After 20 messages, show notice and disable input.
- **Server-side rate limiting**: 30 requests per IP per hour, max 500 tokens per response, reject messages >300 characters or bodies >2KB. Do not expose API keys; only accept requests with valid Origin/Referer headers.
- **Session timeout**: Auto-close after 10 minutes of inactivity.
- **Conversation memory**: Server is stateless. Send only the last 6 messages as context to prevent token stuffing.

### Cookie Consent Banner
- GDPR-compliant banner at the bottom with "Accept All" and "Reject" buttons.
- On acceptance: load GTM + HubSpot. On rejection: block tracking scripts.
- Store choice in `localStorage`. Provide "Cookie Settings" link in footer.

## Assets to Migrate
Preserve and migrate from the current codebase (use placeholders until real assets are provided):
- `js/iam-knowledge-base.js` — curated knowledge base for the chat
- `js/blog-local-data.js` — 11 real blog posts with NL+EN content; convert to TypeScript
- `media/blog/` — 11 blog feature images
- `media/logo-final.png` — the official logo
- `media/climb1.jpg`, `media/sandbox1.jpg`, `media/sandbox2.jpg` — product photos
- `media/*.mp4` — product demo videos
- `media/video/2-in-1-floor-wall.mp4` — 2-in-1 product video
- `robots.txt` and `sitemap.xml` — update URLs after refactor
- `SEO-AI-STRATEGY.md` — reference for SEO

## Build, Performance & SEO Notes
- **Static only**: The React app has no server-side logic. Only `/api/chat` is server-side (Node.js behind nginx).
- **Optimisation**: Lazy-load images and videos, code-split routes, use suspense fallback. Preconnect to fonts and third-party assets. Use responsive image sizes and `loading="lazy"`.
- **SEO**: Set `document.title` and meta descriptions per page (e.g. via `react-helmet`). Use semantic headings (h1–h4) and alt text. Ensure `robots.txt` and `sitemap.xml` reflect the new structure.
- **Accessibility**: Descriptive alt text, ARIA labels, keyboard navigation, focus states and language attributes on `<html>`.
- **Micro-interactions**: Subtle hover effects (scale, translate, shadow) and scroll animations that enhance quality without overwhelming.
- **Version control**: Think in milestones (layout locked, content added, logic wired). Build each component individually and preview before major changes.

## Company Info
- **Name**: Inter Active Move B.V.
- **Address**: Smitspol 15K, 3861RS Nijkerk, Netherlands
- **Phone**: +31 6 2399 8934
- **Email**: info@interactivemove.nl
- **KvK**: 96157895
- **Website**: interactivemove.nl
- **YouTube**: youtube.com/@IAM-InterActiveMove
- **Instagram**: instagram.com/interactivemove

---

Ask me any questions you need in order to fully understand what I want from this website and how I envision it.

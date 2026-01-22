# Project: InterActiveMove Website

Last Updated: 2026-01-22

---

## Project Overview

- **Purpose:** Modern, interactive promotional website for Inter Active Move B.V., a Dutch company selling interactive projection systems for education, healthcare, entertainment, and rehabilitation sectors.
- **Tech Stack:** HTML5, CSS3 (Vanilla), HTMX 1.9.10, Vanilla JavaScript (Canvas API)
- **Architecture:** Static Site with Shell + Partials Pattern (HTMX-based SPA-like behavior)
- **Status:** Production-ready

---

## MCP Tools Integration

**CRITICAL: Always utilize available MCP (Model Context Protocol) tools for enhanced capabilities.**

### Available MCP Servers

#### Context7 - Library Documentation
**When to use:** Getting up-to-date documentation for any library or framework

**Available Tools:**
- `mcp__context7__resolve-library-id` - Convert library name to Context7 ID
- `mcp__context7__get-library-docs` - Fetch comprehensive documentation

**Project-Specific Usage:**
```markdown
- HTMX documentation: resolve-library-id("htmx") → get-library-docs for HTMX patterns
- Canvas API: Use for particle physics implementation in projector.js
```

**When to ALWAYS use:**
- Working with HTMX attributes or patterns
- Implementing Canvas animations
- CSS3 modern features (Flexbox, Grid, custom properties)

#### Sequential Thinking - Complex Problem Solving
**When to use:** Breaking down complex problems with multi-step reasoning

**Available Tools:**
- `mcp__sequential-thinking__sequentialthinking` - Chain of thought reasoning

**When to ALWAYS use:**
- Designing new i18n content structure
- Debugging HTMX partial loading issues
- Performance optimization for particle animation
- Complex CSS layout problems

#### Playwright - Browser Automation
**When to use:** Testing web applications, screenshots, UI automation

**Available Tools:**
- `mcp__playwright__browser_navigate` - Navigate to URLs
- `mcp__playwright__browser_snapshot` - Capture accessibility tree
- `mcp__playwright__browser_click` - Click elements
- `mcp__playwright__browser_take_screenshot` - Capture visual screenshots

**Project-Specific Usage:**
- Test language switching functionality (NL/EN)
- Verify particle background renders correctly
- Test mobile navigation hamburger menu
- Validate HTMX partial swapping

---

## Technology Stack

### Frontend
- **Structure:** Semantic HTML5
- **Styling:** Vanilla CSS3 (~1,696 lines) with CSS Custom Properties, Flexbox, Grid
- **Interactivity:** HTMX 1.9.10 (CDN: unpkg.com)
- **Animation:** Vanilla JavaScript with Canvas API (particle physics engine)
- **Fonts:** Inter (Google Fonts - weights 300, 400, 600, 800)
- **Icons:** Inline SVGs

### Backend
- **None** - 100% static site, no server-side processing required

### Infrastructure
- **Deployment:** Any static hosting (Netlify, Vercel, GitHub Pages, Hostinger)
- **CDN Dependencies:**
  - HTMX: `https://unpkg.com/htmx.org@1.9.10`
  - Google Fonts: Inter font family
- **Build Process:** None required - files are production-ready

### Development Tools
- **Version Control:** Git
- **Local Server:** Python 3 (`python3 -m http.server`) or any static server
- **i18n Migration:** Python 3 script (`tools/migrate_i18n.py`)

---

## Architecture Overview

### Design Patterns

- **Shell + Partial Pattern:** Each page has a shell HTML file containing `<head>`, global `<canvas>`, and `<div id="page-wrapper">`. Content is dynamically loaded via HTMX.
- **i18n via HTMX:** Language switching triggers partial HTML swaps without full page reload.
- **Canvas Background:** Interactive particle system runs on all pages via `projector.js`.

### Key Components

- **Page Shells (14 files):** Container pages with meta, scripts, and page-wrapper div
- **Content Partials (30 files):** NL and EN versions of each page's content
- **projector.js:** Interactive particle background with cursor-reactive physics
- **styles.css:** Centralized stylesheet with CSS custom properties

### Data Flow
```
User visits page → Shell loads → Default partial (NL) inserted into #page-wrapper
                                            ↓
User clicks language button → HTMX fetches new partial → Content swaps → URL updates
```

### Directory Structure
```
iam-website/
├── index.html                    # Homepage shell
├── styles.css                    # Global stylesheet (~1,696 lines)
├── projector.js                  # Interactive particle background (248 lines)
│
├── products/                     # Product page shells (6 files)
│   ├── interactieve-vloer.html
│   ├── interactieve-muur.html
│   ├── interactieve-zandbak.html
│   ├── interactieve-klimwand.html
│   ├── mobiele-vloer.html
│   └── software-maatwerk.html
│
├── [Page Shells]                 # Other page shells (7 files)
│   ├── bouw-een-park.html
│   ├── 3d-spellen.html
│   ├── parken-speelhallen.html
│   ├── onderwijs.html
│   ├── zorg-revalidatie.html
│   ├── over-ons.html
│   └── prijzen.html
│
├── partials/                     # HTMX content partials (30 files)
│   ├── index-nl.html / index-en.html
│   ├── products/
│   │   └── [product]-nl.html / [product]-en.html
│   └── [page]-nl.html / [page]-en.html
│
├── media/                        # Static assets (~17MB)
│   ├── logo-final.png
│   ├── hero-video.webm
│   ├── products/
│   └── [various images]
│
├── tools/
│   └── migrate_i18n.py           # i18n migration script
│
├── reference/                    # Design references (not for production)
├── CLAUDE.md                     # This file
└── README.md                     # Project documentation
```

---

## Development Commands

### Setup
```bash
# Clone repository
git clone [repository-url]
cd iam-website

# No dependencies to install - it's a static site!
```

### Development
```bash
# Start local development server (Python)
python3 -m http.server 8000
# Open http://localhost:8000

# Alternative: Node.js
npx serve .

# Alternative: PHP
php -S localhost:8000
```

### i18n Migration
```bash
# Generate/update i18n partials (if modifying page structure)
python3 tools/migrate_i18n.py
```

### Deployment
```bash
# Netlify - drag & drop or Git integration
# Vercel
vercel --prod

# GitHub Pages - push to main, enable Pages in settings

# Traditional hosting - upload all files via FTP
```

---

## Agent Dispatch History

### 2026-01-22 - Initial CLAUDE.md Customization
- **Agents Used:**
  - Explore (codebase analysis)
- **Skills Used:** None
- **MCP Tools Used:** None
- **Outcome:** Comprehensive CLAUDE.md created with project-specific documentation
- **Learnings:** Project uses HTMX shell+partial pattern for SPA-like i18n

---

## Recent Decisions

### Initial Commit - Shell + Partial Architecture for i18n
- **Context:** Needed multi-language support without backend or build process
- **Decision:** HTMX-based shell + partial swapping pattern
- **Rationale:**
  - No build step required
  - Fast language switching without page reload
  - SEO-friendly (each page has full HTML shell)
  - Simple to maintain and deploy
- **Alternatives Considered:**
  - JavaScript i18n library: Would require build step
  - Server-side rendering: Would require backend
  - Separate domains (nl.site.com): Complex DNS setup
- **Impact:** All pages follow shell + partial pattern; 30 partial files for 15 pages

---

## Established Patterns & Conventions

### File Naming
- **Page shells:** `kebab-case.html` (e.g., `interactieve-vloer.html`)
- **Partials:** `[page-name]-[lang].html` (e.g., `interactieve-vloer-nl.html`)
- **Languages:** `nl` (Dutch - default), `en` (English)

### HTML Structure
- **Shell pages** contain: `<!DOCTYPE>`, `<head>`, `<canvas>`, `<div id="page-wrapper">`, scripts
- **Partials** contain: Content from `<header>` through `<footer>` only
- **HTMX attributes** on language buttons: `hx-get`, `hx-target="#page-wrapper"`, `hx-swap="innerHTML"`, `hx-push-url`

### CSS Patterns
- **Custom properties** for colors, spacing, radii (defined at `:root`)
- **BEM-like naming** for component classes
- **Glassmorphism** via `backdrop-filter: blur()` with semi-transparent backgrounds
- **Pill shapes** via `border-radius: 999px`

### JavaScript Patterns
- **Vanilla JS only** - no frameworks or libraries (except HTMX)
- **Canvas API** for particle animation
- **HTMX lifecycle hooks** for reinitializing canvas after content swap

### HTMX Integration
```html
<!-- Language toggle pattern -->
<button class="lang-btn active"
        hx-get="partials/[page]-nl.html"
        hx-target="#page-wrapper"
        hx-swap="innerHTML"
        hx-push-url="?lang=nl">NL</button>
<button class="lang-btn"
        hx-get="partials/[page]-en.html"
        hx-target="#page-wrapper"
        hx-swap="innerHTML"
        hx-push-url="?lang=en">EN</button>
```

---

## Known Issues & Solutions

### migrate_i18n.py Hardcoded Path
- **Problem:** Script contains hardcoded developer path (`/Users/ottogen/Projects/...`)
- **Symptoms:** Script fails on other machines
- **Solution:** Update script to use `os.getcwd()` or detect project root
- **Prevention:** Always use relative paths or environment detection

### Canvas Performance on Low-End Devices
- **Problem:** 25 particles with connection calculations may strain older devices
- **Symptoms:** Choppy animation, high CPU usage on mobile
- **Solution:** Consider reducing particle count or disabling on mobile
- **Prevention:** Test on low-end devices during development

### HTMX CDN Dependency
- **Problem:** Site requires internet to load HTMX from unpkg
- **Symptoms:** Language switching fails offline
- **Solution:** Bundle HTMX locally if offline support needed
- **Prevention:** Include local fallback or service worker

---

## Skills Configuration

### Recommended Skills for Common Tasks
```
Task                              → Recommended Approach
────────────────────────────────────────────────────────
Add new page                      → Create shell + NL/EN partials
Add new product                   → Create in products/ + partials/products/
Update content                    → Edit appropriate partial (NL and EN)
Change styling                    → Edit styles.css, use CSS custom properties
Modify particle animation         → Edit projector.js
Test language switching           → Use Playwright browser automation
Add new language                  → Create new partials, update language toggle
```

---

## Security & Authentication

### Security Measures
- **No Backend:** No server-side vulnerabilities possible
- **Static Content:** No user input processing server-side
- **Form Handling:** Contact form submits to WhatsApp (external service)
- **XSS Prevention:** No dynamic content injection from user input

### External Integrations
```
WhatsApp Business: +31 6 2399 8934
URL Pattern: https://wa.me/31623998934?text=[urlencoded message]
```

---

## Testing Strategy

### Manual Testing
- **Language Switching:** Verify NL/EN toggle works on all pages
- **Mobile Navigation:** Test hamburger menu on mobile viewports
- **Particle Background:** Verify canvas renders and responds to cursor
- **Links:** Test all internal and external links

### Automated Testing (via Playwright MCP)
```markdown
1. Navigate to each page
2. Click language toggle, verify content swaps
3. Take screenshots at various breakpoints
4. Verify HTMX requests complete successfully
```

---

## Performance Considerations

### Current Optimizations
- **CSS Versioning:** `styles.css?v=1.2` for cache busting
- **WebM Video:** Modern format for hero video
- **Inline SVGs:** No additional HTTP requests for icons
- **Google Fonts Preconnect:** Fast font loading

### Potential Optimizations
- **Image Compression:** Media folder is 17MB, could benefit from optimization
- **Lazy Loading:** Add `loading="lazy"` to below-fold images
- **Font Subsetting:** Reduce font file sizes if not using all characters
- **Canvas Optimization:** Reduce particles on mobile devices

---

## Company Information

### Inter Active Move B.V.
- **Address:** Smitspol 15K, 3861RS Nijkerk, Netherlands
- **Phone:** +31 6 2399 8934
- **Email:** klantcontact@interactivemove.nl
- **KvK (Chamber of Commerce):** 96157895

### Products
1. **Interactieve Vloer** - Interactive floor projection
2. **Interactieve Muur** - Interactive wall projection
3. **Interactieve Zandbak** - AR sandbox
4. **Interactieve Klimwand** - Interactive climbing wall
5. **Mobiele Vloer** - Mobile/rental floor for events
6. **Software & Maatwerk** - Custom software and game editor

### Target Markets
- Parks & Arcades (Entertainment venues)
- Education (Schools, learning centers)
- Healthcare & Rehabilitation (Therapy, elderly care)

---

## Design System

### Color Palette
| Name | Hex | Usage |
|------|-----|-------|
| Primary (Amber) | `#feba04` | CTAs, highlights, hover states |
| Danger (Red) | `#d23234` | Secondary accent, danger buttons |
| Background | `#ffffff` | Main page background |
| Surface | `#f8f9fa` | Card backgrounds |
| Text | `#1d1e22` | Body text, headings |
| Text Muted | `#666666` | Secondary text |
| Dark BG | `#1d1e22` | Dark sections |
| Dark Surface | `#2a2b30` | Dark card backgrounds |
| Text on Dark | `#f0f0f0` | Light text on dark |

### CSS Custom Properties
```css
--color-primary: #feba04;
--color-danger: #d23234;
--color-bg: #ffffff;
--color-surface: #f8f9fa;
--color-text: #1d1e22;
--color-text-muted: #666666;
--spacing-xs: 0.5rem;
--spacing-sm: 1.5rem;
--spacing-md: 3rem;
--spacing-lg: 8rem;
--radius-card: 24px;
--radius-btn: 999px;
```

### Typography
- **Font Family:** Inter (Google Fonts)
- **Weights:** 300 (light), 400 (regular), 600 (semibold), 800 (bold)
- **H1:** 5rem, weight 800
- **H2:** 3.5rem, weight 800
- **H3:** 1.5rem, weight 600
- **Body:** 1rem, weight 400

---

## Next Steps

**Immediate:**
- [ ] Fix hardcoded path in `tools/migrate_i18n.py`
- [ ] Optimize images in media folder

**Short Term:**
- [ ] Add lazy loading to images
- [ ] Consider service worker for offline support
- [ ] Performance testing on mobile devices

**Long Term:**
- [ ] Analytics integration
- [ ] A/B testing for CTAs
- [ ] Additional language support (German, French)

**Backlog:**
- [ ] Contact form with email integration (alternative to WhatsApp)
- [ ] Blog/news section
- [ ] Customer testimonials with video

---

## Additional Resources

### HTMX Documentation
- Official docs: https://htmx.org/docs/
- Use Context7 MCP for quick reference

### Canvas API
- MDN Canvas Tutorial: https://developer.mozilla.org/en-US/docs/Web/API/Canvas_API/Tutorial

### CSS Reference
- CSS Custom Properties: https://developer.mozilla.org/en-US/docs/Web/CSS/--*
- Backdrop Filter: https://developer.mozilla.org/en-US/docs/Web/CSS/backdrop-filter

---

## Collaboration Guidelines

### Code Review Checklist
- [ ] Both NL and EN partials updated for content changes
- [ ] CSS custom properties used (no hardcoded colors)
- [ ] HTMX attributes correct on language buttons
- [ ] Tested on mobile viewport
- [ ] Canvas background still functions
- [ ] CLAUDE.md updated if patterns changed

### PR Template
```markdown
## Summary
[Brief description]

## Pages Affected
- [ ] index.html
- [ ] [other pages]

## Partials Updated
- [ ] partials/[page]-nl.html
- [ ] partials/[page]-en.html

## Testing
- [ ] Language switching tested
- [ ] Mobile view tested
- [ ] Canvas background verified

## Screenshots
[Before/after if UI changes]
```

---

## Project-Specific Notes

### Important Quirks
- **Default language is NL:** Partials load Dutch content on initial page load
- **URL query params:** `?lang=nl` or `?lang=en` controls language state
- **Canvas z-index:** Canvas is behind all content; opaque sections hide it

### Local Development Tips
- Always test both NL and EN versions when changing content
- Use browser DevTools to monitor HTMX requests in Network tab
- Canvas can be temporarily disabled by commenting out `new InteractiveFloor()` for faster iteration

### Common Gotchas
- **Partial paths:** Partials in `products/` subfolder need correct relative paths in shell files
- **HTMX not working:** Ensure HTMX script is loaded before using hx-* attributes
- **Canvas not appearing:** Check that canvas element exists and `projector.js` is loaded

---

## Changelog

### 2026-01-22
- Added: Initial customized CLAUDE.md based on codebase analysis
- Changed: Replaced template placeholders with project-specific information

---

**Last Reviewed:** 2026-01-22
**Maintained By:** Orchestrator Agent + Team
**Template Version:** 1.0.0

---

## Using This File

**For Orchestrator Agent:**
- Read this file at the start of EVERY task
- Update relevant sections after completing work
- Reference the directory structure for file locations
- Follow established HTMX patterns for new features

**For All Agents:**
- Reference Design System for styling
- Follow File Naming conventions
- Update both NL and EN partials for content changes
- Use Playwright MCP for UI testing

**For Developers:**
- Keep this file current as the project evolves
- Document any new HTMX patterns discovered
- Update Known Issues when problems are resolved

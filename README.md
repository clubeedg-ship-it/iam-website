# InterActiveMove Website (IAM Website)

A modern, interactive promotional website for **Inter Active Move B.V.**, a company specializing in interactive projection systems for education, healthcare, entertainment, and rehabilitation.

---

## ✨ Key Features

- **100% Static Site**: No backend required. Deployable to any static host (Netlify, Vercel, GitHub Pages, Hostinger).
- **HTMX-Powered**: Dynamic content swapping without heavy JavaScript frameworks.
- **Multi-Language Support**: Full Dutch (NL) and English (EN) support via HTMX partial loading.
- **Interactive Background**: Cursor-reactive particle animation using vanilla JavaScript Canvas API.
- **Glassmorphism UI**: Modern design with frosted-glass effects, pill-shaped buttons, and dynamic hover states.
- **Responsive Design**: Mobile-first CSS with full desktop and tablet support.

---

## 📁 Project Structure

```
iam-website/
├── index.html                   # Homepage (Shell)
├── styles.css                   # Global stylesheet (~1700 lines)
├── projector.js                 # Interactive particle background animation
│
├── products/                    # Product detail pages
│   ├── interactieve-vloer.html  # Interactive Floor
│   ├── interactieve-muur.html   # Interactive Wall
│   ├── interactieve-zandbak.html# Interactive Sandbox
│   ├── interactieve-klimwand.html# Interactive Climbing Wall
│   ├── mobiele-vloer.html       # Mobile (Rental) Floor
│   └── software-maatwerk.html   # Software & Customization
│
├── bouw-een-park.html           # "Build a Park" configurator page
├── 3d-spellen.html              # 3D Games showcase
├── parken-speelhallen.html      # Parks & Arcades solutions
├── onderwijs.html               # Education solutions
├── zorg-revalidatie.html        # Healthcare & Rehabilitation
├── over-ons.html                # About Us
├── prijzen.html                 # Pricing
│
├── partials/                    # HTMX language partials
│   ├── index-nl.html            # Dutch homepage content
│   ├── index-en.html            # English homepage content
│   ├── products/                # Product partials (NL & EN)
│   │   ├── interactieve-vloer-nl.html
│   │   ├── interactieve-vloer-en.html
│   │   └── ...
│   └── [page-name]-nl.html / -en.html
│
├── media/                       # Static assets
│   ├── logo-final.png           # Company logo
│   ├── icon.png                 # Favicon
│   ├── hero-video.webm          # Homepage hero video
│   ├── hero_*.png               # Page-specific hero images
│   └── products/                # Product images
│
├── tools/                       # Development scripts
│   └── migrate_i18n.py          # i18n migration automation script
│
└── reference/                   # Design references (not for production)
```

---

## 🛠 Technology Stack

| Component          | Technology                         |
|--------------------|-------------------------------------|
| **Structure**      | Semantic HTML5                      |
| **Styling**        | Vanilla CSS (CSS Variables, Flexbox, Grid) |
| **Interactivity**  | [HTMX 1.9+](https://htmx.org/) for SPA-like behavior |
| **Animation**      | Vanilla JavaScript (Canvas API)     |
| **Fonts**          | [Inter](https://fonts.google.com/specimen/Inter) via Google Fonts |
| **Icons**          | Inline SVGs                         |
| **Backend**        | None (Static Site)                  |

---

## 🎨 Design System

### Color Palette

| Name           | Hex       | Usage                           |
|----------------|-----------|----------------------------------|
| Primary (Amber)| `#feba04` | CTAs, highlights, icons          |
| Danger (Red)   | `#d23234` | Secondary accent, tooltips       |
| Background     | `#ffffff` | Page background                  |
| Surface        | `#f8f9fa` | Cards, panels                    |
| Text           | `#1d1e22` | Body text                        |
| Text Muted     | `#666666` | Secondary/subtle text            |
| Dark BG        | `#1d1e22` | Dark sections                    |
| Dark Surface   | `#2a2b30` | Dark cards                       |
| Text on Dark   | `#f0f0f0` | Text on dark backgrounds         |

### Typography

- **Font Family**: `'Inter', system-ui, -apple-system, sans-serif`
- **Weights**: 300 (Light), 400 (Regular), 600 (Semi-Bold), 800 (Extra Bold)
- **Heading Style**: Tightly kerned (`letter-spacing: -0.03em`)

### Spacing & Radii

| Token       | Value   |
|-------------|---------|
| xs          | 0.5rem  |
| sm          | 1.5rem  |
| md          | 3rem    |
| lg          | 8rem    |
| Card Radius | 24px    |
| Button Radius| 999px (Pill)|

---

## 🌐 Multi-Language System (i18n)

The site uses **HTMX** for dynamic language switching without page reloads.

### How it Works

1. Each page has a "Shell" HTML file containing `<head>`, canvas, and a `<div id="page-wrapper">`.
2. Language toggle buttons use HTMX attributes:
   ```html
   <button class="lang-btn active" 
           hx-get="partials/index-nl.html" 
           hx-target="#page-wrapper" 
           hx-swap="innerHTML" 
           hx-push-url="?lang=nl">NL</button>
   ```
3. Clicking a language button loads the corresponding partial into `#page-wrapper`.
4. On page load, JavaScript checks for `?lang=en` and fetches the English partial if present.

### Partials Directory

- `partials/index-nl.html` — Dutch homepage
- `partials/index-en.html` — English homepage
- `partials/products/interactieve-vloer-nl.html` — Dutch product page
- `partials/products/interactieve-vloer-en.html` — English product page
- *(Same pattern for all pages)*

---

## 🎬 Interactive Background (`projector.js`)

A lightweight particle physics engine that:

- Renders 25 particles on a full-screen Canvas.
- Reacts to mouse/touch movement (repulsion effect).
- Creates subtle connection lines between nearby particles.
- Uses brand colors (Amber, Red, Dark Greys).
- Supports HTMX content swaps (reinitializes on `htmx:afterSwap`).

### Configuration (in `projector.js`)

```javascript
this.particleCount = 25;       // Number of particles
this.connectionDistance = 200; // Max distance for connection lines
this.mouseRadius = 300;        // Cursor interaction radius
this.baseSpeed = 0.5;          // Default particle velocity
```

---

## 🚀 Deployment

### Static Hosting (Recommended)

Simply upload the entire `iam-website/` folder to:

- **Netlify**: Drag & drop or connect Git.
- **Vercel**: `vercel --prod` from CLI.
- **GitHub Pages**: Push to `main` and enable Pages.
- **Hostinger/cPanel**: Upload via FTP.

### Local Development

```bash
# From iam-website directory
python3 -m http.server 8000
# OR
npx serve .
```

Then open `http://localhost:8000`.

---

## 📄 Page Overview

| Page                    | URL Path                         | Description                                |
|-------------------------|----------------------------------|--------------------------------------------|
| Homepage                | `/index.html`                    | Hero, products, FAQ, contact               |
| Interactive Floor       | `/products/interactieve-vloer.html` | Floor projection product                |
| Interactive Wall        | `/products/interactieve-muur.html`  | Wall projection product                 |
| Interactive Sandbox     | `/products/interactieve-zandbak.html`| AR sandbox product                     |
| Interactive Climbing Wall| `/products/interactieve-klimwand.html`| Climbing wall game product           |
| Mobile Floor            | `/products/mobiele-vloer.html`   | Event rental product                       |
| Software & Custom       | `/products/software-maatwerk.html`| Game Editor & custom solutions           |
| Build a Park            | `/bouw-een-park.html`            | Park configurator with interactive map     |
| 3D Games                | `/3d-spellen.html`               | Game library showcase                      |
| Parks & Arcades         | `/parken-speelhallen.html`       | Entertainment venue solutions              |
| Education               | `/onderwijs.html`                | School & learning solutions                |
| Care & Rehab            | `/zorg-revalidatie.html`         | Healthcare applications                    |
| About Us                | `/over-ons.html`                 | Company info, team, values                 |
| Pricing                 | `/prijzen.html`                  | Product pricing tiers                      |

---

## 📝 Contact & Conversion

All CTAs link to **WhatsApp Business** for direct communication:

```
https://wa.me/31623998934?text=Hello%2C%20I%20would%20like%20more%20information...
```

---

## 🔧 Development Scripts

### `tools/migrate_i18n.py`

Automates the creation of i18n partials:

1. Extracts `<header>` through `</footer>` from each page.
2. Creates NL partial (original content).
3. Creates EN partial (auto-translated nav/footer, placeholder body).
4. Updates original page to serve as Shell with `#page-wrapper`.
5. Adds HTMX attributes to language toggle buttons.

**Usage:**
```bash
cd iam-website
python3 tools/migrate_i18n.py
```

---

## 📜 License

This project is proprietary to **Inter Active Move B.V.**

© 2026 InterActiveMove B.V. All rights reserved.

---

## 👥 Credits

- **Design & Development**: IAM Development Team
- **Brand Style Guide**: IAM Brand Style Guide v1.0
- **HTMX**: [htmx.org](https://htmx.org/)
- **Inter Font**: [Google Fonts](https://fonts.google.com/specimen/Inter)

# InterActiveMove Website
## UX & High-Converting Landing Page Strategy Report

**Document Version:** 1.0  
**Date:** January 2026  
**Prepared for:** Inter Active Move B.V.  
**Prepared by:** UX & Conversion Strategy Consultant

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Conversion Psychology Framework](#2-conversion-psychology-framework)
3. [Visual Storytelling Architecture](#3-visual-storytelling-architecture)
4. [Trust Signal Strategy](#4-trust-signal-strategy)
5. [Page-by-Page UX Blueprint](#5-page-by-page-ux-blueprint)
   - 5.1 [Homepage (index.html)](#51-homepage-indexhtml)
   - 5.2 [Product Pages](#52-product-pages)
   - 5.3 [Solution/Industry Pages](#53-solutionindustry-pages)
   - 5.4 [About Us Page](#54-about-us-page-over-onshtml)
   - 5.5 [Pricing Page](#55-pricing-page-prijzenhtml)
   - 5.6 [Build a Park Configurator](#56-build-a-park-configurator-bouw-een-parkhtml)
   - 5.7 [3D Games Showcase](#57-3d-games-showcase-3d-spellenhtml)
6. [Navigation & Information Architecture](#6-navigation--information-architecture)
7. [CTA Strategy & Placement](#7-cta-strategy--placement)
8. [Mobile-First Conversion Optimization](#8-mobile-first-conversion-optimization)
9. [Microinteractions & Delight Factors](#9-microinteractions--delight-factors)
10. [Accessibility as UX](#10-accessibility-as-ux)
11. [Implementation Priority Matrix](#11-implementation-priority-matrix)
12. [Appendix: Component Library Recommendations](#12-appendix-component-library-recommendations)

---

## 1. Executive Summary

### Current State Assessment

InterActiveMove sells **high-ticket B2B interactive projection systems** (€5,000–€50,000+ range) to decision-makers in education, healthcare, and entertainment sectors. The website must accomplish:

1. **Educate** — Explain what interactive projection systems are
2. **Inspire** — Show transformative possibilities
3. **Build Trust** — Establish credibility for significant investment
4. **Convert** — Generate qualified leads via WhatsApp/contact

### Key Conversion Challenges

| Challenge | Impact | Priority |
|-----------|--------|----------|
| High-ticket items require extensive trust-building | Visitors need 7-12 touchpoints before purchase decision | Critical |
| Abstract product (projection systems) needs visualization | Visitors can't "imagine" the product in their space | Critical |
| Multiple buyer personas (teachers, healthcare admins, park owners) | Different value propositions needed per segment | High |
| Dutch B2B market expects professionalism + warmth | Balance between corporate and approachable | High |
| WhatsApp as primary CTA may feel informal for large purchases | Need to frame WhatsApp as "direct expert consultation" | Medium |

### Strategic Pillars

```
┌─────────────────────────────────────────────────────────────────┐
│                    CONVERSION STRATEGY PILLARS                   │
├─────────────────┬─────────────────┬─────────────────────────────┤
│   CREDIBILITY   │   VISUALIZATION │      EMOTIONAL RESONANCE    │
│                 │                 │                             │
│ • Case studies  │ • Video demos   │ • Child joy imagery         │
│ • Client logos  │ • 360° views    │ • Patient recovery stories  │
│ • Certifications│ • AR preview    │ • Teacher testimonials      │
│ • Years in biz  │ • Before/after  │ • ROI success metrics       │
└─────────────────┴─────────────────┴─────────────────────────────┘
```

---

## 2. Conversion Psychology Framework

### 2.1 Cialdini's Principles Applied to IAM

| Principle | Application for IAM | Implementation |
|-----------|---------------------|----------------|
| **Social Proof** | "500+ installations across Netherlands" | Counter animation on homepage, logo wall |
| **Authority** | Partnerships with schools, hospitals | Official partner badges, certifications |
| **Scarcity** | "Limited installation slots per month" | Booking calendar with availability |
| **Reciprocity** | Free ROI calculator, game demo videos | Downloadable resources, video library |
| **Liking** | Friendly Dutch team photos, casual tone | Team section with personality, video intros |
| **Commitment** | Progressive engagement (watch → download → call) | Multi-step lead capture funnel |

### 2.2 The "Jobs to Be Done" Framework

Each visitor has a specific "job" they're trying to accomplish:

```
EDUCATION BUYER:
├── Job: "Make learning more engaging for my students"
├── Fears: Budget approval, teacher adoption, maintenance
├── Desires: Measurable learning outcomes, easy setup
└── Trigger: Saw competitor school with interactive floor

HEALTHCARE BUYER:
├── Job: "Improve patient rehabilitation outcomes"
├── Fears: Clinical efficacy, hygiene, durability
├── Desires: Evidence-based results, patient satisfaction
└── Trigger: Research on gamified therapy effectiveness

ENTERTAINMENT BUYER:
├── Job: "Create unique attractions that drive repeat visits"
├── Fears: ROI timeline, technical reliability, content updates
├── Desires: Wow factor, low maintenance, fresh content
└── Trigger: Declining visitor numbers, competition pressure
```

### 2.3 The Persuasion Path

```
AWARENESS → INTEREST → DESIRE → ACTION
    │           │          │         │
    ▼           ▼          ▼         ▼
  Hero       Product    Social    WhatsApp
  Video      Benefits   Proof     CTA
    │           │          │         │
    └─── Emotional ──┴── Rational ──┴── Urgent ───┘
```

---

## 3. Visual Storytelling Architecture

### 3.1 The "Transformation Narrative"

Every page should tell a **before/after transformation story**:

```
┌────────────────────┐         ┌────────────────────┐
│      BEFORE        │   →→→   │       AFTER        │
├────────────────────┤         ├────────────────────┤
│ Bored students     │         │ Engaged learners   │
│ Static rehab       │         │ Gamified recovery  │
│ Empty play areas   │         │ Packed attractions │
│ Passive waiting    │         │ Interactive fun    │
└────────────────────┘         └────────────────────┘
```

### 3.2 Visual Hierarchy Principles

**F-Pattern for Information Pages:**
```
┌─────────────────────────────────────┐
│ ████████████████████████████████    │  ← Logo, Nav, Language Toggle
├─────────────────────────────────────┤
│ ██████████████████████████          │  ← Headline (scan left-to-right)
│ █████████████████                   │  ← Subheadline
│                                     │
│ ████████  ████████  ████████        │  ← Key benefits (3 columns)
│                                     │
│ █████                               │  ← CTA Button
│ ███                                 │  ← Secondary action
└─────────────────────────────────────┘
```

**Z-Pattern for Landing Pages:**
```
┌─────────────────────────────────────┐
│ Logo ─────────────────────── CTA    │  ← Start top-left, end top-right
│      ╲                     ╱        │
│        ╲                 ╱          │
│          ╲             ╱            │
│            ╲         ╱              │
│              ╲     ╱                │
│                ╲ ╱                  │
│ Headline ─────────────────── Image  │  ← Diagonal to bottom-left
│                                     │
│ ████████████ CTA BUTTON ████████████│  ← End at primary CTA
└─────────────────────────────────────┘
```

### 3.3 Color Psychology for IAM

| Color | Hex | Psychological Effect | Usage |
|-------|-----|---------------------|-------|
| **Amber/Gold** | `#feba04` | Energy, optimism, playfulness | Primary CTAs, highlights |
| **Deep Red** | `#d23234` | Urgency, passion, importance | Accents, alerts, secondary |
| **White** | `#ffffff` | Cleanliness, simplicity, trust | Backgrounds, breathing room |
| **Dark Grey** | `#1d1e22` | Sophistication, authority | Text, dark sections |
| **Soft Grey** | `#f8f9fa` | Calm, neutral, professional | Card backgrounds |

**Recommended Addition:**
| Color | Hex | Purpose |
|-------|-----|---------|
| **Success Green** | `#22c55e` | Testimonials, checkmarks, success states |
| **Trust Blue** | `#3b82f6` | Links, information icons, healthcare sections |

### 3.4 Imagery Guidelines

**DO Use:**
- ✅ Real children laughing and playing on IAM products
- ✅ Actual Dutch schools/hospitals with IAM installations
- ✅ Behind-the-scenes installation photos
- ✅ Team members in action (installing, training)
- ✅ Close-ups of the projection quality and interactivity
- ✅ Video testimonials from actual clients

**DON'T Use:**
- ❌ Generic stock photos of happy people
- ❌ Overly polished/staged photography
- ❌ Images without context (just the product, no people)
- ❌ Low-resolution or pixelated media
- ❌ Competitor product imagery

---

## 4. Trust Signal Strategy

### 4.1 Trust Signal Hierarchy

```
TIER 1: IMMEDIATE TRUST (Above the fold)
├── Professional logo and design
├── SSL certificate indicator
├── Clear contact information
├── Dutch language/local presence
└── Recognizable client logos (if available)

TIER 2: SOCIAL PROOF (First scroll)
├── Number of installations ("500+ systemen geïnstalleerd")
├── Years in business ("Sinds 2015")
├── Client testimonials with photos/names
└── Video case studies

TIER 3: AUTHORITY MARKERS (Throughout)
├── Industry certifications
├── Partnership badges (education boards, healthcare associations)
├── Media mentions/press coverage
├── Award recognitions
└── Technical certifications (CE marking, safety standards)

TIER 4: RISK REDUCTION (Near CTAs)
├── Warranty information
├── Support/maintenance promises
├── Money-back or satisfaction guarantees
├── Free consultation offer
└── "No obligation" language
```

### 4.2 Recommended Trust Elements to Add

#### Client Logo Wall
```html
<!-- Suggested placement: Homepage, just below hero -->
<section class="trust-logos">
  <p class="trust-label">Vertrouwd door toonaangevende organisaties</p>
  <div class="logo-carousel">
    <!-- Add actual client logos: schools, hospitals, parks -->
    <img src="media/clients/client-1.png" alt="[School Name]">
    <img src="media/clients/client-2.png" alt="[Hospital Name]">
    <!-- etc. -->
  </div>
</section>
```

#### Statistics Counter
```html
<!-- Animated counters that count up on scroll -->
<section class="stats-bar">
  <div class="stat">
    <span class="stat-number" data-target="500">0</span>+
    <span class="stat-label">Installaties</span>
  </div>
  <div class="stat">
    <span class="stat-number" data-target="10">0</span>
    <span class="stat-label">Jaar ervaring</span>
  </div>
  <div class="stat">
    <span class="stat-number" data-target="50">0</span>+
    <span class="stat-label">Spellen beschikbaar</span>
  </div>
  <div class="stat">
    <span class="stat-number" data-target="98">0</span>%
    <span class="stat-label">Klanttevredenheid</span>
  </div>
</section>
```

#### Testimonial Cards
```html
<!-- Real testimonials with full attribution -->
<div class="testimonial-card">
  <div class="testimonial-content">
    <p>"De interactieve vloer heeft onze gymles volledig getransformeerd. 
    Kinderen kunnen niet wachten om te bewegen!"</p>
  </div>
  <div class="testimonial-author">
    <img src="media/testimonials/maria.jpg" alt="Maria de Vries">
    <div class="author-info">
      <strong>Maria de Vries</strong>
      <span>Directeur, Basisschool De Regenboog</span>
      <span class="location">Amsterdam</span>
    </div>
  </div>
</div>
```

---

## 5. Page-by-Page UX Blueprint

---

### 5.1 Homepage (`index.html`)

#### Current State Analysis
The homepage serves as the primary entry point and must accomplish multiple jobs:
- Explain what IAM does (education)
- Showcase product range (awareness)
- Build credibility (trust)
- Route visitors to relevant sections (navigation)
- Generate leads (conversion)

#### Recommended Section Flow

```
┌─────────────────────────────────────────────────────────────────┐
│ SECTION 1: HERO (100vh)                                         │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Video Background: Children playing on interactive floor]      │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  HEADLINE:                                               │   │
│  │  "Breng Elke Vloer, Muur of Zandbak tot Leven"          │   │
│  │                                                          │   │
│  │  SUBHEADLINE:                                            │   │
│  │  "Interactieve projectiesystemen die leren, spelen      │   │
│  │   en revalideren transformeren"                          │   │
│  │                                                          │   │
│  │  [PRIMARY CTA: Bekijk Producten]  [SECONDARY: Video ▶]  │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ↓ Scroll indicator animation                                   │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SECTION 2: TRUST BAR (Sticky or Static)                         │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  "Vertrouwd door 500+ scholen, ziekenhuizen en speelparken"    │
│                                                                 │
│  [Logo] [Logo] [Logo] [Logo] [Logo] [Logo]                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SECTION 3: PROBLEM/SOLUTION BRIDGE                              │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Waarom Interactieve Projectie?"                     │
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐             │
│  │ 🎯 PROBLEEM │  │ 💡 OPLOSSING│  │ ✨ RESULTAAT│             │
│  │             │  │             │  │             │             │
│  │ Passieve    │  │ Bewegend    │  │ Actief      │             │
│  │ kinderen    │→ │ leren met   │→ │ leren,      │             │
│  │ achter      │  │ interactieve│  │ betere      │             │
│  │ schermen    │  │ projectie   │  │ resultaten  │             │
│  └─────────────┘  └─────────────┘  └─────────────┘             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SECTION 4: PRODUCT SHOWCASE (Interactive Cards)                 │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Onze Producten"                                     │
│  SUBHEAD: "Kies het systeem dat past bij uw ruimte"            │
│                                                                 │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │ [Video/GIF]  │ │ [Video/GIF]  │ │ [Video/GIF]  │            │
│  │              │ │              │ │              │            │
│  │ INTERACTIEVE │ │ INTERACTIEVE │ │ INTERACTIEVE │            │
│  │    VLOER     │ │    MUUR      │ │   ZANDBAK    │            │
│  │              │ │              │ │              │            │
│  │ Vanaf €X.XXX │ │ Vanaf €X.XXX │ │ Vanaf €X.XXX │            │
│  │              │ │              │ │              │            │
│  │ [Meer Info →]│ │ [Meer Info →]│ │ [Meer Info →]│            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
│                                                                 │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐            │
│  │ KLIMWAND     │ │ MOBIELE UNIT │ │ SOFTWARE     │            │
│  │ [...]        │ │ [...]        │ │ [...]        │            │
│  └──────────────┘ └──────────────┘ └──────────────┘            │
│                                                                 │
│  [CTA: Alle Producten Bekijken →]                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SECTION 5: USE CASE NAVIGATOR                                   │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Voor Elke Sector een Oplossing"                     │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  [Tab: Onderwijs] [Tab: Zorg] [Tab: Entertainment]      │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │                                                          │   │
│  │  ┌─────────────────┐  ┌─────────────────────────────┐   │   │
│  │  │                 │  │ ONDERWIJS                    │   │   │
│  │  │  [Image/Video   │  │                              │   │   │
│  │  │   of school     │  │ • Bewegend leren             │   │   │
│  │  │   installation] │  │ • STEM-integratie            │   │   │
│  │  │                 │  │ • Inclusief onderwijs        │   │   │
│  │  │                 │  │                              │   │   │
│  │  │                 │  │ "95% van de leerkrachten     │   │   │
│  │  │                 │  │  meldt hogere betrokkenheid" │   │   │
│  │  │                 │  │                              │   │   │
│  │  │                 │  │ [Bekijk Onderwijs Oplossingen]│   │   │
│  │  └─────────────────┘  └─────────────────────────────┘   │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SECTION 6: SOCIAL PROOF / TESTIMONIALS                          │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Wat Onze Klanten Zeggen"                           │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  [Video Testimonial Player]                              │   │
│  │                                                          │   │
│  │  ▶ "De kinderen zijn niet meer weg te slaan..."         │   │
│  │    — Jan Pietersen, Basisschool Het Kompas              │   │
│  │                                                          │   │
│  │  [Thumbnail] [Thumbnail] [Thumbnail] [Thumbnail]         │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌───────────┐ ┌───────────┐ ┌───────────┐                     │
│  │ ★★★★★     │ │ ★★★★★     │ │ ★★★★★     │                     │
│  │ "Geweldig │ │ "Beste    │ │ "Onze     │                     │
│  │  product" │ │  investering│ │  patiënten│                    │
│  │           │ │  ooit"    │ │  zijn blij"│                    │
│  │ — School  │ │ — Speelhal│ │ — Kliniek │                     │
│  └───────────┘ └───────────┘ └───────────┘                     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SECTION 7: HOW IT WORKS (Process)                               │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Van Eerste Contact tot Installatie"                 │
│                                                                 │
│  ┌─────┐      ┌─────┐      ┌─────┐      ┌─────┐               │
│  │  1  │ ──── │  2  │ ──── │  3  │ ──── │  4  │               │
│  └─────┘      └─────┘      └─────┘      └─────┘               │
│  Gratis       Offerte      Installatie  Training              │
│  Advies       op Maat      door Experts & Support             │
│                                                                 │
│  [Timeline/Progress visualization]                              │
│                                                                 │
│  "Gemiddelde levertijd: 4-6 weken"                             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SECTION 8: FAQ (Accordion)                                      │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Veelgestelde Vragen"                               │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ ▼ Hoe groot moet de ruimte zijn?                        │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │ ▶ Wat is de levensduur van de projector?                │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │ ▶ Bieden jullie onderhoud en support?                   │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │ ▶ Kunnen we de spellen aanpassen?                       │   │
│  ├─────────────────────────────────────────────────────────┤   │
│  │ ▶ Wat zijn de stroomvereisten?                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  [Link: Alle FAQ's bekijken →]                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SECTION 9: FINAL CTA (Conversion Zone)                          │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Background: Subtle gradient or image]                         │
│                                                                 │
│  HEADLINE: "Klaar om Uw Ruimte te Transformeren?"              │
│                                                                 │
│  SUBHEAD: "Plan een gratis adviesgesprek met onze experts"     │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │  [████ WHATSAPP CONTACT ████]  [📞 Bel Direct]          │   │
│  │                                                          │   │
│  │  of laat uw gegevens achter:                            │   │
│  │                                                          │   │
│  │  [Naam         ] [Email        ] [Telefoon    ]         │   │
│  │  [Organisatie  ] [Type: ▼      ]                        │   │
│  │                                                          │   │
│  │  [████████ GRATIS OFFERTE AANVRAGEN ████████]           │   │
│  │                                                          │   │
│  │  ✓ Vrijblijvend  ✓ Reactie binnen 24 uur               │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ FOOTER                                                          │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Logo]                                                         │
│                                                                 │
│  PRODUCTEN        SECTOREN       OVER ONS       CONTACT        │
│  • Vloer          • Onderwijs    • Ons Verhaal  • WhatsApp     │
│  • Muur           • Zorg         • Team         • Email        │
│  • Zandbak        • Entertainment• Vacatures    • Adres        │
│  • Klimwand       • Evenementen                                │
│  • Mobiel                                                       │
│                                                                 │
│  [Social Icons: LinkedIn, YouTube, Instagram]                   │
│                                                                 │
│  ─────────────────────────────────────────────────────────────  │
│  © 2026 Inter Active Move B.V. | KvK: XXXXXXXX                 │
│  Privacybeleid | Algemene Voorwaarden | Cookiebeleid           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### Hero Section Deep Dive

**Headline Formula:**
```
[Action Verb] + [Object] + [Transformation]
"Breng" + "Elke Vloer, Muur of Zandbak" + "tot Leven"
```

**Video Background Specifications:**
- Format: WebM with MP4 fallback
- Duration: 15-20 seconds, seamless loop
- Content: Montage of children/patients interacting with different products
- Audio: Muted by default, optional sound toggle
- Mobile: Replace with static hero image for performance

**CTA Hierarchy:**
1. **Primary:** "Bekijk Producten" (Amber button, high contrast)
2. **Secondary:** "Bekijk Video ▶" (Ghost button, plays product showcase)
3. **Tertiary:** Scroll indicator (subtle animation)

---

### 5.2 Product Pages

#### Product Page Template Structure

Each product page (`interactieve-vloer.html`, `interactieve-muur.html`, etc.) should follow this conversion-optimized structure:

```
┌─────────────────────────────────────────────────────────────────┐
│ PRODUCT HERO                                                    │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  ┌─────────────────────┐  ┌─────────────────────────────────┐  │
│  │                     │  │                                 │  │
│  │  [Product Image/    │  │  INTERACTIEVE VLOER            │  │
│  │   Video Gallery]    │  │                                 │  │
│  │                     │  │  ★★★★★ (47 reviews)            │  │
│  │  [Thumb][Thumb]     │  │                                 │  │
│  │  [Thumb][Thumb]     │  │  "Transform elke vloer in een  │  │
│  │                     │  │   interactief speelveld"       │  │
│  │  [360° View Button] │  │                                 │  │
│  │                     │  │  ✓ 50+ spellen inbegrepen      │  │
│  │                     │  │  ✓ Eenvoudige installatie      │  │
│  │                     │  │  ✓ 2 jaar garantie             │  │
│  │                     │  │                                 │  │
│  │                     │  │  Vanaf €X.XXX                  │  │
│  │                     │  │                                 │  │
│  │                     │  │  [OFFERTE AANVRAGEN]           │  │
│  │                     │  │  [Download Brochure]           │  │
│  │                     │  │                                 │  │
│  └─────────────────────┘  └─────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ BENEFIT STRIP                                                   │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  🎯 Multi-touch     🔧 Plug & Play    📱 App Control    🛡️ CE │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ DEMO VIDEO SECTION                                              │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Zie de Interactieve Vloer in Actie"                │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │           [Embedded Video Player - 16:9]                │   │
│  │                        ▶                                │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ FEATURE DEEP DIVE                                               │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  ┌───────────────────────┐  ┌───────────────────────────┐      │
│  │ [Feature Image]       │  │ FEATURE 1                 │      │
│  │                       │  │ Multi-Touch Technologie   │      │
│  │                       │  │                           │      │
│  │                       │  │ Tot 20 simultane touch-   │      │
│  │                       │  │ punten voor groepsspellen │      │
│  │                       │  │ en samenwerkingsactiviteiten│    │
│  └───────────────────────┘  └───────────────────────────┘      │
│                                                                 │
│  ┌───────────────────────┐  ┌───────────────────────────┐      │
│  │ FEATURE 2             │  │ [Feature Image]           │      │
│  │ Robuuste Constructie  │  │                           │      │
│  │                       │  │                           │      │
│  │ Industriële kwaliteit │  │                           │      │
│  │ bestand tegen intensief│ │                           │      │
│  │ gebruik in scholen    │  │                           │      │
│  └───────────────────────┘  └───────────────────────────┘      │
│                                                                 │
│  [Continue alternating layout for additional features]          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ GAME LIBRARY PREVIEW                                            │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "50+ Spellen Inbegrepen"                            │
│  SUBHEAD: "En nieuwe spellen worden regelmatig toegevoegd"     │
│                                                                 │
│  ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐ ┌────┐     │
│  │Game│ │Game│ │Game│ │Game│ │Game│ │Game│ │Game│ │+43 │     │
│  │ 1  │ │ 2  │ │ 3  │ │ 4  │ │ 5  │ │ 6  │ │ 7  │ │meer│     │
│  └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ └────┘ └────┘     │
│                                                                 │
│  Categories: [Educatief] [Sport] [Creatief] [Sensorisch]       │
│                                                                 │
│  [Bekijk Alle Spellen →]                                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ TECHNICAL SPECIFICATIONS (Collapsible)                          │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Technische Specificaties"                          │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Afmetingen           │ 3m x 2m (standaard)              │   │
│  │ Projectie            │ 4K Ultra Short Throw             │   │
│  │ Touch Punten         │ 20 simultaan                     │   │
│  │ Responstijd          │ <8ms                             │   │
│  │ Helderheid           │ 4000 ANSI Lumens                 │   │
│  │ Levensduur Lamp      │ 20.000 uur                       │   │
│  │ Stroomverbruik       │ 350W                             │   │
│  │ Geluidsniveau        │ <28dB                            │   │
│  │ Certificeringen      │ CE, RoHS, FCC                    │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  [Download Volledige Specificaties (PDF)]                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ USE CASE GALLERY                                                │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Waar Wordt de Interactieve Vloer Gebruikt?"        │
│                                                                 │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │ [School     │ │ [Therapy    │ │ [Play       │               │
│  │  Photo]     │ │  Photo]     │ │  Park Photo]│               │
│  │             │ │             │ │             │               │
│  │ Basisscholen│ │ Revalidatie │ │ Speelhallen │               │
│  │             │ │ Centra      │ │             │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PRODUCT-SPECIFIC TESTIMONIAL                                    │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │  "De interactieve vloer was de beste investering die   │   │
│  │   we hebben gedaan. De kinderen zijn actiever en de    │   │
│  │   leerkrachten hebben meer tools om les te geven."     │   │
│  │                                                          │   │
│  │  [Photo] Directeur Jan van der Berg                    │   │
│  │          Basisschool De Fontein, Utrecht               │   │
│  │                                                          │   │
│  │  [Bekijk Case Study →]                                 │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PRICING & PACKAGES                                              │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Kies Uw Pakket"                                    │
│                                                                 │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐   │
│  │    ESSENTIAL    │ │   PROFESSIONAL  │ │    ENTERPRISE   │   │
│  │                 │ │   ★ POPULAIR    │ │                 │   │
│  │   Vanaf        │ │   Vanaf         │ │   Vanaf         │   │
│  │   €X.XXX       │ │   €X.XXX        │ │   €X.XXX        │   │
│  │                 │ │                 │ │                 │   │
│  │ • Projector    │ │ • Projector     │ │ • Projector     │   │
│  │ • 25 spellen   │ │ • 50+ spellen   │ │ • Alle spellen  │   │
│  │ • 1 jaar       │ │ • 2 jaar        │ │ • 5 jaar        │   │
│  │   garantie     │ │   garantie      │ │   garantie      │   │
│  │                 │ │ • Installatie   │ │ • Installatie   │   │
│  │                 │ │ • Training      │ │ • Training      │   │
│  │                 │ │                 │ │ • Maatwerk      │   │
│  │                 │ │                 │ │ • Prioriteit    │   │
│  │                 │ │                 │ │   Support       │   │
│  │                 │ │                 │ │                 │   │
│  │ [Meer Info]    │ │ [KIES DIT]      │ │ [Meer Info]     │   │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘   │
│                                                                 │
│  "Niet zeker welk pakket? Wij adviseren graag!"               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ RELATED PRODUCTS                                                │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Combineer met Andere Producten"                    │
│                                                                 │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐   │
│  │ Interactieve    │ │ Interactieve    │ │ Software        │   │
│  │ Muur            │ │ Zandbak         │ │ Maatwerk        │   │
│  │ [Image]         │ │ [Image]         │ │ [Image]         │   │
│  │ [Bekijk →]      │ │ [Bekijk →]      │ │ [Bekijk →]      │   │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘   │
│                                                                 │
│  "Bouw een compleet interactief park! [Configurator →]"        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ STICKY CTA BAR (Mobile)                                         │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  Vanaf €X.XXX    [OFFERTE AANVRAGEN]    [📞]                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### Product-Specific Recommendations

##### Interactieve Vloer (`interactieve-vloer.html`)
- **Hero Video:** Children playing soccer game, then switching to educational math game
- **Key Differentiator:** "Grootste projectie-oppervlak" / "Largest projection surface"
- **Target Testimonial:** Elementary school principal
- **Objection Handling:** FAQ about floor durability and cleaning

##### Interactieve Muur (`interactieve-muur.html`)
- **Hero Video:** Waiting room transformation, kids hitting targets
- **Key Differentiator:** "Geen vloerruimte nodig" / "No floor space required"
- **Target Testimonial:** Healthcare facility manager
- **Objection Handling:** FAQ about wall mounting requirements

##### Interactieve Zandbak (`interactieve-zandbak.html`)
- **Hero Video:** AR terrain mapping, volcano simulation, water flow
- **Key Differentiator:** "Unieke AR ervaring" / "Unique AR experience"
- **Target Testimonial:** Museum or science center
- **Objection Handling:** FAQ about sand hygiene and maintenance

##### Interactieve Klimwand (`interactieve-klimwand.html`)
- **Hero Video:** Kids climbing with projected game elements
- **Key Differentiator:** "Fysieke uitdaging + digitale beleving" / "Physical + digital"
- **Target Testimonial:** Indoor playground owner
- **Objection Handling:** FAQ about safety certifications

##### Mobiele Vloer (`mobiele-vloer.html`)
- **Hero Video:** Event setup timelapse, birthday party in action
- **Key Differentiator:** "Plug & play in 15 minuten" / "Ready in 15 minutes"
- **Target Testimonial:** Event planner
- **Objection Handling:** FAQ about rental terms and transportation

##### Software & Maatwerk (`software-maatwerk.html`)
- **Hero Video:** Game Editor interface, custom branded game
- **Key Differentiator:** "Uw visie, onze technologie" / "Your vision, our tech"
- **Target Testimonial:** Marketing agency or large corporate
- **Objection Handling:** FAQ about development timeline and costs

---

### 5.3 Solution/Industry Pages

These pages speak directly to specific buyer personas and their unique needs.

#### Onderwijs (`onderwijs.html`) — Education

```
┌─────────────────────────────────────────────────────────────────┐
│ HERO: EDUCATION FOCUS                                           │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Background: Classroom with interactive floor, kids learning]  │
│                                                                 │
│  HEADLINE: "Bewegend Leren dat Beklijft"                       │
│                                                                 │
│  SUBHEAD: "Interactieve projectiesystemen die kinderen         │
│            activeren, motiveren en laten leren"                │
│                                                                 │
│  Key Stats Bar:                                                 │
│  [95% hogere betrokkenheid] [40% betere retentie] [100+ scholen]│
│                                                                 │
│  [GRATIS SCHOOLDEMO AANVRAGEN]                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PROBLEM/SOLUTION: EDUCATION                                     │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ "Herkent u dit?"                                          │ │
│  │                                                            │ │
│  │ 😔 Kinderen die niet stil kunnen zitten                   │ │
│  │ 😔 Moeite om alle leerlingen te betrekken                 │ │
│  │ 😔 Beperkte gymzaal-mogelijkheden                         │ │
│  │ 😔 Schermtijd verminderen maar digitaal blijven           │ │
│  │                                                            │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
│                           ↓                                     │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐ │
│  │ "Onze oplossing"                                          │ │
│  │                                                            │ │
│  │ ✅ Bewegend leren: rekenen, taal, motoriek combineren     │ │
│  │ ✅ Inclusief: alle kinderen kunnen meedoen                │ │
│  │ ✅ Flexibel: gym, speelzaal, of hal                       │ │
│  │ ✅ Actieve schermtijd die daadwerkelijk beweegt           │ │
│  │                                                            │ │
│  └───────────────────────────────────────────────────────────┘ │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ CURRICULUM ALIGNMENT                                            │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Past in Uw Lesplan"                                │
│                                                                 │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐  │
│  │ Rekenen │ │ Taal    │ │ Gym     │ │ Muziek  │ │ Sociale │  │
│  │ 🔢      │ │ 📚      │ │ 🏃      │ │ 🎵      │ │ Vaard.  │  │
│  │         │ │         │ │         │ │         │ │ 🤝      │  │
│  │ 15      │ │ 12      │ │ 20      │ │ 8       │ │ 10      │  │
│  │ spellen │ │ spellen │ │ spellen │ │ spellen │ │ spellen │  │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘ └─────────┘  │
│                                                                 │
│  "Alle spellen zijn afgestemd op kerndoelen basisonderwijs"   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ TEACHER TESTIMONIALS                                            │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Video: Teacher explaining how they use the floor]             │
│                                                                 │
│  "Sinds we de interactieve vloer hebben, is de gymles het      │
│   favoriete moment van de week. Kinderen leren zonder het      │
│   door te hebben!"                                              │
│                                                                 │
│  — Juf Lisa, Groep 4, Basisschool De Regenboog                 │
│                                                                 │
│  [Case Study: Basisschool De Regenboog →]                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SCHOOL PACKAGES                                                 │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Speciale Onderwijspakketten"                       │
│                                                                 │
│  ┌─────────────────────┐  ┌─────────────────────┐              │
│  │   BASISSCHOOL       │  │   SBO / SPECIAAL    │              │
│  │                     │  │                     │              │
│  │ • Interactieve vloer│  │ • Interactieve vloer│              │
│  │ • 50 educatieve     │  │ • 50 educatieve     │              │
│  │   spellen           │  │   spellen           │              │
│  │ • Leerkracht-       │  │ • Sensorische       │              │
│  │   training          │  │   spellen module    │              │
│  │ • Lesplan-integratie│  │ • Extra training    │              │
│  │                     │  │   inclusief gebruik │              │
│  │ Vanaf €X.XXX        │  │ Vanaf €X.XXX        │              │
│  │                     │  │                     │              │
│  │ [OFFERTE]           │  │ [OFFERTE]           │              │
│  └─────────────────────┘  └─────────────────────┘              │
│                                                                 │
│  "Subsidie-advies beschikbaar — wij helpen met aanvragen"      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SCHOOL SUCCESS METRICS                                          │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Meetbare Resultaten"                               │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │   [Bar Chart Animation]                                 │   │
│  │                                                          │   │
│  │   Betrokkenheid:     ████████████████████░░ +95%        │   │
│  │   Concentratie:      ████████████████░░░░░░ +67%        │   │
│  │   Samenwerking:      █████████████████████░ +89%        │   │
│  │   Fysieke Activiteit:████████████████████░░ +120%       │   │
│  │                                                          │   │
│  │   Bron: Intern onderzoek bij 50 basisscholen, 2025      │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ EDUCATOR FAQ                                                    │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  ▼ Hoe past dit in ons bestaande lesplan?                      │
│  ▶ Welke training krijgen onze leerkrachten?                   │
│  ▶ Hoe zit het met onderhoud en updates?                       │
│  ▶ Kunnen wij eigen spellen maken?                             │
│  ▶ Zijn er subsidies beschikbaar?                              │
│  ▶ Wat is de minimale ruimte vereiste?                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ SCHOOL CTA                                                      │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Plan een Gratis Schooldemonstratie"                │
│                                                                 │
│  "Wij komen naar uw school voor een live demonstratie.         │
│   Laat leerlingen en leerkrachten zelf ervaren wat              │
│   interactief leren kan betekenen."                             │
│                                                                 │
│  [DEMO AANVRAGEN]  [BROCHURE DOWNLOADEN]                       │
│                                                                 │
│  ✓ Vrijblijvend  ✓ Op uw locatie  ✓ Inclusief presentatie     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### Zorg & Revalidatie (`zorg-revalidatie.html`) — Healthcare

```
┌─────────────────────────────────────────────────────────────────┐
│ HERO: HEALTHCARE FOCUS                                          │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Background: Rehab patient interacting with wall projection]   │
│                                                                 │
│  HEADLINE: "Revalidatie die Patiënten Motiveert"               │
│                                                                 │
│  SUBHEAD: "Gamified therapie voor betere resultaten            │
│            en hogere therapietrouw"                             │
│                                                                 │
│  Trust Signals:                                                 │
│  [CE Medisch] [50+ Zorginstellingen] [Evidence-Based]          │
│                                                                 │
│  [INFORMATIE VOOR ZORGPROFESSIONALS]                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ CLINICAL USE CASES                                              │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Klinische Toepassingen"                            │
│                                                                 │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐   │
│  │ MOTORISCHE      │ │ COGNITIEVE      │ │ SENSORISCHE     │   │
│  │ REVALIDATIE     │ │ THERAPIE        │ │ INTEGRATIE      │   │
│  │                 │ │                 │ │                 │   │
│  │ • CVA herstel   │ │ • Dementie      │ │ • Autisme       │   │
│  │ • Orthopedie    │ │ • Hersenletsel  │ │ • Zintuiglijke  │   │
│  │ • Parkinson     │ │ • Concentratie  │ │   beperking     │   │
│  │ • Pediatrisch   │ │ • Geheugen      │ │ • Prikkelarm    │   │
│  │                 │ │                 │ │                 │   │
│  │ [Meer Info]     │ │ [Meer Info]     │ │ [Meer Info]     │   │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ EVIDENCE & RESEARCH                                             │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Wetenschappelijk Onderbouwd"                       │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │  📊 "Gamified revalidatie verhoogt therapietrouw        │   │
│  │      met 67% vergeleken met traditionele methoden"      │   │
│  │                                                          │   │
│  │      — Journal of Rehabilitation Research, 2024         │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  [Download Whitepaper: Gamified Rehabilitation Evidence]       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ HYGIENE & SAFETY                                                │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Ontworpen voor Zorginstellingen"                   │
│                                                                 │
│  ✓ Contactloos (projectie, geen touchscreens)                  │
│  ✓ CE-gecertificeerd voor medisch gebruik                      │
│  ✓ Eenvoudig te reinigen oppervlakken                          │
│  ✓ Geen kabels op de grond (plafondmontage)                    │
│  ✓ Instelbare intensiteit voor gevoelige patiënten             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ THERAPIST TESTIMONIAL                                           │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Video: Fysio therapist explaining patient outcomes]           │
│                                                                 │
│  "Patiënten die eerst weerstand hadden tegen oefeningen,       │
│   vragen nu zelf om meer sessies. De interactieve muur         │
│   heeft onze therapie getransformeerd."                         │
│                                                                 │
│  — Drs. Anna Jansen, Fysiotherapeut                            │
│    Revalidatiecentrum De Hoogstraat, Utrecht                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ HEALTHCARE CTA                                                  │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Informatie voor Zorgprofessionals"                 │
│                                                                 │
│  "Ontvang onze uitgebreide informatiepakket inclusief          │
│   klinische toepassingen, onderzoeksreferenties en prijzen."   │
│                                                                 │
│  [INFORMATIEPAKKET AANVRAGEN]                                  │
│                                                                 │
│  Of plan direct een gesprek met onze zorgspecialist:           │
│  [DEMO INPLANNEN]                                               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

#### Parken & Speelhallen (`parken-speelhallen.html`) — Entertainment

```
┌─────────────────────────────────────────────────────────────────┐
│ HERO: ENTERTAINMENT FOCUS                                       │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Background: Packed indoor playground with multiple IAM units] │
│                                                                 │
│  HEADLINE: "Attracties die Bezoekers Terugbrengen"             │
│                                                                 │
│  SUBHEAD: "Interactieve systemen die uw speelparadijs          │
│            onderscheiden van de rest"                           │
│                                                                 │
│  ROI Focus:                                                     │
│  [+35% herhaalbezoekers] [2.5 jaar ROI] [Laag onderhoud]       │
│                                                                 │
│  [BOUW UW EIGEN PARK →]  [ROI CALCULATOR]                      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ ATTRACTION PORTFOLIO                                            │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Populaire Attractie-Combinaties"                   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ STARTER PARK           │ PREMIUM PARK    │ MEGA PARK    │   │
│  │                        │ ★ BESTSELLER    │              │   │
│  │ 1x Interactieve Vloer  │ 1x Vloer XL     │ 2x Vloer XL  │   │
│  │                        │ 1x Muur         │ 2x Muur      │   │
│  │                        │ 1x Klimwand     │ 1x Klimwand  │   │
│  │                        │                 │ 1x Zandbak   │   │
│  │                        │                 │              │   │
│  │ Ideaal voor:           │ Ideaal voor:    │ Ideaal voor: │   │
│  │ Kleine speelzaal       │ Medium indoor   │ Grote parken │   │
│  │                        │ playground      │              │   │
│  │                        │                 │              │   │
│  │ Vanaf €XX.XXX          │ Vanaf €XX.XXX   │ Op aanvraag  │   │
│  │                        │                 │              │   │
│  │ [OFFERTE]              │ [OFFERTE]       │ [CONTACT]    │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ ROI CALCULATOR (Interactive)                                    │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Bereken Uw Return on Investment"                   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │  Gemiddeld aantal bezoekers per maand: [____] 👈        │   │
│  │                                                          │   │
│  │  Entreeprijsverhoging door IAM:        €[2,50]          │   │
│  │                                                          │   │
│  │  Geschatte toename herhaalbezoekers:   [20%]            │   │
│  │                                                          │   │
│  │  ─────────────────────────────────────────────────────  │   │
│  │                                                          │   │
│  │  📊 GESCHATTE TERUGVERDIENTIJD: 18 maanden              │   │
│  │  💰 EXTRA JAAROMZET: €XX.XXX                            │   │
│  │                                                          │   │
│  │  [VOLLEDIGE ROI ANALYSE ONTVANGEN]                      │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PARK OWNER TESTIMONIAL                                          │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Video: Park owner showing installation and busy playground]   │
│                                                                 │
│  "De investering was binnen 2 jaar terugverdiend.              │
│   Ouders vertellen vrienden over 'die gave vloer' en           │
│   boeken verjaardagsfeestjes juist voor deze attractie."       │
│                                                                 │
│  — Peter de Groot, Eigenaar                                    │
│    Monkey Town Amsterdam                                        │
│                                                                 │
│  [Bekijk Case Study →]                                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ CONTENT UPDATES                                                 │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Altijd Nieuwe Content"                             │
│                                                                 │
│  "Bezoekers vervelen zich nooit dankzij regelmatige updates"   │
│                                                                 │
│  🎮 Nieuwe spellen: Maandelijks                                │
│  🎄 Seizoensthema's: Kerst, Pasen, Zomer, Halloween            │
│  🎂 Feestmodi: Verjaardagen, schoolreisjes                     │
│  🏆 Competitie-opties: Leaderboards, toernooien                │
│                                                                 │
│  [Bekijk Spelbibliotheek →]                                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ ENTERTAINMENT CTA                                               │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Maak Uw Park Onvergetelijk"                        │
│                                                                 │
│  [BOUW UW PARK CONFIGURATOR]  [BEL ONZE SALES]                 │
│                                                                 │
│  "Wij komen graag langs voor een vrijblijvend adviesgesprek"   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5.4 About Us Page (`over-ons.html`)

```
┌─────────────────────────────────────────────────────────────────┐
│ HERO: COMPANY STORY                                             │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Background: Team photo or office/warehouse]                   │
│                                                                 │
│  HEADLINE: "Wij Zijn Inter Active Move"                        │
│                                                                 │
│  SUBHEAD: "Een Nederlands bedrijf met een missie:              │
│            beweging en plezier verbinden met technologie"      │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ ORIGIN STORY (Narrative)                                        │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Ons Verhaal"                                       │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │  [Image: Founder]                                       │   │
│  │                                                          │   │
│  │  "In 2015 zag ik hoe kinderen urenlang naar schermen    │   │
│  │   staarden. Ik dacht: wat als we die schermtijd         │   │
│  │   konden omzetten in bewegingstijd?"                    │   │
│  │                                                          │   │
│  │  Wat begon als een experiment in een Amsterdamse        │   │
│  │  gymzaal, is uitgegroeid tot een bedrijf dat            │   │
│  │  inmiddels 500+ installaties door heel Nederland        │   │
│  │  heeft gedaan.                                          │   │
│  │                                                          │   │
│  │  — [Founder Name], Oprichter                            │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  [Timeline: 2015 → 2018 → 2021 → 2024 → Nu]                    │
│  Oprichting → Eerste 100 → Zorg markt → 500+ → Internationaal  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ MISSION & VALUES                                                │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Onze Missie"                                       │
│                                                                 │
│  "Wij geloven dat technologie mensen moet verbinden,           │
│   niet isoleren. Onze systemen brengen kinderen, patiënten    │
│   en bezoekers samen in beweging en plezier."                  │
│                                                                 │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐               │
│  │ 💡          │ │ 🤝          │ │ 🌱          │               │
│  │ INNOVATIE   │ │ PARTNERSCHAP│ │ IMPACT      │               │
│  │             │ │             │ │             │               │
│  │ Continu     │ │ Langdurige  │ │ Positieve   │               │
│  │ ontwikkelen │ │ relaties    │ │ bijdrage    │               │
│  │ van nieuwe  │ │ met onze    │ │ aan         │               │
│  │ oplossingen │ │ klanten     │ │ samenleving │               │
│  └─────────────┘ └─────────────┘ └─────────────┘               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ TEAM SECTION                                                    │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Het Team Achter IAM"                               │
│                                                                 │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐              │
│  │ [Photo] │ │ [Photo] │ │ [Photo] │ │ [Photo] │              │
│  │         │ │         │ │         │ │         │              │
│  │ Naam    │ │ Naam    │ │ Naam    │ │ Naam    │              │
│  │ CEO     │ │ Sales   │ │ Tech    │ │ Support │              │
│  │         │ │         │ │ Lead    │ │ Manager │              │
│  │ [LI]    │ │ [LI]    │ │ [LI]    │ │ [LI]    │              │
│  └─────────┘ └─────────┘ └─────────┘ └─────────┘              │
│                                                                 │
│  "Ons team combineert passie voor technologie met kennis       │
│   van onderwijs, zorg en entertainment."                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ DUTCH QUALITY SECTION                                           │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "100% Nederlands"                                   │
│                                                                 │
│  🇳🇱 Hoofdkantoor in [Stad]                                    │
│  🇳🇱 Nederlandse klantenservice                                │
│  🇳🇱 Lokale installatieteams                                   │
│  🇳🇱 KvK-geregistreerd                                         │
│                                                                 │
│  [Map showing office location]                                  │
│                                                                 │
│  Inter Active Move B.V.                                         │
│  [Adres]                                                        │
│  [Postcode, Stad]                                               │
│  KvK: XXXXXXXX                                                  │
│  BTW: NL XXXXXXXXX                                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ CERTIFICATIONS & PARTNERSHIPS                                   │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Certificeringen & Partners"                        │
│                                                                 │
│  [CE Logo] [ISO Logo] [Partner Logo] [Partner Logo]            │
│                                                                 │
│  • CE-gecertificeerd voor EU-markt                             │
│  • ISO 9001 kwaliteitsmanagement                               │
│  • Partner van [Onderwijsorganisatie]                          │
│  • Lid van [Branchevereniging]                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ CAREERS TEASER                                                  │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Werken bij IAM?"                                   │
│                                                                 │
│  "Wij zoeken mensen die net zo enthousiast zijn over           │
│   interactieve technologie als wij."                           │
│                                                                 │
│  [BEKIJK VACATURES →]                                          │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5.5 Pricing Page (`prijzen.html`)

```
┌─────────────────────────────────────────────────────────────────┐
│ PRICING HERO                                                    │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Transparante Prijzen, Geen Verrassingen"           │
│                                                                 │
│  SUBHEAD: "Kies het pakket dat past bij uw situatie"           │
│                                                                 │
│  [Toggle: Koop | Huur | Lease]                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PRICING MATRIX                                                  │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  ┌────────────────────────────────────────────────────────────┐│
│  │                 ESSENTIAL   PROFESSIONAL   ENTERPRISE      ││
│  │                             ★ POPULAIR                     ││
│  ├────────────────────────────────────────────────────────────┤│
│  │ INTERACTIEVE                                               ││
│  │ VLOER (3x2m)    €X.XXX      €X.XXX        Op aanvraag     ││
│  ├────────────────────────────────────────────────────────────┤│
│  │ INTERACTIEVE                                               ││
│  │ MUUR            €X.XXX      €X.XXX        Op aanvraag     ││
│  ├────────────────────────────────────────────────────────────┤│
│  │ INTERACTIEVE                                               ││
│  │ ZANDBAK         €X.XXX      €X.XXX        Op aanvraag     ││
│  ├────────────────────────────────────────────────────────────┤│
│  │ INTERACTIEVE                                               ││
│  │ KLIMWAND        €X.XXX      €X.XXX        Op aanvraag     ││
│  ├────────────────────────────────────────────────────────────┤│
│  │ MOBIELE                                                    ││
│  │ VERHUUR         €XXX/dag    €XXX/dag      Weekprijs       ││
│  └────────────────────────────────────────────────────────────┘│
│                                                                 │
│  Alle prijzen excl. BTW                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ WHAT'S INCLUDED                                                 │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Wat Zit er in Elk Pakket?"                         │
│                                                                 │
│  ┌───────────────┬───────────────┬───────────────┐             │
│  │   ESSENTIAL   │  PROFESSIONAL │   ENTERPRISE  │             │
│  ├───────────────┼───────────────┼───────────────┤             │
│  │ ✓ Hardware    │ ✓ Hardware    │ ✓ Hardware    │             │
│  │ ✓ 25 spellen  │ ✓ 50+ spellen │ ✓ Alle spellen│             │
│  │ ✓ 1 jr garantie│✓ 2 jr garantie│✓ 5 jr garantie│            │
│  │ ✗ Installatie │ ✓ Installatie │ ✓ Installatie │             │
│  │ ✗ Training    │ ✓ Training    │ ✓ Training    │             │
│  │ ✗ Support     │ ✓ 1 jr support│ ✓ 5 jr support│             │
│  │ ✗ Maatwerk    │ ✗ Maatwerk    │ ✓ Maatwerk    │             │
│  │ ✗ Prioriteit  │ ✗ Prioriteit  │ ✓ Prioriteit  │             │
│  ├───────────────┼───────────────┼───────────────┤             │
│  │ [OFFERTE]     │ [OFFERTE]     │ [CONTACT]     │             │
│  └───────────────┴───────────────┴───────────────┘             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ FINANCING OPTIONS                                               │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Flexibele Financieringsopties"                     │
│                                                                 │
│  ┌─────────────────────┐  ┌─────────────────────┐              │
│  │ 💳 LEASE            │  │ 📅 BETALING IN      │              │
│  │                     │  │    TERMIJNEN        │              │
│  │ Vanaf €XXX/maand    │  │                     │              │
│  │                     │  │ 3, 6, of 12 termijnen│             │
│  │ • Geen grote        │  │                     │              │
│  │   investering       │  │ • Spreidt de kosten │              │
│  │ • Inclusief support │  │ • Geen rente bij    │              │
│  │ • Fiscaal voordelig │  │   3 termijnen       │              │
│  │                     │  │                     │              │
│  │ [Meer over Lease]   │  │ [Meer over Termijnen]│             │
│  └─────────────────────┘  └─────────────────────┘              │
│                                                                 │
│  "Ook subsidie-advies beschikbaar voor onderwijsinstellingen"  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PRICE GUARANTEE                                                 │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ 🛡️ ONZE PRIJSGARANTIE                                   │   │
│  │                                                          │   │
│  │ "De prijs in uw offerte is de prijs die u betaalt.      │   │
│  │  Geen verborgen kosten, geen verrassingen achteraf."    │   │
│  │                                                          │   │
│  │ ✓ Installatie inclusief (bij Professional+)            │   │
│  │ ✓ Verzendkosten inclusief (NL)                         │   │
│  │ ✓ Training inclusief (bij Professional+)               │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PRICING FAQ                                                     │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  ▼ Zijn er bijkomende kosten na aankoop?                       │
│  ▶ Wat als ik later wil upgraden?                              │
│  ▶ Bieden jullie kortingen voor meerdere systemen?             │
│  ▶ Hoe werkt de verhuur precies?                               │
│  ▶ Zijn de prijzen inclusief BTW?                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PRICING CTA                                                     │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Ontvang een Offerte op Maat"                       │
│                                                                 │
│  "Elke situatie is anders. Vertel ons over uw wensen           │
│   en wij maken een passend voorstel."                          │
│                                                                 │
│  [OFFERTE AANVRAGEN]  [BEL VOOR ADVIES]                        │
│                                                                 │
│  ✓ Reactie binnen 24 uur  ✓ Vrijblijvend  ✓ Persoonlijk       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5.6 Build a Park Configurator (`bouw-een-park.html`)

This is a **key differentiator** — an interactive tool that creates engagement and qualified leads.

```
┌─────────────────────────────────────────────────────────────────┐
│ CONFIGURATOR HERO                                               │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Ontwerp Uw Eigen Interactieve Speelparadijs"       │
│                                                                 │
│  SUBHEAD: "Selecteer producten, bekijk de layout,              │
│            en ontvang direct een indicatieprijs"               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ STEP INDICATOR                                                  │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [1. Ruimte] ─── [2. Producten] ─── [3. Layout] ─── [4. Offerte]│
│      ●              ○                  ○                ○       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ STEP 1: SPACE DEFINITION                                        │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Vertel ons over uw ruimte"                         │
│                                                                 │
│  Wat voor locatie heeft u?                                      │
│  [□ Indoor Speeltuin] [□ School] [□ Zorginstelling]            │
│  [□ Evenementenlocatie] [□ Anders]                             │
│                                                                 │
│  Afmetingen (bij benadering):                                   │
│  Lengte: [____] m    Breedte: [____] m                         │
│                                                                 │
│  Plafond hoogte: [____] m                                       │
│                                                                 │
│  [VOLGENDE: KIES PRODUCTEN →]                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ STEP 2: PRODUCT SELECTION                                       │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Selecteer uw producten"                            │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │  ┌─────────────┐                                        │   │
│  │  │ [Vloer Img] │  INTERACTIEVE VLOER                    │   │
│  │  │             │  "Het populairste product"              │   │
│  │  │             │  Vanaf €X.XXX                          │   │
│  │  │             │                                         │   │
│  │  │             │  Aantal: [-] 0 [+]                      │   │
│  │  └─────────────┘                                        │   │
│  │                                                          │   │
│  │  [Similar cards for: Muur, Zandbak, Klimwand]           │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ UW SELECTIE:                                             │   │
│  │ 2x Interactieve Vloer    €XX.XXX                        │   │
│  │ 1x Interactieve Muur     €XX.XXX                        │   │
│  │ ───────────────────────────────                         │   │
│  │ Indicatieprijs:          €XX.XXX                        │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  [← TERUG]  [VOLGENDE: BEKIJK LAYOUT →]                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ STEP 3: INTERACTIVE LAYOUT                                      │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Plaats de producten in uw ruimte"                  │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │            DRAG & DROP CANVAS                           │   │
│  │  ┌──────────────────────────────────────────────────┐   │   │
│  │  │                                                   │   │   │
│  │  │     ┌───────┐              ┌───────┐             │   │   │
│  │  │     │ VLOER │              │ VLOER │             │   │   │
│  │  │     │   1   │              │   2   │             │   │   │
│  │  │     └───────┘              └───────┘             │   │   │
│  │  │                                                   │   │   │
│  │  │                    ┌───────┐                     │   │   │
│  │  │                    │ MUUR  │                     │   │   │
│  │  │                    └───────┘                     │   │   │
│  │  │                                                   │   │   │
│  │  │  10m x 8m                                        │   │   │
│  │  └──────────────────────────────────────────────────┘   │   │
│  │                                                          │   │
│  │  [Zoom +/-] [Reset] [Screenshot]                        │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  ⚠️ Let op: minimale afstand tussen vloerprojecties is 2m     │
│                                                                 │
│  [← TERUG]  [VOLGENDE: OFFERTE AANVRAGEN →]                    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ STEP 4: QUOTE REQUEST                                           │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Bijna klaar! Ontvang uw persoonlijke offerte"      │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │  UW CONFIGURATIE SAMENVATTING:                          │   │
│  │                                                          │   │
│  │  📍 Ruimte: 10m x 8m Indoor Speeltuin                   │   │
│  │  📦 2x Interactieve Vloer (3x2m)                        │   │
│  │  📦 1x Interactieve Muur                                │   │
│  │                                                          │   │
│  │  💰 Indicatieprijs: €XX.XXX - €XX.XXX                   │   │
│  │     (Exacte prijs in offerte)                           │   │
│  │                                                          │   │
│  │  [Layout Screenshot/PDF]                                │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Uw gegevens voor de offerte:                                  │
│                                                                 │
│  [Naam*              ] [Bedrijf/Organisatie* ]                 │
│  [Email*             ] [Telefoon             ]                 │
│  [Opmerkingen/Vragen                                    ]      │
│                                                                 │
│  □ Ja, ik wil nieuws en tips ontvangen                         │
│                                                                 │
│  [████ OFFERTE AANVRAGEN ████]                                 │
│                                                                 │
│  ✓ Binnen 2 werkdagen reactie                                  │
│  ✓ Layout inbegrepen                                           │
│  ✓ Vrijblijvend                                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

### 5.7 3D Games Showcase (`3d-spellen.html`)

```
┌─────────────────────────────────────────────────────────────────┐
│ GAMES LIBRARY HERO                                              │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [Background: Montage of game screenshots]                      │
│                                                                 │
│  HEADLINE: "50+ Interactieve Spellen"                          │
│                                                                 │
│  SUBHEAD: "Educatief, sportief en creatief —                   │
│            voor elke leeftijd en toepassing"                   │
│                                                                 │
│  [Filter: Alle | Educatief | Sport | Creatief | Sensorisch]    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ GAMES GRID                                                      │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌───────────┐ │
│  │ [Game Thumb]│ │ [Game Thumb]│ │ [Game Thumb]│ │ [Game    ]│ │
│  │             │ │             │ │             │ │           │ │
│  │ Voetbal     │ │ Rekenpuzzel │ │ Verf Canvas │ │ Memory    │ │
│  │             │ │             │ │             │ │           │ │
│  │ 🏃 Sport    │ │ 📚 Educatief│ │ 🎨 Creatief │ │ 🧠 Cognitief│ │
│  │ 👶 4-8 jaar │ │ 👧 6-10 jaar│ │ 👶 Alle     │ │ 👴 Alle   │ │
│  │             │ │             │ │             │ │           │ │
│  │ [▶ Demo]    │ │ [▶ Demo]    │ │ [▶ Demo]    │ │ [▶ Demo]  │ │
│  └─────────────┘ └─────────────┘ └─────────────┘ └───────────┘ │
│                                                                 │
│  [Continue grid for all 50+ games...]                          │
│                                                                 │
│  [LAAD MEER]                                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ GAME MODAL (On click)                                           │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ [X Close]                                                │   │
│  │                                                          │   │
│  │  ┌───────────────────────────────────────────────────┐  │   │
│  │  │                                                    │  │   │
│  │  │            [VIDEO PLAYER]                         │  │   │
│  │  │                   ▶                               │  │   │
│  │  │                                                    │  │   │
│  │  └───────────────────────────────────────────────────┘  │   │
│  │                                                          │   │
│  │  VOETBAL                                                │   │
│  │                                                          │   │
│  │  Een virtueel voetbalveld waar kinderen samen of       │   │
│  │  tegen elkaar kunnen scoren. Ideaal voor gym en         │   │
│  │  buitenschoolse opvang.                                 │   │
│  │                                                          │   │
│  │  🏷️ Categorieën: Sport, Samenwerking                   │   │
│  │  👶 Leeftijd: 4-12 jaar                                 │   │
│  │  👥 Spelers: 2-10                                       │   │
│  │  ⏱️ Duur: 3-5 minuten per ronde                        │   │
│  │  📱 Beschikbaar op: Vloer, Muur                         │   │
│  │                                                          │   │
│  │  Educatieve doelen:                                     │   │
│  │  ✓ Motorische coördinatie                              │   │
│  │  ✓ Teamwork                                            │   │
│  │  ✓ Reactiesnelheid                                     │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ CUSTOM GAMES TEASER                                             │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Uw Eigen Spel Nodig?"                              │
│                                                                 │
│  "Wij ontwikkelen ook maatwerk spellen op basis van            │
│   uw specifieke wensen, curriculum of merkidentiteit."         │
│                                                                 │
│  [MEER OVER MAATWERK →]                                        │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ UPDATE CYCLE                                                    │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  HEADLINE: "Altijd Nieuwe Spellen"                             │
│                                                                 │
│  🗓️ Nieuwe spellen: Maandelijks                                │
│  🎄 Seizoensthema's: Kerst, Pasen, Zomer, Halloween            │
│  📲 Automatische updates: Geen actie nodig                     │
│  💡 Suggesties welkom: Deel uw ideeën met ons                  │
│                                                                 │
│  Recente toevoegingen:                                          │
│  [Game] [Game] [Game] — Toegevoegd januari 2026                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 6. Navigation & Information Architecture

### 6.1 Recommended Navigation Structure

```
┌─────────────────────────────────────────────────────────────────┐
│ PRIMARY NAVIGATION (Desktop)                                    │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [LOGO]    Producten ▼   Oplossingen ▼   Over Ons   Prijzen   │
│                                                                 │
│            ┌─────────────────────────────────────────────────┐ │
│            │ PRODUCTEN                                       │ │
│            │                                                  │ │
│            │ ┌─────────────┐ ┌─────────────┐                │ │
│            │ │ [Icon]      │ │ [Icon]      │                │ │
│            │ │ Interactieve│ │ Interactieve│                │ │
│            │ │ Vloer       │ │ Muur        │                │ │
│            │ └─────────────┘ └─────────────┘                │ │
│            │ ┌─────────────┐ ┌─────────────┐                │ │
│            │ │ Interactieve│ │ Interactieve│                │ │
│            │ │ Zandbak     │ │ Klimwand    │                │ │
│            │ └─────────────┘ └─────────────┘                │ │
│            │ ┌─────────────┐ ┌─────────────┐                │ │
│            │ │ Mobiele     │ │ Software &  │                │ │
│            │ │ Vloer       │ │ Maatwerk    │                │ │
│            │ └─────────────┘ └─────────────┘                │ │
│            │                                                  │ │
│            │ ───────────────────────────────                 │ │
│            │ [🎮 Bekijk Alle Spellen]                        │ │
│            │ [🏗️ Bouw Uw Eigen Park]                        │ │
│            └─────────────────────────────────────────────────┘ │
│                                                                 │
│            ┌─────────────────────────────────────────────────┐ │
│            │ OPLOSSINGEN                                     │ │
│            │                                                  │ │
│            │ [📚] Onderwijs                                  │ │
│            │ [🏥] Zorg & Revalidatie                         │ │
│            │ [🎢] Parken & Speelhallen                       │ │
│            │ [🎉] Evenementen & Verhuur                      │ │
│            └─────────────────────────────────────────────────┘ │
│                                                                 │
│                                        [NL|EN]  [CONTACT ▶]    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Mobile Navigation

```
┌─────────────────────────────────────────────────────────────────┐
│ MOBILE NAVIGATION                                               │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  [LOGO]                                    [☰ Menu]            │
│                                                                 │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │                                                          │   │
│  │  ▼ Producten                                            │   │
│  │      • Interactieve Vloer                               │   │
│  │      • Interactieve Muur                                │   │
│  │      • Interactieve Zandbak                             │   │
│  │      • Interactieve Klimwand                            │   │
│  │      • Mobiele Vloer                                    │   │
│  │      • Software & Maatwerk                              │   │
│  │      ────────────────────                               │   │
│  │      • Alle Spellen                                     │   │
│  │      • Bouw Uw Park                                     │   │
│  │                                                          │   │
│  │  ▶ Oplossingen                                          │   │
│  │                                                          │   │
│  │  Over Ons                                               │   │
│  │                                                          │   │
│  │  Prijzen                                                │   │
│  │                                                          │   │
│  │  ────────────────────────────────                       │   │
│  │                                                          │   │
│  │  [🇳🇱 NL] [🇬🇧 EN]                                       │   │
│  │                                                          │   │
│  │  [████████ CONTACT ████████]                            │   │
│  │                                                          │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.3 Breadcrumb Implementation

```html
<!-- Example for product page -->
<nav class="breadcrumb" aria-label="Breadcrumb">
  <ol>
    <li><a href="/">Home</a></li>
    <li><a href="/producten">Producten</a></li>
    <li aria-current="page">Interactieve Vloer</li>
  </ol>
</nav>
```

---

## 7. CTA Strategy & Placement

### 7.1 CTA Hierarchy

| Level | CTA Type | Visual Treatment | Usage |
|-------|----------|------------------|-------|
| **Primary** | "Offerte Aanvragen" / "Contact" | Solid Amber (#feba04), large | Main conversion action |
| **Secondary** | "Meer Info" / "Bekijk Demo" | Ghost/outline, medium | Information seeking |
| **Tertiary** | "Download Brochure" / "Lees Meer" | Text link with arrow | Content engagement |

### 7.2 CTA Button Specifications

```css
/* Primary CTA */
.cta-primary {
  background: linear-gradient(135deg, #feba04 0%, #f5a800 100%);
  color: #1d1e22;
  font-weight: 600;
  padding: 16px 32px;
  border-radius: 999px; /* Pill shape */
  font-size: 1rem;
  text-transform: none;
  box-shadow: 0 4px 14px rgba(254, 186, 4, 0.4);
  transition: transform 0.2s, box-shadow 0.2s;
}

.cta-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(254, 186, 4, 0.5);
}

/* Secondary CTA */
.cta-secondary {
  background: transparent;
  color: #feba04;
  border: 2px solid #feba04;
  padding: 14px 28px;
  border-radius: 999px;
}

/* Tertiary CTA */
.cta-tertiary {
  background: none;
  color: #feba04;
  text-decoration: none;
  font-weight: 500;
}

.cta-tertiary::after {
  content: " →";
  transition: transform 0.2s;
}

.cta-tertiary:hover::after {
  transform: translateX(4px);
}
```

### 7.3 CTA Placement Rules

**Above the Fold:**
- One primary CTA in hero section
- One secondary CTA option (video, learn more)

**Throughout Page:**
- CTA after every 2-3 content sections
- Vary CTA text based on context (e.g., "Bekijk Demo" near videos)

**Bottom of Page:**
- Dedicated conversion section
- Multiple contact options (WhatsApp, form, phone)

**Sticky Elements (Mobile):**
```
┌─────────────────────────────────────────────────────────────────┐
│ [Fixed bottom bar on product pages]                             │
│                                                                 │
│  Vanaf €X.XXX        [OFFERTE]  [📞]                           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 7.4 WhatsApp CTA Enhancement

Currently the site uses WhatsApp as primary contact. To elevate this:

```html
<!-- Instead of just "WhatsApp" -->
<a href="https://wa.me/31623998934?text=..." class="cta-whatsapp">
  <span class="cta-icon">💬</span>
  <span class="cta-text">
    <strong>Direct Contact met een Expert</strong>
    <small>Gemiddelde reactietijd: 15 minuten</small>
  </span>
</a>
```

**Pre-filled message templates:**
```javascript
const whatsappMessages = {
  general: "Hallo, ik heb interesse in jullie interactieve systemen.",
  product: (productName) => `Hallo, ik wil graag meer weten over de ${productName}.`,
  quote: "Hallo, ik zou graag een vrijblijvende offerte ontvangen.",
  demo: "Hallo, ik zou graag een demonstratie inplannen."
};
```

---

## 8. Mobile-First Conversion Optimization

### 8.1 Mobile-Specific Considerations

| Aspect | Desktop Approach | Mobile Adaptation |
|--------|------------------|-------------------|
| **Hero Video** | Auto-play background | Static image + play button |
| **Navigation** | Mega menu on hover | Accordion menu |
| **Product Cards** | 3-column grid | Single column stack |
| **CTAs** | Inline with content | Sticky bottom bar |
| **Forms** | Multi-column | Single column, larger inputs |
| **Testimonials** | Carousel | Swipeable cards |

### 8.2 Touch-Friendly Design

```css
/* Minimum touch targets */
.btn, .link, .interactive {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 16px;
}

/* Spacing between tappable elements */
.cta-group {
  gap: 12px;
}

/* Form inputs */
input, select, textarea {
  font-size: 16px; /* Prevents iOS zoom */
  padding: 14px;
}
```

### 8.3 Mobile Page Speed Priorities

1. **Lazy load images** below the fold
2. **Defer non-critical JavaScript** (particle animation)
3. **Use WebP format** with fallbacks
4. **Preload critical assets** (hero image, fonts)
5. **Minimize CSS** (current ~1700 lines could be reduced)

### 8.4 Mobile-Specific CTAs

```
┌─────────────────────────────────────────────────────────────────┐
│ MOBILE STICKY FOOTER                                            │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│  Option A: Product Pages                                        │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │ Vanaf €X.XXX   [OFFERTE]  [📞 BEL]                      │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
│  Option B: All Pages                                            │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │          [████ WHATSAPP CONTACT ████]                   │   │
│  └─────────────────────────────────────────────────────────┘   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 9. Microinteractions & Delight Factors

### 9.1 Recommended Microinteractions

| Element | Interaction | Purpose |
|---------|-------------|---------|
| **CTA Buttons** | Subtle lift on hover | Affordance, feedback |
| **Product Cards** | Scale up slightly on hover | Focus attention |
| **Navigation Links** | Underline animation | Visual feedback |
| **Form Success** | Checkmark animation | Confirmation delight |
| **Scroll Progress** | Progress bar in header | Reading progress |
| **Image Gallery** | Smooth fade transitions | Polish |
| **FAQ Accordion** | Smooth height animation | Smooth UX |
| **Number Counters** | Count-up on scroll into view | Engagement |
| **Video Play** | Pulsing play button | Encourage interaction |

### 9.2 Loading States

```css
/* Skeleton loading for product cards */
.product-card--loading {
  background: linear-gradient(
    90deg,
    #f0f0f0 25%,
    #e0e0e0 50%,
    #f0f0f0 75%
  );
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite;
}

@keyframes shimmer {
  0% { background-position: 200% 0; }
  100% { background-position: -200% 0; }
}
```

### 9.3 Scroll-Triggered Animations

```javascript
// Intersection Observer for fade-in animations
const observerOptions = {
  threshold: 0.1,
  rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('animate-in');
    }
  });
}, observerOptions);

document.querySelectorAll('.animate-on-scroll').forEach(el => {
  observer.observe(el);
});
```

### 9.4 Particle Background Enhancement

The existing `projector.js` is good but consider:

1. **Reduce particle count on mobile** (currently 25 → 10 on mobile)
2. **Pause animation when tab not visible** (performance)
3. **Add subtle color pulse** matching brand amber on CTAs
4. **Reduce opacity** slightly to not distract from content

---

## 10. Accessibility as UX

Accessibility isn't just compliance — it's good UX for everyone.

### 10.1 Color Contrast Requirements

| Text Type | Current | Required (WCAG AA) | Recommendation |
|-----------|---------|-------------------|----------------|
| Body text on white | #1d1e22 | ✅ 16.1:1 | Good |
| Amber on white | #feba04 | ❌ 2.1:1 | Darken to #c79400 for text |
| White on dark | #f0f0f0 on #1d1e22 | ✅ 13.5:1 | Good |
| Amber buttons | #1d1e22 on #feba04 | ✅ 9.6:1 | Good |

### 10.2 Focus States

```css
/* Visible focus for keyboard navigation */
:focus-visible {
  outline: 3px solid #feba04;
  outline-offset: 2px;
}

/* Skip to content link */
.skip-link {
  position: absolute;
  top: -40px;
  left: 0;
  background: #feba04;
  color: #1d1e22;
  padding: 8px 16px;
  z-index: 100;
}

.skip-link:focus {
  top: 0;
}
```

### 10.3 ARIA Implementation

```html
<!-- Navigation -->
<nav aria-label="Hoofdnavigatie">
  <button aria-expanded="false" aria-controls="menu">Menu</button>
  <ul id="menu" role="menu">
    <li role="menuitem"><a href="/">Home</a></li>
    <!-- ... -->
  </ul>
</nav>

<!-- Accordion FAQ -->
<div class="faq">
  <button 
    aria-expanded="false" 
    aria-controls="faq-1"
    id="faq-1-trigger"
  >
    Hoe groot moet de ruimte zijn?
  </button>
  <div 
    id="faq-1" 
    role="region" 
    aria-labelledby="faq-1-trigger"
    hidden
  >
    <p>Minimaal 4x3 meter voor de interactieve vloer...</p>
  </div>
</div>

<!-- Image with alt text -->
<img 
  src="media/products/vloer.jpg" 
  alt="Kinderen spelen voetbal op een interactieve vloer in een gymzaal"
  loading="lazy"
>
```

### 10.4 Motion Preferences

```css
/* Respect user's motion preferences */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  
  /* Disable particle animation */
  #projector-canvas {
    display: none;
  }
}
```

---

## 11. Implementation Priority Matrix

### Phase 1: Quick Wins (Week 1-2)
| Task | Impact | Effort | Priority |
|------|--------|--------|----------|
| Add trust logos/stats to homepage | High | Low | 🔴 Critical |
| Improve CTA button hierarchy | High | Low | 🔴 Critical |
| Add testimonial section | High | Medium | 🔴 Critical |
| Fix mobile sticky CTA | High | Low | 🔴 Critical |
| Optimize hero section copy | High | Low | 🔴 Critical |

### Phase 2: Core Improvements (Week 3-4)
| Task | Impact | Effort | Priority |
|------|--------|--------|----------|
| Rebuild product page structure | High | Medium | 🟠 High |
| Add video testimonials | High | Medium | 🟠 High |
| Implement FAQ accordions | Medium | Low | 🟠 High |
| Add pricing comparison table | High | Medium | 🟠 High |
| Industry page content refresh | High | Medium | 🟠 High |

### Phase 3: Advanced Features (Week 5-8)
| Task | Impact | Effort | Priority |
|------|--------|--------|----------|
| Build park configurator | Very High | High | 🟡 Medium |
| Games library with filtering | Medium | Medium | 🟡 Medium |
| ROI calculator for entertainment | High | Medium | 🟡 Medium |
| Add case study pages | High | High | 🟡 Medium |
| Implement scroll animations | Low | Medium | 🟢 Low |

### Phase 4: Polish & Optimization (Ongoing)
| Task | Impact | Effort | Priority |
|------|--------|--------|----------|
| A/B testing CTAs | Medium | Low | 🟢 Low |
| Performance optimization | Medium | Medium | 🟢 Low |
| Add live chat option | Medium | Low | 🟢 Low |
| Seasonal content templates | Low | Low | 🟢 Low |

---

## 12. Appendix: Component Library Recommendations

### 12.1 Reusable Components to Build

```
COMPONENTS/
├── hero/
│   ├── hero-video.html
│   ├── hero-image.html
│   └── hero-split.html
├── cards/
│   ├── product-card.html
│   ├── testimonial-card.html
│   ├── feature-card.html
│   └── game-card.html
├── sections/
│   ├── trust-bar.html
│   ├── stats-counter.html
│   ├── cta-banner.html
│   ├── faq-accordion.html
│   └── pricing-table.html
├── navigation/
│   ├── header.html
│   ├── footer.html
│   ├── breadcrumb.html
│   └── mobile-menu.html
├── forms/
│   ├── contact-form.html
│   ├── quote-form.html
│   └── newsletter-signup.html
└── modals/
    ├── video-modal.html
    └── game-detail-modal.html
```

### 12.2 CSS Architecture Recommendation

```css
/* Suggested CSS structure */
styles/
├── base/
│   ├── reset.css
│   ├── typography.css
│   └── variables.css
├── components/
│   ├── buttons.css
│   ├── cards.css
│   ├── forms.css
│   └── navigation.css
├── layouts/
│   ├── header.css
│   ├── footer.css
│   ├── grid.css
│   └── sections.css
├── pages/
│   ├── home.css
│   ├── product.css
│   └── pricing.css
└── utilities/
    ├── animations.css
    ├── spacing.css
    └── visibility.css
```

---

## Summary & Next Steps

This report provides a comprehensive UX and conversion strategy for the InterActiveMove website. The key themes are:

1. **Trust First** — B2B buyers need extensive trust signals before considering high-ticket items
2. **Visual Storytelling** — Show transformation, not just products
3. **Persona-Driven Content** — Education, healthcare, and entertainment buyers have different needs
4. **Clear Conversion Path** — Every page should guide toward contact/quote request
5. **Mobile Excellence** — Touch-friendly, fast, with sticky CTAs

**Immediate Action Items:**
1. ✅ Add trust elements to homepage (logos, stats, testimonials)
2. ✅ Restructure product pages with video demos and specs
3. ✅ Create dedicated industry landing pages with relevant social proof
4. ✅ Implement sticky mobile CTAs
5. ✅ Begin collecting video testimonials from existing customers

---

*Document prepared by UX & Conversion Strategy Consultant*  
*Version 1.0 — January 2026*
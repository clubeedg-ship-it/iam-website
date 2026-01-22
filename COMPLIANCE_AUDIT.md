# InterActiveMove Website
## GDPR & EU/Dutch Compliance Audit Report

**Document Version:** 1.0  
**Date:** January 2026  
**Prepared for:** Inter Active Move B.V.  
**Prepared by:** Privacy & Compliance Consultant  
**Jurisdiction:** European Union / Netherlands

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Regulatory Framework Overview](#2-regulatory-framework-overview)
3. [Current Compliance Assessment](#3-current-compliance-assessment)
4. [GDPR Compliance Requirements](#4-gdpr-compliance-requirements)
5. [Dutch UAVG Specific Requirements](#5-dutch-uavg-specific-requirements)
6. [ePrivacy & Cookie Compliance](#6-eprivacy--cookie-compliance)
7. [Website Legal Pages (Required)](#7-website-legal-pages-required)
8. [Third-Party Services Audit](#8-third-party-services-audit)
9. [WhatsApp Business Compliance](#9-whatsapp-business-compliance)
10. [Contact Forms & Lead Generation](#10-contact-forms--lead-generation)
11. [Digital Services Act (DSA) Compliance](#11-digital-services-act-dsa-compliance)
12. [Accessibility Compliance (WCAG/EN 301 549)](#12-accessibility-compliance-wcagen-301-549)
13. [Dutch Consumer Law (B2B/B2C)](#13-dutch-consumer-law-b2bb2c)
14. [Implementation Checklist](#14-implementation-checklist)
15. [Template Documents](#15-template-documents)
16. [Appendix: Technical Implementation](#16-appendix-technical-implementation)

---

## 1. Executive Summary

### Compliance Status Overview

| Regulation | Current Status | Risk Level | Priority |
|------------|---------------|------------|----------|
| **GDPR** | ⚠️ Partial | High | Critical |
| **Dutch UAVG** | ⚠️ Partial | High | Critical |
| **ePrivacy (Cookies)** | ❌ Non-compliant | High | Critical |
| **Digital Services Act** | ⚠️ Partial | Medium | High |
| **WCAG 2.1 Accessibility** | ⚠️ Partial | Medium | High |
| **Dutch Consumer Law** | ⚠️ Partial | Medium | Medium |

### Critical Issues Identified

```
┌─────────────────────────────────────────────────────────────────┐
│ 🔴 CRITICAL COMPLIANCE GAPS                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ 1. No Privacy Policy (Privacybeleid) present                   │
│ 2. No Cookie Consent mechanism implemented                      │
│ 3. No Terms & Conditions (Algemene Voorwaarden)                │
│ 4. Google Fonts loaded externally (GDPR concern)               │
│ 5. WhatsApp data processing not documented                     │
│ 6. No contact form consent checkboxes                          │
│ 7. Missing legal entity information in footer                  │
│ 8. No accessibility statement                                   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Estimated Penalty Exposure

| Violation Type | Maximum Fine (GDPR) |
|---------------|---------------------|
| Missing Privacy Policy | Up to €20M or 4% annual turnover |
| Missing Cookie Consent | Up to €20M or 4% annual turnover |
| Unlawful Data Processing | Up to €20M or 4% annual turnover |
| Missing Legal Information | Up to €10,000 (Dutch law) |

**Note:** Dutch Data Protection Authority (Autoriteit Persoonsgegevens) has been increasingly active in enforcement. In 2024-2025, they issued significant fines to Dutch companies for cookie consent violations.

---

## 2. Regulatory Framework Overview

### 2.1 Applicable Regulations

| Regulation | Scope | Enforcing Authority |
|------------|-------|---------------------|
| **GDPR** (EU 2016/679) | Personal data processing of EU residents | Autoriteit Persoonsgegevens (AP) |
| **UAVG** (Dutch GDPR Implementation) | Dutch-specific GDPR provisions | Autoriteit Persoonsgegevens (AP) |
| **ePrivacy Directive** (2002/58/EC) | Cookies, electronic communications | Autoriteit Consument & Markt (ACM) |
| **Telecommunicatiewet** | Dutch cookie law implementation | ACM |
| **Digital Services Act** (EU 2022/2065) | Online platform transparency | ACM / European Commission |
| **European Accessibility Act** | Website accessibility for public entities | National accessibility authority |
| **BW Book 6** | Dutch Consumer Protection | ACM |

### 2.2 IAM's Data Processing Profile

Based on website analysis, Inter Active Move B.V. processes:

| Data Category | Source | Legal Basis Required |
|--------------|--------|---------------------|
| Contact information (name, email, phone) | Contact forms, WhatsApp | Consent or Legitimate Interest |
| Business information (company name, type) | Quote requests | Contract performance |
| Website usage data | Analytics, cookies | Consent |
| IP addresses | Server logs, Google Fonts | Legitimate Interest (limited) |
| Communication content | WhatsApp messages | Contract performance |

### 2.3 Data Controller Identification

```
Data Controller:
Inter Active Move B.V.
[Address]
[Postcode], [City]
Netherlands

KvK (Chamber of Commerce): [Number]
BTW (VAT): NL[Number]B01

Contact for privacy matters:
Email: privacy@interactivemove.nl (recommended to create)
```

---

## 3. Current Compliance Assessment

### 3.1 Website Technical Audit

| Element | Status | Issue | Risk |
|---------|--------|-------|------|
| Privacy Policy page | ❌ Missing | No `/privacybeleid.html` found | Critical |
| Cookie Policy page | ❌ Missing | No cookie information | Critical |
| Cookie Consent Banner | ❌ Missing | No consent mechanism | Critical |
| Terms & Conditions | ❌ Missing | No `/algemene-voorwaarden.html` | High |
| Legal footer info | ⚠️ Incomplete | KvK number not visible | Medium |
| SSL Certificate | ✅ Present | HTTPS enforced | Low |
| Contact page consent | ❌ Missing | No checkbox for data processing | High |
| Data retention info | ❌ Missing | Not documented | High |

### 3.2 Third-Party Services Identified

| Service | Data Transferred | Location | GDPR Concern |
|---------|-----------------|----------|--------------|
| **Google Fonts** | IP address, browser info | USA | ⚠️ High - Requires consent or local hosting |
| **WhatsApp Business** | Messages, phone numbers, metadata | USA (Meta) | ⚠️ Medium - Requires DPA |
| **HTMX CDN** | IP address | Varies | ⚠️ Low - Consider self-hosting |
| **Web Hosting** | All website data | Unknown | ⚠️ Check location |

### 3.3 Data Flow Analysis

```
┌─────────────────────────────────────────────────────────────────┐
│ CURRENT DATA FLOWS                                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  VISITOR                                                        │
│     │                                                           │
│     ├──► Website Visit ──► IP logged (server)                  │
│     │                  ──► Google Fonts request (USA) ⚠️       │
│     │                  ──► HTMX CDN request ⚠️                 │
│     │                                                           │
│     ├──► Contact Form ──► Form data ──► [Where?] ⚠️            │
│     │    (no consent)                                          │
│     │                                                           │
│     └──► WhatsApp Click ──► Phone number shared ──► Meta (USA) │
│          (no consent)       Message content ──► Meta (USA) ⚠️   │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. GDPR Compliance Requirements

### 4.1 Lawful Basis for Processing (Article 6)

For each data processing activity, IAM must establish a lawful basis:

| Processing Activity | Recommended Legal Basis | Requirements |
|--------------------|------------------------|--------------|
| Website analytics | **Consent** | Explicit opt-in via cookie banner |
| Contact form submissions | **Consent** or **Legitimate Interest** | Checkbox + privacy notice |
| Quote/demo requests | **Contract Performance** (Art. 6(1)(b)) | Pre-contractual steps |
| WhatsApp communication | **Consent** + **Contract Performance** | Clear notice before use |
| Marketing emails | **Consent** (Art. 6(1)(a)) | Explicit opt-in, easy opt-out |
| Google Fonts | **Consent** or **Self-host** | Banner consent or eliminate transfer |

### 4.2 Transparency Requirements (Articles 13-14)

When collecting personal data, IAM must inform individuals of:

```
REQUIRED INFORMATION AT POINT OF COLLECTION:

□ Identity of data controller (Inter Active Move B.V.)
□ Contact details (including DPO if appointed)
□ Purposes of processing
□ Legal basis for processing
□ Recipients or categories of recipients
□ Transfer to third countries (USA via Google/Meta)
□ Retention period
□ Rights of the data subject
□ Right to withdraw consent
□ Right to lodge complaint with AP
□ Whether provision is statutory/contractual requirement
□ Existence of automated decision-making (if any)
```

### 4.3 Data Subject Rights (Articles 15-22)

IAM must facilitate these rights:

| Right | Article | Implementation Required |
|-------|---------|------------------------|
| **Access** | Art. 15 | Process to provide data copies within 30 days |
| **Rectification** | Art. 16 | Process to correct inaccurate data |
| **Erasure** ("Right to be Forgotten") | Art. 17 | Process to delete data on request |
| **Restriction** | Art. 18 | Process to limit processing |
| **Data Portability** | Art. 20 | Provide data in machine-readable format |
| **Object** | Art. 21 | Process to stop processing on objection |
| **Automated Decisions** | Art. 22 | N/A (no automated decision-making identified) |

**Required:** Create `privacy@interactivemove.nl` email and document response procedures.

### 4.4 Data Protection by Design (Article 25)

Current website lacks privacy-by-design principles:

| Principle | Current State | Required Action |
|-----------|--------------|-----------------|
| Data Minimization | ⚠️ Unknown | Only collect necessary data |
| Purpose Limitation | ❌ Not documented | Document specific purposes |
| Storage Limitation | ❌ Not documented | Define retention periods |
| Integrity & Confidentiality | ✅ HTTPS present | Maintain SSL, secure forms |
| Accountability | ❌ Not demonstrated | Document all processing |

### 4.5 Records of Processing Activities (Article 30)

IAM must maintain a register of processing activities:

```
┌─────────────────────────────────────────────────────────────────┐
│ TEMPLATE: RECORD OF PROCESSING ACTIVITIES                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ Processing Activity: Website Contact Form                       │
│ ─────────────────────────────────────────────────────────────── │
│                                                                 │
│ Controller: Inter Active Move B.V.                             │
│ Purpose: Respond to inquiries, provide quotes                  │
│ Legal Basis: Consent / Legitimate Interest                     │
│ Data Categories: Name, email, phone, company, message          │
│ Data Subjects: Prospective customers                           │
│ Recipients: IAM sales team, CRM system (if any)               │
│ Transfers: None / [Specify if using cloud services]           │
│ Retention: 2 years after last contact                         │
│ Security Measures: SSL encryption, access controls             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 5. Dutch UAVG Specific Requirements

### 5.1 Dutch Implementation Details

The UAVG (Uitvoeringswet Algemene Verordening Gegevensbescherming) adds Dutch-specific provisions:

| UAVG Provision | Requirement | IAM Impact |
|----------------|-------------|------------|
| **Article 25** | National ID number processing restrictions | Do not collect BSN |
| **Article 26** | Criminal data processing restrictions | N/A |
| **Article 29** | Children's consent (16 years in NL) | Ensure parental consent if targeting minors |
| **Article 30** | Exemptions for small businesses | Some documentation exemptions may apply |

### 5.2 Age of Consent for Children

In the Netherlands, the digital age of consent is **16 years** (not 13 as in some countries).

**IAM Consideration:** If products target schools with children under 16:
- Obtain consent from parent/guardian
- Verify consent mechanism
- Include clear age-appropriate privacy notices

### 5.3 Dutch Language Requirements

All privacy documentation must be available in **Dutch** for Dutch visitors:

| Document | English | Dutch | Status |
|----------|---------|-------|--------|
| Privacy Policy | Required | **Required** | ❌ Missing |
| Cookie Policy | Required | **Required** | ❌ Missing |
| Terms & Conditions | Required | **Required** | ❌ Missing |
| Consent texts | Required | **Required** | ❌ Missing |

### 5.4 Autoriteit Persoonsgegevens (AP) Focus Areas

The Dutch DPA has specifically targeted:

1. **Cookie walls** — Blocking access without cookie consent is illegal
2. **Dark patterns** — Manipulative consent interfaces
3. **Google services** — Particularly Google Analytics and Fonts
4. **Tracking without consent** — Any form of tracking before opt-in

---

## 6. ePrivacy & Cookie Compliance

### 6.1 Dutch Cookie Law (Telecommunicatiewet Art. 11.7a)

The Netherlands has strict cookie regulations:

```
┌─────────────────────────────────────────────────────────────────┐
│ COOKIE CONSENT REQUIREMENTS                                     │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ STRICTLY NECESSARY COOKIES:                                     │
│ ✅ No consent required                                          │
│ Examples: Session ID, shopping cart, language preference       │
│                                                                 │
│ FUNCTIONAL COOKIES:                                             │
│ ⚠️ Consent recommended (gray area)                             │
│ Examples: Chat widget state, user preferences                  │
│                                                                 │
│ ANALYTICAL COOKIES:                                             │
│ ❌ CONSENT REQUIRED before placing                              │
│ Examples: Google Analytics, Hotjar, Matomo (unless configured) │
│                                                                 │
│ MARKETING/TRACKING COOKIES:                                     │
│ ❌ CONSENT REQUIRED before placing                              │
│ Examples: Facebook Pixel, Google Ads, retargeting             │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.2 Current Cookie Audit

Based on website analysis, the following cookies/tracking may be present:

| Cookie/Tracker | Category | Consent Required | Current Status |
|----------------|----------|------------------|----------------|
| Google Fonts request | Tracking (IP transfer) | Yes | ❌ No consent |
| HTMX (if storing state) | Functional | Debatable | ⚠️ Review |
| Language preference | Strictly Necessary | No | ✅ OK |
| Session storage | Strictly Necessary | No | ✅ OK |

### 6.3 Compliant Cookie Banner Requirements

A compliant cookie banner must:

```
┌─────────────────────────────────────────────────────────────────┐
│ COOKIE BANNER REQUIREMENTS                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ ✅ MUST HAVE:                                                   │
│ • Appear before ANY non-essential cookies are placed           │
│ • Offer genuine choice (Accept / Reject / Customize)           │
│ • "Reject All" must be equally prominent as "Accept All"       │
│ • Link to full cookie policy                                   │
│ • List specific cookies and purposes                           │
│ • Allow granular consent per category                          │
│ • Store consent proof (timestamp, version, choices)            │
│ • Allow easy withdrawal of consent                             │
│ • Not use dark patterns or manipulative design                 │
│                                                                 │
│ ❌ MUST NOT:                                                    │
│ • Pre-tick any non-essential cookie boxes                      │
│ • Use "cookie walls" (block access without consent)            │
│ • Make "Reject" harder to find than "Accept"                   │
│ • Use confusing language                                       │
│ • Assume consent from scrolling or continued use               │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 6.4 Recommended Cookie Consent Implementation

**Option A: Lightweight Self-Hosted Solution**

```html
<!-- Cookie Consent Banner HTML -->
<div id="cookie-consent" class="cookie-banner" role="dialog" aria-labelledby="cookie-title" aria-modal="true">
  <div class="cookie-content">
    <h2 id="cookie-title">Wij respecteren uw privacy</h2>
    <p>
      Wij gebruiken cookies om uw ervaring te verbeteren. 
      <a href="/cookiebeleid.html">Lees ons cookiebeleid</a>.
    </p>
    
    <div class="cookie-options">
      <label>
        <input type="checkbox" checked disabled>
        <span>Noodzakelijk</span>
        <small>Altijd actief</small>
      </label>
      <label>
        <input type="checkbox" id="cookie-analytics">
        <span>Analytisch</span>
        <small>Helpt ons de website te verbeteren</small>
      </label>
      <label>
        <input type="checkbox" id="cookie-marketing">
        <span>Marketing</span>
        <small>Persoonlijke advertenties</small>
      </label>
    </div>
    
    <div class="cookie-buttons">
      <button id="cookie-reject" class="btn-secondary">Alles weigeren</button>
      <button id="cookie-accept-selected" class="btn-secondary">Selectie opslaan</button>
      <button id="cookie-accept-all" class="btn-primary">Alles accepteren</button>
    </div>
  </div>
</div>
```

**Option B: Third-Party Consent Management Platform (CMP)**

Recommended CMPs compliant with Dutch/EU law:

| CMP | Pricing | Features | Recommendation |
|-----|---------|----------|----------------|
| **Cookiebot** | Free (≤100 pages) | Auto-scan, compliant | ✅ Good for SMB |
| **Complianz** | €49/year | WordPress focus | N/A (static site) |
| **Osano** | Free tier available | Simple setup | ✅ Good option |
| **OneTrust** | Enterprise pricing | Full compliance suite | For larger orgs |
| **Klaro** | Open source | Self-hosted, customizable | ✅ Best for static sites |

**Recommendation for IAM:** Use **Klaro** (open source) for maximum control on static site, or **Cookiebot** for ease of implementation.

### 6.5 Google Fonts Compliance Solution

**Problem:** Loading Google Fonts from Google's servers transfers visitor IP addresses to USA.

**Solutions:**

| Solution | Effort | Privacy Benefit | Performance |
|----------|--------|-----------------|-------------|
| **Self-host fonts** (Recommended) | Low | ✅ Complete | ✅ Faster |
| Consent before loading | Medium | ✅ Compliant | ⚠️ Delayed |
| Use system fonts | Very Low | ✅ Complete | ✅ Fastest |

**Self-Hosting Implementation:**

```bash
# Download Inter font files
# Place in /media/fonts/

# Directory structure:
media/
└── fonts/
    ├── Inter-Regular.woff2
    ├── Inter-Medium.woff2
    ├── Inter-SemiBold.woff2
    └── Inter-Bold.woff2
```

```css
/* Replace Google Fonts import with local fonts */

/* OLD (Remove this): */
/* @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;800&display=swap'); */

/* NEW (Add this): */
@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 400;
  font-display: swap;
  src: url('/media/fonts/Inter-Regular.woff2') format('woff2');
}

@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 500;
  font-display: swap;
  src: url('/media/fonts/Inter-Medium.woff2') format('woff2');
}

@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 600;
  font-display: swap;
  src: url('/media/fonts/Inter-SemiBold.woff2') format('woff2');
}

@font-face {
  font-family: 'Inter';
  font-style: normal;
  font-weight: 700;
  font-display: swap;
  src: url('/media/fonts/Inter-Bold.woff2') format('woff2');
}
```

**Download fonts from:** https://google-webfonts-helper.herokuapp.com/fonts/inter

---

## 7. Website Legal Pages (Required)

### 7.1 Required Legal Pages

| Page | Dutch Name | URL | Priority |
|------|------------|-----|----------|
| Privacy Policy | Privacybeleid | `/privacybeleid.html` | 🔴 Critical |
| Cookie Policy | Cookiebeleid | `/cookiebeleid.html` | 🔴 Critical |
| Terms & Conditions | Algemene Voorwaarden | `/algemene-voorwaarden.html` | 🟠 High |
| Accessibility Statement | Toegankelijkheidsverklaring | `/toegankelijkheid.html` | 🟡 Medium |
| Imprint/Legal Notice | Colofon | Footer section | 🟠 High |

### 7.2 Privacy Policy Structure (Privacybeleid)

```markdown
# Privacybeleid

**Laatst bijgewerkt:** [Datum]

## 1. Wie zijn wij?
Inter Active Move B.V.
[Adres]
[Postcode, Plaats]
KvK-nummer: [Nummer]
E-mail: privacy@interactivemove.nl

## 2. Welke persoonsgegevens verwerken wij?

### 2.1 Gegevens die u ons verstrekt
- Naam
- E-mailadres
- Telefoonnummer
- Bedrijfsnaam
- Inhoud van uw bericht

### 2.2 Gegevens die automatisch worden verzameld
- IP-adres (geanonimiseerd in analytics)
- Browsertype en -versie
- Apparaattype
- Bezochte pagina's
- Datum en tijd van bezoek

## 3. Waarvoor gebruiken wij uw gegevens?

| Doel | Rechtsgrond | Bewaartermijn |
|------|-------------|---------------|
| Beantwoorden van vragen | Toestemming / Gerechtvaardigd belang | 2 jaar na laatste contact |
| Offertes maken | Uitvoering overeenkomst | 7 jaar (fiscale bewaarplicht) |
| Nieuwsbrief verzenden | Toestemming | Tot intrekking toestemming |
| Website verbeteren | Toestemming (analytics) | 26 maanden |

## 4. Delen wij uw gegevens?

Wij delen uw gegevens met:
- **WhatsApp/Meta** (voor communicatie via WhatsApp)
- **[Hostingprovider]** (websitehosting)
- **[Eventuele andere partijen]**

Wij sluiten verwerkersovereenkomsten met deze partijen.

### Doorgifte buiten de EU
WhatsApp/Meta is gevestigd in de Verenigde Staten. Voor deze doorgifte 
baseren wij ons op de Standard Contractual Clauses van de Europese Commissie.

## 5. Uw rechten

U heeft de volgende rechten:
- **Inzage**: U kunt opvragen welke gegevens wij van u hebben
- **Rectificatie**: U kunt onjuiste gegevens laten corrigeren
- **Verwijdering**: U kunt vragen uw gegevens te wissen
- **Beperking**: U kunt vragen de verwerking te beperken
- **Bezwaar**: U kunt bezwaar maken tegen verwerking
- **Overdraagbaarheid**: U kunt uw gegevens in digitaal formaat ontvangen

Neem contact op via privacy@interactivemove.nl

## 6. Beveiliging

Wij nemen passende maatregelen om uw gegevens te beschermen:
- SSL-versleuteling op onze website
- Beperkte toegang tot persoonsgegevens
- Regelmatige beveiligingsupdates

## 7. Cookies

Zie ons [Cookiebeleid](/cookiebeleid.html) voor informatie over cookies.

## 8. Wijzigingen

Wij kunnen dit privacybeleid wijzigen. De meest recente versie staat 
altijd op deze pagina met de datum van laatste wijziging.

## 9. Klachten

Heeft u een klacht over hoe wij met uw gegevens omgaan? 
Neem contact met ons op via privacy@interactivemove.nl.

U kunt ook een klacht indienen bij de Autoriteit Persoonsgegevens:
https://autoriteitpersoonsgegevens.nl/nl/zelf-doen/gebruik-uw-privacyrechten/klacht-melden-bij-de-ap

## 10. Contact

Inter Active Move B.V.
[Adres]
[Postcode, Plaats]
privacy@interactivemove.nl
+31 6 23 99 89 34
```

### 7.3 Cookie Policy Structure (Cookiebeleid)

```markdown
# Cookiebeleid

**Laatst bijgewerkt:** [Datum]

## Wat zijn cookies?

Cookies zijn kleine tekstbestanden die op uw apparaat worden opgeslagen 
wanneer u onze website bezoekt. Ze helpen ons de website te laten 
functioneren en te verbeteren.

## Welke cookies gebruiken wij?

### Noodzakelijke cookies
Deze cookies zijn essentieel voor het functioneren van de website.

| Cookie | Doel | Bewaartermijn |
|--------|------|---------------|
| cookie_consent | Onthoudt uw cookievoorkeuren | 1 jaar |
| lang | Onthoudt uw taalvoorkeur | 1 jaar |

### Analytische cookies
Deze cookies helpen ons te begrijpen hoe bezoekers onze website gebruiken.

| Cookie | Doel | Bewaartermijn |
|--------|------|---------------|
| [Indien van toepassing] | | |

**Let op:** Wij plaatsen analytische cookies alleen met uw toestemming.

### Marketing cookies
Momenteel gebruiken wij geen marketing cookies.

## Cookies beheren

U kunt uw cookievoorkeuren op elk moment wijzigen via de 
cookiebanner of door op de volgende link te klikken:
[Cookie-instellingen wijzigen]

U kunt cookies ook blokkeren via uw browserinstellingen:
- [Chrome](https://support.google.com/chrome/answer/95647)
- [Firefox](https://support.mozilla.org/nl/kb/cookies-in-en-uitschakelen)
- [Safari](https://support.apple.com/nl-nl/guide/safari/sfri11471/mac)
- [Edge](https://support.microsoft.com/nl-nl/microsoft-edge/cookies-verwijderen-in-microsoft-edge-63947406-40ac-c3b8-57b9-2a946a29ae09)

## Contact

Vragen over cookies? Neem contact op via privacy@interactivemove.nl.
```

### 7.4 Terms & Conditions Structure (Algemene Voorwaarden)

For B2B sales of high-ticket items, comprehensive terms are essential:

```markdown
# Algemene Voorwaarden

**Inter Active Move B.V.**
Versie: 1.0
Datum: [Datum]

## Artikel 1 - Definities

In deze voorwaarden wordt verstaan onder:
1. **IAM**: Inter Active Move B.V., gevestigd te [Plaats], KvK [Nummer]
2. **Klant**: de rechtspersoon of natuurlijke persoon die een overeenkomst aangaat met IAM
3. **Product**: interactieve projectiesystemen en bijbehorende software
4. **Overeenkomst**: de afspraken tussen IAM en Klant

## Artikel 2 - Toepasselijkheid

1. Deze voorwaarden zijn van toepassing op alle aanbiedingen, offertes 
   en overeenkomsten tussen IAM en Klant.
2. Afwijkingen zijn alleen geldig indien schriftelijk overeengekomen.
3. Eventuele inkoop- of andere voorwaarden van Klant worden niet geaccepteerd.

## Artikel 3 - Offertes en Prijzen

1. Alle offertes zijn vrijblijvend en 30 dagen geldig.
2. Prijzen zijn exclusief BTW en installatiekosten, tenzij anders vermeld.
3. IAM behoudt zich het recht voor prijzen te wijzigen.

## Artikel 4 - Levering en Installatie

1. Levertijden zijn indicatief en geen fatale termijnen.
2. Installatie geschiedt door of namens IAM, tenzij anders overeengekomen.
3. Klant zorgt voor geschikte ruimte en stroomaansluiting.

## Artikel 5 - Garantie

1. IAM biedt [X] jaar garantie op hardware.
2. Software-updates worden [X] jaar kosteloos verstrekt.
3. Garantie vervalt bij oneigenlijk gebruik of wijzigingen door derden.

## Artikel 6 - Aansprakelijkheid

1. IAM is niet aansprakelijk voor indirecte schade.
2. Aansprakelijkheid is beperkt tot het factuurbedrag.
3. [Verdere beperkingen]

## Artikel 7 - Intellectueel Eigendom

1. Software blijft eigendom van IAM of haar licentiegevers.
2. Klant verkrijgt een gebruiksrecht voor de duur van de overeenkomst.
3. Reverse engineering is niet toegestaan.

## Artikel 8 - Privacy

IAM verwerkt persoonsgegevens conform het Privacybeleid op de website.

## Artikel 9 - Klachten

Klachten dienen binnen 14 dagen na ontdekking schriftelijk te worden gemeld.

## Artikel 10 - Toepasselijk Recht

1. Op alle overeenkomsten is Nederlands recht van toepassing.
2. Geschillen worden voorgelegd aan de rechtbank [Plaats].

## Contact

Inter Active Move B.V.
[Adres]
[Email]
[Telefoon]
KvK: [Nummer]
```

### 7.5 Footer Legal Requirements

Dutch law requires specific information in your website footer:

```html
<footer>
  <!-- Other footer content -->
  
  <div class="legal-info">
    <p>
      <strong>Inter Active Move B.V.</strong><br>
      [Straatnaam 123]<br>
      [1234 AB Plaatsnaam]<br>
      Nederland
    </p>
    <p>
      KvK: [12345678]<br>
      BTW: NL[123456789]B01
    </p>
    <p>
      <a href="tel:+31623998934">+31 6 23 99 89 34</a><br>
      <a href="mailto:info@interactivemove.nl">info@interactivemove.nl</a>
    </p>
  </div>
  
  <nav class="legal-links" aria-label="Juridische informatie">
    <a href="/privacybeleid.html">Privacybeleid</a>
    <a href="/cookiebeleid.html">Cookiebeleid</a>
    <a href="/algemene-voorwaarden.html">Algemene Voorwaarden</a>
    <a href="/toegankelijkheid.html">Toegankelijkheid</a>
  </nav>
  
  <p class="copyright">
    © 2026 Inter Active Move B.V. Alle rechten voorbehouden.
  </p>
</footer>
```

---

## 8. Third-Party Services Audit

### 8.1 Current Third-Party Services

| Service | Purpose | Data Processed | Location | GDPR Status |
|---------|---------|----------------|----------|-------------|
| **Google Fonts** | Typography | IP address | USA | ⚠️ Requires action |
| **WhatsApp Business** | Communication | Messages, phone, name | USA | ⚠️ Requires DPA |
| **HTMX (CDN)** | Functionality | IP address | Global | ⚠️ Consider self-host |
| **Web Host** | Hosting | All website data | ? | ⚠️ Verify location |

### 8.2 Required Actions per Service

#### Google Fonts
**Risk Level:** High  
**Action Required:** Self-host fonts (see Section 6.5)

#### WhatsApp Business
**Risk Level:** Medium  
**Actions Required:**
1. Document WhatsApp in privacy policy
2. Review Meta's Data Processing Agreement
3. Add notice before WhatsApp link explaining data transfer
4. Consider alternative EU-based options for sensitive inquiries

#### HTMX CDN
**Risk Level:** Low  
**Recommended Action:** Self-host HTMX library

```html
<!-- Current (CDN): -->
<script src="https://unpkg.com/htmx.org@1.9.x"></script>

<!-- Recommended (Self-hosted): -->
<script src="/js/htmx.min.js"></script>
```

#### Web Hosting
**Action Required:** Verify hosting provider's location and GDPR compliance
- If hosted in EU: Good
- If hosted outside EU: Ensure Standard Contractual Clauses in place
- Recommended EU hosts: TransIP, Hostnet, Antagonist (all Dutch)

### 8.3 Data Processing Agreement (DPA) Checklist

For each processor, ensure you have:

```
□ Signed Data Processing Agreement (Verwerkersovereenkomst)
□ Documented purposes and scope of processing
□ Security measures specified
□ Sub-processor list and notification procedure
□ Audit rights
□ Data deletion procedures
□ Breach notification procedures
□ Standard Contractual Clauses (if outside EU)
```

---

## 9. WhatsApp Business Compliance

### 9.1 WhatsApp & GDPR Considerations

WhatsApp Business processes data through Meta (USA). Key compliance points:

| Aspect | Requirement | Implementation |
|--------|-------------|----------------|
| **Notice** | Inform users before they click WhatsApp | Add notice text near button |
| **Legal Basis** | Consent or Legitimate Interest | Consent recommended |
| **DPA** | Meta's Data Processing Terms | Accept in WhatsApp Business settings |
| **Privacy Policy** | Document WhatsApp use | Add section to privacy policy |
| **Data Transfer** | USA transfer notification | Mention in privacy policy |

### 9.2 Pre-WhatsApp Notice Implementation

```html
<!-- Before WhatsApp CTA -->
<div class="whatsapp-notice">
  <a href="https://wa.me/31623998934?text=..." class="cta-whatsapp">
    <span class="whatsapp-icon">💬</span>
    <span class="whatsapp-text">WhatsApp Contact</span>
  </a>
  <p class="whatsapp-privacy-note">
    Door via WhatsApp contact op te nemen, worden uw gegevens verwerkt 
    door Meta (VS). Zie ons <a href="/privacybeleid.html">privacybeleid</a>.
  </p>
</div>
```

### 9.3 Alternative Contact Options

Consider offering GDPR-friendlier alternatives:

| Channel | GDPR Impact | Recommendation |
|---------|-------------|----------------|
| WhatsApp | Medium (USA transfer) | Keep as option, with notice |
| Email | Low (if EU-hosted) | Offer prominently |
| Phone | Very Low | Display number clearly |
| Contact Form | Low (if self-hosted) | Add as primary option |
| Signal | Low (EU-friendly) | Consider for privacy-conscious |

---

## 10. Contact Forms & Lead Generation

### 10.1 Current Form Issues

Based on website structure, contact forms likely lack:
- Consent checkbox for data processing
- Link to privacy policy
- Clear purpose statement
- Retention information

### 10.2 Compliant Contact Form Template

```html
<form action="[endpoint]" method="POST" class="contact-form">
  <h2>Neem contact op</h2>
  
  <!-- Standard fields -->
  <div class="form-group">
    <label for="name">Naam *</label>
    <input type="text" id="name" name="name" required>
  </div>
  
  <div class="form-group">
    <label for="email">E-mailadres *</label>
    <input type="email" id="email" name="email" required>
  </div>
  
  <div class="form-group">
    <label for="phone">Telefoonnummer</label>
    <input type="tel" id="phone" name="phone">
  </div>
  
  <div class="form-group">
    <label for="company">Organisatie</label>
    <input type="text" id="company" name="company">
  </div>
  
  <div class="form-group">
    <label for="message">Uw bericht *</label>
    <textarea id="message" name="message" rows="4" required></textarea>
  </div>
  
  <!-- GDPR REQUIRED: Consent checkbox -->
  <div class="form-group checkbox-group">
    <input type="checkbox" id="privacy-consent" name="privacy_consent" required>
    <label for="privacy-consent">
      Ik ga akkoord met de verwerking van mijn gegevens zoals beschreven 
      in het <a href="/privacybeleid.html" target="_blank">privacybeleid</a>. *
    </label>
  </div>
  
  <!-- OPTIONAL: Marketing consent (separate from processing consent) -->
  <div class="form-group checkbox-group">
    <input type="checkbox" id="marketing-consent" name="marketing_consent">
    <label for="marketing-consent">
      Ja, ik wil graag nieuws en updates ontvangen van Inter Active Move.
    </label>
  </div>
  
  <!-- Purpose statement -->
  <p class="form-notice">
    Wij gebruiken uw gegevens om uw vraag te beantwoorden en, indien 
    van toepassing, een offerte te maken. 
    <a href="/privacybeleid.html">Meer informatie</a>.
  </p>
  
  <button type="submit" class="cta-primary">Verstuur</button>
</form>
```

### 10.3 Form Submission Handling

```javascript
// Store consent proof
const formData = {
  // User data
  name: form.name.value,
  email: form.email.value,
  // ... other fields
  
  // GDPR consent proof (IMPORTANT)
  consent: {
    privacy_accepted: form.privacy_consent.checked,
    marketing_accepted: form.marketing_consent.checked,
    timestamp: new Date().toISOString(),
    ip_address: '[server-side]', // Capture on server
    privacy_policy_version: '1.0',
    form_location: window.location.href
  }
};
```

### 10.4 Quote Request Form (Offerte)

For the "Bouw een Park" configurator and quote requests:

```html
<!-- Additional consent text for quote forms -->
<div class="form-group checkbox-group">
  <input type="checkbox" id="quote-consent" name="quote_consent" required>
  <label for="quote-consent">
    Ik vraag een vrijblijvende offerte aan en ga akkoord met de verwerking 
    van mijn gegevens voor dit doel. Mijn gegevens worden maximaal 2 jaar 
    bewaard. <a href="/privacybeleid.html" target="_blank">Privacybeleid</a>. *
  </label>
</div>
```

---

## 11. Digital Services Act (DSA) Compliance

### 11.1 DSA Applicability

The Digital Services Act (EU 2022/2065) applies to "intermediary services." For a B2B website like IAM:

| DSA Category | Applicability | Requirements |
|--------------|---------------|--------------|
| Hosting Services | ❌ Not applicable | N/A |
| Online Platforms | ❌ Not applicable | N/A |
| Very Large Platforms | ❌ Not applicable | N/A |
| **Basic Website** | ✅ Minimal requirements | Transparency only |

### 11.2 Applicable DSA Requirements

For a standard business website:

| Requirement | Description | IAM Action |
|-------------|-------------|------------|
| **Point of Contact** | Provide contact for authorities | Add to legal pages |
| **Legal Representative** | If outside EU (N/A for Dutch company) | Not required |
| **Transparency** | Clear commercial communications | Label ads clearly |

### 11.3 Recommended Implementation

```html
<!-- Add to footer or legal page -->
<section class="dsa-info">
  <h3>Digital Services Act Contact</h3>
  <p>
    Contactpunt voor autoriteiten en gebruikers conform de 
    Digital Services Act (Verordening (EU) 2022/2065):
  </p>
  <p>
    Inter Active Move B.V.<br>
    E-mail: legal@interactivemove.nl<br>
    Telefoon: +31 6 23 99 89 34
  </p>
</section>
```

---

## 12. Accessibility Compliance (WCAG/EN 301 549)

### 12.1 Legal Framework

| Regulation | Scope | Deadline | Penalty |
|------------|-------|----------|---------|
| **Web Accessibility Directive** (EU 2016/2102) | Public sector | Already in force | Varies |
| **European Accessibility Act** (EU 2019/882) | Private sector (some) | June 28, 2025 | Varies |
| **Dutch Equal Treatment Act** | All websites serving Dutch public | Ongoing | Discrimination claims |

### 12.2 Recommended Standard: WCAG 2.1 Level AA

| Principle | Examples | Current Gaps |
|-----------|----------|--------------|
| **Perceivable** | Alt text, captions, contrast | Review all images |
| **Operable** | Keyboard navigation, no seizure risks | Test keyboard flow |
| **Understandable** | Clear language, predictable UI | Review navigation |
| **Robust** | Valid HTML, ARIA labels | Validate markup |

### 12.3 Quick Accessibility Audit Checklist

```
PERCEIVABLE
□ All images have descriptive alt text
□ Videos have captions (if applicable)
□ Color contrast meets 4.5:1 ratio for text
□ Text can be resized to 200% without loss
□ Content doesn't rely solely on color

OPERABLE  
□ All functionality available via keyboard
□ Focus indicators visible
□ No keyboard traps
□ Skip navigation link present
□ Page titles are descriptive
□ Links have descriptive text (not "click here")

UNDERSTANDABLE
□ Language declared in HTML (<html lang="nl">)
□ Forms have clear labels and error messages
□ Navigation is consistent across pages
□ Error messages explain how to fix issues

ROBUST
□ Valid HTML (passes W3C validator)
□ ARIA labels used correctly
□ Works with screen readers
□ Compatible with assistive technologies
```

### 12.4 Accessibility Statement Template

```markdown
# Toegankelijkheidsverklaring

**Laatst bijgewerkt:** [Datum]

## Onze toewijding

Inter Active Move B.V. streeft ernaar deze website toegankelijk te maken 
voor iedereen, inclusief mensen met een beperking.

## Standaard

Wij streven naar conformiteit met WCAG 2.1 niveau AA.

## Huidige status

[Beschrijf huidige status, bijv.:]
- De meeste pagina's voldoen aan WCAG 2.1 niveau AA
- Wij werken actief aan verbeteringen

## Bekende problemen

[Lijst van bekende toegankelijkheidsproblemen en planning voor oplossing]

## Feedback

Ervaart u problemen met de toegankelijkheid van onze website? 
Neem contact met ons op:

E-mail: toegankelijkheid@interactivemove.nl
Telefoon: +31 6 23 99 89 34

Wij streven ernaar binnen 5 werkdagen te reageren.

## Handhaving

Als u niet tevreden bent met onze reactie, kunt u contact opnemen met:
[Relevant authority, e.g., College voor de Rechten van de Mens]
```

### 12.5 Priority Accessibility Fixes

| Issue | Impact | Effort | Priority |
|-------|--------|--------|----------|
| Add `lang="nl"` to HTML | High | Very Low | 🔴 Critical |
| Add alt text to all images | High | Low | 🔴 Critical |
| Add skip navigation link | Medium | Low | 🟠 High |
| Ensure color contrast | Medium | Medium | 🟠 High |
| Add focus styles | Medium | Low | 🟠 High |
| Test keyboard navigation | High | Medium | 🟠 High |
| Validate HTML | Medium | Low | 🟡 Medium |
| Add ARIA landmarks | Medium | Medium | 🟡 Medium |

---

## 13. Dutch Consumer Law (B2B/B2C)

### 13.1 B2B vs B2C Considerations

IAM primarily serves B2B customers (schools, hospitals, businesses), but some rules still apply:

| Requirement | B2C | B2B | IAM Focus |
|-------------|-----|-----|-----------|
| Right of withdrawal (14 days) | ✅ Required | ❌ Not required | B2B only |
| Price transparency | ✅ Required | ⚠️ Good practice | Include in quotes |
| Pre-contractual information | ✅ Required | ⚠️ Good practice | Provide comprehensive info |
| Unfair terms protection | ✅ Strong | ⚠️ Limited | Review AV for fairness |

### 13.2 Price Display Requirements

For Dutch websites:

```
┌─────────────────────────────────────────────────────────────────┐
│ PRICE DISPLAY REQUIREMENTS                                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ B2C (if applicable):                                           │
│ • Show total price including VAT                               │
│ • Include all mandatory costs                                  │
│ • Don't hide fees until checkout                               │
│                                                                 │
│ B2B (IAM's case):                                              │
│ • Prices may be shown ex-VAT (common practice)                │
│ • Must clearly state "excl. BTW" or "ex. VAT"                 │
│ • Installation costs should be clearly communicated           │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 13.3 Recommended Price Display

```html
<!-- Product pricing display -->
<div class="price-display">
  <span class="price-amount">€ 12.500</span>
  <span class="price-note">excl. BTW</span>
</div>

<p class="price-includes">
  Inclusief: Hardware, 50 spellen, 2 jaar garantie<br>
  Exclusief: Installatie (vanaf € 500), verzendkosten
</p>
```

---

## 14. Implementation Checklist

### Phase 1: Critical (Week 1)

```
LEGAL PAGES
□ Create privacybeleid.html with full privacy policy
□ Create cookiebeleid.html with cookie information
□ Add privacy policy link to footer
□ Add cookie policy link to footer

COOKIE CONSENT
□ Implement cookie consent banner
□ Block non-essential cookies before consent
□ Add consent storage mechanism
□ Test consent flow

GOOGLE FONTS
□ Download Inter font files
□ Self-host fonts locally
□ Remove Google Fonts external reference
□ Test font rendering

FOOTER COMPLIANCE
□ Add KvK number
□ Add BTW number
□ Add full address
□ Add all legal page links
```

### Phase 2: High Priority (Week 2)

```
FORMS
□ Add privacy consent checkbox to contact form
□ Add privacy consent checkbox to quote form
□ Add consent checkbox to configurator form
□ Link to privacy policy from all forms
□ Implement consent logging

WHATSAPP
□ Add data processing notice near WhatsApp buttons
□ Document WhatsApp in privacy policy
□ Review Meta DPA

THIRD PARTIES
□ Self-host HTMX library
□ Verify web hosting location
□ Document all third-party services
□ Obtain/verify DPAs
```

### Phase 3: Important (Week 3-4)

```
TERMS & CONDITIONS
□ Draft algemene-voorwaarden.html
□ Legal review of terms
□ Add link to footer

ACCESSIBILITY
□ Add lang="nl" to HTML
□ Audit all images for alt text
□ Add skip navigation link
□ Test keyboard navigation
□ Check color contrast
□ Create toegankelijkheid.html

DOCUMENTATION
□ Create processing activities register
□ Document data retention periods
□ Create data subject request procedure
□ Document consent management
```

### Phase 4: Ongoing Maintenance

```
REGULAR TASKS
□ Review privacy policy annually
□ Update cookie list when adding new services
□ Respond to data subject requests within 30 days
□ Log all consent changes
□ Monitor regulatory updates
□ Conduct annual accessibility audit
```

---

## 15. Template Documents

### 15.1 Data Subject Request Response Template

```
Onderwerp: Reactie op uw verzoek inzake persoonsgegevens

Geachte [Naam],

Bedankt voor uw verzoek van [datum] betreffende [type verzoek: 
inzage/rectificatie/verwijdering/etc.].

[VOOR INZAGE:]
Bijgaand vindt u een overzicht van de persoonsgegevens die wij 
van u verwerken:

- Naam: [naam]
- E-mailadres: [email]
- [andere gegevens]

Verwerkingsdoelen: [doelen]
Bewaartermijn: [termijn]
Ontvangers: [ontvangers]

[VOOR VERWIJDERING:]
Wij bevestigen dat wij uw gegevens hebben verwijderd uit onze systemen.
Dit is effectief per [datum].

[VOOR RECTIFICATIE:]
Wij hebben de volgende gegevens aangepast:
- [oud] → [nieuw]

Heeft u nog vragen? Neem gerust contact met ons op.

Met vriendelijke groet,

[Naam]
Inter Active Move B.V.
privacy@interactivemove.nl
```

### 15.2 Data Breach Notification Template (AP)

```
MELDINGSFORMULIER DATALEK - AUTORITEIT PERSOONSGEGEVENS

1. CONTACTGEGEVENS MELDER
Organisatie: Inter Active Move B.V.
KvK: [nummer]
Contactpersoon: [naam]
Functie: [functie]
E-mail: [email]
Telefoon: [telefoon]

2. AARD VAN HET INCIDENT
Datum ontdekking: [datum]
Datum incident: [datum]
Type incident: [beschrijving]

3. BETROKKEN PERSOONSGEGEVENS
Categorieën: [bijv. naam, email, telefoon]
Aantal betrokkenen: [aantal]
Gevoelige gegevens: [ja/nee]

4. MOGELIJKE GEVOLGEN
[Beschrijving van mogelijke gevolgen voor betrokkenen]

5. GENOMEN MAATREGELEN
[Beschrijving van maatregelen om schade te beperken]

6. MELDING AAN BETROKKENEN
Betrokkenen geïnformeerd: [ja/nee]
Indien ja, datum: [datum]
Indien nee, reden: [reden]
```

### 15.3 Consent Log Template

```
CONSENT REGISTRATION LOG

Datum/Tijd: [ISO timestamp]
IP-adres: [geanonimiseerd indien nodig]
Pagina: [URL waar consent gegeven]
Consent Type: [privacy/cookies/marketing]
Consent Gegeven: [ja/nee]
Consent Tekst Versie: [versie nummer]
Cookie Banner Versie: [versie nummer]
User Agent: [browser info]
Methode: [checkbox/banner/etc.]
```

---

## 16. Appendix: Technical Implementation

### 16.1 Complete Cookie Consent Implementation (Klaro)

```html
<!-- Add to <head> -->
<link rel="stylesheet" href="/css/klaro.css">

<!-- Add before </body> -->
<script defer src="/js/klaro.js"></script>
<script>
var klaroConfig = {
    version: 1,
    elementID: 'klaro',
    storageMethod: 'localStorage',
    storageName: 'iam_consent',
    htmlTexts: true,
    cookieExpiresAfterDays: 365,
    privacyPolicy: '/privacybeleid.html',
    
    // Dutch translations
    translations: {
        nl: {
            consentModal: {
                title: 'Cookies & Privacy',
                description: 'Wij gebruiken cookies om uw ervaring te verbeteren. U kunt hieronder uw voorkeuren beheren.',
            },
            consentNotice: {
                description: 'Wij gebruiken cookies. {purposes}. {privacyPolicy}.',
                learnMore: 'Meer informatie',
                privacyPolicy: {
                    name: 'privacybeleid',
                    text: 'Lees ons {privacyPolicy}.'
                }
            },
            purposes: {
                necessary: {
                    title: 'Noodzakelijk',
                    description: 'Deze cookies zijn nodig voor de website.'
                },
                analytics: {
                    title: 'Analytisch', 
                    description: 'Deze cookies helpen ons de website te verbeteren.'
                },
                marketing: {
                    title: 'Marketing',
                    description: 'Deze cookies worden gebruikt voor advertenties.'
                }
            },
            ok: 'Alles accepteren',
            decline: 'Alles weigeren',
            save: 'Opslaan',
            acceptSelected: 'Selectie accepteren',
            close: 'Sluiten'
        }
    },
    
    // Define services/cookies
    services: [
        {
            name: 'functional',
            title: 'Functionele Cookies',
            purposes: ['necessary'],
            required: true,
            cookies: [
                ['lang', '/', 'interactivemove.nl'],
                ['iam_consent', '/', 'interactivemove.nl']
            ]
        },
        // Add analytics if using
        // {
        //     name: 'matomo',
        //     title: 'Matomo Analytics',
        //     purposes: ['analytics'],
        //     cookies: [
        //         ['_pk_id', '/', 'interactivemove.nl'],
        //         ['_pk_ses', '/', 'interactivemove.nl']
        //     ],
        //     callback: function(consent, service) {
        //         if (consent) {
        //             // Enable analytics
        //         }
        //     }
        // }
    ],
    
    // Must show both accept and decline equally
    mustConsent: false,
    acceptAll: true,
    hideDeclineAll: false,
    hideLearnMore: false
};
</script>
```

### 16.2 Privacy-Compliant Analytics Alternative

Instead of Google Analytics, consider privacy-friendly alternatives:

**Option 1: Matomo (Self-hosted)**
```html
<!-- Matomo - Privacy-friendly, self-hosted -->
<script>
  var _paq = window._paq = window._paq || [];
  // Require consent before tracking
  _paq.push(['requireConsent']);
  _paq.push(['trackPageView']);
  _paq.push(['enableLinkTracking']);
  (function() {
    var u="//[YOUR-MATOMO-URL]/";
    _paq.push(['setTrackerUrl', u+'matomo.php']);
    _paq.push(['setSiteId', '1']);
    var d=document, g=d.createElement('script'), s=d.getElementsByTagName('script')[0];
    g.async=true; g.src=u+'matomo.js'; s.parentNode.insertBefore(g,s);
  })();
</script>
```

**Option 2: Plausible (EU-hosted, no cookies)**
```html
<!-- Plausible - No cookies needed, EU-hosted -->
<script defer data-domain="interactivemove.nl" src="https://plausible.io/js/script.js"></script>
```

**Option 3: Simple Analytics (EU-based, no cookies)**
```html
<!-- Simple Analytics - No cookies, EU-based -->
<script async defer src="https://scripts.simpleanalyticscdn.com/latest.js"></script>
```

### 16.3 Contact Form with Consent Logging

```javascript
// form-handler.js
class GDPRForm {
  constructor(formElement) {
    this.form = formElement;
    this.init();
  }
  
  init() {
    this.form.addEventListener('submit', (e) => this.handleSubmit(e));
  }
  
  async handleSubmit(e) {
    e.preventDefault();
    
    const formData = new FormData(this.form);
    
    // Build consent record
    const consentRecord = {
      timestamp: new Date().toISOString(),
      form_id: this.form.id,
      page_url: window.location.href,
      privacy_consent: formData.get('privacy_consent') === 'on',
      marketing_consent: formData.get('marketing_consent') === 'on',
      privacy_policy_version: '1.0', // Update when policy changes
      consent_text: this.form.querySelector('label[for="privacy-consent"]').textContent.trim()
    };
    
    // Add consent record to form data
    formData.append('consent_record', JSON.stringify(consentRecord));
    
    try {
      const response = await fetch(this.form.action, {
        method: 'POST',
        body: formData
      });
      
      if (response.ok) {
        this.showSuccess();
      } else {
        this.showError();
      }
    } catch (error) {
      console.error('Form submission error:', error);
      this.showError();
    }
  }
  
  showSuccess() {
    this.form.innerHTML = `
      <div class="form-success">
        <h3>Bedankt voor uw bericht!</h3>
        <p>Wij nemen zo spoedig mogelijk contact met u op.</p>
      </div>
    `;
  }
  
  showError() {
    alert('Er is een fout opgetreden. Probeer het later opnieuw.');
  }
}

// Initialize all GDPR forms
document.querySelectorAll('form[data-gdpr]').forEach(form => {
  new GDPRForm(form);
});
```

### 16.4 Language Attribute Fix

```html
<!-- index.html and all pages -->
<!DOCTYPE html>
<html lang="nl">
<head>
  <!-- For English partial pages -->
  <!-- When loading English content, update lang attribute -->
</head>
```

```javascript
// Add to language switcher
function switchLanguage(lang) {
  document.documentElement.lang = lang;
  // ... rest of language switching logic
}
```

### 16.5 Complete File Structure for Legal Pages

```
iam-website/
├── index.html
├── privacybeleid.html          ← NEW (Privacy Policy)
├── cookiebeleid.html           ← NEW (Cookie Policy)  
├── algemene-voorwaarden.html   ← NEW (Terms & Conditions)
├── toegankelijkheid.html       ← NEW (Accessibility Statement)
├── partials/
│   ├── privacybeleid-nl.html   ← NEW (Dutch privacy partial)
│   ├── privacybeleid-en.html   ← NEW (English privacy partial)
│   ├── cookiebeleid-nl.html    ← NEW
│   ├── cookiebeleid-en.html    ← NEW
│   └── ...
├── js/
│   ├── klaro.js                ← NEW (Cookie consent)
│   ├── htmx.min.js             ← NEW (Self-hosted HTMX)
│   └── form-handler.js         ← NEW (GDPR forms)
├── css/
│   ├── klaro.css               ← NEW (Cookie banner styles)
│   └── ...
├── media/
│   └── fonts/                  ← NEW (Self-hosted fonts)
│       ├── Inter-Regular.woff2
│       ├── Inter-Medium.woff2
│       ├── Inter-SemiBold.woff2
│       └── Inter-Bold.woff2
└── ...
```

---

## Summary & Compliance Roadmap

### Immediate Actions (This Week)

| Priority | Task | Responsible | Deadline |
|----------|------|-------------|----------|
| 🔴 | Create Privacy Policy | Legal/Marketing | Day 1-2 |
| 🔴 | Implement cookie consent | Developer | Day 2-3 |
| 🔴 | Self-host Google Fonts | Developer | Day 1 |
| 🔴 | Add legal info to footer | Developer | Day 1 |
| 🔴 | Add form consent checkboxes | Developer | Day 2 |

### Short-Term (2-4 Weeks)

| Priority | Task | Responsible | Deadline |
|----------|------|-------------|----------|
| 🟠 | Create Cookie Policy | Legal/Marketing | Week 2 |
| 🟠 | Create Terms & Conditions | Legal | Week 2-3 |
| 🟠 | Document all processing activities | Compliance | Week 3 |
| 🟠 | Implement accessibility fixes | Developer | Week 3-4 |
| 🟠 | Create Accessibility Statement | Compliance | Week 4 |

### Ongoing Maintenance

| Task | Frequency | Responsible |
|------|-----------|-------------|
| Review privacy policy | Annually | Legal |
| Audit cookies/tracking | Quarterly | Developer |
| Respond to data requests | Within 30 days | Compliance |
| Accessibility audit | Annually | External/Developer |
| Staff training | Annually | Management |

---

## Disclaimer

This report provides general guidance based on publicly available information about the InterActiveMove website. It is not legal advice. We recommend consulting with a qualified Dutch privacy lawyer or data protection consultant before implementation, particularly for:

- Final privacy policy and terms wording
- Complex data processing activities
- International data transfers
- Data Protection Impact Assessments (if required)

---

*Document prepared by Privacy & Compliance Consultant*  
*Version 1.0 — January 2026*

---

## Quick Reference Card

```
┌─────────────────────────────────────────────────────────────────┐
│ IAM GDPR QUICK REFERENCE                                        │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│ DATA SUBJECT REQUESTS                                           │
│ • Respond within: 30 days                                      │
│ • Email: privacy@interactivemove.nl                            │
│ • Can extend by: 2 months (complex requests)                   │
│                                                                 │
│ DATA BREACH                                                     │
│ • Report to AP within: 72 hours                                │
│ • AP website: autoriteitpersoonsgegevens.nl                    │
│ • Notify individuals if: high risk to rights                   │
│                                                                 │
│ CONSENT                                                         │
│ • Must be: Freely given, specific, informed, unambiguous       │
│ • Withdrawal: Must be as easy as giving consent               │
│ • Children: 16+ in Netherlands                                 │
│                                                                 │
│ RETENTION PERIODS                                               │
│ • Contact forms: 2 years after last contact                    │
│ • Invoices/contracts: 7 years (fiscal)                         │
│ • Analytics: Max 26 months                                     │
│ • Marketing consent: Until withdrawn                           │
│                                                                 │
│ KEY CONTACTS                                                    │
│ • AP: +31 70 888 8500                                          │
│ • ACM: +31 70 722 2000                                         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```
# Stitch 2.0 prompt – Kestrel marketing site

Paste the **master prompt** first to establish the design system on the canvas, then generate the pages one at a time with the per-page prompts so every screen inherits the same design language. Use text input, not voice – this brief is precision work.

---

## Master prompt (paste first)

Design a marketing website for **Kestrel**, a fictional self-hosted network monitoring tool for homelab enthusiasts. Kestrel watches your LAN, pings your services, and sends you a push notification before your family notices the Wi-Fi is down. The site is a landing page plus five sub-pages: Features, Pricing, Docs, About, and Contact.

**Design system – apply to every screen:**
- **Look:** modern, clean, confident. Generous whitespace, large type, soft depth. No skeuomorphism, no glassmorphism, no stock photos of people pointing at laptops.
- **Colors:** near-black background `#0B0E14`, off-white text `#E8EAF0`, primary accent teal `#2DD4BF` for CTAs and links, secondary accent amber `#F59E0B` used sparingly for status highlights, card surfaces `#151A23` with a 1px border of `#232A36`.
- **Typography:** a geometric sans for headings (Space Grotesk or similar), a humanist sans for body (Inter or similar), monospace (JetBrains Mono or similar) for code snippets and stats. Base size 18px, line height 1.6, headings tight at 1.1.
- **Layout:** max content width 1200px, 12-column grid, 8px spacing scale. Sticky top nav with logo left, five links center, one teal "Download" button right. Footer with four link columns and a newsletter field.
- **Components:** pill-shaped primary buttons, ghost secondary buttons, cards with 12px radius and subtle hover lift, a thin teal top-border accent on active nav items.
- **Imagery:** abstract line-art illustrations of network topology (nodes and edges), simple dashboard mockups in dark UI, no photography.

**Technical constraints (carry into code export):**
- Semantic HTML5 (`header`, `nav`, `main`, `section`, `article`, `footer`), one `h1` per page.
- Plain CSS with custom properties for the palette and spacing scale – no Tailwind, no frameworks.
- **JavaScript only where HTML and CSS cannot do the job.** Use `<details>`/`<summary>` for the FAQ accordion, `scroll-behavior: smooth` for anchor scrolling, CSS-only hover and focus states. The single permitted script is the mobile hamburger nav toggle.
- Fully responsive at 375px, 768px, and 1280px breakpoints. Visible focus outlines, WCAG AA contrast throughout.

---

## Landing page (generate first)

Generate the **landing page** first: hero with headline "Know your network before it knows you're gone", one-line subhead, teal primary CTA ("Download free") and ghost secondary CTA ("Read the docs"), a dashboard mockup below the fold, a three-column feature teaser row, a stats band (uptime checks/day, average alert latency, self-hosted installs) in monospace, one testimonial card, and a closing CTA section above the footer.

---

## Features page

Generate the **Features page**: compact hero with headline "Everything on your network, watched." and one-line subhead. A six-card feature grid (two rows of three); each card has a line-art icon, a title, a one-line description, and a monospace stat. Features: automatic LAN device discovery, per-service ping checks, push notifications before outages spread, 30-day uptime history, and fully self-hosted — your data never leaves your network. Below the grid, a three-step "how an alert works" band (Detect → Notify → Resolve) with numbered steps. Then a dashboard mockup section in dark UI. Close with the standard closing CTA section above the footer.

---

## Pricing page

Generate the **Pricing page**: headline "Simple pricing for home labs of every size." with one-line subhead. Three pricing cards: Hobby (Free — 25 devices, 1-minute checks, community support), Pro ($8/month — 200 devices, 15-second checks, push notifications, 90-day history), Team ($24/month — unlimited devices, 5-second checks, multi-user, API access). Highlight the middle card with a teal border and a "Most popular" pill. Below, an FAQ accordion built with `<details>`/`<summary>` (five questions: is the free tier really free, does Kestrel phone home, which platforms are supported, can I migrate from another monitor, how do push notifications work). Close with the standard closing CTA section above the footer.

---

## Docs page

Generate the **Docs page**: two-column layout with a sticky left sidebar nav (Getting started, Installation, Configuration, Alerts, FAQ) and a main content column. Content: installation via a single Docker command in a monospace code block, a configuration table (check interval, timeout, notification channels), and callout boxes for notes and warnings. Sidebar anchor links scroll with `scroll-behavior: smooth`. Code snippets in JetBrains Mono on card-surface backgrounds. Close with the standard closing CTA section above the footer.

---

## About page

Generate the **About page**: headline "Built by a homelabber, for homelabbers." A story section in two columns — text on the left (why Kestrel exists: tired of learning the Wi-Fi was down from family members), line-art illustration on the right. A three-card principles row: self-hosted first, no tracking ever, boring technology that just works. A monospace tech strip (single binary, SQLite, ~15MB Docker image). One testimonial card. Close with the standard closing CTA section above the footer.

---

## Contact page

Generate the **Contact page**: headline "Talk to a human (who also runs a homelab)." A contact form with native HTML validation — name, email, topic select (Support, Feature request, Press, Other), and a message textarea — with a teal pill submit button. Beside the form, three contact cards: email (hello@kestrel.example), community chat, and GitHub issues. Below, a two-question FAQ teaser linking to the docs. Close with the standard closing CTA section above the footer.

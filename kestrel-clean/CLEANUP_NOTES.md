# Cleanup pass — Kestrel site (Stitch 2.0 export)

Date: 2026-09-29. Source: `stitch_kestrel_network_monitor_site.zip` (Stitch project "Kestrel Network Monitor Site").
Spec: Fable's master brief (`../stitch-prompt.md`) + Stitch's own `DESIGN.md` (copied here).

## Canonical pages chosen
Stitch exported two generations per page (`_1` drafts auto-built from the master prompt, `_2` per-page-prompt regens).
Kept the `_2` regens throughout. Exception: docs — `_3` (the accidental duplicate regen) matches the brief's
sidebar spec (Getting started, Installation, Configuration, Alerts, FAQ) while `_2` only had 3 of 5 items.

## Checked — already fine (Stitch 2.0 did NOT repeat the article's failures)
- Mobile nav: hamburger button + dropdown + working toggle script present on all 6 pages (the article's missing-hamburger bug did not occur).
- Inline styles: 0 across all pages (article reported 246).
- Contrast: all 8 key pairs pass WCAG AA — lowest is muted text #94A3B8 on card #151A23 at 6.80:1; body 16.06:1, teal accents 10.38:1.
- One `<h1>` per page; semantic header/nav/main/section/footer throughout.
- Pricing FAQ uses native `<details>`/`<summary>`; contact form uses native `required` validation, no `novalidate`.

## Fixed in this pass
1. **Global `:focus-visible` ring** added to all 6 pages (was entirely absent): 2px solid #2DD4BF, 3px offset.
2. **`aria-expanded`** on the mobile toggle: initialized `false` on the button, toggled by the existing script (same single permitted script, extended, not a new one).
3. **Nav rewired to real pages.** The landing page's nav used `#anchors`; all five sub-pages' navs were dead `href="#"` placeholders. Header, mobile, and footer navs now point at `index/features/pricing/docs/about/contact.html`; logo links to `index.html`.
4. **Pricing FAQ rewritten**: Stitch's 4 questions had drifted off-brief (donations, supporter subscriptions). Replaced with the brief's 5: free tier, phone-home, platforms, migration, push notifications — same `<details>` styling.

## Flagged — intentionally NOT fixed
- **Tailwind CDN.** The brief demands plain CSS, no frameworks; Stitch shipped `cdn.tailwindcss.com` with ~800–1300 utility tokens per page. Removing it is a full rewrite of ~250KB of HTML, not a cleanup task. Say the word and it's a separate job.
- **Extra scripts beyond the single permitted one**: pricing billing-period toggle, docs install-tab switcher + copy-snippet, contact fake-submit animation + PGP copy button. All functional; all violate "JavaScript only where HTML and CSS cannot do the job."
- **Logo hotlink**: `lh3.googleusercontent.com/aida/...` — unreachable/fragile. Replace with a local asset before any real deploy.
- **Footer link columns** still point at `"#"` placeholders; "Download" CTAs point at `#downloads`, which exists on no page.

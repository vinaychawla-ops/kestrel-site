# Kestrel — Claude → Stitch → Code Pipeline

An end-to-end run of the website pipeline from the XDA article
["I built a website with Claude Code and Stitch 2.0"](https://www.xda-developers.com/built-website-claude-code-and-stitch-2-understand-why-developers-are-switching/)
(Sep 28, 2026): design brief drafted with Claude, site generated with Google Stitch,
cleaned up by hand, deployed to Modal.

The demo product is **Kestrel**, a fictional passive homelab network monitor —
landing page plus five sub-pages, dark "mission control" aesthetic.

## Pipeline

1. **Brief** — `stitch-prompt.md`: master design brief plus six per-page prompts.
   The master brief and landing-page prompt were transcribed from the article's
   screenshots (`fable-prompt.jpg` is the screenshot of Fable's response); the
   Features / Pricing / Docs / About / Contact prompts were drafted in the same
   style, since the article only showed the first two.
2. **Generate** — Google Stitch produced all six pages
   ([Stitch project](https://stitch.withgoogle.com/projects/9158354424930560977)).
3. **Clean** — `kestrel-clean/` is the export after a manual cleanup pass
   (details in `kestrel-clean/CLEANUP_NOTES.md`).
4. **Deploy** — `modal_app.py` serves the cleaned site on Modal:
   https://chawlavinay--kestrel-site-web.modal.run

## What Stitch got right (vs. the article)

The article's build suffered two headline failures — broken mobile navigation and
inline styles everywhere. This run had **neither**: every page shipped a working
hamburger menu, there were zero `style=""` attributes, every page had exactly one
`<h1>`, and all measured color pairs passed WCAG AA (lowest 6.80:1).

## What the cleanup actually fixed

- Added a global teal `:focus-visible` ring (keyboard users had no visible focus)
- Added/updated `aria-expanded` on every mobile-menu toggle
- Rewired dead sub-page nav links to the real pages
  (`index/features/pricing/docs/about/contact.html`)
- Rewrote Stitch's drifted 4-question Pricing FAQ back to the brief's 5 topics
  (free tier, phone-home behavior, supported platforms, migration, push notifications)

## Known limitations (deliberately left as-is)

- Every page loads `cdn.tailwindcss.com` — the brief says "plain CSS, no
  frameworks". Removing Tailwind is a full rewrite, not a cleanup.
- Extra JavaScript beyond the brief's single permitted script (pricing billing
  toggle, docs tabs/copy, contact fake-submit + PGP copy).
- The logo is a fragile `lh3.googleusercontent.com` hotlink — replace with a
  local asset before any real deployment.
- The contact form is a visual demo (no real message delivery); some footer
  links are placeholders and "Download" CTAs point to `#downloads`.

## Run locally

```bash
cd kestrel-clean && python3 -m http.server 8000
```

## Deploy to Modal

```bash
modal deploy modal_app.py
```

Serves `kestrel-clean/` as a static site via FastAPI `StaticFiles`
(`html=True`, so `/` resolves to `index.html`). Files are baked into the image
with `copy=True` so redeploys can never serve stale code.

## Repo contents

| Path | What it is |
|---|---|
| `kestrel-clean/` | The six cleaned pages + Stitch's `DESIGN.md` + `CLEANUP_NOTES.md` |
| `stitch-prompt.md` | Master brief + all six per-page Stitch prompts |
| `fable-prompt.jpg` | Screenshot of the original Fable response (brief provenance) |
| `modal_app.py` | Modal deploy script (static file server) |
| `README.md` | This file |
| `AGENTS.md` | Notes for agents working in this repo |

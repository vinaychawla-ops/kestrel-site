---
name: Obsidian Telemetry
colors:
  surface: '#10131a'
  surface-dim: '#10131a'
  surface-bright: '#363940'
  surface-container-lowest: '#0b0e14'
  surface-container-low: '#191c22'
  surface-container: '#1d2026'
  surface-container-high: '#272a31'
  surface-container-highest: '#32353c'
  on-surface: '#e1e2eb'
  on-surface-variant: '#bacac5'
  inverse-surface: '#e1e2eb'
  inverse-on-surface: '#2e3037'
  outline: '#859490'
  outline-variant: '#3c4a46'
  surface-tint: '#3cddc7'
  primary: '#57f1db'
  on-primary: '#003731'
  primary-container: '#2dd4bf'
  on-primary-container: '#00574d'
  inverse-primary: '#006b5f'
  secondary: '#ffb95f'
  on-secondary: '#472a00'
  secondary-container: '#ee9800'
  on-secondary-container: '#5b3800'
  tertiary: '#66f3b6'
  on-tertiary: '#003824'
  tertiary-container: '#44d69b'
  on-tertiary-container: '#00593b'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#62fae3'
  primary-fixed-dim: '#3cddc7'
  on-primary-fixed: '#00201c'
  on-primary-fixed-variant: '#005047'
  secondary-fixed: '#ffddb8'
  secondary-fixed-dim: '#ffb95f'
  on-secondary-fixed: '#2a1700'
  on-secondary-fixed-variant: '#653e00'
  tertiary-fixed: '#6ffbbe'
  tertiary-fixed-dim: '#4edea3'
  on-tertiary-fixed: '#002113'
  on-tertiary-fixed-variant: '#005236'
  background: '#10131a'
  on-background: '#e1e2eb'
  surface-variant: '#32353c'
typography:
  headline-xl:
    fontFamily: Space Grotesk
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 52px
    letterSpacing: -0.03em
  headline-xl-mobile:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Space Grotesk
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Space Grotesk
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.015em
  headline-sm:
    fontFamily: Space Grotesk
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: -0.01em
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28.8px
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 25.6px
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 21px
    letterSpacing: '0'
  code-lg:
    fontFamily: JetBrains Mono
    fontSize: 16px
    fontWeight: '500'
    lineHeight: 24px
    letterSpacing: -0.02em
  code-md:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: -0.02em
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: '0'
  label-md:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: JetBrains Mono
    fontSize: 10px
    fontWeight: '600'
    lineHeight: 14px
    letterSpacing: 0.08em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 2rem
  margin-mobile: 1rem
  space-xs: 0.5rem
  space-sm: 0.75rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
  space-2xl: 3rem
---

## Brand & Style

This design system establishes a high-precision, technical aesthetic tailored for infrastructure administrators, self-hosters, and homelab engineers. The visual atmosphere balances industrial utility with refined modernism: deep, light-absorbent backdrops contrast with luminous telemetry nodes and status indicators.

The design movement combines **Minimalism** with **Technical Precision**:
- High data density without visual friction.
- Tactile, mechanical rhythm driven by monospace data visualization, subtle grid overlays, and vector topology schematics.
- Unapologetic dark mode architecture built to alleviate eye strain during low-light network monitoring operations.
- Direct, functional, and authoritative tone: typography sits tight and crisp, conveying diagnostic reliability and enterprise-grade speed in a local environment.

## Colors

The palette operates on calibrated contrast tiers designed for absolute clarity across dark displays:

- **Canvas & Background (`#0B0E14`):** A near-black baseline that absorbs ambient glow and anchors the interface.
- **Card Surface (`#151A23`):** Elevated structure tier providing distinct separation from the canvas, bounded by a structural outline (`#232A36`).
- **Surface Hover (`#1C2330`):** Interactive lift state for cards, tables, and rows.
- **Primary Teal (`#2DD4BF`):** Reserved for primary interactive controls, operational health indicators, key metrics, and selected states.
- **Secondary Amber (`#F59E0B`):** Dedicated to degradation warnings, threshold triggers, high latency flags, and diagnostic alerts.
- **System Emerald (`#10B981`):** Optimal ping and peer-connected indicators.
- **System Rose (`#F43F5E`):** Downed interfaces, packet loss dropouts, and fatal error nodes.
- **Text Primary (`#E8EAF0`):** Clean off-white providing high contrast readability without glare.
- **Text Secondary / Muted (`#94A3B8`):** Steel slate for metadata, axis scales, inactive states, and hardware signatures.

## Typography

The typographic hierarchy implements three distinct roles:
1. **Space Grotesk (Headings):** Engineered, mechanical grotesque cut with an intentional 1.1 line-height factor for titles and high-level card metric titles. Delivers immediate structural presence.
2. **Inter (Body & Content):** Tuned for sustained reading at 18px base (`body-lg`) with an expansive 1.6 line height ratio (`28.8px`), balancing dense infrastructure information with spatial clarity.
3. **JetBrains Mono (Data & Telemetry):** Strictly utilized for all numerical readouts, IP/MAC addresses, latency statistics, bandwidth rates, CLI code blocks, and micro-metric badges. Tabular figures ensure clean vertical alignment across diagnostic tables and graphs.

## Layout & Spacing

The layout is anchored around a fixed-fluid maximum container width of **1200px** centered horizontally within the viewport. Spacing operates strictly on an 8-point base module (8px / 16px / 24px / 32px / 48px).

### Breakpoints & Adaptability
- **Desktop (≥1280px):** 12-column layout, 24px gutters, fixed max-width 1200px. Complex topology graphs and side-by-side terminal telemetry views remain fully expanded.
- **Tablet (768px – 1279px):** 8-column layout, 24px gutters, flexible 32px outer canvas margins. Multi-metric summary cards collapse from 4-up to 2-up grids.
- **Mobile (≤767px, baseline 375px):** 4-column layout, 16px gutters, 16px outer margins. Topology canvases convert into stacked network interface lists. Stat readouts switch to horizontal key-value pairs.

## Elevation & Depth

Visual hierarchy uses low-contrast outlines and tonal layering instead of dramatic drop shadows, maintaining an authentic command-line feel.

- **Base Layer:** Background `#0B0E14` acts as zero-elevation canvas.
- **Surface Layer (Cards, Panels):** Solid `#151A23` elevated purely through a hairline 1px border of `#232A36`. No heavy ambient shadows; clean, edge-defined architecture.
- **Interactive Hover Layer:** Surfaces transition to `#1C2330` with the 1px border brightening to `#2DD4BF` at 30% opacity (`rgba(45, 212, 191, 0.3)`), creating a sharp instrument-like glow.
- **Overlays & Modals:** Elevated to `#1A202C` with a 1px border `#334155` and a subtle directional shadow (`0 20px 25px -5px rgba(0, 0, 0, 0.6), 0 8px 10px -6px rgba(0, 0, 0, 0.6)`).
- **Network Topography Overlays:** Vector line-art and node diagrams sit directly on the card background with connection paths drawn in `#232A36`, activating into `#2DD4BF` or `#F59E0B` when telemetry is routed.

## Shapes

The design system incorporates geometric contrast: structural card frames use standard containment radii, while actionable triggers and diagnostic badges adopt high-radius pill styling.

- **Cards & Data Panels:** Exactly `12px` border radius (`rounded-lg`), producing clean enclosures that do not distract from analytical data grids.
- **Interactive Buttons & Badges:** `9999px` full pill shapes, providing an ergonomic, tactile contrast against the sharp borders of the surrounding dashboards.
- **Inputs & Dropdowns:** `8px` corner radius, aligning functionally with nested form groupings.
- **Status Dots & Pulse Indicators:** Strict circles (`50%`), often paired with an outer breathing ring for live telemetry pings.

## Components

### Buttons
- **Primary:** Pill-shaped (`border-radius: 9999px`). Background `#2DD4BF`, text `#0B0E14`, font `Inter` 14px bold. On hover, background shifts to `#5EEAD4` with a subtle teal glow (`0 0 16px rgba(45, 212, 191, 0.4)`).
- **Secondary / Outline:** Pill-shaped. Background transparent, 1px solid border `#232A36`, text `#E8EAF0`. On hover, background fills to `#1C2330` with border `#94A3B8`.
- **Destructive:** Pill-shaped. Background transparent, 1px solid border `#F43F5E`, text `#F43F5E`. On hover, fills `#F43F5E` with text `#0B0E14`.

### Cards & Panels
- Background `#151A23`, border `1px solid #232A36`, border-radius `12px`, internal padding `24px` (`space-lg`).
- Header includes a `Space Grotesk` title (18px), a node count or status badge on the right, and an optional hairline divider (`1px solid #232A36`) separating content.

### Telemetry Chips & Status Badges
- Pill-shaped badges, height `24px`, padding `0 10px`. Font `JetBrains Mono` 11px uppercase (`label-sm`).
- **Nominal:** Background `rgba(45, 212, 191, 0.1)`, text `#2DD4BF`, border `1px solid rgba(45, 212, 191, 0.25)`.
- **Degraded / High Latency:** Background `rgba(245, 158, 11, 0.1)`, text `#F59E0B`, border `1px solid rgba(245, 158, 11, 0.25)`.
- **Critical / Offline:** Background `rgba(244, 63, 94, 0.1)`, text `#F43F5E`, border `1px solid rgba(244, 63, 94, 0.25)`.

### Input Fields & Controls
- Background `#0B0E14`, border `1px solid #232A36`, border-radius `8px`, height `42px`, padding `0 14px`. Text `#E8EAF0`, font `JetBrains Mono` 14px. Focus state shifts border to `#2DD4BF` without outline offset.
- Checkboxes: 16x16px squares with `4px` radius, border `#232A36`, background `#0B0E14`. Checked state fills `#2DD4BF` with `#0B0E14` checkmark icon.

### Network Topology & Telemetry Visualizations
- Vector diagrams drawn with 1.5px paths in `#232A36`.
- Live connection links animate via CSS stroke-dashoffset using `#2DD4BF` for normal traffic flow and `#F59E0B` for constrained interfaces.
- Host machine nodes render as nested `#151A23` pill containers with Monospace IP headers.
# Design — Bitcoin FilmFest

A locked design system for the Jekyll rebuild. Every page reads this file before design changes. Extend this system when a new component is needed; do not invent a new visual language per route.

## Genre

Atmospheric editorial — a film-festival site viewed through a physical cinema screen. Playful details come from the real BFF rabbit and aperture mark, not generic cards or decorative UI.

## Audience and use

- Filmgoers discover the next edition and move between years.
- Filmmakers and contributors find participation paths.
- Press and partners find official information and credits.
- Returning community members reach stories, newsletters, and archives.

The primary action on the homepage is to enter an edition; the secondary action is to stay on set via e-mail or npub.

## Macrostructure family

- Marketing/home pages: **Marquee Hero / cinema poster** — blue screen, rabbit-led asymmetric composition, edition listings as showtimes rather than cards.
- Edition pages: **Programme board** — date/place masthead, films/events in typographic rows, restrained imagery.
- Content/newsletter pages: **Long Document** — warm paper screen, readable measure, no decorative section cards.
- Utility/index pages: **Index-first** — categorized route or credit lists, visible status, minimal containment.

## Theme

- Room: near-black `oklch(7% 0.005 245)`.
- Screen blue: BFF blue `oklch(62.777% 0.15202 243.075)`.
- Paper: warm cinema paper `oklch(95.472% 0.02182 92.508)`.
- Ink: blue-tinted charcoal `oklch(20.394% 0.00253 247.951)`.
- Accent: projector amber `oklch(77.499% 0.16885 65.777)`.
- Focus: warm gold `oklch(74.082% 0.13117 82.062)`.

The blue may fill the homepage screen because it is a brand surface, not a generic UI accent. On content pages, blue returns to links, active states, and small anchors.

## Typography

- Display: Syne Mono, weight 400, upright.
- Body: Courier Prime, weights 400 and 700.
- Logo: real BFF image assets, never recreated as styled text.
- Headings are upright, compact, and may be uppercase when inherited from the BFF festival language.
- Body measure: 45–70 characters.
- Maximum families: two.

## Spacing

A 4-point named scale lives in `tokens.css`. Components use named tokens or fluid clamps built from them; no ad-hoc spacing values.

## Cinema screen

- The viewport has a near-black room frame on all sides.
- A fixed inner bezel/shadow gives the screen depth without a grey page tail.
- The screen edge is defined only by a soft bezel shadow. Do not add a perforation pattern.
- Cinema seats stay fixed to the true bottom edge.
- The shared footer always closes on the room black and includes enough bottom padding for the seats.

## Navigation

- The BFF image logo is the canonical home link.
- Desktop editions open on hover and `:focus-within`; keyboard and touch use a native disclosure.
- Mobile uses a real menu button and panel; no hover-only paths.
- The current page or current group is visibly marked in blue and with an underline/marker.
- Navigation data lives in `_data/navigation.yml`; markup lives in `_includes/nav.html`.

## Footer

One shared colophon footer from `_includes/footer.html` appears on every route. It contains the BFF mark, festival statement, subscription form, compact labelled social icons, and copyright. It is a lifted charcoal canvas inside the outer dark room frame; do not repeat primary navigation there.

## Motion

- Enter: `cubic-bezier(0.16, 1, 0.3, 1)`.
- Exit: `cubic-bezier(0.7, 0, 0.84, 0)`.
- State: `cubic-bezier(0.65, 0, 0.35, 1)`.
- One short hero entrance; body text does not continually animate on scroll.
- Same-origin page links use progressive-enhancement document swapping and the View Transitions API when available.
- Reduced motion becomes an opacity-only change of at most 150ms.

## CTA and interaction voice

- Primary links look like programme/showtime rows or underlined text, not generic rounded cards.
- Buttons are square or lightly clipped, matching tickets and projector labels.
- Hover uses one signal only: underline, colour, or a 1px translation.
- Focus rings appear immediately and meet contrast requirements.

## Per-page allowances

- Homepage and edition pages may use real rabbit, aperture, poster, and festival photography assets.
- Content pages prioritize reading and use imagery only when the article supplies it.
- Utility pages are typographic and list-led.

## What every page must share

- Logo home control, navigation, screen bezel, top pattern, cinema seats, and footer.
- Brand palette, type pairing, spacing scale, focus style, and active-page behavior.
- Black final screen after the footer.

## What pages may vary

- Screen surface: blue for home/editions, warm paper for reading pages.
- Internal composition within the approved macrostructure family.
- Real edition imagery and content-specific media.

## Modularity and future backend

- `_data/navigation.yml` controls navigation structure.
- `_data/sitemap.json` is a builder-only route inventory. It must not be rendered or linked publicly.
- `_includes/` owns shared shell components.
- `tokens.css` owns design tokens.
- `assets/css/cinema-frame.css` owns component/layout rules.
- `assets/js/main.js` owns navigation, active states, and progressive page transitions.
- `assets/js/subscribe.js` owns the current subscribe adapter and can later be replaced with a backend client without changing page markup.

## Exports

### tokens.css

The canonical CSS export is the project-root `tokens.css` file.

### Tailwind v4 mapping

```css
@theme {
  --color-room: oklch(7% 0.005 245);
  --color-screen: oklch(62.777% 0.15202 243.075);
  --color-paper: oklch(95.472% 0.02182 92.508);
  --color-ink: oklch(20.394% 0.00253 247.951);
  --color-accent: oklch(77.499% 0.16885 65.777);
  --font-display: "Syne Mono", monospace;
  --font-body: "Courier Prime", monospace;
  --ease-out: cubic-bezier(0.16, 1, 0.3, 1);
}
```

### DTCG core mapping

```json
{
  "color": {
    "room": { "$value": "oklch(7% 0.005 245)", "$type": "color" },
    "screen": { "$value": "oklch(62.777% 0.15202 243.075)", "$type": "color" },
    "paper": { "$value": "oklch(95.472% 0.02182 92.508)", "$type": "color" },
    "ink": { "$value": "oklch(20.394% 0.00253 247.951)", "$type": "color" },
    "accent": { "$value": "oklch(77.499% 0.16885 65.777)", "$type": "color" }
  },
  "font": {
    "display": { "$value": "Syne Mono", "$type": "fontFamily" },
    "body": { "$value": "Courier Prime", "$type": "fontFamily" }
  }
}
```

### shadcn/ui core mapping

```css
:root {
  --background: 95.472% 0.02182 92.508;
  --foreground: 20.394% 0.00253 247.951;
  --primary: 62.777% 0.15202 243.075;
  --primary-foreground: 95.472% 0.02182 92.508;
  --muted: 91.984% 0.02798 88.756;
  --muted-foreground: 47.097% 0.00344 264.528;
  --border: 82% 0.012 92;
  --input: 82% 0.012 92;
  --ring: 74.082% 0.13117 82.062;
  --radius: 0.25rem;
}
```

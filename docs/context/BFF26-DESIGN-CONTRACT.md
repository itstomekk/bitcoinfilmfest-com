# BFF'26 design contract

This contract freezes the markup vocabulary and visual behavior for the BFF'26 Jekyll page. The content worker and CSS worker must use the same names and boundaries. It extends the existing cinema-frame system; it does not create a second design system.

## 1. Page boundary and shared shell

The page is a normal Jekyll page with the shared default layout:

```yaml
---
layout: default
permalink: /26/
screen: blue
---
```

The page body starts and ends inside the shared layout content slot. It must not contain `<html>`, `<head>`, `<body>`, a second navigation, a second footer, cinema seats, a reset, a page-wide font declaration, or standalone scripts. The layout already owns the screen bezel, cinema atmosphere, fixed seats, footer, route status, navigation scripts, font links, metadata includes, and global CSS.

The page root is:

```html
<article class="edition-page edition-page--bff26">
  ...
</article>
```

Use the existing shared `stage--blue`, `.screen-canvas`, `.inner`, `.edition-page`, `.edition-masthead`, `.edition-actions`, `.showtime`, `.cinema-index`, `.cinema-stat`, `.cinema-section-nav`, and focus rules where they fit. BFF'26 selectors are namespaced with `bff26-` so the CSS addition cannot leak into other editions.

The page is a post-festival BFF'26 page. It keeps the wrap, recap, public testimonials, practical Warsaw information, and BFF'27 next-edition action. It is not shortened to an archive index.

## 2. Canonical section skeleton

The order below is the contract. Section IDs preserve old public anchors where they remain useful. The `tickets` anchor may remain as a compatibility alias on the recap section, but no stale ticket-selling copy may be presented as current.

```html
<article class="edition-page edition-page--bff26">
  <header class="bff26-hero" id="hero">
    <div class="bff26-hero-copy">...</div>
    <figure class="bff26-hero-art">...</figure>
    <div class="bff26-hero-cta">...</div>
  </header>

  <nav class="bff26-jumpnav" aria-label="BFF'26 page sections">
    <ul>...</ul>
  </nav>

  <section class="bff26-band bff26-band--agenda" id="agenda" aria-labelledby="bff26-agenda-title">
    <header class="bff26-section-heading">...</header>
    <div class="bff26-agenda">...</div>
  </section>

  <section class="bff26-band bff26-band--recap" id="recap" aria-labelledby="bff26-recap-title">
    <header class="bff26-section-heading">...</header>
    <div class="bff26-recap">...</div>
  </section>

  <section class="bff26-band bff26-band--voices" id="voices" aria-labelledby="bff26-voices-title">...</section>
  <section class="bff26-band bff26-band--photos" id="gallery" aria-labelledby="bff26-gallery-title">...</section>

  <section class="bff26-band bff26-band--travel" id="warsaw" aria-labelledby="bff26-warsaw-title">...</section>
  <section class="bff26-band bff26-band--friends" id="bff-friends" aria-labelledby="bff26-friends-title">...</section>
  <section class="bff26-band bff26-band--press" id="press" aria-labelledby="bff26-press-title">...</section>
  <section class="bff26-band bff26-band--support" id="support" aria-labelledby="bff26-support-title">...</section>
  <section class="bff26-band bff26-band--faq" id="faq" aria-labelledby="bff26-faq-title">...</section>

  <section class="bff26-band bff26-band--next" id="next-edition" aria-labelledby="bff26-next-title">...</section>
</article>
```

Every section heading is a real `h2` with a unique ID. Subsections use `h3`, then `h4` only when a real nested heading is needed. Sections may share a visual band, but each content group remains identifiable in source order and in the accessibility tree.

## 3. Shared naming and component contract

| Selector | Semantic element | Required role |
|---|---|---|
| `.bff26-band` and `.bff26-band--*` | `section` | Full-width editorial section inside the article. The modifier selects surface and rhythm, not a new palette. |
| `.bff26-section-heading` | `header` | Section label, `h2`, and optional lede. Keep the heading outside rows and disclosures. |
| `.bff26-hero` | `header` | Edition identity, dates, place, tagline, visual and next-edition action. |
| `.bff26-jumpnav` | `nav` with `ul` | In-page index. Links point to real section IDs. No JS scrolling dependency. |
| `.bff26-agenda` | `div` or `ol` wrapper | Programme board. Each day is a named group. |
| `.bff26-day` | `section` or `div` with heading | One chronological day column. It has a visible date and place. |
| `.bff26-showtime` | `article` or `li` | One time, activity type, title, venue, and optional description. Use `time` for dates/times. |
| `.bff26-film-list` | `ol` or `ul` | Film rows with title, creator, runtime or status, description, and reviewed link where available. |
| `.bff26-vod` | `aside` or `section` | Clearly labelled attendee-gated after-festival VOD information. |
| `.bff26-winner-list` | `ol` or `ul` | Award results. Each item names award, film, creator, and outcome. |
| `.bff26-ai-result` | `aside` or `section` | AI contest context and confirmed result. Amounts are text, not image-only. |
| `.bff26-monerokon` | `aside` or `section` | Partner callout. Keep MoneroKon separate from BFF identity. |
| `.bff26-stat-grid` | `dl` | Recap facts. Each `dt` labels a `dd`; no statistic is conveyed only through decoration. |
| `.bff26-stat` | `div` inside `dl` | One confirmed statistic. Use `.bff26-stat-value` and `.bff26-stat-label` only for styling. |
| `.bff26-highlight-list` | `ul` | Moments, people, art, community-stage, workshop, social, and satellite highlights. Use list rhythm, not tiles. |
| `.bff26-photo-strip` | `figure` plus `ul` or `div` | Curated photographic bridge. Every image has a caption or a meaningful alt. |
| `.bff26-testimonials` | `section` containing `blockquote` elements | Complete static quote list. JavaScript may enhance presentation, but is not required. |
| `.bff26-travel-grid` | `div` wrapper around `section`/`article` blocks | Warsaw arrival, weather, money, packing, lodging, Prague follow-up, and food guide. It stacks as editorial lists. |
| `.bff26-resource-list` | `ul` | External maps, transport, lodging, food, press, or social links. |
| `.bff26-logo-wall` | `ul` | Finite friend/partner list. Each link has visible or screen-reader text. |
| `.bff26-press-facts` | `dl` or `ul` | Public fact sheet and reviewed coverage. |
| `.bff26-support-list` | `ul` | Volunteer, share, contribute, film, testimonial, feedback, and donation actions. |
| `.bff26-donation` | `aside` | Public Lightning Address and QR with a text alternative. |
| `.bff26-faq` | `div` containing `details` | Native accessible disclosure list. Each `summary` is the question. |
| `.bff26-cta` | `section` or `aside` | A prominent action row, especially the BFF'27 destination. |

The CSS worker may add modifier selectors under these names, such as `.bff26-showtime--gala`, `.bff26-showtime--workshop`, `.bff26-band--paper`, or `.bff26-photo-strip--wide`. A modifier changes emphasis or surface only. It must not introduce a rounded card family, a second spacing scale, or a new color token.

## 4. Hero and jump navigation

### Hero

The hero preserves the old page's weight while using the shared blue screen:

- Show the real BFF mark or approved BFF'26 poster asset, never a text recreation of the logo.
- State BFF'26, the fourth edition, June 4-7, 2026, Warsaw, and Kinoteka, Palace of Culture and Science.
- Preserve the line `Fix the Money. Fix the Culture.` and the grassroots Bitcoin cinema framing.
- State the post-festival context: four days of films, art, music, conversation, and the co-located MoneroKon weekend.
- Keep BFF and MoneroKon visually adjacent but textually distinct. BFF remains Bitcoin-only.
- Include a visible BFF'27 showtime-style action for June 24-27, 2027 in Warsaw and a reviewed gallery route.
- Use one stable editorial hero image or poster. Do not reproduce the old random-image inline script.

The hero markup uses a heading hierarchy such as:

```html
<header class="bff26-hero" id="hero">
  <div class="bff26-hero-copy">
    <p class="bff26-kicker">Fourth edition / Warsaw / 2026</p>
    <h1>BFF'26</h1>
    <p class="bff26-dateline"><time datetime="2026-06-04">4 June</time>-<time datetime="2026-06-07">7 June 2026</time> · Warsaw</p>
    <p class="bff26-hero-lede">...</p>
    <p class="bff26-tagline">Fix the Money. Fix the Culture.</p>
  </div>
  <figure class="bff26-hero-art">
    <img src="{{ '/26/26-assets/bff26-poster.jpg' | relative_url }}" alt="Bitcoin FilmFest 2026 poster">
    <figcaption>Kinoteka, Palace of Culture and Science</figcaption>
  </figure>
  <p class="bff26-hero-cta">
    <a class="showtime" href="{{ '/27/' | relative_url }}">BFF'27 / 24-27 June 2027 / Warsaw</a>
  </p>
</header>
```

The exact copy can be edited against the public source, but the facts and hierarchy above cannot be removed.

### Jump navigation

`.bff26-jumpnav` is a real in-page `nav` immediately after the hero. Use a short `ul` of links to `agenda`, `recap`, `voices`, `gallery`, `warsaw`, `bff-friends`, `press`, `support`, `faq`, and `next-edition`. It is not sticky by default. If made sticky, it must remain below the shared top navigation, use a token background, and not obscure a focused target. Fragment navigation works with JavaScript disabled. Add `scroll-margin-block-start` to targets using a token-based value if the fixed shell otherwise hides headings.

## 5. Programme board

The agenda uses the edition-page macrostructure from `design.md`: typographic programme rows, not a generic card grid.

```html
<section class="bff26-band bff26-band--agenda" id="agenda" aria-labelledby="bff26-agenda-title">
  <header class="bff26-section-heading">
    <p class="bff26-kicker">As it ran</p>
    <h2 id="bff26-agenda-title">Programme</h2>
    <p>...</p>
  </header>
  <div class="bff26-agenda" aria-label="BFF'26 programme by day">
    <section class="bff26-day" aria-labelledby="bff26-day-0">
      <header><p class="bff26-day-number">Day 0</p><h3 id="bff26-day-0">Thursday 4 June</h3><p>Samocentrum / Warsaw</p></header>
      <ol class="bff26-showtimes">
        <li class="bff26-showtime">...</li>
      </ol>
    </section>
  </div>
</section>
```

Each `.bff26-showtime` row contains, in this order:

1. A `time` or time range with a machine-readable `datetime` where an exact time is confirmed.
2. A visible type label such as film, talk, workshop, social, satellite, gala, or partner.
3. The activity title as a heading or strong text, never as an image-only label.
4. Venue and external map/schedule link when reviewed.
5. Optional short description, creator, runtime, or access note.

Use an ordered list for a strictly chronological day. If parallel events cannot be represented in one order without implying a false sequence, use separate labelled sublists such as `Programme A` and `Programme B`, each with its own times. Do not merge conflicting source records into a new time or order.

Agenda content must include the four day groups, Day 0, films, VOD, Golden Rabbits, AI contest, MoneroKon, Art Beyond Cinema, Community Stage, workshops, social events, satellite events, and the inclusive people/VIP statement. Workshops and side events remain visibly distinct from film screenings through type labels and small accent changes, not separate card designs.

### Decision boundary for agenda reconciliation

The implementation must not invent a final agenda reconciliation. The content map remains the editorial record of the old-page versus confirmed-agenda conflicts, including Longy and the Friday lunch/venue discrepancy, the live film list versus VOD exclusions, and any time or ordering mismatch. Until the owner confirms a final public running order, the page must either:

- render only rows whose time, order, venue, and status are confirmed by the approved source; or
- present the conflicting source records as explicitly labelled historical/source notes without implying that the implementation resolved them.

Do not silently add, remove, move, rename, or combine an agenda item to make the grid look complete. Do not use the old `18 confirmed titles` label as a headline. The only headline stats are confirmed final facts from the post-festival source and approved editorial wording: 16 finished films screened, 15+ countries only after the country wording is confirmed against the map's correction note, 400+ attendees, 500+ Bitcoin/Lightning payments, and a 2.5M sats AI pool. If the 15+ acceptance wording is not approved, use the corrected source fact of 15 countries rather than manufacture a larger number.

## 6. Programme sub-blocks

These are editorial rows or labelled blocks inside the programme section, not independent card grids.

### Films

`.bff26-film-list` is an `ol` or `ul` of `.bff26-film-row` items. Each row includes title, creator, runtime where confirmed, a one or two sentence description, screening status, and a reviewed public detail link if one exists. Preserve title casing and public descriptions. Reconcile the old 18-title block against the final 16-film fact before presenting a final catalogue. The page may show an editorially marked source note while that work is pending, but it may not imply that a reconciliation has already happened.

### VOD

`.bff26-vod` must be labelled `After the festival` or `Attendee VOD`. State that IndeeHub access is for ticket holders and is not a public film stream. Keep VOD-only titles distinct from the live programme. Resolve the `Hummingbird` status against the approved final source before giving it a catalogue status. Do not expose ticket records, private viewing links, or credentials.

### Winners

`.bff26-winner-list` contains only awarded outcomes:

- *Bitcoin Castle* / *Bitcoin Schloss*, Bruno Schiebel: Best Movie and Audience Choice.
- *MaxisClub*, by Redy: Best Short.

The Best Story category may be named only with the explicit outcome `not awarded`. Do not invent a winner or publish unresolved private photographer material.

### AI contest

`.bff26-ai-result` names `Future of Money, Money of the Future`, audience voting, the 2.5M sats total pool, Naritamoto as the UK filmmaker receiving the 1.5M sats first prize, and the remainder rolling to BFF'27. The pre-event brief link at `https://ordain.art/bff26` remains external and must not be presented as a current submission CTA.

### MoneroKon

`.bff26-monerokon` is a partner callout with a partner label and a link to the official site/schedule. State that MoneroKon was co-located at Kinoteka on the same weekend, reciprocal access meant a BFF ticket covered MoneroKon and a MoneroKon ticket covered BFF, and the two brands remain separate. Do not style the block as a merged festival identity or as a sponsor card.

## 7. Recap, stats, people, photos, and voices

### Recap

The recap begins with `That's a wrap` and thanks filmmakers, artists, volunteers, friends, first-timers, and public named partners. It may use a warm paper or dark editorial band while retaining the shared screen and cinematic rhythm.

`.bff26-stat-grid` is a `dl`, not a visual-only counter wall:

```html
<dl class="bff26-stat-grid">
  <div class="bff26-stat"><dt class="bff26-stat-label">Films screened</dt><dd class="bff26-stat-value">16</dd></div>
  <div class="bff26-stat"><dt class="bff26-stat-label">Countries</dt><dd class="bff26-stat-value">15+</dd></div>
</dl>
```

Use only confirmed final facts for the prominent values. The recap may add the 8 works in progress, fourth edition since 2022, the 400+ combined attendance context, 500+ Bitcoin/Lightning payments, AI pool, winners, films, moments, faces, and public quotes. Keep the source conflict notes in `BFF26-CONTENT-MAP.md`; do not resolve them through CSS or by choosing a convenient number in markup.

### Editorial highlights and people

Use `.bff26-highlight-list` for `Making art in the fiat world`, Wiktor Piątkowski's screenwriter panel, the AI live vote, Roger9000's meditation concert, the Saturday Bitcoin Walk, Day 0 beforeparty/afterparty, the privacy-mask group photo, and Paco de la India yoga. Use a readable prose block or list for public guests, artists, volunteers, and the Patrick/Monika newcomer story. Do not import private contact data or CRM notes.

### Photos

`.bff26-photo-strip` is a controlled horizontal strip or a small editorial grid, never an automatically rotating gallery. Use real local files from `26-assets/photos/`, `photos/thumbs/`, `bff26-poster.jpg`, `satellite/side-events.png`, and the approved background photos. Each image has meaningful alt text unless it is explicitly decorative and the adjacent caption already conveys the same information. Use `figure` and `figcaption` for editorial images and credit text where supplied.

The old visual bridge is preserved: cinematic audience/event photography, a full-house Kinoteka closing image, the gallery teaser and a clear link to `{{ '/gallery/' | relative_url }}`. The strip may contain archive images from BFF'23-BFF'25, but the caption must not imply that an archive image is a BFF'26 event photograph.

### Testimonials

`.bff26-testimonials` renders every approved public quote as a static list of `blockquote` elements. Each quote contains a `p` and a `cite` with speaker and platform/context. JavaScript is not required to reveal, rotate, paginate, or switch quotes. If progressive enhancement adds previous/next controls, the complete list remains available with JS disabled, controls are real buttons with accessible names, and keyboard focus is never trapped. Do not copy private DMs. Preserve quote text verbatim when attributed and resolve the Anic/Anik spelling with the owner before publication.

## 8. Warsaw and practical details

`.bff26-band--travel` is list-led practical information, not a generic four-card panel. Use nested labelled blocks with `.bff26-resource-list` and `<address>` only for actual addresses. The content order is:

1. Kinoteka as the base and the roughly ten-minute walking radius.
2. Getting in: Chopin and Modlin, public transport, Uber/Bolt, and Veturilo.
3. Weather and vibe: the dated 17-23 C guidance, layers/rain, Type E 230 V, and tipping note, clearly framed as event-period advice.
4. Bitcoin in Warsaw: Bazzart/BarBazaar, bitomat and BTC Map references after current-link review.
5. Bring with you: Lightning wallet, comfortable shoes, eSIM/roaming, and curiosity.
6. Where to stay: Mercure Warszawa Centrum and Novotel Warszawa Centrum as dated proximity guidance. Do not publish unverified current prices, availability, scores, or group-rate claims.
7. After BFF: the BTC Prague connection and the train/flight/bus guidance only after current-link review. Use `{{ '/26/prague/' | relative_url }}` only if the child route exists; otherwise use a reviewed public fallback or omit it.
8. Eat, drink, and explore: the source's Bitcoin-friendly, Polish classics, milk bars, steak/burgers, pizza, food halls, beer, coffee/brunch, rooftop, and alternative lists. External links stay external and are reviewed before publishing.
9. Kinoteka facade figure, public festival map, and public useful-information spreadsheet. The spreadsheet must be inspected for private rows before any link is published.

A historical weather widget or old inline fetch script is not part of this contract. Use a plain labelled historical note or omit it.

On mobile, travel subsections may use native `details` disclosures when the answer remains complete and the summary names the content. On tablet and desktop, the same content is visible as stacked editorial blocks. No important travel fact may exist only inside a hover state.

## 9. Friends, logos, press, support, and FAQ

### BFF & Friends

The friends section keeps the public story of a Poland-founded grassroots project that grows Bitcoin cinema and connects creators, friends, and films. Use one real community image and a caption, then `.bff26-logo-wall` for the finite public friend/partner list.

Logo items are ordinary list items with links where a reviewed destination exists. Each image has alt text naming the organisation; if the adjacent link text already names it, the image may use `alt=""`. The list must remain understandable as text with images disabled. Do not duplicate the old featured/regular marquee markup, use `aria-hidden` duplicate copies, or add auto-scrolling logo motion. It is acceptable to visually group featured and regular partners with headings, but both groups are finite accessible lists.

### Press

`.bff26-press` uses `.bff26-press-facts` for public description, dates, Kinoteka, MoneroKon's co-location and reciprocal ticket relationship, awards context, tagline, press email, mission, selected coverage, press room, laurels/assets, and gallery. BFF'25 scale claims must be labelled historical or removed. The wider press room is a route, not a private content dump.

### Support

`.bff26-support` is an action list for volunteering, spreading the word, bringing someone, photographing, writing, recording films, testimonials, feedback, film/art submissions, and donating sats. Use `{{ '/join/' | relative_url }}` only when the current route owns the action; otherwise use a reviewed external destination or omit the action. The public Lightning Address `bitcoinfilmfest@blink.sv` and QR image may be shown with a visible copyable text alternative. Never include seeds, API keys, credentials, or private contact lists.

### FAQ

`.bff26-faq` is a native `<details>` list. Each item follows this pattern:

```html
<details>
  <summary>Question</summary>
  <div class="bff26-faq-answer"><p>Short, reviewed answer.</p></div>
</details>
```

Answers cover the public historical facts that remain useful: Kinoteka registration/wristbands, on-site ticket context, transfers, conduct and photo rules, attendee VOD, accessibility, language/subtitles, press accreditation, submissions, children, and public contact channels. Convert event-operational answers to past-tense archive wording or remove stale ticket/submission claims. `details` must work with keyboard and JS disabled. Do not require a custom accordion script.

## 10. BFF'27 CTA

The final `.bff26-cta` is a full-width showtime-style next-edition row, not a rounded promotional card:

- BFF'27, the fifth edition.
- June 24-27, 2027, Warsaw.
- Save-the-date language and the reviewed actions that belong on the BFF'27 page.
- Internal route: `{{ '/27/' | relative_url }}`.

Repeat the BFF line `Fix the Money. Fix the Culture.` in the sign-off or final CTA context. The shared footer follows; the page does not recreate it.

## 11. Responsive contract

These are the exact content breakpoints for the BFF'26 selectors. They complement the existing shared CSS breakpoints at `40rem`, `52rem`, `60rem`, and the shared `max-width: 22rem` safety rule.

### Mobile: `< 40rem` (below 640px)

- Keep the shared fixed shell and screen frame. The page content is one column with token padding; nothing may require horizontal scrolling except the deliberately labelled photo strip.
- Hero becomes one vertical flow: copy, poster/photo, then CTA. The hero title uses the existing display clamp and may wrap; never shrink below readable text to preserve one line.
- Jump navigation wraps into a compact list or becomes a vertically stacked in-page index. It remains ordinary links.
- Programme days are one chronological column in source order: Day 0, Friday, Saturday, Sunday. Each row stacks time, type, title, venue, and description. Parallel entries use labelled sublists, not compressed columns.
- Film, winner, AI, and MoneroKon blocks are full-width editorial rows with borders and whitespace. No side-by-side card grid.
- Stats use one or two columns only when each label/value remains readable; a `dl` may stack each term and description.
- Photos use a horizontal strip with `overflow-x: auto`, `scroll-snap-type: x proximity`, and visible affordance. The strip must not be the only way to read captions or access the gallery route.
- Testimonials show the full static quote list. No carousel is required.
- Travel, press, support, and FAQ blocks stack. Travel and FAQ may use native `details` for long answers, but the summary must expose the subject and the answer must remain complete.
- Logos remain a wrapped or horizontally scrollable finite list with accessible names; no auto-scroll.
- Long words, URLs, and Lightning Address values wrap with `overflow-wrap: anywhere`; no horizontal overflow at 320px.

### Tablet: `40rem <= width < 64rem` (640px-1023px)

- Keep the shared navigation behavior: the mobile menu remains until the existing `52rem` desktop-nav threshold; do not create a second nav breakpoint.
- Hero may use a two-track copy/art layout when space allows, with the CTA spanning the content width. At narrow tablet widths it may remain one column.
- Jump links may sit in two wrapped rows.
- Programme days use two columns. Preserve chronological order within each day and keep each `.bff26-day` intact; the sequence is Day 0/Friday in the first row, Saturday/Sunday in the second. If a day column becomes too narrow, it spans both columns rather than squeezing text.
- Showtime rows use a time/type column and a flexible title/details column. Parallel events remain labelled and readable.
- Film rows can place metadata beside the title, but descriptions stay below and remain in the DOM order.
- Stats may use two or three columns with consistent `dt`/`dd` pairing. Winners and AI result may share a row only as separate editorial blocks with their own headings.
- Photo strips may show two or three visual items while retaining horizontal overflow for the remaining list. Travel blocks may use two columns; FAQ remains a single readable column.
- Friends logos may wrap into several rows. Press and support lists remain list-led.

### Desktop: `>= 64rem` (1024px and up)

- The shared nav is desktop at its existing `>= 52rem` breakpoint. BFF'26 content uses the wider desktop composition only at `>= 64rem`.
- Hero uses an asymmetric two-column composition with copy dominant and art/poster as the secondary track. The BFF'27 action aligns with the copy as a showtime row.
- Jump navigation may be a single horizontal row with wrapped fallback for long labels.
- Programme board uses four day columns for Day 0, Friday, Saturday, and Sunday. Each column has equal visual priority, a visible day heading, and independent chronological rows. A very long day may extend vertically; do not reduce type below tokens to equalize heights.
- Showtime rows can use time, type/title, venue/details, and action metadata in a stable grid. Hover may add the existing one-signal translation or underline only on fine pointers; keyboard focus has the stronger focus ring.
- Film rows, winners, AI result, and MoneroKon use editorial bands and rule-separated lists. They do not become four-up rounded cards.
- Stats use a horizontal `dl` with generous gaps and a rule above. Long-form recap prose stays within `--prose-max` while media may use the content max.
- Photos can use a controlled three- or four-item strip/grid with captions. The layout must tolerate a missing image without collapsing text.
- Travel can use two or three editorial columns, but each subsection remains a labelled list. Press, support, and FAQ stay readable at the project measure rather than stretching across the viewport.
- Friends logos may be grouped into featured and regular rows. Both remain finite, keyboard-reachable, and text-labelled.

At all widths, the shared seat foreground, room frame, footer, top navigation, and bezel remain owned by the default layout and existing CSS. BFF'26 content must not place fixed elements above the shared stack or create a second viewport frame.

## 12. Tokens and CSS rules

All BFF'26 styles use the variables already defined in `site/tokens.css`:

- Surfaces: `--color-screen`, `--color-screen-bright`, `--color-screen-soft`, `--color-paper`, `--color-paper-2`, `--color-room`, `--color-room-raised`, and `--color-footer`.
- Text and rules: `--color-ink`, `--color-ink-2`, `--color-muted`, `--color-on-screen`, `--color-on-dark`, `--color-rule`, and `--color-room-rule`.
- Accents: `--color-accent` for projector amber, `--color-focus` for focus, and blue variables for active links and programme emphasis.
- Type: `--font-display` for display labels and headings; `--font-body` for prose, descriptions, and controls. Keep the two-family limit.
- Spacing: `--space-3xs` through `--space-4xl`; use `clamp()` only with these named tokens as endpoints or in existing patterns.
- Type sizes: `--text-xs` through `--text-display`; use existing clamps for hero and section headings.
- Motion: `--ease-out`, `--ease-in`, `--ease-in-out`, `--dur-micro`, `--dur-short`, and `--dur-long`.
- Shape and layout: `--radius-control`, `--radius-panel`, `--rule-thin`, `--content-max`, `--prose-max`, `--frame-side`, `--nav-height`, and `--frame-bottom`.

Do not add hex colors, arbitrary spacing values, a second font stack, a global reset, a generic `.card` class, large pill controls, drop-shadow-heavy panels, or a new CSS variable in the BFF'26 section. Use borders, underlines, background changes, type hierarchy, and whitespace to signal grouping. Rounded corners are limited to the existing control/panel radii and are not the visual grammar of the page.

Keep the BFF'26 CSS in a clearly labelled section of `site/assets/css/cinema-frame.css`. Do not modify shared nav, footer, seats, atmosphere, or unrelated edition selectors unless a proven regression requires it.

## 13. Accessibility, focus, and semantics

- Use the shared skip link and `main#main-content`; do not add another skip target.
- Preserve a logical heading outline: one page `h1`, section `h2`s, then subsection `h3`s.
- Use `nav`, `header`, `main` from the shared layout, `section`, `article`, `figure`, `figcaption`, `ol`/`ul`, `dl`, `time`, `blockquote`, `cite`, `address`, `details`, and `summary` according to meaning, not styling convenience.
- Every jump link, CTA, external link, map link, press link, and logo link has a meaningful accessible name. External links may say that they open externally where it matters.
- All interactive targets retain `:focus-visible` with the shared 3px `--color-focus` outline and 3px offset. Do not replace focus with a color-only change or hide it behind a clipped row.
- Do not use hover to expose essential content. A row that changes background or translates on hover remains fully readable and actionable with keyboard and touch.
- Maintain text alternatives for all film, programme, winner, partner, donation, and FAQ information. Images never carry the only copy.
- Decorative images use `alt=""` and `aria-hidden="true"` only when adjacent text supplies the meaning. Meaningful photos have specific alt text; logo images name the organisation unless visible link text already does so.
- The page remains usable with images blocked, external fonts unavailable, JavaScript disabled, zoom increased, and a keyboard as the only pointer.
- Ensure contrast for paper/ink, blue/on-screen, dark/on-dark, and amber accents. Do not use amber as body text on paper where contrast is insufficient.
- Native `details` controls must open and close with Enter/Space and must not require custom JS. If a disclosure is opened by a fragment or browser history, its heading remains visible.

## 14. Motion and progressive enhancement

The page has no required JavaScript behavior. In particular, no script is required for the agenda, jump navigation, photos, testimonials, logo list, travel details, or FAQ.

- Do not copy old inline random-image, weather-fetch, marquee, delayed-reveal, testimonial-rotation, or logo-duplication scripts.
- A CSS transition may use the existing state/enter timing, but hover uses one signal only.
- There is at most one short hero entrance. Do not animate body sections into view on scroll.
- Do not auto-rotate photos, testimonials, or logos. If a progressive enhancement is later added, the static DOM remains complete and the controls are keyboard accessible.
- Under `prefers-reduced-motion: reduce`, disable continuous grain/scratch/flicker effects for the page where possible, remove seat-scroll and carousel-like movement, set transitions and opacity changes to no more than 150ms, and keep every item visible and readable.
- Fragment links, native disclosures, form controls, external links, and all content work without JavaScript. The shared `main.js` may continue to provide site-wide navigation and progressive document transitions because it is owned by the default layout.

## 15. Liquid URLs and asset policy

Every same-origin page route and every local BFF'26 asset uses `relative_url`:

```liquid
{{ '/26/26-assets/photos/bff25-143.jpg' | relative_url }}
{{ '/26/26-assets/logos/kinoteka.png' | relative_url }}
{{ '/gallery/' | relative_url }}
{{ '/27/' | relative_url }}
{{ '/join/' | relative_url }}
```

Do not write root-relative literals such as `/26/26-assets/...` into `src`, `href`, `srcset`, CSS inline styles, or data attributes. The temporary project-site build must work with a non-empty `baseurl`.

External URLs remain verbatim external URLs and do not receive `relative_url`: Kinoteka and venue maps, MoneroKon, Ordain, IndeeHub, airports, transport, Veturilo, BTC Map, hotels, Booking/Accor, restaurants, public spreadsheets/maps, friend sites, press coverage, public forms, social networks, and public contact mailboxes. A route not yet migrated must use an explicitly reviewed canonical production fallback or be omitted, never a broken local path. Record each fallback in the editorial content map.

The complete approved `site/26/26-assets/` bundle is 126 files and 15,916,490 bytes according to the content map. Preserve all relative paths and use the bundle by role:

- Identity and metadata: `bff-logo.png`, `bff26-poster.jpg`, `og-poster.jpg`, `rabbit.png`.
- Shared/legacy visual references: `seats.png` and the approved local poster/rabbit files. Do not render a duplicate seat layer; the default layout owns seats.
- Programme and donation: `satellite/side-events.png`, `lightning-qr.png`, `trezor-mark.png`, and the approved `promo/` images where a reviewed context needs them.
- Photos: every approved `photos/*.jpg` file for selected editorial figures and the full `photos/thumbs/` pool for a deterministic gallery/teaser. The old dynamic hero pool is a content dependency, not permission to add random runtime selection.
- Backgrounds: `photos/bff25-143-bg.jpg` for the hero treatment, `photos/bff25-72-bg.jpg` for Warsaw, and `photos/bff25-23-bg.jpg` for BFF & Friends when the CSS worker uses those surfaces.
- Friends and partners: every approved file under `logos/`, including alternate formats. Logos are supplemental to text-labelled links and never the only partner information.

The page need not render every bundle file at once, but the implementation must preserve the complete bundle, account for every local dependency, and never substitute a missing or invented asset. Query-string cache busters are not filenames. Excluded source surfaces remain excluded: scripts, credentials, PHP/photo backends, caches, archives, private data, and deployment configuration.

## 16. Old-page visual elements to preserve

The rebuild preserves the old `/26/` visual intent while moving to the new shell:

- Bold BFF'26 hero with real logo/rabbit/poster treatment and strong date/place identity.
- Blue screen opening, warm paper/editorial sections, and dark closing rhythm inside the shared cinema frame.
- Kinoteka and Warsaw photographic bands, including the hero, travel, community, and full-house images where approved.
- Agenda as a prominent programme board with times and venues, not a compressed text dump.
- Film, VOD, Golden Rabbits, AI, MoneroKon, art, community, workshop, social, satellite, and people sections in the old information-architecture order.
- Recap numbers, winners, AI result, film/moment/people editorial, public voices, and the wrap thank-you.
- Gallery teaser/photo strip and link to the full gallery.
- Friends story, partner/friend logo presence, press kit, support/donation action, FAQ, sign-off, and BFF'27 save-the-date.
- The shared top navigation, bezel, cinema atmosphere, fixed seats, footer, and black final screen from the default layout.

The rebuild does not preserve old inline CSS, standalone shell markup, random image selection, live past-date weather fetching, duplicated marquee DOM, stale ticket/submission claims, invented agenda reconciliation, or generic rounded card grids.

## 17. Implementation checks

Before the page or CSS is considered contract-compliant, verify:

- The page uses only the shared default layout and the skeleton/classes in this file.
- All required section headings and section IDs exist, with no duplicate IDs.
- The agenda has four day groups, uses semantic time/venue/type rows, and does not silently reconcile source conflicts.
- Headline stats use confirmed final facts; the old 18-title label is absent as a headline.
- Winners, AI result, MoneroKon relationship, and BFF'27 dates match the approved public sources.
- The complete 126-file public asset bundle remains present and all local URLs use `relative_url`.
- No generic card grid, old inline script, private data, duplicate shell, or stale operational claim was introduced.
- Mobile at 320px, 390px, and below 40rem has no accidental horizontal overflow; tablet uses two agenda columns; desktop at 64rem and above uses four day columns.
- Keyboard focus, native disclosures, meaningful image/link names, JS-off reading, and reduced motion all leave the full public content available.
- `git diff --check` is clean after implementation.

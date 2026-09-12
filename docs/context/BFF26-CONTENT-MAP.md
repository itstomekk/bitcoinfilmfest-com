# BFF'26 public content map

Status: Wave 1A content-audit artifact. This file maps the public BFF'26 page to the Jekyll rebuild. It is an editorial map, not a page implementation.

## Scope and source priority

- **Old public page:** `BFF26-guest-page/index.html` (the live-style `/26/` recap page; section and line references below use this file).
- **Confirmed programme source:** `BFF26-guest-page/BFF26-AGENDA-confirmed.md`.
- **Post-festival facts:** `BFF26-guest-page/press/BFF26-POST-FESTIVAL-SOURCE.md`.
- **New-design references:** `site/design.md`, `site/24.md`, `site/bff25.md`, and `site/27.md`.
- The requested source paths `BFF26-AGENDA-confirmed.md` and `press/BFF26-POST-FESTIVAL-SOURCE.md` are located under `BFF26-guest-page/` in the public source tree.

Use the post-festival source for final recap facts, the confirmed agenda for the running order, and the old page for the complete public information architecture and link inventory. Do not copy old HTML shell, inline CSS, inline JavaScript, or PHP into the new page.

## Non-negotiable public facts

These facts must survive the migration, with the final wording checked against the source conflict notes below:

- **BFF'26 ran June 4-7, 2026, in Warsaw at Kinoteka, Palace of Culture and Science.** June 4 was the Day 0 opening social; the main programme ran June 5-7.
- The public recap must state **16 films**. The post-festival source says 16 finished titles screened, plus 8 works in progress presented. The old page also contains an 18-title selection block and must not be copied without reconciliation.
- The public recap must state **15+ countries represented** as required for this migration. The current post-festival publication note says the corrected headline is **15 countries**, replacing an earlier approximately 20-country figure. Treat the plus sign as an editorial acceptance criterion to confirm before final copy; do not silently turn the source's corrected 15 into 20+.
- **Golden Rabbits:** *Bitcoin Castle* / *Bitcoin Schloss* won Best Movie and Audience Choice; *MaxisClub* won Best Short. Best Story was not awarded and should not be invented or listed as a winner.
- **AI contest:** “Future of Money, Money of the Future”; audience-voted AI-assisted short films; total pool **2.5M sats**; first prize **1.5M sats** went to **Naritamoto, a filmmaker from the UK**; the remainder rolls to BFF'27.
- **MoneroKon relationship:** co-located with BFF at Kinoteka on the same weekend, with shared social energy and reciprocal access; a BFF ticket covered MoneroKon and a MoneroKon ticket covered BFF. BFF remains a Bitcoin-only festival and the brands must not be presented as one blended event.
- **BFF'27:** the fifth edition is **June 24-27, 2027, in Warsaw**. Keep save-the-date links prominent.
- Preserve the BFF line: **“Fix the Money. Fix the Culture.”**

### Reconciliation flags

1. The old page's Film Selection says “18 confirmed titles” and lists a larger live-programme block than the final recap statistic. The confirmed agenda also contains titles later dropped from the confirmed-with-description filter and separately excludes VOD-only titles. The migration should expose the final public film set only after a deliberate editorial reconciliation. Do not use the old “18” label as the headline.
2. The old page calls the award block four categories, but the post-festival source says Best Story was not awarded. Retain the category context only if it clearly says no Best Story winner; the public winner cards must be the three awarded outcomes above.
3. The page is a **post-festival recap**, so pre-event language such as “tickets available”, “submission deadline May 20”, and “selection subject to change” must be removed or clearly marked historical if retained for archive context.

## Ordered public content map

The order below is the order a visitor encounters the old page. Each row names the old section, facts to preserve, source, and the intended Jekyll/design treatment.

| Order | Old public section and source | Key facts and content to preserve | Intended new-design component |
|---|---|---|---|
| 0 | Head metadata and structured event data, `index.html` lines 1-34 and 918-952 | Title and description identify BFF'26 as a June 4-7, 2026 Warsaw recap; canonical `/26/`; OG image; Festival schema with Kinoteka, Warsaw, dates, organizer, and BFF'27 next edition. | Jekyll front matter consumed by the shared head include. Preserve canonical/OG/Twitter metadata, but use `relative_url` for internal page URLs and the site's configured canonical base for production fallback. Keep schema truthful to a completed event, not `EventScheduled` if the final implementation uses current status vocabulary. |
| 1 | Fixed top navigation, `index.html` lines 957-968 | BFF'26 home anchor; Agenda; Recap; Warsaw Travel; BFF & Friends; Gallery; prominent BFF'27 CTA. | Shared data-driven navigation from `_data/navigation.yml`, with the edition page active. Section anchors may remain fragment links; route links must use Jekyll `relative_url`. |
| 2 | BFF'27 announcement banner, `index.html` lines 972-975 | BFF'26 has wrapped; save June 24-27, 2027 in Warsaw. | Edition-page announcement/showtime row above the masthead. Link to `{{ '/27/' | relative_url }}` with canonical-domain fallback handled by the site configuration, not a hard-coded old absolute URL. |
| 3 | Hero and intro, `index.html` lines 977-1023 | Real BFF logo; fourth edition; June 4-7, 2026; Kinoteka, Warsaw; “Fix the Money. Fix the Culture.”; grassroots Bitcoin cinema; co-location with MoneroKon; paid in sats; recap framing; wrap thank-you; BFF'27 save-the-date; link to photo gallery. | `edition-masthead` family used by `site/24.md`, `site/bff25.md`, and `site/27.md`, expanded with an edition hero/showtime row and real rabbit/poster photography. Use the new shared cinema shell. Do not reproduce the random-image inline script; use a stable editorial image or an approved progressive-enhancement gallery component. |
| 4 | Agenda section shell and disclaimer, `index.html` lines 1028-1044 | “Agenda as it ran”; BFF'26 dates and Warsaw; absent venue means Kinoteka, Palace of Culture. | Edition **Programme board** per `site/design.md`: readable typographic rows, date/place masthead, restrained imagery. The details disclosure may become a native accessible section or visible archive heading; do not depend on hover. |
| 4a | Agenda daily grid: Thursday June 4 / Day 0, `index.html` lines 1050-1061; source agenda lines 27-36 | 18:00 opening social at Samocentrum; live music/DJs; **Longy at 20:00**; DOT Dominus; RENIK; outdoor *SINNERS*; MadMunky. The old grid omits Longy and uses different times. **Decision boundary:** the owner must confirm whether the confirmed agenda is the final public running order before implementation; until that choice is made, preserve both source records and do not invent a reconciled time/order. | Programme-board day column with date, time, event type, venue and optional description. Keep side events visually distinct from screenings; preserve venue links. |
| 4b | Agenda daily grid: Friday June 5, `index.html` lines 1063-1103; source agenda lines 38-54 | Run for Hal; breakfast; Kinoteka registration; MoneroKon starts; AI Film Jam intro; anti-AI aesthetic roundtable; **Friday public pierogi lunch at 13:15 at Samocentrum**; “Can everyone be an artist now?” screening block; networking break; group photo; “Changing minds with fiction”; Vistula River disco. The old page places this public lunch at 13:15, while the confirmed agenda omits the lunch row. **Decision boundary:** final inclusion/order follows the same owner confirmation as the running order; do not silently add, remove, or move it. Final venue is BarBazaar, ul. Ząbkowska 12, not Cud nad Wisłą. | Programme-board day column with a named screening block and a separate shared-partner row. Preserve the venue-change note in archive copy, not as an ambiguous live warning. |
| 4c | Agenda daily grid: Saturday June 6, `index.html` lines 1106-1139; source agenda lines 56-74 | Paco Yoga in Park Saski; breakfast; AI Film Jam with ElevenLabs; Lightning Piggy; Film lifecycle with Zack Mahoney; “Bitcoin on the ground”; networking; “Making art in the fiat world”; outdoor *GREAT MARTY*; Palace Bass Journey at Barstudio. | Programme-board day column. Parallel 12:00 workshop/talk entries must remain understandable on narrow screens. |
| 4d | Agenda daily grid: Sunday June 7, `index.html` lines 1142-1160; source agenda lines 76-85 | Bitcoin Walk; Palace Tower tour; Entrepreneurs lunch; BFF x MoneroKon Final Gala; AI Contest voting; Roger9000 concert; Golden Rabbits; Goodbye at Amondo. | Programme-board day column with a highlighted gala block and clear transition to the recap. Preserve the final-gala relationship to MoneroKon. |
| 4e | Agenda notes, gallery note, closing cinema photo, `index.html` lines 1163-1169 | All times CEST; agenda was confirmed but historical; public attendee photos tagged `#BFF26` and `#bitcoinfilmfest`; full-house Kinoteka image and caption. | Small archive note below the programme board plus a content-specific figure. Image must be local and credited/captioned if the final source supplies credit. |
| 4f | Agenda sub-section: AI Contest, `index.html` lines 1171-1182 | “Future of Money, Money of the Future”; 1-5 minute AI-assisted animations; audience chooses; 2,500,000 sats pool; workshop route; brief at `ordain.art/bff26`. For recap, add the awarded 1.5M sats Naritamoto result and rollover. | Highlighted programme-board callout or sharp showtime row, using the approved blue accent. Separate pre-event brief link from post-event result. |
| 4g | Agenda sub-section: Film Selection, `index.html` lines 1184-1277 | Film titles, descriptions, creators and runtimes where public; live Kinoteka context. Preserve film title casing and short descriptions where still correct. | Programme-board film rows or the existing Cinema collection/detail pattern, not generic rounded cards. Link to public film detail pages only where a reviewed record exists. Reconcile the 18-title old block against the final 16-film fact before publishing. |
| 4h | Agenda sub-section: VOD, `index.html` lines 1279-1305 | Ticket holders get VOD access through IndeeHub; three VOD-only titles in the old page: *Bitcoin: Digital Gold*, *Gimp and the Hitman*, *Rabbit Hole*. The confirmed agenda also marks *Hummingbird - The Bitcoin Jungle Story* as VOD-excluded from the live pull, while the recap says it premiered, so resolve status before a film catalogue is generated. | A clearly labelled “After the festival” archive callout or film-list subsection. Do not imply public access; IndeeHub is attendee-gated. No private ticket data. |
| 4i | Agenda sub-section: Golden Rabbits, `index.html` lines 1307-1319 | Award context; categories shown as Best Movie, Best Short, Best Story, Audience Award. Final winner facts belong in the recap: *Bitcoin Castle* won Best Movie and Audience Choice; *MaxisClub* won Best Short; Best Story not awarded. | Award strip or typographic laurels block. Use real approved award assets only if available; no invented winner for Best Story. |
| 4j | Agenda sub-section: MoneroKon, `index.html` lines 1321-1333 | Technical privacy/financial-technology conference; Fri-Sun 10:00-17:00; same Kinoteka; one ticket covered both; shared socials; BFF remains Bitcoin-only; links to monerokon.org and full schedule. | Highlighted partner callout inside the programme board, with amber partner accent allowed by the existing design system. Keep reciprocal-access statement exact and distinguish partner from sponsor. |
| 4k | Agenda sub-sections: Art Beyond Cinema and Community Stage, `index.html` lines 1335-1350 | Artists, authors and creators beside screenings; browse/talk/buy. Community Stage shared with MoneroKon; lightning talks, demos, mini-panels. The old May 20 submission deadline is historical and must not be presented as current. | Programme-board supporting rows or a short editorial subsection. Convert any still-valid participation action to the current `/join/` or contribution route; otherwise keep as archive context without a stale form CTA. |
| 4l | Agenda sub-section: Workshops, `index.html` lines 1352-1358 | AI Film Jam on Friday and Saturday; Lightning Piggy on Saturday; all workshops in the Kinoteka café; hands-on, open-source Lightning piggy banks. | Programme-board workshop rows with an optional “workshop” label and accessible details. Preserve the Kinoteka café venue. |
| 4m | Agenda sub-section: Social Events, `index.html` lines 1360-1371 | Thursday Samocentrum; Friday BarBazaar after venue change; Saturday Palace Bass Journey at Barstudio; Sunday Goodbye at Amondo; morning walks/runs/yoga. | Side-event rows in the programme board, with venue links and a compact archive note for changes. |
| 4n | Agenda sub-section: Satellite Events, `index.html` lines 1373-1389 | Outdoor cinema: *SINNERS* Thursday and *GREAT MARTY* Saturday; Run for Hal; Paco Yoga; Sunday Bitcoin Walk route; Palace Tower Tour. Most free and open. Public route map link. | Supporting editorial block with a real side-events image and list-led activity rows. Use the existing paper/blue/amber tokens, not a new card system. |
| 4o | Agenda sub-section: People & VIPs, `index.html` lines 1391-1398 | No VIP tier, premium pass or backstage rope; same lanyard, chair and dance floor; filmmakers, partners and newcomers together. | Short manifesto/callout within the edition page. Preserve the inclusive meaning; do not reproduce delayed reveal as essential content. |
| 5 | Recap / thank-you section shell, `index.html` lines 1407-1425 | “That's a wrap”; best event of Bitcoin culture; four days of films, art, music and conversation with MoneroKon; thank filmmakers, artists, volunteers, friends and first-timers; named partner thanks; soft support nudge. | Edition recap section following the programme board, using the `edition-page` editorial hierarchy and a warm paper screen. Keep “Friends” language where the public source uses it; do not turn the list into a private sponsor database. |
| 5a | Recap numbers, `index.html` lines 1428-1436; post-festival source lines 25-32 and 43-48 | Public stat strip: 400+ attendees, 500+ Bitcoin/Lightning payments, 2.5M sats AI pool, 16 films, 15 countries, fourth edition since 2022. The source distinguishes 150+ BFF and 250 MoneroKon within 400+ combined; only publish that split if desired and verified. | Edition statistics strip / showtime-style fact rows. Use the required 16 films and 15+ countries acceptance wording with the reconciliation note above. |
| 5b | Golden Rabbits 2026 winners, `index.html` lines 1438-1453; post-festival source lines 34-41 | *Bitcoin Castle* / *Bitcoin Schloss*, Bruno Schiebel: Best Movie plus Audience Choice. *MaxisClub*, by Redy: Best Short. Statuette, prestige and merch bag. Do not publish the source's private/unresolved photographer award material or a Best Story winner. | Two winner rows or award laurels with title, creator and award labels. This is a high-priority recap block, not a generic ticket card. |
| 5c | AI Contest result, `index.html` lines 1455-1462; post-festival source lines 43-48 | Contest title; audience vote; Naritamoto, UK filmmaker; 1.5M sats first prize; 2.5M total pool; remainder rolls to BFF'27. | Featured result block with prize amount as a typographic value and a link to BFF'27. Keep pseudonym spelling exactly. |
| 5d | On-screen and film list, `index.html` lines 1464-1466; post-festival source lines 50-57 | 16 finished films screened; 8 works in progress presented; *Bitcoin Castle* strongest reaction and first festival screening; *Self Custody* European premiere with Garrett Patten video message, not Adrian Grenier attendance; *Hummingbird* premiered with HODL/Paul Keating from Costa Rica; Finding Satoshi creators did not appear and that absence should not be promoted. | Long-form editorial paragraph plus curated film links/rows into Cinema detail pages. Keep attendee-only IndeeHub access out of public-facing assumptions. |
| 5e | “Moments we won't forget”, `index.html` lines 1468-1478; post-festival source lines 77-82 and 106-116 | “Making art in the fiat world”; Wiktor Piątkowski screenwriter panel; AI live vote; Roger9000 meditation concert; Saturday Bitcoin Walk; Day 0 beforeparty and late afterparty; privacy-mask group photo; Paco de la India yoga. | Editorial highlights list, not a tiled card wall. Use a short list with optional real-photo figure. |
| 5f | “Faces of BFF'26”, `index.html` lines 1480-1482; post-festival source lines 59-75 and 96-104 | Guests from 15 countries; named public guests Setu, Jimmy and Phi, Ox Power, Paul Keating, Bruno Schiebel; artists Jeffrey Peel, AgiChoote, Shadrah and 5Ksana; 15-strong volunteer crew; Patrick and Monika newcomer story and quote. | People-and-community editorial block with readable measure. Keep names and spellings; do not import private contact/CRM details. |
| 5g | Recap voices, `index.html` lines 1484-1500 and post-festival source lines 144-163 | Public quotes from Tomek, Bruno Schiebel, John McManus and Anik Malcolm as used on the old page; cite speaker and context. The source has a spelling conflict for Anic/Anik; use the published old-page spelling only after owner confirmation. | Pull-quote stack in the Long Document / edition recap family. Quote text must remain verbatim when attributed. |
| 5h | BFF'27 recap CTA, `index.html` lines 1502-1509 | Fifth edition; June 24-27, 2027; Warsaw; early-bird tickets, film call and programme to follow. | Prominent next-edition showtime row / square CTA linking to `{{ '/27/' | relative_url }}`. |
| 5i | Recap closing photo, `index.html` lines 1511-1514 | Full house at Kinoteka. | Content-specific figure using an approved local image and caption. |
| 6 | Rotating “Voices from the BFF'26 community”, `index.html` lines 1522-1576 | 16 short public posts from Nostr, X and Telegram; rotating quotes, speaker/handle/platform, previous/next controls. | Prefer a static accessible quote list or progressive-enhancement carousel. All quotes must be public, attributed, keyboard reachable, and readable with JavaScript off. Do not copy private DMs from the testimonial database. |
| 7 | Gallery photo strip, `index.html` lines 1578-1592 | Eight-image visual bridge; link and CTA to the full gallery. Images are mostly BFF'23-BFF'25 archive images, not necessarily BFF'26. | Shared gallery teaser/film-strip component. Use `relative_url` for the gallery route and local production assets only. |
| 8 | Warsaw Travel section shell and intro, `index.html` lines 1594-1606 | Kinoteka as base; everything within roughly a 10-minute walk. | Supporting practical-information section within the edition page, list-led and mobile readable. |
| 8a | Travel in / Weather & vibe / Bitcoin in Warsaw / Bring with you, `index.html` lines 1608-1646 | Chopin and Modlin airport guidance; public transport, Uber/Bolt, Veturilo; typical 17-23 C, layers/rain, Type E 230 V, 10% tipping; Bazzart/Bazaar Bitcoin-friendly note, 80+ bitomat ATMs and BTC Map; Lightning wallet, shoes, eSIM/roaming and curiosity. These are time-sensitive archive recommendations and need re-verification before reuse as current advice. | Four-column information grid translated to stacked list sections on mobile. Avoid generic cards; use editorial showtime/list rows. |
| 8b | Dynamic Warsaw forecast, `index.html` lines 1648-1684 | Historical Jun 4-7 forecast widget from Open-Meteo with timeanddate fallback. It calls a live API for past dates and should not be carried over as a live forecast without a new purpose. | Either remove from the post-event archive or replace with a plainly labelled historical weather note. Do not deploy old inline fetch script in the content page. |
| 8c | Where to Stay, `index.html` lines 1686-1722 | Mercure Warszawa Centrum and Novotel Warszawa Centrum; five-minute proximity; prices, room counts, scores, amenities, direct and Booking links; group-rate email. Prices and availability are volatile and require re-verification. | Practical lodging list with external-link rows. Treat commercial details as dated archive information, not evergreen facts. Preserve public contact email only. |
| 8d | After BFF to BTC Prague, `index.html` lines 1724-1731 | Many attendees continue to BTC Prague; trains, sleeper, flights, buses and BlaBlaCar; LeoExpress from EUR 18 and Bitcoin checkout; link to the old local Prague guide. Price and route data are historical. | Related-guide link row. Use `{{ '/26/prague/' | relative_url }}` only if that child route is migrated; otherwise canonical fallback to an approved public travel guide or omit. |
| 8e | Eat, Drink & Explore, `index.html` lines 1733-1819 | Crew-curated Warsaw recommendations grouped as Bitcoin-friendly; Polish classics; milk bars; steak and burgers; pizza; food courts/halls; craft beer; coffee/brunch; rooftops/views; something different. Preserve names and external URLs only after current-link checks. | List-led local guide subsection. On a paper screen, use headings and compact lists rather than 10 new card variants. |
| 8f | Warsaw closing photo, map and useful-info spreadsheet, `index.html` lines 1821-1835 | Kinoteka facade image; Google My Maps festival locations; public full-map editor/viewer link; public useful-info spreadsheet. The spreadsheet is an external public dependency and must be checked for accidental private rows before linking. | Figure plus external resource links. No embedded spreadsheet credentials or private data. The map may use a safe external link rather than an iframe. |
| 9 | BFF & Friends section shell and story, `index.html` lines 1843-1867 | Grassroots project founded in Poland in 2022; grows Bitcoin Cinema; connects creators, friends and films; link to About; community image and caption. | Edition context block or link to the existing Storyboard/About route. Use a real image and the shared cinema shell. |
| 9a | Our Friends logo marquees, `index.html` lines 1869-1934 | Public linked friend/partner logos, separated into featured and regular rows; CTA to become a Friend. Preserve names and destinations, but use a finite accessible logo list on reduced motion and mobile. | Sponsor/friend strip component if already supported by the design system, otherwise a simple logo index. Do not copy duplicated `aria-hidden` carousel markup or add a new auto-scrolling dependency without an accessible fallback. |
| 9b | Press Kit, `index.html` lines 1936-1976 | Public BFF description, fourth-edition fact sheet, dates, Kinoteka, MoneroKon co-location and one-ticket relationship, awards categories, tagline, press email, selected past coverage, mission, and links to press room, laurels/assets and gallery. Remove stale BFF'25 scale as the BFF'26 fact unless clearly labelled historical. | Long Document / press-information block, with concise fact list and external coverage links. The broader press room should become a separate route, not a private content dump. |
| 9c | How You Can Help, `index.html` lines 1978-2003 | Volunteer; spread the word; bring someone; photograph; write; record films; testimonial; feedback; submit film/art; donate sats. Public Lightning Address `bitcoinfilmfest@blink.sv` and QR image. | Contribution/action list plus a donation callout. Link to `{{ '/join/' | relative_url }}` where the current route supports it; keep the Lightning Address as public donation data, never expose a wallet seed or private credential. |
| 9d | FAQ, `index.html` lines 2005-2053 | Wristband/registration at Kinoteka; on-site tickets; no refunds but ticket transfer via public community channels; conduct/photo rules; attendee VOD; accessibility; mostly English and English subtitles; press accreditation; film submission; children; contact channels. Since the page is now a recap, convert event-operational answers to historical archive answers or remove stale ticket/submission claims. | Accessible native disclosure list inside a Long Document/utility block. Keep answer text short and link only to reviewed public routes. |
| 9e | Sign-off and closing photo, `index.html` lines 2055-2066 | Culture is forged; thanks; “Fix the Money. Fix the Culture.”; Mr. Rabbit sign-off; community-on-stage photo. | Editorial sign-off with one final figure before the shared footer. No scripted quote reveal is needed. |
| 10 | Footer, `index.html` lines 2074-2121 | Logo; BFF'26 dates and Kinoteka/Warsaw; Do links for BFF'27, volunteer, submit film, become a Friend; Read links for About, gallery, press room, Credits, press kit assets; Talk links for email, Telegram, X, Nostr and LinkedIn; copyright; fixed cinema seats. | Shared `_includes/footer.html` and persistent cinema shell. Keep footer links data-driven; route links use `relative_url`; keep local seats/logo in the shared asset set rather than page content. |

## Link migration inventory

### Same-origin and old-local routes

Use Jekyll `relative_url` for all routes that belong to this site. Do not preserve absolute `https://bitcoinfilmfest.com/...` links inside the source page unless the route is intentionally an external canonical fallback.

| Old reference | Use in the rebuild | Fallback / note |
|---|---|---|
| `#hero`, `#agenda`, `#tickets`, `#warsaw`, `#bff-friends` | Keep as fragment IDs if those sections remain on one edition page. | The old `#tickets` ID is actually the recap section; prefer a clearer internal label only if redirects/anchors preserve old links. |
| `/gallery/` | `{{ '/gallery/' | relative_url }}` | Canonical public gallery route. |
| `https://bitcoinfilmfest.com/27` | `{{ '/27/' | relative_url }}` | Canonical fallback is the configured production domain `/27/`. |
| `https://bitcoinfilmfest.com/about/` | `{{ '/about/' | relative_url }}` | Existing Storyboard/About route. |
| `https://bitcoinfilmfest.com/sponsor/` | `{{ '/join/' | relative_url }}` only if the contribution page owns this action. | Otherwise retain a reviewed canonical `/sponsor/` route or remove; do not create a dead link. |
| `press/` | `{{ '/26/press/' | relative_url }}` only if the public child page is migrated. | Fallback to `{{ '/press-and-media/' | relative_url }}`. |
| `prague/` | `{{ '/26/prague/' | relative_url }}` only if the guide is migrated. | Otherwise link to a reviewed external BTC Prague guide or omit stale travel detail. |
| `/26/laurels/` | `{{ '/logos/' | relative_url }}` if the new public logos route exists. | The builder handoff records `/26/laurels/`, `/26/logo/`, and `/26/logos/` as legacy targets intended to redirect to `/logos/`; do not invent a route in this content pass. |
| `/cinema-digest/`, `/press-and-media/`, `/credits` | `{{ '/cinema-digest/' | relative_url }}`, `{{ '/press-and-media/' | relative_url }}`, `{{ '/credits/' | relative_url }}`. | Verify route existence before implementation. |
| `/gallery/thumbs/...` | `{{ '/gallery/thumbs/...' | relative_url }}` if the gallery thumb route is retained. | These are old gallery assets, not BFF'26 event photos. |
| `mailto:hello@bitcoinfilmfest.com` | Preserve as a `mailto:` link. | Public press/contact address; no private address data. |

### External links to preserve as external links

Keep these destinations external and verbatim unless a link check finds a replacement. They do not receive `relative_url`: Kinoteka and venue Google Maps links; Samocentrum; Freedom Lounge; Barstudio; BarBazaar; Park Saski; Słoik; Amondo; MoneroKon (`monerokon.org`) and its schedule; `ordain.art/bff26`; `indeehub.studio`; Run for Hal / Bitcoin Runners; BTC Prague; LeoExpress; Open-Meteo and the timeanddate fallback; Accor and Booking.com; airport and Warsaw public-transport sites; Veturilo; BTC Map; the listed Warsaw restaurants, bars, food halls, breweries, coffee venues and rooftops; all friend/partner websites; public Google My Maps and the public useful-information spreadsheet; forms for volunteering and submissions; public Community Telegram, BFF Telegram, X, Nostr and LinkedIn; past press coverage.

External-link review requirements:

- Recheck commercial prices, schedules, availability, map destinations, and social URLs before republishing them as current advice.
- Keep attendee-gated IndeeHub wording explicit: access is for ticket holders, not a public film stream.
- The public spreadsheet must be reviewed for private rows before it is linked.
- Keep the public Lightning donation address and QR, but never place wallet seeds, API keys, credentials, private contact lists or private databases in this repository.

## Exhaustive unique href inventory

The old page contains **186 href attributes and 115 unique href values**. This table is generated from `BFF26-guest-page/index.html` in first-occurrence order. To match the spec-review count, classification follows the literal old href form: five fragments, three relative same-origin routes (`/gallery/`, `prague/`, `press/`), and **107 external/mailto destinations**. Absolute `bitcoinfilmfest.com` hrefs are therefore listed as `external/mailto` here even when their intended rebuild target is an internal Jekyll route.

The source URL for every row is the old public page: `https://bitcoinfilmfest.com/26/`.

| # | Source URL / line | Unique old href | Link class | Intended target / fallback | Needs rechecking |
|---:|---|---|---|---|---|
| 1 | `https://bitcoinfilmfest.com/26/`<br>index.html:L12 | `https://bitcoinfilmfest.com/26/` | external/mailto | Canonical BFF'26 route: `{{ '/26/' | relative_url }}`; fallback: configured production canonical URL. | Yes — recheck destination, availability, and historical/current status. |
| 2 | `https://bitcoinfilmfest.com/26/`<br>index.html:L32 | `https://fonts.googleapis.com` | external/mailto | Google Fonts dependency; fallback: local/system Courier Prime and Syne Mono stack if the external font service is unavailable. | Yes — recheck destination, availability, and historical/current status. |
| 3 | `https://bitcoinfilmfest.com/26/`<br>index.html:L33 | `https://fonts.gstatic.com` | external/mailto | Google Fonts dependency; fallback: local/system Courier Prime and Syne Mono stack if the external font service is unavailable. | Yes — recheck destination, availability, and historical/current status. |
| 4 | `https://bitcoinfilmfest.com/26/`<br>index.html:L34 | `https://fonts.googleapis.com/css2?family=Syne+Mono&family=Courier+Prime:wght@400;700&display=swap` | external/mailto | Google Fonts dependency; fallback: local/system Courier Prime and Syne Mono stack if the external font service is unavailable. | Yes — recheck destination, availability, and historical/current status. |
| 5 | `https://bitcoinfilmfest.com/26/`<br>index.html:L960 | `#hero` | internal fragment | BFF'26 masthead; fallback: page top if the hero section is renamed. | Yes — confirm the anchor survives the section migration. |
| 6 | `https://bitcoinfilmfest.com/26/`<br>index.html:L961 | `#agenda` | internal fragment | Programme board; fallback: preserve `/26/#agenda` as an alias if the section ID changes. | Yes — confirm the anchor survives the section migration. |
| 7 | `https://bitcoinfilmfest.com/26/`<br>index.html:L962 | `#tickets` | internal fragment | Recap section (the old label points here); fallback: preserve the legacy anchor while removing stale ticket claims. | Yes — confirm the anchor survives the section migration. |
| 8 | `https://bitcoinfilmfest.com/26/`<br>index.html:L963 | `#warsaw` | internal fragment | Warsaw Travel archive section; fallback: keep the section in the edition recap or remove the old anchor deliberately. | Yes — confirm the anchor survives the section migration. |
| 9 | `https://bitcoinfilmfest.com/26/`<br>index.html:L964 | `#bff-friends` | internal fragment | BFF & Friends section; fallback: reviewed `/about/` or `/join/` route if the edition subsection is split out. | Yes — confirm the anchor survives the section migration. |
| 10 | `https://bitcoinfilmfest.com/26/`<br>index.html:L965 | `/gallery/` | same-origin route | `{{ '/gallery/' | relative_url }}`; fallback: omit only if the public gallery route is not migrated. | Yes — confirm the route is migrated and resolves. |
| 11 | `https://bitcoinfilmfest.com/26/`<br>index.html:L966 | `https://bitcoinfilmfest.com/27` | external/mailto | BFF'27 save-the-date: `{{ '/27/' | relative_url }}`; fallback: configured production `/27/` canonical route. | Yes — recheck destination, availability, and historical/current status. |
| 12 | `https://bitcoinfilmfest.com/26/`<br>index.html:L986 | `https://maps.app.goo.gl/sMv2G3qEdweauBd98` | external/mailto | Named venue/location map; fallback: publish the named venue and street address as text if the short link fails. | Yes — recheck destination, availability, and historical/current status. |
| 13 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1055 | `https://maps.app.goo.gl/4qbeGbgEPUg5e9eq7` | external/mailto | Named venue/location map; fallback: publish the named venue and street address as text if the short link fails. | Yes — recheck destination, availability, and historical/current status. |
| 14 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1068 | `https://maps.app.goo.gl/oXYHewuxFzccEzMQ7` | external/mailto | Named venue/location map; fallback: publish the named venue and street address as text if the short link fails. | Yes — recheck destination, availability, and historical/current status. |
| 15 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1069 | `https://maps.app.goo.gl/Xy8dKgXdAr4iiuDu5` | external/mailto | Named venue/location map; fallback: publish the named venue and street address as text if the short link fails. | Yes — recheck destination, availability, and historical/current status. |
| 16 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1070 | `https://maps.app.goo.gl/iwwB4VpW1vzLYGZZ8` | external/mailto | Named venue/location map; fallback: publish the named venue and street address as text if the short link fails. | Yes — recheck destination, availability, and historical/current status. |
| 17 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1071 | `https://cfp.twed.org/mk6/schedule/` | external/mailto | MoneroKon schedule; fallback: the official MoneroKon programme page or a plain co-location note. | Yes — recheck destination, availability, and historical/current status. |
| 18 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1102 | `https://maps.app.goo.gl/XXXKQjmRrdyhJYYL7` | external/mailto | Named venue/location map; fallback: publish the named venue and street address as text if the short link fails. | Yes — recheck destination, availability, and historical/current status. |
| 19 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1111 | `https://maps.app.goo.gl/BLTMLfTmJnDvPUSD7` | external/mailto | Named venue/location map; fallback: publish the named venue and street address as text if the short link fails. | Yes — recheck destination, availability, and historical/current status. |
| 20 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1149 | `https://maps.app.goo.gl/Z8r44KRm4QjCs4yk6` | external/mailto | Named venue/location map; fallback: publish the named venue and street address as text if the short link fails. | Yes — recheck destination, availability, and historical/current status. |
| 21 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1158 | `https://maps.app.goo.gl/1YQBcBXa4Ptfhxao7` | external/mailto | Named venue/location map; fallback: publish the named venue and street address as text if the short link fails. | Yes — recheck destination, availability, and historical/current status. |
| 22 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1180 | `https://ordain.art/bff26` | external/mailto | AI Contest public brief; fallback: post-event result block without a stale submission CTA. | Yes — recheck destination, availability, and historical/current status. |
| 23 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1227 | `https://www.findingsatoshi.com/` | external/mailto | Finding Satoshi public film destination; fallback: reviewed film record or omit if the page is unavailable. | Yes — recheck destination, availability, and historical/current status. |
| 24 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1284 | `https://indeehub.studio` | external/mailto | Attendee-gated IndeeHub archive; fallback: explicitly state that no public stream is available. | Yes — recheck destination, availability, and historical/current status. |
| 25 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1331 | `https://www.monerokon.org/` | external/mailto | MoneroKon partner site; fallback: public co-location/reciprocal-access copy without a partner link. | Yes — recheck destination, availability, and historical/current status. |
| 26 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1348 | `https://forms.gle/zXjGdzRDQQS84pPW8` | external/mailto | Historical talk/film submission form; fallback: current `{{ '/join/' | relative_url }}` or remove the stale CTA. | Yes — recheck destination, availability, and historical/current status. |
| 27 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1383 | `https://bitcoinrunners.org/events/run-for-hal-bitcoin-film-fest-2026/` | external/mailto | Run for Hal event details; fallback: the confirmed activity row with no external CTA. | Yes — recheck destination, availability, and historical/current status. |
| 28 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1385 | `https://www.google.com/maps/d/viewer?mid=1ZvVtzTEnrUo9d4roX1ee55q0uHcDE0o` | external/mailto | Public Bitcoin Walk route map; fallback: route description and start point in text. | Yes — recheck destination, availability, and historical/current status. |
| 29 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1423 | `https://bitcoinfilmfest.com/sponsor/` | external/mailto | Contribution/Friends action: `{{ '/join/' | relative_url }}` if that route owns the action; fallback: reviewed `/sponsor/` or omit. | Yes — recheck destination, availability, and historical/current status. |
| 30 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1612 | `https://www.lotnisko-chopina.pl/en/index.html` | external/mailto | Warsaw arrival/transport information; fallback: dated archive guidance without a dead external link. | Yes — recheck destination, availability, and historical/current status. |
| 31 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1613 | `https://en.modlinairport.pl/` | external/mailto | Warsaw arrival/transport information; fallback: dated archive guidance without a dead external link. | Yes — recheck destination, availability, and historical/current status. |
| 32 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1614 | `https://www.wtp.waw.pl/en/public-transport-step-by-step/` | external/mailto | Warsaw arrival/transport information; fallback: dated archive guidance without a dead external link. | Yes — recheck destination, availability, and historical/current status. |
| 33 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1616 | `https://veturilo.waw.pl/en/` | external/mailto | Warsaw arrival/transport information; fallback: dated archive guidance without a dead external link. | Yes — recheck destination, availability, and historical/current status. |
| 34 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1631 | `https://www.facebook.com/BarBazaarPraga/` | external/mailto | Warsaw Bitcoin-friendly venue/map reference; fallback: venue name, address and dated note without the link. | Yes — recheck destination, availability, and historical/current status. |
| 35 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1633 | `https://btcmap.org/map#8/52.30198/21.39621` | external/mailto | Warsaw Bitcoin-friendly venue/map reference; fallback: venue name, address and dated note without the link. | Yes — recheck destination, availability, and historical/current status. |
| 36 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1651 | `https://open-meteo.com` | external/mailto | Weather-data provider attribution for the historical widget; fallback: remove the live widget and retain only a labelled historical note. | Yes — recheck destination, availability, and historical/current status. |
| 37 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1681 | `https://www.timeanddate.com/weather/poland/warsaw/ext` | external/mailto | Historical weather fallback; fallback: labelled archive note with no live forecast claim. | Yes — recheck destination, availability, and historical/current status. |
| 38 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1689 | `mailto:hello@bitcoinfilmfest.com` | external/mailto | Public BFF contact/press mailbox; fallback: the reviewed public contact channel, never a private address. | Yes — recheck destination, availability, and historical/current status. |
| 39 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1701 | `https://all.accor.com/hotel/3385/index.en.shtml?dateIn=20260604&amp;nights=3&amp;compositions=2` | external/mailto | Historical hotel booking destination; fallback: hotel name and dated proximity note without volatile prices or availability. | Yes — recheck destination, availability, and historical/current status. |
| 40 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1702 | `https://www.booking.com/hotel/pl/mercure-warszawa-centrum.html?checkin=2026-06-04&amp;checkout=2026-06-07&amp;group_adults=2` | external/mailto | Historical hotel booking destination; fallback: hotel name and dated proximity note without volatile prices or availability. | Yes — recheck destination, availability, and historical/current status. |
| 41 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1715 | `https://all.accor.com/hotel/3383/index.en.shtml?dateIn=20260604&amp;nights=3&amp;compositions=2` | external/mailto | Historical hotel booking destination; fallback: hotel name and dated proximity note without volatile prices or availability. | Yes — recheck destination, availability, and historical/current status. |
| 42 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1716 | `https://www.booking.com/hotel/pl/novotelwarszawacentrumwarszawa.html?checkin=2026-06-04&amp;checkout=2026-06-07&amp;group_adults=2` | external/mailto | Historical hotel booking destination; fallback: hotel name and dated proximity note without volatile prices or availability. | Yes — recheck destination, availability, and historical/current status. |
| 43 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1727 | `https://btcprague.com` | external/mailto | Related BTC Prague/transport destination; fallback: dated route guidance without price claims. | Yes — recheck destination, availability, and historical/current status. |
| 44 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1728 | `https://leoexpress.com` | external/mailto | Related BTC Prague/transport destination; fallback: dated route guidance without price claims. | Yes — recheck destination, availability, and historical/current status. |
| 45 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1729 | `prague/` | same-origin route | `{{ '/26/prague/' | relative_url }}` if migrated; fallback: approved public BTC Prague guide or omit the historical travel detail. | Yes — confirm the route is migrated and resolves. |
| 46 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1742 | `https://www.facebook.com/samo.centrum.warszawa/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 47 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1743 | `https://kinoamondo.pl/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 48 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1749 | `https://restauracjastarydom.pl/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 49 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1750 | `https://www.restauracjarozana.com.pl/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 50 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1751 | `https://www.facebook.com/zapiecekpolskiepierogranie` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 51 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1752 | `https://gosciniec.waw.pl/restauracje/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 52 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1753 | `https://www.mateuszgessler.com.pl/restauracje/warszawski-sen/index.html#txt-2col-189252` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 53 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1759 | `https://www.facebook.com/people/Bar_mleczny_lindleya14/100063597881245/` | external/mailto | Preserve the named public destination as an external link; fallback: plain-text reference or omit after editorial review. | Yes — recheck destination, availability, and historical/current status. |
| 54 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1760 | `https://barbambino.pl/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 55 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1761 | `https://wanderlog.com/place/details/4185537/marsza%C5%82kowski-bar-mleczny` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 56 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1767 | `https://the-farm.pl/en/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 57 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1768 | `https://butcheryandwine.pl/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 58 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1769 | `https://primecut.pl/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 59 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1775 | `https://nonna.com.pl/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 60 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1776 | `https://www.google.com/maps/place/Pizzaiolo+Pawilony/@52.2330557,21.0180012,17z/data=!3m1!4b1!4m6!3m5!1s0x471ecd3aa9d79679:0xa4f6aa2853d5ec8f!8m2!3d52.2330524!4d21.0205761!16s%2Fg%2F11l6tks3cd?hl=en&amp;entry=ttu` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 61 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1782 | `https://koszyki.com/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 62 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1783 | `https://elektrowniapowisle.com/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 63 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1784 | `https://fabrykanorblina.pl/en/norblin-factory/#o-projekcie` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 64 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1785 | `https://browarywarszawskie.com.pl/en/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 65 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1791 | `https://bier-traveller.com/polska-poland/warszawa/piwpaw-beer-heaven-warszawa/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 66 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1792 | `https://craftbeernomads.com/craft-beer-in-poland-browar-pinta-and-pinta-barrel-brewing/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 67 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1793 | `https://www.facebook.com/HoppinessMultitap/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 68 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1799 | `https://www.etnocafe.pl/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 69 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1800 | `https://www.greencaffenero.pl/pl/menu` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 70 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1801 | `https://nabank.pl/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 71 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1807 | `https://www.panoramaskybar.pl/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 72 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1808 | `https://theroofskybar.com/en/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 73 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1814 | `https://www.zachodnibrzeg.pl/` | external/mailto | Warsaw food/drink recommendation; fallback: retain the named place as dated archive text only if the destination or current status cannot be confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 74 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1833 | `https://www.google.com/maps/d/u/1/edit?mid=1GwJ2MIAILS0DmNwZLM26ATdJgwnronI&usp=sharing` | external/mailto | Public festival locations map; fallback: safe public viewer link or omit if permissions expose editing/private data. | Yes — recheck destination, availability, and historical/current status. |
| 75 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1835 | `https://docs.google.com/spreadsheets/d/1929mDtpqGcAasJp-byDj0PcD3JjXNz7lHJTasJyKzM8/edit?usp=sharing` | external/mailto | Public useful-information spreadsheet; fallback: omit until public rows are reviewed and the sheet remains accessible. | Yes — recheck destination, availability, and historical/current status. |
| 76 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1855 | `https://bitcoinfilmfest.com/about/` | external/mailto | About/Story route: `{{ '/about/' | relative_url }}`; fallback: edition context text without a duplicate route. | Yes — recheck destination, availability, and historical/current status. |
| 77 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1875 | `https://cashify.eu` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 78 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1876 | `https://thebitcoindistrict.com` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 79 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1877 | `https://bitcoin.org.pl` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 80 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1878 | `https://quark.house` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 81 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1879 | `https://bitcoinvn.io` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 82 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1880 | `https://angor.io` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 83 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1881 | `https://orangefren.com` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 84 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1882 | `https://kinoteka.pl` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 85 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1884 | `https://ghostswap.io` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 86 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1900 | `https://trezor.io` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 87 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1901 | `https://satsback.com` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 88 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1902 | `https://studentsforliberty.org` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 89 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1903 | `https://bitcoin.pl` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 90 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1904 | `https://cryptosteel.com` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 91 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1905 | `https://bahamafilms.pl` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 92 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1906 | `https://comparic.pl` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 93 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1907 | `https://bujac.pl` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 94 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1908 | `https://bitblik.app` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 95 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1909 | `https://finonity.com` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 96 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1910 | `https://www.instagram.com/samo_centrum/` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 97 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1911 | `https://lightningpiggy.com` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 98 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1913 | `https://www.bitcoinforthearts.org/` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 99 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1914 | `https://bitrefill.com` | external/mailto | Public friend/partner destination; fallback: retain the friend name/logo without a link if the site has moved or is not confirmed. | Yes — recheck destination, availability, and historical/current status. |
| 100 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1961 | `https://cointelegraph.com/news/bitcoin-film-fest-bitcoin-cinema-hits-warsaw` | external/mailto | Past press/coverage article; fallback: cite the publication in plain text if the article is unavailable. | Yes — recheck destination, availability, and historical/current status. |
| 101 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1962 | `https://blog.bitfinex.com/announcements/what-is-the-bitcoin-film-fest/` | external/mailto | Past press/coverage article; fallback: cite the publication in plain text if the article is unavailable. | Yes — recheck destination, availability, and historical/current status. |
| 102 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1963 | `https://bitcoinnews.com/press-release/bitcoin-filmfest-2025-beyond-the-frame/` | external/mailto | Past press/coverage article; fallback: cite the publication in plain text if the article is unavailable. | Yes — recheck destination, availability, and historical/current status. |
| 103 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1964 | `https://thecryptoradio.com/Bitcoin-FilmFest-2025-Stories-no-one-else-is-telling` | external/mailto | Past press/coverage article; fallback: cite the publication in plain text if the article is unavailable. | Yes — recheck destination, availability, and historical/current status. |
| 104 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1965 | `https://www.jeffreypeel.com/p/bitcoin-filmfest` | external/mailto | Past press/coverage article; fallback: cite the publication in plain text if the article is unavailable. | Yes — recheck destination, availability, and historical/current status. |
| 105 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1966 | `https://bitcoinfilmfest.com/cinema-digest/` | external/mailto | `{{ '/cinema-digest/' | relative_url }}`; fallback: plain-text publication reference if the route is not migrated. | Yes — recheck destination, availability, and historical/current status. |
| 106 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1967 | `https://bitcoinfilmfest.com/press-and-media/` | external/mailto | `{{ '/press-and-media/' | relative_url }}`; fallback: `{{ '/26/press/' | relative_url }}` only when the child page exists. | Yes — recheck destination, availability, and historical/current status. |
| 107 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1971 | `press/` | same-origin route | `{{ '/26/press/' | relative_url }}` if migrated; fallback: `{{ '/press-and-media/' | relative_url }}`. | Yes — confirm the route is migrated and resolves. |
| 108 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1972 | `https://bitcoinfilmfest.com/26/laurels/` | external/mailto | Approved public logos/laurels destination, likely `{{ '/logos/' | relative_url }}`; fallback: reviewed legacy redirect, never an invented route. | Yes — recheck destination, availability, and historical/current status. |
| 109 | `https://bitcoinfilmfest.com/26/`<br>index.html:L1984 | `https://forms.gle/Atsj6bsyP7twyBxX8` | external/mailto | Historical subscribe form; fallback: current reviewed subscription/contribution route or remove. | Yes — recheck destination, availability, and historical/current status. |
| 110 | `https://bitcoinfilmfest.com/26/`<br>index.html:L2018 | `https://t.me/+yfXLveSIRsw3YTJk` | external/mailto | Public BFF community/social destination; fallback: current public social/contact index. | Yes — recheck destination, availability, and historical/current status. |
| 111 | `https://bitcoinfilmfest.com/26/`<br>index.html:L2018 | `https://x.com/bitcoinfilmfest` | external/mailto | Public BFF community/social destination; fallback: current public social/contact index. | Yes — recheck destination, availability, and historical/current status. |
| 112 | `https://bitcoinfilmfest.com/26/`<br>index.html:L2050 | `https://t.me/+_fTPO9H0SS0yMTQ0` | external/mailto | Public BFF community/social destination; fallback: current public social/contact index. | Yes — recheck destination, availability, and historical/current status. |
| 113 | `https://bitcoinfilmfest.com/26/`<br>index.html:L2050 | `https://njump.me/npub1rjtrs7xqdvj3588r9njrexh2n750j7jdwx9qs543nutmdsj6ljaqpfmp8a` | external/mailto | Public BFF community/social destination; fallback: current public social/contact index. | Yes — recheck destination, availability, and historical/current status. |
| 114 | `https://bitcoinfilmfest.com/26/`<br>index.html:L2050 | `https://www.linkedin.com/company/bitcoin-filmfest` | external/mailto | Public BFF community/social destination; fallback: current public social/contact index. | Yes — recheck destination, availability, and historical/current status. |
| 115 | `https://bitcoinfilmfest.com/26/`<br>index.html:L2097 | `https://bitcoinfilmfest.com/credits` | external/mailto | `{{ '/credits/' | relative_url }}`; fallback: shared footer credits route after confirming the trailing-slash redirect. | Yes — recheck destination, availability, and historical/current status. |

## Old-page local asset inventory

Every old-page local asset reference is under the `26-assets/` namespace or the legacy `/gallery/` namespace. The rebuild may copy only approved public BFF assets into the Jekyll asset tree. Query-string cache busters such as `?v=14` are not separate files and should not be carried into canonical asset filenames.

### Shared and metadata assets

- `26-assets/og-poster.jpg` (including old `?v=22` reference)
- `26-assets/bff-logo.png`
- `26-assets/rabbit.png` (old `?v=15` reference)
- `26-assets/seats.png`
- `26-assets/lightning-qr.png` (old `?v=1` reference)
- `26-assets/satellite/side-events.png` (old `?v=49` reference)

### CSS background photos

- `26-assets/photos/bff25-143-bg.jpg` - hero background
- `26-assets/photos/bff25-72-bg.jpg` - Warsaw section background
- `26-assets/photos/bff25-23-bg.jpg` - BFF & Friends background

### Content photos and closing/gallery strip photos

- `26-assets/photos/bff23-4.jpg`
- `26-assets/photos/bff23-7.jpg` (old `?v=21` reference)
- `26-assets/photos/bff25-23.jpg`
- `26-assets/photos/bff25-68.jpg`
- `26-assets/photos/bff25-76.jpg`
- `26-assets/photos/bff25-126.jpg` (old `?v=23` reference)
- `26-assets/photos/bff25-143.jpg` (old `?v=32` reference)
- `26-assets/photos/thumbs/e24-06.jpg`
- `26-assets/photos/thumbs/e24-21.jpg`
- `26-assets/photos/thumbs/e25-04.jpg`
- `26-assets/photos/thumbs/e25-06.jpg`
- `26-assets/photos/thumbs/e25-11.jpg`

### Dynamic hero thumbnail pool referenced by old inline JavaScript

The old page constructs `/gallery/thumbs/<id>.jpg` at runtime from this complete pool. Treat every item as a local dependency even when it is not in the initial HTML:

- `e24-01` through `e24-21` (`/gallery/thumbs/e24-01.jpg` ... `/gallery/thumbs/e24-21.jpg`)
- `e25-01` through `e25-11` (`/gallery/thumbs/e25-01.jpg` ... `/gallery/thumbs/e25-11.jpg`)

The initial six displayed examples are `e25-04`, `e24-06`, `e25-06`, `e24-21`, `e25-11`, and `e24-13`.

### Dynamic BFF & Friends photo pool referenced by old inline JavaScript

The community image can be replaced at runtime from this local pool:

- `26-assets/photos/bff25-23.jpg`
- `26-assets/photos/bff25-126.jpg`
- `26-assets/photos/bff25-68.jpg`
- `26-assets/photos/bff25-76.jpg`
- `26-assets/photos/bff25-102.jpg`
- `26-assets/photos/bff25-108.jpg`
- `26-assets/photos/bff23-1.jpg`
- `26-assets/photos/bff23-2.jpg`
- `26-assets/photos/bff23-5.jpg`
- `26-assets/photos/bff23-7.jpg`
- `26-assets/photos/e24-08.jpg`
- `26-assets/photos/e24-13.jpg`
- `26-assets/photos/e25-03.jpg`
- `26-assets/photos/e25-07.jpg`

### Partner/friend logo assets

The old page references these local logo files in featured and regular marquees. The featured/regular duplicate markup points to the same files; list each file once:

- `26-assets/logos/amondo.png`
- `26-assets/logos/angor.png`
- `26-assets/logos/bahama-films.png`
- `26-assets/logos/bitblik.png`
- `26-assets/logos/bitcoin-district.png`
- `26-assets/logos/bitcoin-for-the-arts.png`
- `26-assets/logos/bitcoinpl.png`
- `26-assets/logos/bitcoinvn.png`
- `26-assets/logos/bitrefill.png`
- `26-assets/logos/bujac.png`
- `26-assets/logos/cashify.png`
- `26-assets/logos/comparic.png`
- `26-assets/logos/cryptosteel.png`
- `26-assets/logos/finonity.png`
- `26-assets/logos/ghostswap.png`
- `26-assets/logos/indeehub.png`
- `26-assets/logos/kinoteka.png`
- `26-assets/logos/lightning-piggy.png`
- `26-assets/logos/orangefren.png`
- `26-assets/logos/polskie-stowarzyszenie-bitcoin.png`
- `26-assets/logos/quark.png`
- `26-assets/logos/samocentrum.png`
- `26-assets/logos/satsback.png`
- `26-assets/logos/students-for-liberty.png`
- `26-assets/logos/trezor.png`

Old version suffixes include `?v=14`, `?v=23`, `?v=26`, `?v=33`, `?v=34`, and `?v=35`; preserve only if the asset pipeline genuinely needs cache invalidation.

## Public source asset total and deterministic copied-file manifest

The approved public source asset copy is `site/26/26-assets/`. Its exact total is **126 files and 15,916,490 bytes (15916490 bytes)**. The manifest below is deterministic: relative paths are sorted lexicographically using POSIX separators, and byte sizes are read from the copied files. Query-string cache busters in the old page do not create additional files.

| # | Relative path | Bytes | MIME type |
|---:|---|---:|---|
| 1 | `bff-logo.png` | 68604 | `image/png` |
| 2 | `bff26-poster.jpg` | 72739 | `image/jpeg` |
| 3 | `lightning-qr.png` | 1993 | `image/png` |
| 4 | `logos/amondo.png` | 22335 | `image/png` |
| 5 | `logos/angor.png` | 23075 | `image/png` |
| 6 | `logos/bahama-films.png` | 62737 | `image/png` |
| 7 | `logos/bitblik.png` | 6772 | `image/png` |
| 8 | `logos/bitblik.svg` | 531 | `image/svg+xml` |
| 9 | `logos/bitcoin-district.png` | 27467 | `image/png` |
| 10 | `logos/bitcoin-for-the-arts.png` | 54305 | `image/png` |
| 11 | `logos/bitcoin-poland.png` | 15154 | `image/png` |
| 12 | `logos/bitcoinpl.png` | 32772 | `image/png` |
| 13 | `logos/bitcoinvn.png` | 17246 | `image/png` |
| 14 | `logos/bitomat.png` | 48864 | `image/png` |
| 15 | `logos/bitrefill.png` | 28922 | `image/png` |
| 16 | `logos/bujac.png` | 33844 | `image/png` |
| 17 | `logos/cashify.png` | 72251 | `image/png` |
| 18 | `logos/comparic.png` | 23448 | `image/png` |
| 19 | `logos/cryptosteel.png` | 26172 | `image/png` |
| 20 | `logos/finonity.png` | 30904 | `image/png` |
| 21 | `logos/freedom-publishing.png` | 22387 | `image/png` |
| 22 | `logos/ghostswap.png` | 7446 | `image/png` |
| 23 | `logos/indeehub.png` | 55472 | `image/png` |
| 24 | `logos/kinoteka.png` | 15183 | `image/png` |
| 25 | `logos/lightning-piggy.png` | 84379 | `image/png` |
| 26 | `logos/orangefren.png` | 81924 | `image/png` |
| 27 | `logos/polskie-stowarzyszenie-bitcoin.png` | 34842 | `image/png` |
| 28 | `logos/quark.png` | 64915 | `image/png` |
| 29 | `logos/samocentrum.png` | 39465 | `image/png` |
| 30 | `logos/satsback.png` | 27642 | `image/png` |
| 31 | `logos/students-for-liberty.png` | 51373 | `image/png` |
| 32 | `logos/trezor.png` | 10688 | `image/png` |
| 33 | `og-poster.jpg` | 77418 | `image/jpeg` |
| 34 | `photos/bff23-1.jpg` | 257869 | `image/jpeg` |
| 35 | `photos/bff23-2.jpg` | 220447 | `image/jpeg` |
| 36 | `photos/bff23-3.jpg` | 232788 | `image/jpeg` |
| 37 | `photos/bff23-4.jpg` | 167111 | `image/jpeg` |
| 38 | `photos/bff23-5.jpg` | 284337 | `image/jpeg` |
| 39 | `photos/bff23-6.jpg` | 131089 | `image/jpeg` |
| 40 | `photos/bff23-7.jpg` | 153536 | `image/jpeg` |
| 41 | `photos/bff23-8.jpg` | 93178 | `image/jpeg` |
| 42 | `photos/bff23-9.jpg` | 226299 | `image/jpeg` |
| 43 | `photos/bff25-102.jpg` | 101280 | `image/jpeg` |
| 44 | `photos/bff25-108.jpg` | 162816 | `image/jpeg` |
| 45 | `photos/bff25-126.jpg` | 212545 | `image/jpeg` |
| 46 | `photos/bff25-143-bg.jpg` | 109273 | `image/jpeg` |
| 47 | `photos/bff25-143.jpg` | 253515 | `image/jpeg` |
| 48 | `photos/bff25-23-bg.jpg` | 131753 | `image/jpeg` |
| 49 | `photos/bff25-23.jpg` | 316228 | `image/jpeg` |
| 50 | `photos/bff25-27.jpg` | 203783 | `image/jpeg` |
| 51 | `photos/bff25-68.jpg` | 223247 | `image/jpeg` |
| 52 | `photos/bff25-72-bg.jpg` | 133415 | `image/jpeg` |
| 53 | `photos/bff25-72.jpg` | 297670 | `image/jpeg` |
| 54 | `photos/bff25-76.jpg` | 141848 | `image/jpeg` |
| 55 | `photos/bff25-hero.jpg` | 504310 | `image/jpeg` |
| 56 | `photos/e24-01.jpg` | 176643 | `image/jpeg` |
| 57 | `photos/e24-02.jpg` | 395217 | `image/jpeg` |
| 58 | `photos/e24-03.jpg` | 337044 | `image/jpeg` |
| 59 | `photos/e24-04.jpg` | 84216 | `image/jpeg` |
| 60 | `photos/e24-05.jpg` | 182443 | `image/jpeg` |
| 61 | `photos/e24-06.jpg` | 182751 | `image/jpeg` |
| 62 | `photos/e24-07.jpg` | 219412 | `image/jpeg` |
| 63 | `photos/e24-08.jpg` | 276335 | `image/jpeg` |
| 64 | `photos/e24-09.jpg` | 195927 | `image/jpeg` |
| 65 | `photos/e24-10.jpg` | 239599 | `image/jpeg` |
| 66 | `photos/e24-11.jpg` | 210583 | `image/jpeg` |
| 67 | `photos/e24-12.jpg` | 281150 | `image/jpeg` |
| 68 | `photos/e24-13.jpg` | 310947 | `image/jpeg` |
| 69 | `photos/e24-14.jpg` | 249545 | `image/jpeg` |
| 70 | `photos/e24-15.jpg` | 301662 | `image/jpeg` |
| 71 | `photos/e24-16.jpg` | 397947 | `image/jpeg` |
| 72 | `photos/e24-17.jpg` | 255572 | `image/jpeg` |
| 73 | `photos/e24-18.jpg` | 324881 | `image/jpeg` |
| 74 | `photos/e24-19.jpg` | 271214 | `image/jpeg` |
| 75 | `photos/e24-20.jpg` | 399953 | `image/jpeg` |
| 76 | `photos/e24-21.jpg` | 314955 | `image/jpeg` |
| 77 | `photos/e25-01.jpg` | 123136 | `image/jpeg` |
| 78 | `photos/e25-02.jpg` | 386968 | `image/jpeg` |
| 79 | `photos/e25-03.jpg` | 314735 | `image/jpeg` |
| 80 | `photos/e25-04.jpg` | 310409 | `image/jpeg` |
| 81 | `photos/e25-05.jpg` | 195271 | `image/jpeg` |
| 82 | `photos/e25-06.jpg` | 236149 | `image/jpeg` |
| 83 | `photos/e25-07.jpg` | 203921 | `image/jpeg` |
| 84 | `photos/e25-08.jpg` | 189314 | `image/jpeg` |
| 85 | `photos/e25-09.jpg` | 234668 | `image/jpeg` |
| 86 | `photos/e25-10.jpg` | 265631 | `image/jpeg` |
| 87 | `photos/e25-11.jpg` | 384370 | `image/jpeg` |
| 88 | `photos/thumbs/e24-01.jpg` | 35360 | `image/jpeg` |
| 89 | `photos/thumbs/e24-02.jpg` | 46538 | `image/jpeg` |
| 90 | `photos/thumbs/e24-03.jpg` | 38858 | `image/jpeg` |
| 91 | `photos/thumbs/e24-04.jpg` | 17324 | `image/jpeg` |
| 92 | `photos/thumbs/e24-05.jpg` | 33761 | `image/jpeg` |
| 93 | `photos/thumbs/e24-06.jpg` | 25030 | `image/jpeg` |
| 94 | `photos/thumbs/e24-07.jpg` | 32541 | `image/jpeg` |
| 95 | `photos/thumbs/e24-08.jpg` | 33189 | `image/jpeg` |
| 96 | `photos/thumbs/e24-09.jpg` | 32200 | `image/jpeg` |
| 97 | `photos/thumbs/e24-10.jpg` | 31295 | `image/jpeg` |
| 98 | `photos/thumbs/e24-11.jpg` | 25566 | `image/jpeg` |
| 99 | `photos/thumbs/e24-12.jpg` | 42549 | `image/jpeg` |
| 100 | `photos/thumbs/e24-13.jpg` | 46592 | `image/jpeg` |
| 101 | `photos/thumbs/e24-14.jpg` | 35257 | `image/jpeg` |
| 102 | `photos/thumbs/e24-15.jpg` | 38712 | `image/jpeg` |
| 103 | `photos/thumbs/e24-16.jpg` | 46439 | `image/jpeg` |
| 104 | `photos/thumbs/e24-17.jpg` | 35370 | `image/jpeg` |
| 105 | `photos/thumbs/e24-18.jpg` | 36307 | `image/jpeg` |
| 106 | `photos/thumbs/e24-19.jpg` | 32923 | `image/jpeg` |
| 107 | `photos/thumbs/e24-20.jpg` | 34196 | `image/jpeg` |
| 108 | `photos/thumbs/e24-21.jpg` | 37859 | `image/jpeg` |
| 109 | `photos/thumbs/e25-01.jpg` | 17861 | `image/jpeg` |
| 110 | `photos/thumbs/e25-02.jpg` | 43790 | `image/jpeg` |
| 111 | `photos/thumbs/e25-03.jpg` | 47125 | `image/jpeg` |
| 112 | `photos/thumbs/e25-04.jpg` | 45269 | `image/jpeg` |
| 113 | `photos/thumbs/e25-05.jpg` | 30211 | `image/jpeg` |
| 114 | `photos/thumbs/e25-06.jpg` | 38722 | `image/jpeg` |
| 115 | `photos/thumbs/e25-07.jpg` | 26511 | `image/jpeg` |
| 116 | `photos/thumbs/e25-08.jpg` | 21455 | `image/jpeg` |
| 117 | `photos/thumbs/e25-09.jpg` | 32819 | `image/jpeg` |
| 118 | `photos/thumbs/e25-10.jpg` | 38627 | `image/jpeg` |
| 119 | `photos/thumbs/e25-11.jpg` | 49555 | `image/jpeg` |
| 120 | `promo/bff26-promo-300x250.png` | 24382 | `image/png` |
| 121 | `promo/bff26-promo-horizontal-full.png` | 107242 | `image/png` |
| 122 | `promo/bff26-promo-horizontal.png` | 107242 | `image/png` |
| 123 | `rabbit.png` | 19815 | `image/png` |
| 124 | `satellite/side-events.png` | 102959 | `image/png` |
| 125 | `seats.png` | 96434 | `image/png` |
| 126 | `trezor-mark.png` | 74431 | `image/png` |

## Public/private boundary

### Explicitly excluded surfaces and files

The public copy explicitly excludes these deployment, backend, administrative, or private surfaces/files: `upload.py`; `slides/`; `support/`; `audiencevote/`; `wintrezor/`; `winchimney/`; `_archive/`; Python caches (`__pycache__/`, `*.pyc`, `*.pyo`); PHP files (`*.php`); `.htaccess`; `admin_key.txt`; and FTP configuration (including FTP credentials/settings files). These exclusions apply even when a file is present in the source tree or is not linked by the old page.


This content map is for a **public repository and public website**. The public projection may contain only reviewed BFF'26 copy, public facts, public links, approved 26-assets, and deliberately public donation/contact destinations.

Copy only **26-assets** and approved public page content. Never deploy or copy **scripts, credentials, PHP/photo backend code, caches, archives, private CRM/contact data, raw ticket or attendee exports, private film/licensing records, private databases, or internal planning files** into the public site or its generated output. The old inline scripts are implementation references only; the new Jekyll page must use the shared shell and approved site components. A public repo is not a safe place for source material merely because it is not linked from navigation.

## Acceptance checklist for the next worker

- [ ] Page order follows the ordered map above, from BFF'27 banner and hero through agenda, recap, voices, gallery, Warsaw, BFF & Friends, and shared footer.
- [ ] BFF'26 is described as June 4-7, 2026, Warsaw, Kinoteka.
- [ ] The final public headline says 16 films and resolves the old 18-title conflict.
- [ ] Country wording is resolved against the source note and the required 15+ acceptance criterion.
- [ ] Golden Rabbits winners and the no-Best-Story outcome are correct.
- [ ] AI contest title, 2.5M-sat pool, 1.5M-sat Naritamoto result and rollover are correct.
- [ ] MoneroKon is described as co-located, reciprocal-access, and still separate from BFF's Bitcoin-only identity.
- [ ] BFF'27 is June 24-27, 2027, Warsaw, with a working internal link.
- [ ] All old-page local asset references, including dynamic pools and CSS backgrounds, are accounted for.
- [ ] Internal links use `relative_url` or an explicitly reviewed canonical fallback; external links stay external.
- [ ] No scripts, credentials, PHP/photo backend, caches, archives or private source data enter the public page.

# BFF25 content and asset map

Status: local-only preview for canonical `/25/`; `/bff25/` is preserved as a compatibility redirect. No deployment, publication, commit or push was performed.

## Source provenance

| Source | Use in preview |
|---|---|
| `website/static-site/_preview/bff25.html` | Recovered visual rhythm, original agenda labels, historical CTA/context and public partner names. The standalone shell was not copied. |
| `website/static-site/_source/content/bff25.md` | Clean page copy, programme, sponsor/friend links, selection inventory and public context. |
| `website/static-site/_source/content/part-one-official-selection-feature-films-at-bff25.md` | Public feature details for UNBANKABLE, REVOLUCIÓN BITCOIN, HOTEL BITCOIN and NO MORE INFLATION. |
| `website/static-site/_source/content/part-two-official-selection-experimental-shorts-at-bff25.md` | Public short details for SATOSHI: THE CREATION OF BITCOIN, BITCOIN IS THE MYCELIUM OF MONEY and STRANGE CURRENCIES. |
| `BFF25/` | Poster, PoWies artwork and curated public event photographs. PSD, OTF, ZIP, MOV and private material were not copied. |
| `Claude news/BFF-partner-logos/` | Eight public partner logo files used where the BFF25 source-listed logo was available offline. This folder supplied artwork only; no private notes or contact data were used. |

## Wayback references consulted for reconciliation

- Post-event snapshot: <https://web.archive.org/web/20251030185443/https://bitcoinfilmfest.com/bff25/>
- Pre-event snapshot: <https://web.archive.org/web/20250219055248/https://bitcoinfilmfest.com/bff25/>
- May snapshot: <https://web.archive.org/web/20250514141751/https://bitcoinfilmfest.com/bff25/?ref=lnnews>

The archive references are retained as provenance links. Direct Wayback extraction was unavailable in this environment because the web extraction provider returned an account credit-limit error; the local recovered sources and the supplied event facts were used for the page content.

## Public/private boundary

Included only in the deployable bundle:

- Public festival poster, PoWies award artwork, public partner logos and a curated set of public event photographs.
- Public film titles, programme details, public director/producer names, public sponsor/friend names and public links from the recovered page sources.

Explicitly excluded:

- `BFF25/BFF 25 fotki.zip` and the uncurated full-resolution photo folder.
- `BFF25/Beyond the frame bff25.psd` and `BFF25/PoWIes 2025/*.psd` source files.
- `BFF25/PoWIes 2025/*.otf` and font ZIP archives.
- `BFF25/BFF 25 fotki.zip` and all other ZIP archives.
- `BFF25/nagrania 2140 i Rob/Rob LeRican standup BFF25/*.mov` video.
- `BFF25/BFF25 telegram chat.png` private chat screenshot.
- `BFF25/BFF 23-25.05.pdf` source document (not needed by the page).
- Credentials, private databases, contact lists, internal research notes and any private material outside the public source boundary.

## Exact local asset manifest

Destination: `site/25/25-assets/`

The bundle contains **42 files / 17,540,385 bytes**: one poster, two PoWies artworks, eight partner logos, nine previously curated website photos, and **22 newly added event photographs** from the large `BFF 25 fotki/BFF25/` folder. The event-photo addition stays within the requested 12–24 representative-photo range. The 22 event files are resized JPEG derivatives, normally 2200 px on the long edge, to keep the preview practical while retaining usable quality. The two previously oversized 7008 px PNG photo derivatives were also re-encoded as 2400 px JPEGs.

The exact byte total is verified by `scripts/check_bff25_page.py`; do not hand-edit this total without rerunning the validator.

### Destination-to-source mapping

- `bff25-poster.png` ← `BFF25/BFF25 Plakat horizontal lowq.png`
- `powies-2.png` ← `BFF25/PoWIes 2025/Powies 2.png`
- `pow.png` ← `BFF25/PoWIes 2025/PoW.png`
- `photo-102.png`, `photo-126.png`, `photo-143.png`, `photo-23.png`, `photo-27.png`, `photo-68.png`, and `photo-76.png` ← matching public files in `BFF25/Photos for website/` (the `.png` derivatives are used in the page)
- `photo-108.jpg`, `photo-72.jpg` ← matching public files in `BFF25/Photos for website/`, resized/re-encoded to 2400 × 1600 JPEG derivatives for the page.
- `event-002.jpg`, `event-010.jpg`, `event-011.jpg`, `event-016.jpg`, `event-026.jpg`, `event-028.jpg`, `event-034.jpg`, `event-039.jpg`, `event-049.jpg`, `event-050.jpg`, `event-055.jpg`, `event-061.jpg`, `event-067.jpg`, `event-071.jpg`, `event-077.jpg`, `event-082.jpg`, `event-084.jpg`, `event-089.jpg`, `event-107.jpg`, `event-124.jpg`, `event-142.jpg`, `event-155.jpg` ← `BFF25/BFF 25 fotki/BFF25/BFF25-2.jpg`, `BFF25-10.jpg`, `BFF25-11.jpg`, `BFF25-16.jpg`, `BFF25-26.jpg`, `BFF25-28.jpg`, `BFF25-34.jpg`, `BFF25-39.jpg`, `BFF25-49.jpg`, `BFF25-50.jpg`, `BFF25-55.jpg`, `BFF25-61.jpg`, `BFF25-67.jpg`, `BFF25-71.jpg`, `BFF25-77.jpg`, `BFF25-82.jpg`, `BFF25-84.jpg`, `BFF25-89.jpg`, `BFF25-107.jpg`, `BFF25-124.jpg`, `BFF25-142.jpg`, and `BFF25-155.jpg`, respectively. These are local derivatives, not hotlinks to the source folder.
- `partner-alby.png`, `partner-angor.png`, `partner-bitcoinvn.png`, `partner-cryptosteel.png`, `partner-geyser.png`, `partner-indeehub.png`, `partner-kinoteka.png`, `partner-quark.png` ← matching public files in `Claude news/BFF-partner-logos/`

There are 42 distinct files and 43 local references. `photo-23.png` is used twice: once as the Day 0 contextual photograph and once in the photo record.

## Missing or intentionally unbundled public assets

The recovered Markdown references these public files, but matching local files were not present in the offline BFF25 folder and no remote dependency was added:

- Event/page artwork: `BFF-event-laurels.png`, `Bitcoin-Pizza-Day.png`, `pitching-rabbits-1.png`, `Gm-Amondo.png`, the party illustration/photo, `BFF25 Newsletter_June 2024` artwork.
- Feature artwork: `Unbankable-film-by-Luke-Willms-BFF25-Official-Selection.png`, `Revolucion-Bitcoin-film-by-Juan-Pablo-BFF25-Official-Selection.png`, `Hotel-Bitcoin-film-by-Manuel-Sanabria-and-Carlos-Villaverde-BFF25-Official-Selection.png`, `No-More-Inflation-POSTER-scaled.jpg`, and the four selected-scenes images.
- Short artwork: `BFF-25-bitcoin-filmfest-2025-AI-generated-shorts.png`, the three short poster files and the two Satoshi selected-scenes images.
- Source page identity/social artwork: `BFF-logo-white.png`, `Mr-Rabbit.png`, X/Telegram/Nostr assets and `New-Project.png`.
- Partner artwork not available in the selected offline public logo archive: Liberation Travel, FixedFloat, StealthEX, Bringin, KYCnot.me, SilentLink, Bitomat, xchange.me, Bitesize, YakiHonne, Lightning News, Unknown Certainty and Rhino Bitcoin.

The page keeps the corresponding public text and links, but does not pretend those image files are local.

## Content conflicts and editorial decisions

1. **BFF: White date:** one source article calls the BFF White programme “Friday, May 23”; the recovered running order and supplied facts place it on **Saturday, 24 May**. The page follows the running order: Friday is BFF Blue; Saturday is BFF White.
2. **REVOLUCION spelling:** the selection inventory preserves the source's `REVOLUCION BITCOIN`; the feature detail uses the source's full title `REVOLUCIÓN BITCOIN`.
3. **SATOSHI title typo:** one recovered source contains `SATOSHIL THE CREATION OF BITCOIN`; the page uses the corrected full public title `SATOSHI: THE CREATION OF BITCOIN` from the short-selection heading and supplied facts.
4. **NO MORE INFLATION category:** the main inventory lists it under “trailers and others”, while the feature-selection source gives a full feature record. Both facts are preserved: it remains in the inventory and has a feature detail section.
5. **Old sales/countdown material:** ticket prices, countdown labels, “sign up” language and VOD offers were pre-event copy without a clear active destination in the recovered sources. The page labels the material historical and does not present an active ticket or VOD CTA.
6. **PoWies:** the award artwork and public description are preserved as a completed/historical Bitcoin advertisement award programme, not as an open competition.
7. **Dates and venue:** the archive consistently identifies BFF’25 / Bitcoin FilmFest 2025, “Beyond the Frame”, 22–25 May 2025, Kinoteka, Warsaw and the third festival. Those are the page's canonical masthead facts.

## Verification notes

The separate validator is `scripts/check_bff25_page.py`. It checks front matter, forbidden standalone shell markup, required programme/selection markers, local Liquid asset references, missing built assets and the shared nav/footer count in the generated route.

## Explicit parity audit

The supplied audit baseline found approximately **45 images and 13.8k normalized text characters** in the recovered standalone page, versus approximately **21 images and 10.2k normalized text characters** in the earlier BFF25 preview. After this pass, the current source contains **42 local image files / 43 local references** and approximately **14,650 normalized source-text characters** when front matter, Liquid tags, HTML tags and Markdown decoration are removed. Counts are evidence of coverage, not a claim that every old image was safe or available to republish.

### Preserved public sections and facts

- BFF’25 identity: “Beyond the Frame”, the third Bitcoin FilmFest, 22–25 May 2025, Kinoteka / Palace of Culture and Science, Warsaw.
- The chronological public programme: European Bitcoin Pizza Day, Good Mornings @ Amondo, Community Stage, BFF: Blue, Pitching Rabbits and its €3,000 grant, UNBANKABLE, Barbazaar afterparty, BFF: White, REVOLUCION BITCOIN, HOTEL BITCOIN, Vistula afterparty, Entrepreneurs Breakfast, Polish Community Stage, BFF: Orange, Awards Ceremony, PoWies, Golden Rabbits, self-defence workshops and Goodbye @ Amondo.
- Selection framing: Full release, Works in progress, and Trailers and others, with the public title inventory and the four Golden Rabbit categories: Best Movie, Best Story, Best Short and Audience Choice.
- The recovered feature and experimental-short editorial records, including public directors, runtimes, descriptions and quotes from the two selection source files.
- PoWies as the first Bitcoin-only advertising awards context, plus the public workshop, satellite-event and party descriptions.
- Archive-only ticket tiers: General Admission €100, 2x General Admission €150, Remote Supporter €25 and Producer’s Cut €250.
- Historical public orientation: Why Bitcoin FilmFest?, Why Warsaw?, Travel & Commute, Bitcoin in Warsaw, Why sponsor?, How to submit my film?, Bitcoin Cinema Digest/newsletter context, the BFF25 Infoboard/infopage and the Bitcoin FilmFest community chat.
- Public sponsor, friend, venue and media-partner names and links. Local logo artwork is included only for the eight partners available in the selected public offline logo source.
- Phase 3A additions: Golden Rabbits winners (No More Inflation, Satoshi: The Creation of Bitcoin, Hotel Bitcoin, Revolución Bitcoin); PoWies winners (Mempool: Grand Prix and Visual; StreetCyber: Identity); Pitching Rabbits winner Jenna Reid’s Network Effect; and a reported Bitcoin News recap of 200+ attendees from 20+ countries.
- Phase 3A press references: Bitcoin News recap, the public BFF press archive, and Furious BTC’s public video recap.

### Intentionally excluded surfaces

- Standalone old `<html>`, `<head>`, `<body>`, navigation, footer, inline CSS, countdown scripts and random-image scripts. The page uses the shared default layout, menu, bezel, atmosphere and seats.
- Stale active-sales and intake surfaces: ticket purchase links, active VOD or merchandise sales, countdown labels, live “sign up” language, Google submission forms and any implication that PoWies or film submissions are currently open. Historical price/context text is explicitly archive-only.
- Private or unsuitable source material: ZIP archives, PSD files, OTF/font archives, MOV video, private chat screenshot, PDFs/source documents, credentials, private databases, contact lists and internal notes.
- The uncurated full-resolution photo folder as a wholesale copy. Only the 22 selected, resized event-photo derivatives are bundled.

### Still-missing public assets

The page preserves corresponding text where safe, but these public source images were not recovered into the local bundle: BFF event laurels, Bitcoin Pizza Day artwork, Pitching Rabbits artwork, Good Morning @ Amondo artwork, party illustration/photo, newsletter artwork, feature posters/scenes, short posters/scenes, BFF identity/social artwork, and the partner logos listed in the “Missing or intentionally unbundled public assets” section. No remote dependency was added to fill those gaps.

### New asset delta

- Added **22** curated event photographs from `BFF25/BFF 25 fotki/BFF25/` as resized JPEGs.
- Bundle increased from the earlier 20 files / 21,426,351 bytes to **42 files / 17,540,385 bytes**: a net **+22 files / −3,885,966 bytes** because the two oversized existing PNG photos were re-encoded while the new event photographs were added.
- The new photos are used in a true frame-width rail (`width: calc(100vw - 2 * var(--frame-side))`, centered with `left: 50%` and `translateX(-50%)`) plus the readable photo record. The rail collapses to two columns on mobile and remains clipped to the page viewport.

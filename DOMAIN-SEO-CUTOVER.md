# bitcoinfilmfest.com SEO cutover checklist

> **Status: prepared, not activated.**
>
> The Jekyll source already holds the intended production SEO identity:
> `url: "https://bitcoinfilmfest.com"` and `baseurl: ""` in `site/_config.yml`.
>
> GitHub Pages currently uses `site/_config.github-pages.yml` to override those values for the temporary preview URL. Do not add a `CNAME` file, change DNS, or remove that override until the owner explicitly approves the cutover.

## Why this needs a deliberate release

`bitcoinfilmfest.com` currently resolves to an existing non-GitHub server. A hostname can only point to one production destination at a time. Switching it without completing the checks below could take down the current site, leave a certificate mismatch, or expose incorrect canonical URLs to search engines.

The temporary preview remains available here until launch:

https://itstomekk.github.io/bitcoinfilmfest-com/

## What is already ready in the source

- Production `url` and empty `baseurl` in `site/_config.yml`.
- Canonical, Open Graph, X/Twitter, JSON-LD, manifest, favicon, `robots.txt`, and XML sitemap generation use Jekyll URL helpers.
- `robots.txt` and `sitemap.xml` will resolve to `https://bitcoinfilmfest.com/...` when the production configuration is used.
- The default social image is a local, versioned asset, so it does not depend on the temporary Pages hostname.
- The GitHub Pages workflow has an explicit, reversible preview override at `.github/workflows/deploy-pages.yml`.

## Owner-approved cutover steps

Complete these in order, and verify each one before continuing.

1. **Back up the current hosting configuration and site files.**
   Record its DNS zone, current `A`/`AAAA`/`CNAME` records, nameservers, and any email-related records. Do not change MX, SPF, DKIM, or DMARC records as part of the website cutover.

2. **Add the custom domain in GitHub Pages settings.**
   In the repository, open **Settings -> Pages -> Custom domain**, enter `bitcoinfilmfest.com`, and save. GitHub will show the required DNS target and any verification status.

3. **Create the repository `CNAME` file only after step 2 succeeds.**
   Its entire contents must be exactly:

   ```text
   bitcoinfilmfest.com
   ```

4. **Replace only the website DNS records with the values GitHub Pages currently specifies.**
   Follow GitHub's displayed values rather than copying stale IP addresses from an old guide. Keep mail and unrelated subdomain records unchanged. Add `www` only if its redirect/alias behavior has been decided.

5. **Switch the deployment workflow to production URL rendering.**
   In `.github/workflows/deploy-pages.yml`, change the Jekyll build command from:

   ```bash
   bundle exec jekyll build --trace --config _config.yml,_config.github-pages.yml
   ```

   to:

   ```bash
   bundle exec jekyll build --trace --config _config.yml
   ```

   This is the step that makes canonical URLs, sitemap URLs, JSON-LD URLs, and share-image URLs use `https://bitcoinfilmfest.com`.

6. **Push the focused cutover commit and wait for Pages deployment.**
   Enable **Enforce HTTPS** in GitHub Pages after GitHub reports the certificate is ready.

7. **Verify the live domain with a fresh fetch.**
   Confirm all of the following return `200` and contain the stated production URL:

   ```text
   https://bitcoinfilmfest.com/
   https://bitcoinfilmfest.com/robots.txt
   https://bitcoinfilmfest.com/sitemap.xml
   https://bitcoinfilmfest.com/site.webmanifest
   https://bitcoinfilmfest.com/assets/images/social/bff-social-default.jpg
   ```

   Check the homepage and BFF'27 source for canonical, Open Graph, X/Twitter, and JSON-LD URLs beginning with `https://bitcoinfilmfest.com/`.

8. **Register the production property in Google Search Console.**
   Verify ownership and submit:

   ```text
   https://bitcoinfilmfest.com/sitemap.xml
   ```

   Also use Bing Webmaster Tools if it is part of the marketing workflow.

9. **Retain the temporary Pages URL as a technical preview, not the public SEO URL.**
   It can continue to exist, but production pages must not publish `itstomekk.github.io/bitcoinfilmfest-com` canonical URLs after the cutover.

## Rollback

If domain verification, HTTPS, or a production metadata check fails, restore the previous website DNS records from the backup in step 1. Then restore the Pages workflow preview override and redeploy. Do not leave the domain pointed at an unverified configuration.

## Boundaries

- This checklist does not make any DNS change.
- This checklist does not add a `CNAME` file.
- This checklist does not alter the currently deployed temporary Pages site.
- Do not place private film databases, API keys, or hosting credentials in this public repository.

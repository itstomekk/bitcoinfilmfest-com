"""Browser regression checks for BFF27 captions inside the cinema screen.

Requires Playwright and Chromium (optional local verification dependency).
Accepts a generated Jekyll directory or an HTTP origin. The directory is served
on an ephemeral loopback port, so no persistent server is needed.
"""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
from pathlib import Path
import threading
from playwright.sync_api import sync_playwright


class QuietHandler(SimpleHTTPRequestHandler):
    def log_message(self, *_):
        pass


PROBE = r"""() => {
  const rect = e => e.getBoundingClientRect();
  const canvas = document.createElement('canvas');
  canvas.width = canvas.height = 1;
  const ctx = canvas.getContext('2d', {willReadFrequently: true});
  const luminance = rgb => {
    const c = rgb.slice(0, 3).map(x => {
      const v = x / 255;
      return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4;
    });
    return c[0] * .2126 + c[1] * .7152 + c[2] * .0722;
  };
  const contrast = e => {
    const ancestors = [];
    for (let p = e; p; p = p.parentElement) ancestors.unshift(p);
    ctx.clearRect(0, 0, 1, 1);
    ctx.fillStyle = '#000'; ctx.fillRect(0, 0, 1, 1);
    for (const p of ancestors) {
      ctx.fillStyle = getComputedStyle(p).backgroundColor;
      ctx.fillRect(0, 0, 1, 1);
    }
    const bg = luminance([...ctx.getImageData(0, 0, 1, 1).data]);
    ctx.fillStyle = getComputedStyle(e).color; ctx.fillRect(0, 0, 1, 1);
    const fg = luminance([...ctx.getImageData(0, 0, 1, 1).data]);
    return (Math.max(bg, fg) + .05) / (Math.min(bg, fg) + .05);
  };
  const captions = [...document.querySelectorAll('.bff27-photo-rail figcaption')].map(e => {
    let left = 0, right = document.documentElement.clientWidth;
    for (let p = e; p; p = p.parentElement) {
      const cs = getComputedStyle(p);
      if (['hidden', 'clip', 'auto', 'scroll'].includes(cs.overflowX)) {
        const r = rect(p); left = Math.max(left, r.left); right = Math.min(right, r.right);
      }
    }
    const walker = document.createTreeWalker(e, NodeFilter.SHOW_TEXT);
    let n; const clipped = [];
    while (n = walker.nextNode()) {
      for (let i = 0; i < n.length; i++) {
        if (!n.textContent[i].trim()) continue;
        const range = document.createRange(); range.setStart(n, i); range.setEnd(n, i + 1);
        for (const r of range.getClientRects()) {
          if (r.left < left - .5 || r.right > right + .5) clipped.push(n.textContent[i]);
        }
      }
    }
    return {text: e.innerText, clipped: clipped.join(''), ratio: contrast(e)};
  });
  const muted = [...document.querySelectorAll('.bff27-hero-art figcaption, .bff27-photo-caption, .bff27-index span')]
    .map(e => ({text: e.innerText, ratio: contrast(e)}));
  return {width: document.documentElement.clientWidth, scrollWidth: document.documentElement.scrollWidth,
    captions, muted, images: document.querySelectorAll('.bff27-photo-rail img').length};
}"""


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--site', required=True, help='Generated site directory or HTTP origin')
    parser.add_argument('--only', choices=['geometry', 'contrast', 'all'], default='all')
    parser.add_argument('--screenshots', type=Path)
    args = parser.parse_args()
    server = None
    if args.site.startswith(('http://', 'https://')):
        origin = args.site.rstrip('/')
    else:
        server = ThreadingHTTPServer(('127.0.0.1', 0), partial(QuietHandler, directory=str(Path(args.site).resolve())))
        threading.Thread(target=server.serve_forever, daemon=True).start()
        origin = f'http://127.0.0.1:{server.server_port}'
    failures = []
    results = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            for width in [320, 360, 390, 430, 560, 768, 1024, 1440, 1920]:
                page = browser.new_page(viewport={'width': width, 'height': 900}, reduced_motion='reduce')
                response = page.goto(origin + '/27/', wait_until='networkidle')
                page.evaluate('document.fonts.ready')
                page.wait_for_timeout(500)
                result = page.evaluate(PROBE)
                results.append(result)
                if response.status != 200 or result['scrollWidth'] > result['width'] or len(result['captions']) != 6:
                    failures.append(f'{width}px: route/overflow/caption-count failure')
                if args.only in ['geometry', 'all']:
                    for caption in result['captions']:
                        if caption['clipped']:
                            failures.append(f"{width}px: clipped {caption['clipped']!r} in {caption['text']!r}")
                if args.only in ['contrast', 'all']:
                    for caption in result['captions'] + result['muted']:
                        if caption['ratio'] < 4.5:
                            failures.append(f"{width}px: {caption['ratio']:.2f}:1 contrast for {caption['text']!r}")
                if args.screenshots and width in [390, 1440]:
                    args.screenshots.mkdir(parents=True, exist_ok=True)
                    page.evaluate("document.querySelectorAll('img').forEach(i => i.loading = 'eager')")
                    page.wait_for_timeout(600)
                    page.add_style_tag(content='.seat-rows,.cinema-seats {display:none!important;}')
                    for selector, label in [('.bff27-photo-band', 'gallery'), ('.bff27-hero-art', 'hero-caption')]:
                        loc = page.locator(selector)
                        loc.scroll_into_view_if_needed()
                        box = loc.bounding_box()
                        # Element screenshots crop overflowing children to the
                        # narrow article box, which fakes clipped edge captions.
                        page.screenshot(path=str(args.screenshots / f'{width}-{label}.png'), full_page=True,
                                        clip={'x': 0, 'y': box['y'] + page.evaluate('scrollY'),
                                              'width': width, 'height': box['height']})
                page.close()
            browser.close()
    finally:
        if server:
            server.shutdown()
            server.server_close()
    print(json.dumps({'widths': len(results), 'captions_per_width': 6,
                      'minimum_contrast': min(c['ratio'] for r in results for c in r['captions'] + r['muted']),
                      'failures': failures}, indent=2))
    if failures:
        raise SystemExit(1)


if __name__ == '__main__':
    main()

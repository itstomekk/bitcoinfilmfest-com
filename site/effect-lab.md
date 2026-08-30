---
layout: default
title: "Cinema effect lab"
nav_label: "Effect lab"
description: "Private comparison page for Bitcoin FilmFest cinema-screen effects."
robots: "noindex, nofollow"
screen: paper
---

<style>
.effect-lab { max-width: 70rem; }
.effect-lab h1 { max-width: none; }
.effect-lab-controls { display:flex; flex-wrap:wrap; gap:.75rem; margin:1.5rem 0; }
.effect-lab-controls a { padding:.65rem .9rem; border:1px solid var(--color-ink); color:var(--color-ink); text-decoration:none; font-family:var(--font-display); }
.effect-lab-controls a[aria-current="page"] { background:var(--color-ink); color:var(--color-paper); }
.effect-lab-screen { position:relative; isolation:isolate; overflow:hidden; min-height:28rem; padding:3rem; background:#237fc4; color:#f5f0e0; box-shadow:inset 0 0 9rem rgba(0,0,0,.55); }
.effect-lab-screen > * { position:relative; z-index:2; }
.effect-lab-screen::before,.effect-lab-screen::after { content:""; position:absolute; inset:0; pointer-events:none; }
.effect-lab-screen::after { background:radial-gradient(ellipse,transparent 38%,rgba(0,0,0,.7)); }
.effect-lab-screen[data-effect="soft"]::before { opacity:.18; background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='120' height='120'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.82' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E"); animation:lab-grain .6s steps(4) infinite; mix-blend-mode:overlay; }
.effect-lab-screen[data-effect="conic"]::before { inset:-5%; opacity:.28; background-image:repeating-conic-gradient(#000 0 .00003%,transparent .0005% .00095%),repeating-conic-gradient(#000 0 .00005%,transparent .00015% .0009%); animation:lab-grain .5s steps(1) infinite; }
.effect-lab-screen[data-effect="scratch"]::before { width:120%; opacity:.52; background:repeating-linear-gradient(90deg,#0002 0 2px,transparent 4px 37vmin); animation:lab-scratch .45s steps(1) infinite; mix-blend-mode:screen; }
@keyframes lab-grain { 0%,100%{transform:translate(0)} 25%{transform:translate(-2%,1%)} 50%{transform:translate(1%,-2%)} 75%{transform:translate(-1%,-1%)} }
@keyframes lab-scratch { 0%,100%{transform:translateX(0);opacity:.5} 30%{transform:translateX(-2%);opacity:.75} 60%{transform:translateX(8%)} 90%{transform:translateX(-3%);opacity:.25} }
@media (prefers-reduced-motion:reduce){.effect-lab-screen::before{animation:none!important}}
</style>

<section class="effect-lab" data-effect-lab>
  <h1>Cinema effect lab</h1>
  <p>Unlinked comparison page. Select a URL below; all effects are contained inside this demo screen only.</p>
  <nav class="effect-lab-controls" aria-label="Effect variants">
    <a href="?effect=soft" data-effect-link="soft">Original subtle turbulence</a>
    <a href="?effect=conic" data-effect-link="conic">CSS-only conic grain</a>
    <a href="?effect=scratch" data-effect-link="scratch">Old-film scratch layer</a>
  </nav>
  <div class="effect-lab-screen" data-effect-screen>
    <p>Bitcoin FilmFest</p><h2>Now playing</h2><p>This is a contained visual sample, not a production page.</p>
  </div>
</section>
<script>
(function(){var effect=new URLSearchParams(location.search).get('effect')||'soft';if(['soft','conic','scratch'].indexOf(effect)<0)effect='soft';var screen=document.querySelector('[data-effect-screen]');screen.dataset.effect=effect;document.querySelectorAll('[data-effect-link]').forEach(function(link){if(link.dataset.effectLink===effect)link.setAttribute('aria-current','page');});}());
</script>

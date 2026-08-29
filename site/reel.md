---
layout: default
title: "Reel"
nav_label: "Reel"
description: "Bitcoin FilmFest press, blog stories, and the Bitcoin Cinema Digest newsletter."
permalink: /reel/
screen: paper
---

<article class="reel-page">
  <header class="page-masthead">
    <p class="page-context">Everything we've written, screened, and sent</p>
    <h1>Reel</h1>
    <p>Press coverage, blog stories, and the Bitcoin Cinema Digest — all in one place.</p>
  </header>

  <section id="newsletter" class="reel-section">
    <h2>Newsletter</h2>
    <p>Bitcoin Cinema Digest — monthly updates from the heart of Bitcoin cinema.</p>
    <ul class="reel-list">
      {% for post in site.newsletters %}
        <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %Y" }}</time></li>
      {% endfor %}
    </ul>
  </section>

  <section id="press" class="reel-section">
    <h2>Press</h2>
    <p>Coverage and mentions from outlets writing about Bitcoin FilmFest.</p>
    <p class="reel-empty">Press archive migration is in progress. Verified coverage will appear here as it is restored.</p>
  </section>

  <section id="blog" class="reel-section">
    <h2>Blog</h2>
    <p>Interviews, guest posts, and stories from the Bitcoin Cinema Hub.</p>
    <p class="reel-empty">Blog migration is in progress. Interviews and stories will appear here as they are restored.</p>
  </section>
</article>

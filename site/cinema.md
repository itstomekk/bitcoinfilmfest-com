---
layout: default
title: "Cinema"
nav_label: "Cinema"
description: "The Bitcoin Cinema ecosystem — films, studios, and the people building Bitcoin film culture."
permalink: /cinema/
screen: paper
---

<article class="reel-page">
  <header class="page-masthead">
    <p class="page-context">The Bitcoin Cinema Hub</p>
    <h1>Cinema</h1>
    <p>Bitcoin cinema is a real, active industry — major studios, independent producers, dedicated funding platforms, and a growing catalogue of films. This is our record of it.</p>
  </header>

  {% assign released_count = site.films | where: "status", "released" | size %}
  {% assign in_production_count = site.films | where: "status", "in-production" | size %}
  <div class="cinema-masthead-stats">
    <div class="cinema-stat">
      <span class="cinema-stat-value">{{ site.films.size }}</span>
      <span class="cinema-stat-label">Films tracked</span>
    </div>
    <div class="cinema-stat">
      <span class="cinema-stat-value">{{ released_count }}</span>
      <span class="cinema-stat-label">Released</span>
    </div>
    <div class="cinema-stat">
      <span class="cinema-stat-value">{{ in_production_count }}</span>
      <span class="cinema-stat-label">In production</span>
    </div>
    <div class="cinema-stat">
      <span class="cinema-stat-value">{{ site.companies.size }}</span>
      <span class="cinema-stat-label">Companies &amp; platforms</span>
    </div>
  </div>

  <nav class="cinema-section-nav" aria-label="Cinema sections">
    <a href="{{ '/cinema/films/' | relative_url }}">Browse films →</a>
    <a href="{{ '/cinema/companies/' | relative_url }}">Browse companies →</a>
  </nav>

  {% assign featured_films = site.films | where: "featured", true %}
  {% if featured_films.size > 0 %}
    <section class="reel-section">
      <p class="section-label">On our radar</p>
      <h2>Films worth knowing about</h2>
      <ul class="cinema-index">
        {% for film in featured_films %}
          {% include cinema-row.html entry=film kind="film" %}
        {% endfor %}
      </ul>
    </section>
  {% endif %}

  {% assign featured_companies = site.companies | where: "featured", true %}
  {% if featured_companies.size > 0 %}
    <section class="reel-section">
      <p class="section-label">Building the ecosystem</p>
      <h2>Studios &amp; platforms</h2>
      <ul class="cinema-index">
        {% for company in featured_companies %}
          {% include cinema-row.html entry=company kind="company" %}
        {% endfor %}
      </ul>
    </section>
  {% endif %}

  {% if site.films.size == 0 and site.companies.size == 0 %}
    <p class="reel-empty">The Cinema Hub is being assembled. Check back soon for the first entries.</p>
  {% endif %}
</article>

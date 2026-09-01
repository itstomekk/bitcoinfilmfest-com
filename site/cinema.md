---
layout: default
title: "Cinema"
nav_label: "Cinema"
description: "The Bitcoin Cinema ecosystem: films, studios, and the people building Bitcoin film culture."
permalink: /cinema/
screen: paper
---

<article class="reel-page">
  <header class="cinema-hero">
    <div class="cinema-hero-copy">
      <p class="page-context">Bitcoin cinema</p>
      <h1>Cinema</h1>
      <p>Films, studios and the people building a culture around Bitcoin.</p>
    </div>
    <figure class="cinema-hero-art">
      <img src="{{ '/assets/images/brand/bff-rabbit.png' | relative_url }}" alt="Bitcoin FilmFest rabbit mascot in the cinema" width="5073" height="7051">
      <figcaption>From the Bitcoin FilmFest archive</figcaption>
    </figure>
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
    <a href="#films">Browse films ↓</a>
    <a href="#companies">Browse companies ↓</a>
  </nav>

  {% assign featured_films = site.films | where: "featured", true | sort: "essential_rank" %}
  {% if featured_films.size > 0 %}
    <section class="reel-section cinema-shelf">
      <h2>Films that define Bitcoin cinema</h2>
      <p>Our editorial starting point: the titles with the strongest mix of Bitcoin importance, cultural reach, BFF relevance, and public documentation.</p>
      <ul class="cinema-index cinema-featured-list">
        {% for film in featured_films %}
          {% include cinema-row.html entry=film kind="film" %}
        {% endfor %}
      </ul>
    </section>
  {% endif %}

  <section class="reel-section cinema-browser" id="films" data-cinema-browser>
    <div class="cinema-browser-heading">
      <div>
        <h2>Browse the films</h2>
      </div>
      <p class="cinema-browser-count" data-cinema-count>{{ site.films.size }} titles</p>
    </div>
    <div class="cinema-browser-controls" role="search" aria-label="Filter films">
      <label class="cinema-search">
        <span class="sr-only">Search films</span>
        <input type="search" placeholder="Search titles, directors, studios…" data-cinema-search>
      </label>
      <div class="cinema-filter-group" aria-label="Film filters">
        <button type="button" class="cinema-filter is-active" data-cinema-filter="all">All</button>
        <button type="button" class="cinema-filter" data-cinema-filter="Feature">Features</button>
        <button type="button" class="cinema-filter" data-cinema-filter="Documentary">Docs</button>
        <button type="button" class="cinema-filter" data-cinema-filter="in-production">In production</button>
      </div>
    </div>
    <p class="cinema-browser-empty" data-cinema-empty hidden>No titles match that search.</p>
    <ul class="cinema-index cinema-browser-list">
      {% assign all_films = site.films | sort: "title" %}
      {% for film in all_films %}
        <li class="cinema-browser-item" data-cinema-item data-kind="{{ film.type | escape }}" data-status="{{ film.status | escape }}" data-search="{{ film.title | escape }} {{ film.director | escape }} {{ film.studio | escape }} {{ film.synopsis | escape }}">
          {% include cinema-row.html entry=film kind="film" %}
          {% if film.synopsis %}<p class="cinema-row-description">{{ film.synopsis }}</p>{% endif %}
        </li>
      {% endfor %}
    </ul>
    <noscript><p>JavaScript is disabled. Use the full <a href="{{ '/cinema/films/' | relative_url }}">film index</a>.</p></noscript>
  </section>

  <section class="reel-section cinema-browser" id="companies">
    <div class="cinema-browser-heading">
      <div>
        <h2>Studios, platforms &amp; venues</h2>
      </div>
      <p class="cinema-browser-count">{{ site.companies.size }} listed</p>
    </div>
    <p>Companies here are part of film production, distribution, funding, or exhibition. Event sponsors remain separate.</p>
    <ul class="cinema-index">
      {% assign companies = site.companies | sort: "title" %}
      {% for company in companies %}
        {% include cinema-row.html entry=company kind="company" %}
      {% endfor %}
    </ul>
  </section>

  <section class="reel-section cinema-footprint">
    <p class="section-label">The work behind the screen</p>
    <h2>Building the industry</h2>
    <p>Bitcoin FilmFest is more than a yearly screening programme: it is a growing network of festivals, travelling cinema, conferences, filmmakers, and community builders.</p>
    <div class="cinema-masthead-stats">
      {% for stat in site.data.cinema_stats %}
        <div class="cinema-stat">
          <span class="cinema-stat-value">{{ stat.value }}</span>
          <span class="cinema-stat-label">{{ stat.label }}</span>
        </div>
      {% endfor %}
    </div>
  </section>

  {% if site.films.size == 0 and site.companies.size == 0 %}
    <p class="reel-empty">The Cinema Hub is being assembled. Check back soon for the first entries.</p>
  {% endif %}
</article>

---
layout: default
title: "Bitcoin Movies & Documentaries: The Complete List"
nav_label: "Films"
description: "A curated list of Bitcoin films: documentaries, features, shorts and series, each with director, cast, synopsis and its Bitcoin angle."
permalink: /cinema/films/
screen: paper
---

<article class="reel-page">
  <a class="cinema-back" href="{{ '/cinema/' | relative_url }}">← Cinema</a>

  <header class="page-masthead">
    <p class="page-context">The Bitcoin Cinema database</p>
    {% assign all_films = site.films %}
    {% assign doc_count = all_films | where: "type", "Documentary" | size %}
    {% assign feature_count = all_films | where: "type", "Feature" | size %}
    <h1>Bitcoin movies and documentaries</h1>
    <p>This is a curated list of {{ all_films.size }} films and series about Bitcoin: {{ doc_count }} documentaries, {{ feature_count }} features, shorts and TV series. A title makes the list when it has a director, cast or studio attached, at least one credible public source, and a real Bitcoin connection, whether that is the subject, the story or the people behind it. Every entry shows the director, cast, synopsis and what makes it a Bitcoin film.</p>
  </header>

  {% assign films = site.films | sort: "title" %}
  {% if films.size > 0 %}
    <ul class="cinema-index">
      {% for film in films %}
        {% include cinema-row.html entry=film kind="film" %}
      {% endfor %}
    </ul>
  {% else %}
    <p class="reel-empty">The film database is being assembled. Check back soon for the first titles.</p>
  {% endif %}
</article>

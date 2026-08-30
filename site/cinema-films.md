---
layout: default
title: "Films"
nav_label: "Films"
description: "The Bitcoin Cinema film database — features, documentaries, shorts, and TV built around Bitcoin."
permalink: /cinema/films/
screen: paper
---

<article class="reel-page">
  <a class="cinema-back" href="{{ '/cinema/' | relative_url }}">← Cinema</a>

  <header class="page-masthead">
    <p class="page-context">The Bitcoin Cinema database</p>
    <h1>Films</h1>
    <p>Every title in this database has a director, cast, or studio attached, and at least one credible public source.</p>
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

---
layout: default
title: "Companies"
nav_label: "Companies"
description: "The Bitcoin Cinema ecosystem — studios, production companies, distribution platforms, and venues building Bitcoin film."
permalink: /cinema/companies/
screen: paper
---

<article class="reel-page">
  <a class="cinema-back" href="{{ '/cinema/' | relative_url }}">← Cinema</a>

  <header class="page-masthead">
    <p class="page-context">The Bitcoin Cinema ecosystem</p>
    <h1>Companies</h1>
    <p>Studios, production companies, distribution and funding platforms, and venues building Bitcoin cinema.</p>
  </header>

  {% assign companies = site.companies | sort: "title" %}
  {% if companies.size > 0 %}
    <ul class="cinema-index">
      {% for company in companies %}
        {% include cinema-row.html entry=company kind="company" %}
      {% endfor %}
    </ul>
  {% else %}
    <p class="reel-empty">The companies directory is being assembled. Check back soon for the first entries.</p>
  {% endif %}
</article>

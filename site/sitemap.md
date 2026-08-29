---
layout: default
title: "Site map"
nav_label: "Site map"
description: "The Bitcoin FilmFest page map and local rebuild status."
permalink: /sitemap/
screen: paper
---

<article class="sitemap-page">
  <header class="page-masthead">
    <p class="page-context">The full reel</p>
    <h1>Site map</h1>
    <p>{{ site.data.sitemap.summary.public_or_planned_routes }} public or planned routes recovered from the current scaffold, static mirror, and Wayback archive.</p>
  </header>

  <div class="route-key" aria-label="Route status legend">
    <span><i class="route-dot route-dot--live"></i> Built locally</span>
    <span><i class="route-dot route-dot--planned"></i> Planned migration</span>
    <span><i class="route-dot route-dot--redirect"></i> Redirect decision</span>
  </div>

  <div class="sitemap-index">
    {% for category in site.data.sitemap.categories %}
      <section class="sitemap-group">
        <h2>{{ category.name }}</h2>
        <ol>
          {% for entry in category.pages %}
            <li>
              {% if entry.status == 'implemented' %}
                <a href="{{ entry.route | relative_url }}">
                  <span>{{ entry.title }}</span>
                  <code>{{ entry.route }}</code>
                </a>
              {% else %}
                <span class="route-planned">
                  <span>{{ entry.title }}</span>
                  <code>{{ entry.route }}</code>
                </span>
              {% endif %}
              <small class="route-state route-state--{{ entry.status | slugify }}">{{ entry.status }}</small>
            </li>
          {% endfor %}
        </ol>
      </section>
    {% endfor %}
  </div>

  <section class="sitemap-exclusions">
    <h2>Separate or retired</h2>
    <ul>
      {% for entry in site.data.sitemap.excluded %}
        <li><code>{{ entry.route }}</code> — {{ entry.reason }}</li>
      {% endfor %}
    </ul>
  </section>
</article>

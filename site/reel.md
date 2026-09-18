---
layout: default
title: "Reel"
nav_label: "Reel"
description: "Bitcoin FilmFest press, blog stories, and the Bitcoin Cinema Chronicle."
permalink: /reel/
screen: paper
---

<article class="reel-page">
  <header class="page-masthead">
    <p class="page-context">Everything we've written, screened, and sent</p>
    <h1>Reel</h1>
    <p>Press coverage, blog stories, and the Chronicle — a running record of Bitcoin cinema, all in one place.</p>
  </header>

  <nav class="reel-nav" aria-label="Reel sections">
    <a href="#archive">Archive</a>
    <a href="#chronicle">Chronicle</a>
    <a href="#newsletter">Newsletter</a>
  </nav>

  <section id="archive" class="reel-section">
    <p class="section-label">The Reel archive</p>
    <h2>Stories from Bitcoin cinema</h2>
    <p class="reel-lede">Interviews, guest posts, and features from the people making, screening, and supporting independent cinema.</p>

    {% assign reel_entries = site.reel | sort: 'date' | reverse %}
    {% if reel_entries.size > 0 %}
      <ul class="reel-list">
        {% for entry in reel_entries %}
          <li>
            <a href="{{ entry.url | relative_url }}">{{ entry.title }}</a>
            <time datetime="{% if entry.date_precision == 'month' %}{{ entry.date | date: "%Y-%m" }}{% else %}{{ entry.date | date_to_xmlschema }}{% endif %}">{% if entry.published_label %}{{ entry.published_label }}{% else %}{{ entry.date | date: "%B %Y" }}{% endif %}</time>
          </li>
        {% endfor %}
      </ul>
    {% else %}
      <p class="reel-empty">The Reel archive is being assembled. Check back soon for the first entries.</p>
    {% endif %}
  </section>

  <section id="chronicle" class="reel-section">
    <p class="section-label">Bitcoin Cinema Chronicle</p>
    <h2>What's moving in Bitcoin cinema</h2>
    <p class="reel-lede">Short, dated notes on films, festivals, and the people making them — each one links out to where we found it.</p>

    {% assign chronicle_entries = site.chronicle | sort: 'date' | reverse %}
    {% if chronicle_entries.size > 0 %}
      <ol class="chronicle">
        {% for entry in chronicle_entries %}
          <li class="chronicle-entry">
            <div>
              <time class="chronicle-date" datetime="{{ entry.date | date_to_xmlschema }}">{{ entry.date | date: "%b %-d, %Y" }}</time>
              {% if entry.source %}<span class="chronicle-source">{{ entry.source }}</span>{% endif %}
            </div>
            <div class="chronicle-body">
              {{ entry.content }}
              {% if entry.url %}<p><a href="{{ entry.url }}" target="_blank" rel="noopener noreferrer">Read more →</a></p>{% endif %}
            </div>
          </li>
        {% endfor %}
      </ol>
    {% else %}
      <p class="reel-empty">The Chronicle is being assembled. Check back soon for the first entries.</p>
    {% endif %}
  </section>

  <section id="newsletter" class="reel-section">
    <p class="section-label">Bitcoin Cinema Digest</p>
    <h2>Newsletter</h2>
    <p class="reel-lede">Monthly updates from the heart of Bitcoin cinema, sent straight from set.</p>
    {% assign newsletter_posts = site.reel | where: "category", "newsletters" | sort: 'date' | reverse %}
    {% if newsletter_posts.size > 0 %}
      <ul class="reel-list">
        {% for post in newsletter_posts %}
          <li><a href="{{ post.url | relative_url }}">{{ post.title }}</a><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %Y" }}</time></li>
        {% endfor %}
      </ul>
    {% else %}
      <p class="reel-empty">No issues published yet.</p>
    {% endif %}
  </section>

</article>

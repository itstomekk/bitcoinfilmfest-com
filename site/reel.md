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
    <a href="#chronicle">Chronicle</a>
    <a href="#posts">Posts</a>
    <a href="#archive">Archive</a>
  </nav>

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

  <section id="posts" class="reel-section">
    <p class="section-label">Fresh from the edit</p>
    <h2>Posts</h2>
    <p class="reel-lede">New writing and reporting from Bitcoin cinema lands here first.</p>

    {% assign reel_posts = site.reel | where_exp: "entry", "entry.archived != true" | sort: 'date' | reverse %}
    {% if reel_posts.size > 0 %}
      <ul class="cinema-index reel-list">
        {% for entry in reel_posts %}
          {% include cinema-row.html entry=entry kind="reel" %}
        {% endfor %}
      </ul>
    {% else %}
      <p class="reel-empty">New Bitcoin Cinema writing lands here first.</p>
    {% endif %}
  </section>

  <section id="archive" class="reel-section">
    <p class="section-label">The Reel archive</p>
    <h2>Stories from Bitcoin cinema</h2>
    <p class="reel-lede">Interviews, guest posts, features, and newsletters from the people making, screening, and supporting independent cinema.</p>

    {% assign reel_archive = site.reel | where_exp: "entry", "entry.archived == true" | sort: 'date' | reverse %}
    {% if reel_archive.size > 0 %}
      <ul class="cinema-index reel-list">
        {% for entry in reel_archive %}
          {% include cinema-row.html entry=entry kind="reel" %}
        {% endfor %}
      </ul>
    {% else %}
      <p class="reel-empty">The Reel archive is being assembled. Check back soon for the first entries.</p>
    {% endif %}
  </section>

</article>

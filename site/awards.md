---
layout: default
title: "Golden Rabbits"
nav_label: "Golden Rabbits"
description: "The Golden Rabbits archive: Bitcoin FilmFest award winners from 2023 to 2026."
permalink: /awards/
screen: paper
---

<article class="reel-page">
  <a class="cinema-back" href="{{ '/about/' | relative_url }}">← Storyboard</a>

  <header class="page-masthead">
    <p class="page-context">Bitcoin FilmFest archive</p>
    <h1>Golden Rabbits</h1>
    <p>The films that carried home a Golden Rabbit — and the community-vote moments that shaped the early editions.</p>
  </header>

  <section class="reel-section">
    <p class="section-label">The award archive</p>
    <p>Every edition has its own shape. BFF’23 used the language of “most votes” and “most number of voters” in contemporaneous coverage; the organiser’s Best Movie and Audience Choice mapping is shown here with that context intact. In BFF’26, Best Story was not awarded.</p>
  </section>

  {% for edition in site.data.golden_rabbits %}
    <section class="reel-section" id="bff-{{ edition.year }}">
      <p class="section-label">{{ edition.label }}</p>
      <h2>{{ edition.year }}</h2>
      <p>{{ edition.summary }}</p>
      <div class="table-scroll">
        <table class="cinema-awards-table">
          <caption class="sr-only">{{ edition.label }} Golden Rabbits winners</caption>
          <thead>
            <tr>
              <th scope="col">Category</th>
              <th scope="col">Film</th>
              <th scope="col">Filmmaker</th>
            </tr>
          </thead>
          <tbody>
            {% for award in edition.awards %}
              <tr>
                <th scope="row">{{ award.category }}</th>
                <td>
                  {% if award.film_url %}<a href="{{ award.film_url | relative_url }}">{{ award.film }}</a>{% else %}{{ award.film }}{% endif %}
                  {% if award.alias %}<span class="cinema-award-alias">{{ award.alias }}</span>{% endif %}
                </td>
                <td>{% if award.director %}{{ award.director }}{% else %}—{% endif %}</td>
              </tr>
            {% endfor %}
          </tbody>
        </table>
      </div>
      <p class="section-label">Sources</p>
      <p class="cinema-sources">
        {% for source in edition.sources %}<a href="{{ source.url }}" target="_blank" rel="noopener noreferrer">{{ source.label }}</a>{% endfor %}
      </p>
    </section>
  {% endfor %}

  <section class="reel-section">
    <p class="section-label">Keep exploring</p>
    <p><a href="{{ '/cinema/' | relative_url }}">Browse the Cinema catalogue →</a> &nbsp; <a href="{{ '/festivals/roadshows/' | relative_url }}">See Minis &amp; roadshows →</a></p>
  </section>
</article>

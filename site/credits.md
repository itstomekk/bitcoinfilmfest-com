---
layout: default
title: "Credits"
nav_label: "Credits"
description: "Bitcoin FilmFest crew, collaborators, production partners, and special cameos."
permalink: /credits/
screen: credits
---

<style>
  .credits-page {
    width: 100%;
    max-width: 52rem;
    margin: 0 auto;
    padding-inline: 1rem;
    box-sizing: border-box;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    color: #fff;
  }

  .credits-page .page-masthead,
  .credits-page .credits-roll,
  .credits-page .credits-section,
  .credits-page .credits-section ul,
  .credits-page .credits-section li,
  .credits-page .credits-date {
    width: 100%;
    max-width: 100%;
    margin-inline: auto;
    box-sizing: border-box;
    text-align: center;
  }

  .credits-page .page-masthead {
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  .credits-page .page-masthead > * {
    width: 100%;
    margin-inline: auto;
    text-align: center;
    color: #fff !important;
  }

  .credits-page .credits-roll {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 3.5rem;
  }

  .credits-page .credits-section {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin: 0;
  }

  .credits-page .credits-section h2 {
    width: 100%;
    margin: 0 0 1.25rem;
    color: #fff !important;
    font-size: clamp(2.25rem, 6vw, 3.5rem);
    line-height: 1;
    text-align: center;
  }

  .credits-page .credits-section ul {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    gap: 0.55rem;
    margin: 0;
    padding: 0;
    list-style: none;
  }

  .credits-page .credits-section li {
    display: block;
    margin: 0;
    padding: 0;
    text-align: center;
  }

  .credits-page .credits-section a {
    display: block;
    width: 100%;
    color: #fff !important;
    font-family: var(--font-display);
    font-size: clamp(1rem, 2vw, 1.3rem);
    line-height: 1.4;
    text-align: center;
    text-decoration-color: rgba(255, 255, 255, 0.28);
  }

  .credits-page .credits-date {
    margin-top: 3rem;
    color: #fff !important;
    text-align: center;
  }
</style>

<article class="credits-page">
  <header class="page-masthead">
    <h1>Credits</h1>
  </header>

  <div class="credits-roll" data-credits-roll>
    {% for section in site.data.credits.sections %}
      <section class="credits-section">
        <h2>{{ section.name }}</h2>
        <ul>
          {% for entry in section.entries %}
            <li><a href="{{ entry.url }}" target="_blank" rel="noopener noreferrer">{{ entry.name }}</a></li>
          {% endfor %}
        </ul>
      </section>
    {% endfor %}
  </div>

  <p class="credits-date">Collaborations documented through {{ site.data.credits.updated_through }}.</p>
</article>

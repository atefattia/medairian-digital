# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Med.AI.rian is a personal portfolio website for a Senior ML Engineer, built with Flask and a YAML-based content management system. Content is decoupled from templates — page data lives in YAML files, project details in Markdown files.

## Commands

```bash
# Setup (requires uv: https://docs.astral.sh/uv/)
uv sync

# Run locally (debug mode)
uv run python app.py

# Production (Heroku)
gunicorn app:app
```

There are no tests or linters configured.

## Architecture

- **`app.py`** — Flask app factory (`create_app()`), registers blueprints, initializes Flask-Mail
- **`config.py`** — App config; `MAIL_PASSWORD` read from env var
- **`routes/main_routes.py`** — Single blueprint (`main`) with all routes. Uses `ContentLoader` to merge base + page YAML content and passes it as template kwargs
- **`utils/content_loader.py`** — `ContentLoader` class: loads `content/base.yml` once, then deep-merges it with per-page YAML via `get_page_content()` (LRU-cached). Base content (site name, nav, footer, contact) is available on every page
- **`content/`** — YAML content layer:
  - `base.yml` — site-wide data (navigation, footer, contact info)
  - `pages/*.yml` — per-page content (home, about, projects, skills, articles, contact)
  - `projects/*.md` — Markdown files for individual project detail pages, rendered via `markdown2`
- **`templates/`** — Jinja2 templates; `base.html` is the layout, `pages/` has page-specific templates
- **`static/`** — CSS, JS, and images

## Key Patterns

- **Content updates don't require template changes.** Edit YAML files in `content/` to change page content. Add Markdown files in `content/projects/` for new project detail pages.
- **Featured projects** are controlled by `featured: true` in `content/pages/projects.yml` and appear on the home page automatically.
- **Project detail routing**: `/projects/<filename>.md` reads the Markdown file from `content/projects/`, converts to HTML, and renders in `project_detail.html`.
- **Deployment** is on Heroku via `Procfile` (`gunicorn app:app`). Dependencies managed with uv (`pyproject.toml` + `uv.lock`). Heroku detects `uv.lock` and runs `uv sync --locked --no-default-groups` during build.

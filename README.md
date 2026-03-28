# Med.AI.rian - Professional Portfolio

A modern web application showcasing my professional experience as a Senior Generative AI Engineer. The name Med.AI.rian represents my Tunisian roots (Mediterranean) combined with my expertise in Artificial Intelligence.

## Setup Instructions

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

2. Install dependencies:

```bash
uv sync
```

3. Run the application:

```bash
make run
```

## Available Commands

| Command | Description |
|---------|-------------|
| `make run` | Run the app locally (debug mode) |
| `make login` | Login to Heroku CLI |
| `make deploy` | Deploy to Heroku |
| `make help` | Show all available commands |

## Project Structure

```
medairian-digital/
├── app.py                  # Main application entry point
├── config.py               # Configuration settings
├── pyproject.toml          # Dependencies (uv)
├── uv.lock                 # Locked dependencies
├── Makefile                # Dev/deploy commands
├── Procfile                # Heroku process definition
├── content/                # Content management
│   ├── base.yml            # Base content (navigation, footer)
│   ├── pages/              # Page-specific content
│   └── projects/           # Project detail Markdown files
├── static/                 # Static files (CSS, JS, images)
├── templates/              # Jinja2 templates
├── routes/                 # Route handlers
└── utils/                  # Utilities (content loader)
```

## Content Management

The website uses a YAML-based content management system that makes it easy to update content without touching the HTML templates. All content is stored in the `content/` directory:

### Base Content (`content/base.yml`)

Contains site-wide content such as:

- Site name and description
- Navigation menu items
- Footer content and links
- Contact information

### Page Content (`content/pages/`)

Each page has its own YAML file for easy content management:

#### Home Page (`home.yml`)

```yaml
hero:
  title: "Welcome to Med.AI.rian 🌊"
  subtitle: "Hi 👋 I'm Atef Attia — Senior Generative AI Engineer"
  buttons:
    - text: "View Projects"
      link: "/projects"
```

#### Projects Page (`projects.yml`)

```yaml
title: Projects
projects:
  - title: "AI-Powered Image Recognition"
    image: "path/to/image.jpg"
    description: "Project description"
    tags:
      - Python
      - TensorFlow
    link: "#"
    featured: true  # New feature to highlight projects on the home page
```

#### Skills Page (`skills.yml`)

```yaml
title: Skills & Expertise
subtitle: Machine Learning, Development, and Tools
skills:
  - title: Machine Learning & AI
    skills:
      - Deep Learning
      - Computer Vision
```

### Featured Projects

- Projects can now be marked as featured by adding `featured: true` in the `projects.yml` file
- Featured projects will automatically appear on the home page
- Easily control which projects are highlighted by toggling the `featured` flag
- Provides a dynamic way to showcase key projects without duplicating project information

### How to Update Content

1. **Add/Edit Projects**:
   - Open `content/pages/projects.yml`
   - Add a new project entry or modify existing ones
   - Each project needs: title, image, description, tags, and link

2. **Update Skills**:
   - Edit `content/pages/skills.yml`
   - Add or remove skills under each category
   - Modify skill categories as needed

3. **Change Home Page**:
   - Modify `content/pages/home.yml`
   - Update hero section text and buttons
   - Edit featured sections

4. **Site-wide Changes**:
   - Edit `content/base.yml` for navigation, footer, or contact info
   - Changes will reflect across all pages

The templates will automatically update to reflect any changes made to these YAML files, making content management simple and maintainable.

## Deployment

The app is deployed on Heroku using [uv](https://docs.astral.sh/uv/). Heroku automatically detects `uv.lock` and runs `uv sync --locked --no-default-groups` during build.

### First-time Setup

1. Install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. Login and link the app:

   ```bash
   make login
   heroku git:remote -a <your-app-name>
   ```

3. Set environment variables:

   ```bash
   heroku config:set MAIL_PASSWORD=your_mail_password
   ```

### Deploy

```bash
make login
make deploy
```

### Custom Domain

```bash
heroku domains:add www.medairian.ai
heroku domains:add medairian.ai
```

Then add DNS records at your domain registrar:

```
CNAME www -> [your-heroku-dns-target]
ALIAS/ANAME @ -> [your-heroku-dns-target]
```

Get the DNS target with `heroku domains`.

## Features

- Modern, responsive design
- YAML-based content management
- Smooth page transitions
- Easy to maintain and extend
- Professional showcase of Generative AI engineering skills
- Dynamic Projects and Skills pages
- Contact information

# Med.AI.rian - Professional Portfolio

A modern web application showcasing my professional experience as a Senior Machine Learning Engineer. The name Med.AI.rian represents my Tunisian roots (Mediterranean) combined with my expertise in Artificial Intelligence.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Unix/macOS
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

## Project Structure

```
medairian-digital/
├── app.py                  # Main application entry point
├── config.py              # Configuration settings
├── content/              # Content management
│   ├── base.yml         # Base content (navigation, footer)
│   └── pages/           # Page-specific content
│       ├── home.yml     # Home page content
│       ├── contact.yml  # Contact page content
│       ├── projects.yml # Projects page content
│       └── skills.yml   # Skills page content
├── static/               # Static files (CSS, JS, images)
│   ├── css/             # Stylesheets
│   ├── js/              # JavaScript files
│   └── images/          # Image assets
├── templates/           # Jinja2 templates
│   ├── base.html       # Base template
│   ├── components/     # Reusable components
│   └── pages/          # Page-specific templates
└── routes/             # Route handlers
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
  subtitle: "Hi 👋 I'm Atef Attia — Senior Machine Learning Engineer"
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

## Features

- Modern, responsive design
- YAML-based content management
- Smooth page transitions
- Easy to maintain and extend
- Professional showcase of ML engineering skills
- Dynamic Projects and Skills pages
- Contact information

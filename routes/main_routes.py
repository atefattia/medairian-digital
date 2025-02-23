from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime
from flask_mail import Mail, Message
from utils.content_loader import ContentLoader
import pathlib
import markdown2
from flask import send_from_directory

bp = Blueprint('main', __name__)
mail = Mail()

# Initialize content loader
content_loader = ContentLoader(pathlib.Path(__file__).parent.parent / 'content')

@bp.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@bp.route('/')
def index():
    content = content_loader.get_page_content('home')
    projects_content = content_loader.get_page_content('projects')
    content['projects'] = projects_content.get('projects', [])
    return render_template('pages/home.html', **content)

@bp.route('/about')
def about():
    content = content_loader.get_page_content('about')
    return render_template('pages/about.html', **content)

@bp.route('/projects')
def projects():
    content = content_loader.get_page_content('projects')
    return render_template('pages/projects.html', **content)

@bp.route('/projects/<path:filename>')
def project_detail(filename):
    """Serve individual project Markdown files"""
    # Ensure the file is a Markdown file and exists in the projects directory
    if not filename.endswith('.md'):
        return 'Not Found', 404
    
    project_path = pathlib.Path(__file__).parent.parent / 'content' / 'projects' / filename
    
    if not project_path.exists():
        return 'Not Found', 404
    
    # Read the Markdown content and convert to HTML
    with open(project_path, 'r', encoding='utf-8') as f:
        markdown_content = f.read()
        html_content = markdown2.markdown(markdown_content, extras=['fenced-code-blocks', 'tables'])
    
    source_page = request.args.get('from', 'projects')  # Default to 'projects' if not provided
    source_page = '' if source_page == 'home' else source_page
    # Render the new template
    return render_template('pages/project_detail.html', markdown_content=html_content, source_page=source_page)

@bp.route('/static/images/projects/<path:filename>')
def serve_project_image(filename):
    return send_from_directory('static/images/projects', filename)

@bp.route('/skills')
def skills():
    content = content_loader.get_page_content('skills')
    return render_template('pages/skills.html', **content)

@bp.route('/articles')
def articles():
    content = content_loader.get_page_content('articles')
    return render_template('pages/articles.html', **content)

@bp.route('/contact')
def contact():
    content = content_loader.get_page_content('contact')
    return render_template('pages/contact.html', **content)

@bp.route('/send-message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    if not all([name, email, message]):
        flash('Please fill in all fields', 'error')
        return redirect(url_for('main.contact'))
    
    try:
        msg = Message(
            subject=f'New Contact Form Message from {name}',
            sender=email,
            recipients=['attia.atef92@gmail.com'],
            body=f'''
            Name: {name}
            Email: {email}
            
            Message:
            {message}
            '''
        )
        mail.send(msg)
        flash('Your message has been sent successfully!', 'success')
    except Exception as e:
        flash('An error occurred while sending your message. Please try again later.', 'error')
    
    return redirect(url_for('main.contact'))

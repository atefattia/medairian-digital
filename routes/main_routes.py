from flask import Blueprint, render_template, request, flash, redirect, url_for
from datetime import datetime
from flask_mail import Mail, Message
from utils.content_loader import ContentLoader
import os

bp = Blueprint('main', __name__)
mail = Mail()

# Initialize content loader
content_loader = ContentLoader(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'content'))

@bp.context_processor
def inject_current_year():
    return {'current_year': datetime.now().year}

@bp.route('/')
def index():
    content = content_loader.get_page_content('home')
    return render_template('pages/home.html', **content)

@bp.route('/about')
def about():
    content = content_loader.get_page_content('about')
    return render_template('pages/about.html', **content)

@bp.route('/projects')
def projects():
    content = content_loader.get_page_content('projects')
    return render_template('pages/projects.html', **content)

@bp.route('/skills')
def skills():
    content = content_loader.get_page_content('skills')
    return render_template('pages/skills.html', **content)

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

import os

class Config:
    SECRET_KEY = 'your-secret-key-here'  # Change this in production
    TEMPLATES_AUTO_RELOAD = True
    
    # Mail settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'medairian@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')  # Set this in your environment variables

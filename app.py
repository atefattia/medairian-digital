from flask import Flask
from flask_mail import Mail
from config import Config
from routes import main_routes

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.config.from_object(Config)

    # Initialize Flask-Mail
    mail = Mail(app)

    # Pass mail instance to routes
    main_routes.mail = mail

    # Register blueprints
    app.register_blueprint(main_routes.bp)
    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

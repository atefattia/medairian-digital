from flask import Flask, render_template
from flask_mail import Mail
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize Flask-Mail
mail = Mail(app)

# Import routes after app initialization to avoid circular imports
from routes import main_routes

# Pass mail instance to routes
main_routes.mail = mail

# Register blueprints
app.register_blueprint(main_routes.bp)

if __name__ == '__main__':
    app.run(debug=True)

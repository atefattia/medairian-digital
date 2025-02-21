from flask import Flask, request
from flask_mail import Mail
from config import Config
from rag.rag_chatbot import RAGChatbot
from routes import main_routes
from flask_socketio import SocketIO, emit
import logging
import os
import traceback

# Configure logging
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='/static')
    app.config.from_object(Config)
    
    # Generate a secure random secret key
    app.config['SECRET_KEY'] = os.urandom(24)
    
    # Initialize Flask-Mail
    mail = Mail(app)

    # Pass mail instance to routes
    main_routes.mail = mail

    # Register blueprints
    app.register_blueprint(main_routes.bp)
    return app

app = create_app()

# Configure SocketIO with robust settings
socketio = SocketIO(app, 
    cors_allowed_origins="*",  # Allow all origins for development
    async_mode='threading',  # Use threading mode
    ping_timeout=10,  # Increased timeout
    ping_interval=5   # Increased interval
)

# Global RAG Chatbot instance
rag_chatbot = None

def safe_initialize_rag_chatbot():
    """
    Safely initialize RAG chatbot with comprehensive error handling
    """
    global rag_chatbot
    try:
        rag_chatbot = RAGChatbot()
        logger.info("RAG Chatbot initialized successfully")
        return True
    except Exception as e:
        logger.error(f"Failed to initialize RAG Chatbot: {e}")
        logger.error(traceback.format_exc())
        return False

# Initialize RAG Chatbot when the app starts
safe_initialize_rag_chatbot()

@socketio.on('connect')
def handle_connect():
    logger.info(f"Client connected from {request.remote_addr}")
    
    # Ensure chatbot is initialized
    if not rag_chatbot:
        safe_initialize_rag_chatbot()

@socketio.on('disconnect')
def handle_disconnect():
    logger.info(f"Client disconnected from {request.remote_addr}")

@socketio.on('chat_message')
def handle_message(data):
    global rag_chatbot
    
    # Validate input
    user_message = data.get('message', '').strip()
    if not user_message:
        emit('bot_response', {'message': "🤖 Please provide a valid message."})
        return
    
    # Reinitialize chatbot if needed
    if rag_chatbot is None:
        if not safe_initialize_rag_chatbot():
            emit('bot_response', {'message': "🤖 Chatbot is temporarily unavailable."})
            return
    
    try:
        # Generate response
        bot_response = rag_chatbot.generate_response(user_message)
        emit('bot_response', {'message': bot_response})
    except Exception as e:
        logger.error(f"Error processing message: {e}")
        logger.error(traceback.format_exc())
        emit('bot_response', {'message': f"🤖 An error occurred: {str(e)}"})

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)

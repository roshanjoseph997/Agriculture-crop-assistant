# app.py
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import logging
from model_inference import generate_response  # Ensure this import works

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Changed to DEBUG for more detailed logging
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

app = Flask(__name__)  # Direct app creation instead of create_app function

# More comprehensive CORS configuration
CORS(app, resources={
    r"/*": {  # Changed to catch-all route
        "origins": [
            "http://localhost:3000",  # React
            "http://localhost:5173",  # Vite
            "http://localhost:8080",  # Vue/other
            "*"  # Be cautious in production
        ],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Flask server is running"}), 200

@app.route('/chat', methods=['POST', 'OPTIONS'])
def chat():
    # Handle CORS preflight
    if request.method == 'OPTIONS':
        return jsonify({"status": "success"}), 200

    try:
        # Enhanced logging
        logger.debug(f"Received request headers: {request.headers}")
        logger.debug(f"Request method: {request.method}")
        logger.debug(f"Request data: {request.get_data()}")

        # Ensure JSON data is provided
        if not request.is_json:
            logger.warning("Request without JSON data")
            return jsonify({
                'error': 'Invalid request. JSON required',
                'status': 'error'
            }), 400

        data = request.get_json()
        
        # Validate request data
        if not data:
            logger.warning("Empty request body")
            return jsonify({
                'error': 'No data provided',
                'status': 'error'
            }), 400
        
        message = data.get('message', '').strip()
        language = data.get('language', 'en')
        
        # Validate message
        if not message:
            logger.warning("Empty message received")
            return jsonify({
                'error': 'Message is required',
                'status': 'error'
            }), 400
        
        # Generate AI response
        logger.debug(f"Attempting to generate response for message: {message}")
        response = generate_response(message, language)
        
        logger.info(f"Response generated for message: {message}")
        return jsonify({
            'response': response,
            'status': 'success'
        }), 200
    
    except Exception as e:
        logger.error(f"Unexpected error in chat endpoint: {e}", exc_info=True)
        return jsonify({
            'error': 'Internal server error',
            'details': str(e),
            'status': 'error'
        }), 500

# Ensure this is at the end of the file
if __name__ == '__main__':
    # Ensure the correct model path is used
    logger.info("Starting Flask application")
    app.run(
        host='0.0.0.0', 
        port=5000, 
        debug=True  # Set to True for development
    )

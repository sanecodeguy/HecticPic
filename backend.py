from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os
from dotenv import load_dotenv
from werkzeug.utils import secure_filename

load_dotenv()

app = Flask(__name__)

CORS(app, resources={
    r"/upload": {
        "origins": [
            "http://localhost:5000",  
            "https://hecticpic.vercel.app",  
        ],
        "methods": ["POST", "OPTIONS"], 
        "allow_headers": ["Content-Type"],
        "supports_credentials": False,
        "max_age": 600 
    }
})


DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
CHANNEL_ID = os.getenv('DISCORD_CHANNEL_ID')

@app.route('/')
def home():
    return "HecticPic Backend Running. Use /upload for image uploads."

@app.route('/upload', methods=['POST', 'OPTIONS'])
def upload_to_discord():
    if request.method == 'OPTIONS':
        response = jsonify({"status": "preflight"})
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        return response

    if 'image' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "Empty filename"}), 400

    allowed_extensions = {'png', 'jpg', 'jpeg', 'gif'}
    if ('.' not in file.filename or 
        file.filename.split('.')[-1].lower() not in allowed_extensions):
        return jsonify({"error": "Invalid file type"}), 400

    try:
        filename = secure_filename(file.filename)
        if not filename:
            raise ValueError("Invalid filename after sanitization")

        headers = {"Authorization": f"Bot {DISCORD_BOT_TOKEN}"}
        response = requests.post(
            f"https://discord.com/api/v10/channels/{CHANNEL_ID}/messages",
            headers=headers,
            files={"file": (filename, file.stream)},
            timeout=30 
        )

        response.raise_for_status()
        image_url = response.json()["attachments"][0]["url"]
        
        response = jsonify({"url": image_url})
        response.headers.add("Access-Control-Allow-Origin", "*")
        return response

    except requests.exceptions.RequestException as e:
        error_response = jsonify({"error": f"Discord API error: {str(e)}"})
        error_response.headers.add("Access-Control-Allow-Origin", "*")
        return error_response, 500
    except Exception as e:
        error_response = jsonify({"error": f"Server error: {str(e)}"})
        error_response.headers.add("Access-Control-Allow-Origin", "*")
        return error_response, 500

if __name__ == '__main__':
    if not DISCORD_BOT_TOKEN or not CHANNEL_ID:
        raise ValueError("Missing required environment variables")
    
    port = int(os.getenv('PORT', 5001))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('FLASK_DEBUG', 'false') == 'true')

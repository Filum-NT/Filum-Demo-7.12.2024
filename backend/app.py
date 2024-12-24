from flask import Flask, jsonify, request
from flask_cors import CORS
from services.patient_service import search_patients_service
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend communication

# Root route for the homepage
@app.route('/')
def home():
    """
    Welcome page for the API.
    """
    return jsonify({
        "message": "Welcome to the Filum Patient Search API!",
        "endpoints": {
            "search-patients": "POST /search-patients"
        }
    }), 200

@app.route('/search-patients', methods=['POST'])
def search_patients():
    """
    Handles patient search requests.
    """
    # Extract search parameters from the request
    data = request.json
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    condition_code = data.get('condition_code')
    gender = data.get('gender')
    age_range = data.get('age_range')

    if not condition_code or not gender or not age_range:
        return jsonify({"error": "Missing required parameters"}), 400

    # Process the patient search
    try:
        result = search_patients_service(condition_code, gender, age_range)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Set the port to 8080, which is the default for Google Cloud App Engine
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS
from services.patient_service import search_patients_service
from utils.gpt_integration import get_testing_timeline
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
            "search-patients": "POST /search-patients",
            "fetch-testing-timeline": "POST /fetch-testing-timeline"
        }
    }), 200

@app.route('/search-patients', methods=['POST'])
def search_patients():
    """
    Handles patient search requests.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    condition_code = data.get('condition_code')
    gender = data.get('gender')
    age_range = data.get('age_range')

    if not condition_code or not gender or not age_range:
        return jsonify({"error": "Missing required parameters"}), 400

    try:
        # Retrieve patient details (and associated condition info)
        patient_results = search_patients_service(condition_code, gender, age_range)
        # Return results under a "patients" key for clarity.
        return jsonify({"patients": patient_results}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/fetch-testing-timeline', methods=['POST'])
def fetch_testing_timeline():
    """
    Expects a JSON payload with a "patient_details" key containing a patient object.
    Calls the GPT API to generate a testing timeline for that patient.
    """
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid JSON payload"}), 400

    patient_details = data.get("patient_details")
    if not patient_details:
        return jsonify({"error": "Missing patient_details"}), 400

    try:
        # Call GPT integration with the patient details wrapped in a list.
        timeline = get_testing_timeline([patient_details])
        return jsonify({"testing_timeline": timeline}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Set the port to 8080 (the default for Google Cloud App Engine)
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=True)

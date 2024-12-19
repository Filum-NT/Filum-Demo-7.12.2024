from flask import Flask, jsonify, request
import requests
import os
from utils.api_client import fetch_patient_data
from utils.data_filter import filter_patient_data
from flask_cors import CORS
from google.auth.transport.requests import Request
from google.oauth2 import service_account

from dotenv import load_dotenv
load_dotenv()  # This will load the API_KEY from the .env file

app = Flask(__name__)
CORS(app)  # Enable CORS so the frontend can talk to this backend

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
    # Get search parameters from the request
    condition_code = request.json.get('condition_code')
    gender = request.json.get('gender')
    age_range = request.json.get('age_range')

    # Validate the inputs
    if not condition_code or not gender or not age_range:
        return jsonify({"error": "Missing parameters"}), 400

    # Call the Google Cloud Healthcare API to get patients
    patients = get_patients_from_gcp(condition_code, gender, age_range)

    # Return the filtered patients as a response
    return jsonify(patients)

def get_patients_from_gcp(condition_code, gender, age_range):
    # Define the URL for your Google Cloud Healthcare API
    gcp_url = "https://healthcare.googleapis.com/v1/projects/synthea-1000patient-11-11-2024/locations/northamerica-northeast1/datasets/Synthea_Dataset_11.11.2024/fhirStores/Synthetic_data_demo_11.11.2024/fhir/Patient"

    # Path to your service account key file
    service_account_file = os.environ.get('SERVICE_ACCOUNT_FILE_PATH')

    # Authenticate using the service account
    credentials = service_account.Credentials.from_service_account_file(
        service_account_file,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    
    # If the credentials are expired or not yet set, refresh them
    if credentials.expired or not credentials.valid:
        credentials.refresh(Request())

    # Create an authenticated session
    authed_session = Request(credentials)

    # Send a GET request to the Google Cloud Healthcare API
    response = requests.get(
        gcp_url,
        params={
            'condition_code': condition_code,
            'gender': gender,
            'age_range': age_range
        },
        headers={
            'Authorization': f'Bearer {credentials.token}',  # Add the token here
            'Content-Type': 'application/json'
        }
    )

    if response.status_code != 200:
        raise Exception(f"Error fetching data from GCP: {response.status_code}")

    # Return the JSON data (list of patients) from the response
    return response.json()

  
  
    # Get the API key from the environment variables
    api_key = os.environ.get('API_KEY')  # API key for authentication

    # Send a GET request to the Google Cloud Healthcare API, passing the API key for authentication
    response = requests.get(
        gcp_url,
        params={
            'condition_code': condition_code,
            'gender': gender,
            'age_range': age_range
        },
        headers={
            'Authorization': f'Bearer {api_key}',  # Use the API key as a Bearer token
            'Content-Type': 'application/json'
        }
    )

    if response.status_code != 200:
        raise Exception(f"Error fetching data from GCP: {response.status_code}")

    # Return the JSON data (list of patients) from the response
    return response.json()

if __name__ == '__main__':
    # Set the port to 8080, which is the default for Google Cloud App Engine
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

if __name__ == "__main__":
    app.run(debug=True)

print(f"Loaded API Key: {os.getenv('API_KEY')}")
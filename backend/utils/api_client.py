import os
import requests

# Load environment variables
API_KEY = os.getenv("API_KEY")
FHIR_URL = "https://healthcare.googleapis.com/v1/projects/synthea-1000patient-11-11-2024/locations/northamerica-northeast1/datasets/Synthea_Dataset_11.11.2024/fhirStores/Synthetic_data_demo_11.11.2024/fhir/Patient"
def fetch_patient_data():
    """
    Fetch patient data from Google Cloud Healthcare API.
    """
    url = f"{FHIR_URL}/Patient"
    headers = {"Authorization": f"Bearer {API_KEY}"}

    try:
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            raise Exception(f"Error fetching data: {response.status_code}, {response.text}")

        return response.json().get("entry", [])  # Return patient data entries

    except Exception as e:
        raise Exception(f"Failed to fetch patient data: {str(e)}")

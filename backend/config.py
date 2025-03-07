import os
from dotenv import load_dotenv

load_dotenv()  # This will load the API_KEY from the .env file

class Config:
    # Google Cloud Configuration
    GCP_PROJECT_ID = os.getenv("GCP_PROJECT_ID")
    GCP_LOCATION = os.getenv("GCP_LOCATION")
    GCP_DATASET = os.getenv("GCP_DATASET")
    GCP_FHIR_STORE = os.getenv("GCP_FHIR_STORE")

    # Service Account File Path
    SERVICE_ACCOUNT_FILE_PATH = "keys/service_account.json"

    # Derived URLs
    FHIR_BASE_URL = (
        f"https://healthcare.googleapis.com/v1/projects/{GCP_PROJECT_ID}"
        f"/locations/{GCP_LOCATION}/datasets/{GCP_DATASET}"
        f"/fhirStores/{GCP_FHIR_STORE}/fhir"
    )

    # General Settings
    PORT = int(os.getenv("PORT", 8080))
    DEBUG = os.getenv("DEBUG", "false").lower() == "true"

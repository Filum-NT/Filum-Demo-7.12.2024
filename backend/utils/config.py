import os

class Config:
    API_KEY = os.getenv("API_KEY")
    FHIR_BASE_URL = "https://healthcare.googleapis.com/v1/projects/synthea-1000patient-11-11-2024/locations/northamerica-northeast1/datasets/Synthea_Dataset_11.11.2024/fhirStores/Synthetic_data_demo_11.11.2024/fhir/Patient"

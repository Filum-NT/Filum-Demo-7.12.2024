from google.auth.transport import requests
from google.oauth2 import service_account
from config import Config
from utils.date_utils import calculate_birth_date_range

def get_authorized_session():
    """
    Creates an authorized session for GCP.
    """
    credentials = service_account.Credentials.from_service_account_file(
        Config.SERVICE_ACCOUNT_FILE_PATH
    ).with_scopes(["https://www.googleapis.com/auth/cloud-platform"])
    return requests.AuthorizedSession(credentials)

def get_patients_from_gcp(condition_code, gender, age_range):
    """
    Fetches patient data from GCP.
    """
    session = get_authorized_session()
    min_birth_date, max_birth_date = calculate_birth_date_range(age_range)
    query = f"gender={gender}&birthdate=ge{min_birth_date}&birthdate=le{max_birth_date}&condition.code={condition_code}"
    url = f"{Config.FHIR_BASE_URL}/Patient/_search?{query}"

    headers = {"Content-Type": "application/fhir+json;charset=utf-8"}
    response = session.post(url, headers=headers)
    response.raise_for_status()
    return response.json()

def get_conditions_from_gcp(condition_code, gender, age_range):
    """
    Fetches condition data from GCP.
    """
    session = get_authorized_session()
    min_birth_date, max_birth_date = calculate_birth_date_range(age_range)
    query = f"subject.gender={gender}&subject.birthdate=ge{min_birth_date}&subject.birthdate=le{max_birth_date}&code={condition_code}"
    url = f"{Config.FHIR_BASE_URL}/Condition/_search?{query}"

    headers = {"Content-Type": "application/fhir+json;charset=utf-8"}
    response = session.post(url, headers=headers)
    response.raise_for_status()
    return response.json()

import google.auth
from google.auth.transport import requests
from google.auth import impersonated_credentials
from config import Config
from utils.date_utils import calculate_birth_date_range

def get_authorized_session():
    """
    Creates an authorized session for GCP using service account impersonation.
    """
  # Retrieve the default source credentials from the environment.
    source_credentials, _ = google.auth.default()
    
    # Define the scopes required for accessing the Healthcare API.
    target_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
    
    # Create impersonated credentials for the target service account.
    impersonated_creds = impersonated_credentials.Credentials(
        source_credentials=source_credentials,
        target_principal=Config.TARGET_SERVICE_ACCOUNT,
        target_scopes=target_scopes,
        lifetime=3600  # Lifetime of the impersonated credentials in seconds (max 3600)
    )
    
    # Return an AuthorizedSession that will attach the necessary authorization headers.
    return requests.AuthorizedSession(impersonated_creds)

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

def get_conditions_from_gcp(condition_search, gender, age_range):
    """
    Fetches condition data from GCP.
    """
    session = get_authorized_session()
    min_birth_date, max_birth_date = calculate_birth_date_range(age_range)
    query = (
        f"subject.gender={gender}&subject.birthdate=ge{min_birth_date}"
        f"&subject.birthdate=le{max_birth_date}&code:text={condition_search}"
    )
    url = f"{Config.FHIR_BASE_URL}/Condition/_search?{query}"

    headers = {"Content-Type": "application/fhir+json;charset=utf-8"}
    response = session.post(url, headers=headers)
    response.raise_for_status()
    return response.json()

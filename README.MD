# Filum Demo
A demo project showcasing integration with the Google Cloud Healthcare API for managing and querying FHIR resources. This project includes both a backend API and a simple frontend for interacting with patient data.

## Setup Instructions

### Backend
1. Place the service account JSON file from the Google Cloud Console
in `backend/keys/` and rename it to `service_account.json`

2. If it doesn't exist, create a `.env` file in `backend/` with fields:
    - GCP_PROJECT_ID=
    - GCP_LOCATION=
    - GCP_DATASET=
    - GCP_FHIR_STORE=
    - SERVICE_ACCOUNT_FILE_PATH=keys/service_account.json

3. Open terminal and navigate to project directory

4. Navigate to backend: `cd backend`

5. Create virtual environment: `python3 -m venv venv`

6. Activate venv: `source venv/bin/activate`

7. Install dependencies: `pip3 install -r requirements.txt`

8. Run the server: `python3 app.py`

### Frontend

1. Navigate to the project in Finder or File Explorer

2. Open `frontend` folder

3. Right-click on `index.html` and open with your browser of choice

## Notes
The Cloud Healthcare API has limited support for chained and reverse chained searches. For queries that need generalized and scalable SQL join functionality, consider [Exporting FHIR resources to BigQuery](https://cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery).

## Possible Next Steps

### Backend
- Implement additional query parameters such as condition text
- Add user authentication
- Add caching to optimize repeated queries

### Frontend
- Build a React frontend
- Add charts or graphs to visualize data (age distribution, gender ratios)
- Improve UI design with a framework like Tailwind CSS

### Deployment
- Create Docker containers for easy deployment
- Deploy application to a cloud service like Google Cloud Run
# Filum Demo
A demo project showcasing integration with the Google Cloud Healthcare API for managing and querying FHIR resources. This project includes both a backend API and a simple frontend for interacting with patient data.

## Setup Instructions

### Backend
1. Download the service account JSON file from the Google Cloud Console
and rename it to `service_account.json`

2. Create a `keys` folder (if it doesn't exist) in `backend/` and place
`service_account.json` in `backend/keys`

3. Open terminal and navigate to project directory

4. Navigate to backend: `cd backend`

5. Create a `.env` file using `.env_template` and add credentials:
    `cp .env_template .env` (can copy/paste manually too)

6. Create virtual environment: `python3 -m venv venv`

7. Activate venv: `source venv/bin/activate`

8. Install dependencies: `pip3 install -r requirements.txt`

9. Run the server: `python3 app.py`

### Frontend

1. Navigate to the project in Finder or File Explorer

2. Open `frontend` folder

3. Right-click on `index.html` and open with your browser of choice

## Notes
The Cloud Healthcare API has limited support for chained and reverse chained searches. For queries that need generalized and scalable SQL join functionality, consider [Exporting FHIR resources to BigQuery](https://cloud.google.com/healthcare-api/docs/how-tos/fhir-export-bigquery).

## Possible Next Steps

### Backend
- Implement additional query parameters such as condition text [DONE]
- AI or GPT integration [DONE]
- Add user authentication
- Add caching to optimize repeated queries

### Frontend
- Build a React frontend
- Add charts or graphs to visualize data (age distribution, gender ratios)
- Improve UI design with a framework like Tailwind CSS

### Deployment
- Create Docker containers for easy deployment
- Deploy application to a cloud service like Google Cloud Run

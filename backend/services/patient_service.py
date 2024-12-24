from services.gcp_service import get_patients_from_gcp, get_conditions_from_gcp

def search_patients_service(condition_code, gender, age_range):
    """
    Handles patient search and condition matching.
    """
    patients = get_patients_from_gcp(condition_code, gender, age_range)
    conditions = get_conditions_from_gcp(condition_code, gender, age_range)

    # Create a lookup dictionary for patients
    patients_dict = {
        entry['resource']['id']: {
            "id": entry['resource']['id'],
            "name": " ".join(
                entry['resource']['name'][0].get('given', []) +
                [entry['resource']['name'][0].get('family', "")]
            ),
            "birthdate": entry['resource'].get('birthDate'),
            "gender": entry['resource'].get('gender'),
        }
        for entry in patients.get('entry', [])
        if entry['resource']['resourceType'] == "Patient"
    }

    result = []
    for entry in conditions.get('entry', []):
        condition = entry['resource']
        patient_reference = condition['subject']['reference'].split("/")[-1]
        condition_code = condition['code']['coding'][0].get('code')

        # Match condition to patient
        patient_data = patients_dict.get(patient_reference)
        if patient_data:
            result.append({
                "patient_id": patient_data["id"],
                "patient_name": patient_data["name"],
                "patient_birthdate": patient_data["birthdate"],
                "patient_gender": patient_data["gender"],
                "condition_code": condition_code,
            })

    return result

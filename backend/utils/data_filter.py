def filter_patient_data(patients, condition_code, gender, age_range):
    """
    Filter patients based on condition code, gender, and age range.
    """
    filtered_patients = []
    age_min, age_max = map(int, age_range.split('-'))

    for patient in patients:
        patient_resource = patient.get("resource", {})
        patient_gender = patient_resource.get("gender", "").lower()
        patient_conditions = patient_resource.get("condition", [])
        patient_age = patient_resource.get("age", 0)

        # Match gender
        if patient_gender != gender.lower():
            continue

        # Match age range
        if not (age_min <= patient_age <= age_max):
            continue

        # Match condition code
        if any(condition.get("code", {}).get("coding", [{}])[0].get("code") == condition_code for condition in patient_conditions):
            filtered_patients.append(patient_resource)

    return filtered_patients

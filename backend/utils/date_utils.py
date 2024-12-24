from datetime import datetime

def calculate_birth_date_range(age_range):
    """
    Calculate min and max birth dates based on age range.
    """
    today = datetime.today()
    age_min, age_max = map(int, age_range.split('-'))
    max_birth_date = datetime(today.year - age_min, today.month, today.day).strftime('%Y-%m-%d')
    min_birth_date = datetime(today.year - age_max, today.month, today.day).strftime('%Y-%m-%d')
    return min_birth_date, max_birth_date

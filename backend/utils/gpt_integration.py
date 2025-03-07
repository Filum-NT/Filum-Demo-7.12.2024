import os
from openai import OpenAI

# Instantiate the OpenAI client with your API key.
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def get_testing_timeline(patient_details):
    """
    Constructs a prompt with patient details and calls the GPT API using the new ChatCompletion interface
    to get a testing timeline.
    """
    # Format the patient details as a multi-line string.
    formatted_details = "\n".join(
        [
            f"Patient ID: {p['patient_id']}, Name: {p['patient_name']}, "
            f"Birthdate: {p['patient_birthdate']}, Gender: {p['patient_gender']}, "
            f"Condition: {p.get('condition_display', 'N/A')}"
            for p in patient_details
        ]
    )

    # Build your prompt.
    prompt = (
        "You are a medical assistant trained to provide screening and chronic disease management timelines \
        based on evidence-based medical guidelines. Based on the following patient's details, return \
        a structured testing schedule with recommended tests, frequency, and \
        rationale based on guidelines provided by evidence-based bodies and task-forces. Do not diagnose but strictly \
        base recommendations on evidence-based guidelines\n\n"
        "Patient Details:\n"
        f"{formatted_details}\n\n"
    )

    try:
        # Call the Chat Completion API using the new interface.
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # or choose the appropriate model, such as "gpt-3.5-turbo" if needed.
            messages=[
                {"role": "system", "content": "You are a helpful medical advisor."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=800,
            temperature=0.5,
        )
        # Extract the generated timeline from the response.
        timeline = response.choices[0].message.content.strip()
        return timeline

    except Exception as e:
        # Print or log the error for troubleshooting.
        print("Error in GPT API call:", e)
        return "Unable to generate testing timeline at this time."

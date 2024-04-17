import requests

def get_survey_numbers(district, mandal, village):
    url = "https://dharani.telangana.gov.in/getSurveyNumbers"  # Replace this with the actual API endpoint
    params = {
        "district": district,
        "mandal": mandal,
        "village": village
    }

    response = requests.get(url, params=params)
    data = response.json()
    survey_numbers = data["surveyNumbers"] 
    return survey_numbers

district = "Your District"
mandal = "Your Mandal"
village = "Your Village"

survey_numbers = get_survey_numbers(district, mandal, village)
print("Survey Numbers:", survey_numbers)

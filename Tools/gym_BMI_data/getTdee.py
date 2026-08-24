import os
import requests

def getTdee(activityLevel, gender, age, weight, height):
    """
    :API_description: Calculate the Total Daily Energy Expenditure (TDEE) based on user's activity level, gender, age, weight, and height.
    :param activityLevel: The level of physical activity (e.g., 'active').
    :param gender: The gender of the individual (e.g., 'male').
    :param age: The age of the individual (e.g., 25).
    :param weight: The weight of the individual in kilograms (e.g., 78).
    :param height: The height of the individual in centimeters (e.g., 180).
    :response_schema: 
    ```json
{
  "result": 2927
}
```
    """
    url = "https://gym-fit.p.rapidapi.com/v1/calculator/tdee"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"activityLevel": activityLevel, "gender": gender, "age": age, "weight": weight, "height": height}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "gym-fit.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
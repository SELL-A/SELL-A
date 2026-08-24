import os
import requests

def getBmr(weight, height, gender, age):
    """
    :API_description: Calculate the Basal Metabolic Rate (BMR) based on weight, height, gender, and age.
    :param weight: The weight of the individual in kilograms(eg. "70").
    :param height: The height of the individual in centimeters(eg. "175").
    :param gender: The gender of the individual, either 'male' or 'female'.
    :param age: The age of the individual in years(eg. "30").
    :response_schema: 
    ```json
{
  "result": 1785
}
```
    """
    url = "https://gym-fit.p.rapidapi.com/v1/calculator/bmr"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"weight": weight, "height": height, "gender": gender, "age": age}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "gym-fit.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
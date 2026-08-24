import os
import requests

def getBmi(weight, height):
    """
    :API_description: Calculate Body Mass Index (BMI) based on weight and height.
    :param weight: The weight of the individual in kilograms(eg. "70").
    :param height: The height of the individual in centimeters(eg. "175").
    :response_schema: 
    ```json
{
  "result": 24.1
}
```
    """
    url = "https://gym-fit.p.rapidapi.com/v1/calculator/bmi"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"weight": weight, "height": height}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "gym-fit.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


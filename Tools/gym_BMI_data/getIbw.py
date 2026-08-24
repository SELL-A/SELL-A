import os
import requests

def getIbw(height):
    """
    :API_description: Calculate the Ideal Body Weight (IBW) based on height.
    :param height: The height of the individual in centimeters.
    :response_schema: 
    ```json
{
  "result": 75.1
}
```
    """
    url = "https://gym-fit.p.rapidapi.com/v1/calculator/ibw"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"height": height}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "gym-fit.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
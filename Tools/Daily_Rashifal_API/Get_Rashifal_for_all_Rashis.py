import os
import requests

def Get_Rashifal_for_all_Rashis():
    """
    :API_description: Retrieves the daily horoscope for all twelve zodiac signs, providing the name of each sign and its associated horoscope.
    :param: None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "result": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "rashi": {
            "type": "string",
            "description": "The name of the zodiac sign."
          },
          "rashifal": {
            "type": "string",
            "description": "The horoscope or astrological prediction for the zodiac sign."
          }
        },
        "required": ["rashi", "rashifal"]
      }
    }
  },
  "required": ["result"]
}
```
    """
    url = "https://daily-rashifal-api.p.rapidapi.com/all"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "daily-rashifal-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")



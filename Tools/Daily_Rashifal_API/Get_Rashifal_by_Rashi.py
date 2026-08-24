import os
import requests

def Get_Rashifal_by_Rashi(sign):
    """
    :API_description: Retrieve today's horoscope for a specified zodiac sign.
    :param sign: The zodiac sign for which the rashifal is requested (e.g., 'aries').
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "rashi": {
      "type": "string",
      "description": "The zodiac sign, e.g., 'aries'."
    },
    "rashifal": {
      "type": "string",
      "description": "The horoscope or astrological prediction for the given zodiac sign."
    }
  },
  "required": ["rashi", "rashifal"]
}
    ```
    """
    url = f"https://daily-rashifal-api.p.rapidapi.com/{sign}"
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


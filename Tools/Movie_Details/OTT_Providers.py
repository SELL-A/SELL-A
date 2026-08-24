import os
import requests

def OTT_Providers(region):
    """
    :API_description: Retrieve a list of supported streaming services, including their names, short codes, and values, tailored for specific regions like USA and India.
    :param region: The region code for which the OTT platforms are to be retrieved(e.g. "US").currently only USA and India region is supported enter param 'US' for USA and 'IN' for India.
    :response_schema: 
    ```json
    {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "label": {
            "type": "string",
            "description": "The name of the streaming service."
          },
          "short": {
            "type": "string",
            "description": "A short code or abbreviation for the streaming service."
          },
          "value": {
            "type": "string",
            "description": "The value associated with the streaming service, typically a URL or identifier."
          }
        },
        "required": ["label", "short", "value"]
      }
    }
    ```
    """
    url = "https://ott-details.p.rapidapi.com/getPlatforms"

    querystring = {"region": region}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "ott-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
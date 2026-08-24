import os
import requests

def Sports_List():
    """
    :API_description: Retrieves a list of sports, including their full names, optional abbreviated names, and unique identifiers.
    :param None
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "name": {
        "type": "string",
        "description": "The full name of the sport."
      },
      "shortName": {
        "type": "string",
        "description": "The abbreviated name of the sport, if available."
      },
      "id": {
        "type": "integer",
        "description": "A unique identifier for the sport."
      }
    },
    "required": ["name", "id"]
  }
}
```
    """
    url = "https://global-data.p.rapidapi.com/sport/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "global-data.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
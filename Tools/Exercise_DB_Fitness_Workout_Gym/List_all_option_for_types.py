import os
import requests

def List_all_option_for_types():
    """
    :API_description: Retrieve a list of exercise equipment types for categorizing exercises based on required equipment.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "list": {
      "type": "array",
      "description": "An array of strings representing different types of exercise equipment.",
      "items": {
        "type": "string"
      }
    }
  },
  "required": ["list"]
}
```
    """
    url = "https://exercise-db-fitness-workout-gym.p.rapidapi.com/list/equipment"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "exercise-db-fitness-workout-gym.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
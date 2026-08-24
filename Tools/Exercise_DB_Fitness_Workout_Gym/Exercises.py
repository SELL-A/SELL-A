import os
import requests

def Exercises():
    """
    :API_description: This endpoint retrieves a list of exercise IDs, facilitating workout planning and tracking in fitness applications.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "excercises_ids": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "An array of exercise IDs, each representing a specific exercise."
    }
  },
  "required": ["excercises_ids"]
}
```
    """
    url = "https://exercise-db-fitness-workout-gym.p.rapidapi.com/exercises"
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


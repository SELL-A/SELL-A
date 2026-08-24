import os
import requests

def Equipment_Filter(equipment):
    """
    :API_description: Retrieve a list of exercises filtered by equipment, including details like category, force type, and targeted muscles.
    :param equipment: The type of equipment for which exercises are to be retrieved(eg: "barbell").
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "category": {
        "type": "string",
        "description": "The category of the exercise."
      },
      "equipment": {
        "type": "string",
        "description": "The equipment used for the exercise."
      },
      "force": {
        "type": "string",
        "description": "The type of force applied during the exercise (push or pull)."
      },
      "id": {
        "type": "string",
        "description": "Unique identifier for the exercise."
      },
      "images": {
        "type": "array",
        "items": {
          "type": "string",
          "description": "URLs to images illustrating the exercise."
        }
      },
      "instructions": {
        "type": "array",
        "items": {
          "type": "string",
          "description": "Step-by-step instructions for performing the exercise."
        }
      },
      "level": {
        "type": "string",
        "description": "The difficulty level of the exercise (beginner, intermediate, expert)."
      },
      "mechanic": {
        "type": "string",
        "description": "The mechanical type of the exercise (compound or isolation)."
      },
      "name": {
        "type": "string",
        "description": "The name of the exercise."
      },
      "primaryMuscles": {
        "type": "array",
        "items": {
          "type": "string",
          "description": "The primary muscles targeted by the exercise."
        }
      },
      "secondaryMuscles": {
        "type": "array",
        "items": {
          "type": "string",
          "description": "The secondary muscles targeted by the exercise."
        }
      }
    },
    "required": [
      "category",
      "equipment",
      "force",
      "id",
      "images",
      "instructions",
      "level",
      "mechanic",
      "name",
      "primaryMuscles",
      "secondaryMuscles"
    ]
  }
}
```
    """
    url = f"https://exercise-db-fitness-workout-gym.p.rapidapi.com/exercises/equipment/{equipment}"
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


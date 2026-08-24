import os
import requests

def Mechanic_Filter(mechanic):
    """
    :API_description: Retrieve a list of exercises filtered by their mechanical aspect, including details like equipment, force type, and targeted muscle groups.
    :param mechanic: The type of mechanic for the exercises (e.g., isolation, compound).
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "category": {
        "type": "string",
        "description": "The category of the exercise (e.g., strength, stretching)."
      },
      "equipment": {
        "type": ["string", "null"],
        "description": "The equipment used for the exercise (e.g., machine, dumbbell, body only)."
      },
      "force": {
        "type": "string",
        "description": "The type of force applied during the exercise (e.g., pull, push, static)."
      },
      "id": {
        "type": "string",
        "description": "A unique identifier for the exercise."
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
        "description": "The difficulty level of the exercise (e.g., beginner, intermediate, expert)."
      },
      "mechanic": {
        "type": "string",
        "description": "The mechanical aspect of the exercise (e.g., isolation, compound)."
      },
      "name": {
        "type": "string",
        "description": "The name of the exercise."
      },
      "primaryMuscles": {
        "type": "array",
        "items": {
          "type": "string",
          "description": "The primary muscle groups targeted by the exercise."
        }
      },
      "secondaryMuscles": {
        "type": "array",
        "items": {
          "type": "string",
          "description": "The secondary muscle groups targeted by the exercise."
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
    url = f"https://exercise-db-fitness-workout-gym.p.rapidapi.com/exercises/mechanic/{mechanic}"
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
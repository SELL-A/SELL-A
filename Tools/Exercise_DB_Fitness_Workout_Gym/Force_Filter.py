import os
import requests

def Force_Filter(force):
    """
    :API_description: Retrieve a comprehensive list of exercises filtered by force type, including details like category, equipment, difficulty, and targeted muscles.
    :param force: The type of force to filter exercises by (e.g., 'push', 'pull').
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "category": {
        "type": "string",
        "description": "The category of the exercise (e.g., stretching, strength, plyometrics)."
      },
      "equipment": {
        "type": ["string", "null"],
        "description": "The equipment required for the exercise, if any."
      },
      "force": {
        "type": "string",
        "description": "The type of force involved in the exercise (e.g., push, pull)."
      },
      "id": {
        "type": "string",
        "description": "A unique identifier for the exercise."
      },
      "images": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of URLs pointing to images related to the exercise."
      },
      "instructions": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A step-by-step list of instructions for performing the exercise."
      },
      "level": {
        "type": "string",
        "description": "The difficulty level of the exercise (e.g., beginner, intermediate, advanced)."
      },
      "mechanic": {
        "type": ["string", "null"],
        "description": "The mechanical type of the exercise (e.g., compound, isolation)."
      },
      "name": {
        "type": "string",
        "description": "The name of the exercise."
      },
      "primaryMuscles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of primary muscles targeted by the exercise."
      },
      "secondaryMuscles": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "A list of secondary muscles targeted by the exercise."
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
    url = f"https://exercise-db-fitness-workout-gym.p.rapidapi.com/exercises/force/{force}"
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
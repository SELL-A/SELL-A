import os
import requests

def Muscle_Filter(muscle):
    """
    :API_description: Retrieve a comprehensive list of exercises filtered by muscle groups, including details like category, equipment, force type, and targeted muscles.
    :param muscle: The muscle group for which exercises are to be retrieved(eg: "chest").
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "category": {
        "type": "string",
        "description": "The category of the exercise (e.g., strength, stretching, plyometrics)."
      },
      "equipment": {
        "type": "string",
        "description": "The type of equipment used for the exercise (e.g., kettlebells, dumbbell, barbell)."
      },
      "force": {
        "type": "string",
        "description": "The type of force involved in the exercise (e.g., push, pull, static)."
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
        "description": "The mechanical aspect of the exercise (e.g., compound, isolation)."
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
    url = f"https://exercise-db-fitness-workout-gym.p.rapidapi.com/exercises/muscle/{muscle}"
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
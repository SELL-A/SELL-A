import os
import requests

def Exercise_by_ID(exercise_id):
    """
    :API_description: Retrieve comprehensive details about a specific exercise using its unique identifier.
    :param exercise_id: The unique identifier for the exercise(eg: "90_90_Hamstring").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "category": {
      "type": "string",
      "description": "The category of the exercise, e.g., 'stretching'."
    },
    "equipment": {
      "type": "string",
      "description": "The equipment required for the exercise, e.g., 'body only'."
    },
    "force": {
      "type": "string",
      "description": "The type of force used in the exercise, e.g., 'push'."
    },
    "id": {
      "type": "string",
      "description": "A unique identifier for the exercise, e.g., '90_90_Hamstring'."
    },
    "images": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "URLs to images related to the exercise."
      },
      "description": "An array of image URLs associated with the exercise."
    },
    "instructions": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "Step-by-step instructions for performing the exercise."
      },
      "description": "An array of strings containing detailed instructions for the exercise."
    },
    "level": {
      "type": "string",
      "description": "The difficulty level of the exercise, e.g., 'beginner'."
    },
    "mechanic": {
      "type": ["string", "null"],
      "description": "The mechanic type of the exercise, which can be null if not applicable."
    },
    "name": {
      "type": "string",
      "description": "The name of the exercise, e.g., '90/90 Hamstring'."
    },
    "primaryMuscles": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "Names of the primary muscles targeted by the exercise."
      },
      "description": "An array of strings listing the primary muscles involved in the exercise."
    },
    "secondaryMuscles": {
      "type": "array",
      "items": {
        "type": "string",
        "description": "Names of the secondary muscles targeted by the exercise."
      },
      "description": "An array of strings listing the secondary muscles involved in the exercise."
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
    "name",
    "primaryMuscles",
    "secondaryMuscles"
  ]
}
```
    """
    url = f"https://exercise-db-fitness-workout-gym.p.rapidapi.com/exercise/{exercise_id}"
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


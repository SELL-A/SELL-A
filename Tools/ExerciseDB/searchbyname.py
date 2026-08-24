import os
import requests

def searchbyname(name, offset="0", limit="10"):
    """
    :API_description: Retrieve a list of exercises matching the specified name, including details like targeted body parts, equipment, and step-by-step instructions.
    :param name: The name of the exercise to retrieve(eg:"glute") .URL-decoded name fragment used for case-insensitive substring matching. 
    :param offset: The starting point within the collection of resource results.
    :param limit: The maximum number of results to return.
    :response_schema: 
    ```json
[
  {
    "bodyPart": "upper legs",
    "equipment": "assisted",
    "id": "1709",
    "name": "assisted lying glutes stretch",
    "target": "glutes",
    "secondaryMuscles": [
      "hamstrings"
    ],
    "instructions": [
      "Lie on your back with your legs extended.",
      "Bend your right knee and place your right ankle on your left thigh, just above the knee."
    ],
    "description": "...",
    "difficulty": "beginner",
    "category": "stretching"
  },
  {
    "bodyPart": "upper legs",
    "equipment": "assisted",
    "id": "1710",
    "name": "assisted lying gluteus and piriformis stretch",
    "target": "glutes",
    "secondaryMuscles": [
      "hamstrings"
    ],
    "instructions": [
      "Lie on your back with your legs extended.",
      "Bend your right knee and place your right ankle on your left thigh, just above the knee.",
      "Grasp your left thigh with both hands and gently pull it towards your chest."
    ],
    "description": "...",
    "difficulty": "beginner",
    "category": "stretching"
  },
  {
    "bodyPart": "upper legs",
    "equipment": "barbell",
    "id": "1409",
    "name": "barbell glute bridge",
    "target": "glutes",
    "secondaryMuscles": [
      "hamstrings",
      "lower back"
    ],
    "instructions": [
      "Start by lying flat on your back on the ground with your knees bent and feet flat on the floor.",
      "Place a barbell across your hips, holding it securely with both hands.",
      "Engage your glutes and core muscles, then lift your hips off the ground until your body forms a straight line from your knees to your shoulders."
    ],
    "description": "...",
    "difficulty": "intermediate",
    "category": "strength"
  }
]
```
    """
    url = f"https://exercisedb.p.rapidapi.com/exercises/name/{name}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"offset": offset, "limit": limit}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "exercisedb.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
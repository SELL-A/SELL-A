import os
import requests

def listExercisesByTarget(target,limit=10, offset=0):
    """
    :API_description: Retrieve a list of exercises targeting a specific muscle group, including details like equipment type, GIF demonstrations, and step-by-step instructions.
    :param target: The primary muscle group targeted by the exercises the allowed values are: abductors, abs, adductors, biceps, calves, cardiovascular system,delts,forearms,glutes,hamstrings,lats,levator scapulae,pectorals,quads,serratus anterior,spine,traps,triceps.
    :param limit: The maximum number of exercises to return.
    :param offset: The number of exercises to skip before starting to collect the result set.
    :response_schema: 
    ```json
[
  {
    "bodyPart": "upper legs",
    "equipment": "leverage machine",
    "id": "0597",
    "name": "lever seated hip abduction",
    "target": "abductors",
    "secondaryMuscles": [
      "glutes",
      "hamstrings"
    ],
    "instructions": [
      "Adjust the seat height so that your knees are at a 90-degree angle.",
      "Sit on the machine with your back against the backrest and your feet on the footrests.",
      "Place your hands on the side handles for stability."
    ],
    "description": "...",
    "difficulty": "beginner",
    "category": "strength"
  },
  {
    "bodyPart": "upper legs",
    "equipment": "resistance band",
    "id": "3006",
    "name": "resistance band seated hip abduction",
    "target": "abductors",
    "secondaryMuscles": [
      "glutes",
      "hamstrings"
    ],
    "instructions": [
      "Sit on a chair or bench with your back straight and feet flat on the ground.",
      "Wrap the resistance band around your thighs, just above your knees.",
      "Place your hands on the sides of the chair or bench for support."
    ],
    "description": "...",
    "difficulty": "beginner",
    "category": "strength"
  }
]
```
    """
    url = f"https://exercisedb.p.rapidapi.com/exercises/target/{target}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"limit": limit, "offset": offset}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "exercisedb.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
import os
import requests

def listExercises(limit, offset):
    """
    :API_description: Retrieve a list of exercises with details including targeted body parts, equipment, GIF illustrations, unique IDs, names, muscle groups, and instructions.
    :param limit: The maximum number of exercises to return.
    :param offset: The number of exercises to skip before starting to collect the result set.
    :response_schema: 
    ```json
[
  {
    "bodyPart": "back",
    "equipment": "cable",
    "id": "0007",
    "name": "alternate lateral pulldown",
    "target": "lats",
    "secondaryMuscles": [
      "biceps",
      "rhomboids"
    ],
    "instructions": [
      "Sit on the cable machine with your back straight and feet flat on the ground.",
      "Grasp the handles with an overhand grip, slightly wider than shoulder-width apart."
    ],
    "description": "The alternate lateral pulldown is a cable machine exercise targeting the latissimus dorsi, with secondary emphasis on the biceps and rhomboids. It involves pulling handles towards the chest in an alternating fashion, focusing on back strength and muscle engagement.",
    "difficulty": "beginner",
    "category": "strength"
  },
  {
    "bodyPart": "back",
    "equipment": "body weight",
    "id": "3293",
    "name": "archer pull up",
    "target": "lats",
    "secondaryMuscles": [
      "biceps",
      "forearms"
    ],
    "instructions": [
      "Start by hanging from a pull-up bar with an overhand grip, slightly wider than shoulder-width apart.",
      "Engage your core and pull your shoulder blades down and back.",
      "As you pull yourself up, bend one arm and bring your elbow towards your side, while keeping the other arm straight."
    ],
    "description": "The archer pull up is a challenging bodyweight exercise that targets the lats and requires significant strength, coordination, and control. It involves pulling up with one arm while the other remains straight, alternating sides with each repetition.",
    "difficulty": "advanced",
    "category": "strength"
  }
]
```
    """
    url = "https://exercisedb.p.rapidapi.com/exercises"
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


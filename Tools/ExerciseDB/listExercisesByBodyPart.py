import os
import requests

def listExercisesByBodyPart(body_part, limit=10, offset=0):
    """
    :API_description: Retrieve a list of exercises targeting a specific body part, including details like equipment used, GIF illustrations, and muscle groups targeted.
    :param body_part: The body part for which exercises are to be retrieved, the allowed values are: back, cardio, chest, lower arms, lower legs, neck, shoulders, upper arms, upper legs.
    :param limit: The maximum number of exercises to retrieve.
    :param offset: The starting point from which exercises are retrieved.
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
      "Grasp the handles with an overhand grip, slightly wider than shoulder-width apart.",
      "Lean back slightly and pull the handles towards your chest, squeezing your shoulder blades together.",
      "Pause for a moment at the peak of the movement, then slowly release the handles back to the starting position.",
      "Repeat for the desired number of repetitions."
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
      "As you pull yourself up, bend one arm and bring your elbow towards your side, while keeping the other arm straight.",
      "Continue pulling until your chin is above the bar and your bent arm is fully flexed.",
      "Lower yourself back down with control, straightening the bent arm and repeating the movement on the other side.",
      "Alternate sides with each repetition."
    ],
    "description": "The archer pull up is a challenging bodyweight exercise that targets the lats and requires significant strength, coordination, and control. It involves pulling up with one arm while the other remains straight, alternating sides with each repetition.",
    "difficulty": "advanced",
    "category": "strength"
  }
]
```
    """
    url = f"https://exercisedb.p.rapidapi.com/exercises/bodyPart/{body_part}"
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

if __name__ == "__main__":
    print(exercises_bodyPart_bodyPart("chest"))
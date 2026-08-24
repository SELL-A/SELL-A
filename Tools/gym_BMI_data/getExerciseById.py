import os
import requests

def getExerciseById(exercise_id):
    """
    :API_description: Retrieve detailed information about a specific exercise, including muscles involved, alternative exercises, and step-by-step instructions.
    :param exercise_id: The unique identifier for the exercise(eg. "c2b6fccf-2c2c-43e1-aca3-a3cb73caa78b")(depend on searchExercises api).
    :response_schema: 
    ```json
{
  "name": "Bench Press (Barbell)",
  "bodyPart": "Chest",
  "equipment": "Barbell",
  "type": "Compound",
  "image": "",
  "targetMuscles": [
    {
      "id": "ffd76ee8-7633-4062-9c91-9092d637567a",
      "name": "Pectoralis major",
      "bodyPart": "Chest",
      "group": null
    }
  ],
  "secondaryMuscles": [
    {
      "id": "ffd76ee8-7633-4062-9c91-9092d637567a",
      "name": "Pectoralis major",
      "bodyPart": "Chest",
      "group": null
    },
    {
      "id": "dec5954e-80b5-493b-8911-a73ef54d96ee",
      "name": "Triceps brachii",
      "bodyPart": "Arms",
      "group": null
    },
    {
      "id": "d0f075f6-831c-43b9-9749-15e1b74987be",
      "name": "Deltoid",
      "bodyPart": "Shoulders",
      "group": null
    }
  ],
  "instructions": [
    {
      "id": "aaeea543-5402-4a65-b54e-888fd4e66e35",
      "order": 1,
      "description": "Lie on the bench with your eyes directly under the barbell and your feet flat on the ground."
    },
    {
      "id": "b77d7079-2a7c-4f52-80eb-b5a421e6fcd0",
      "order": 2,
      "description": "Grab the bar with a slightly wider than shoulder-width grip and lift it off the rack, fully extending your arms."
    },
    {
      "id": "34d05e76-8454-46ad-b810-4d3f024a57e5",
      "order": 3,
      "description": "Bring your shoulder blades together and lower your shoulders."
    },
    {
      "id": "b55a77a5-f17a-4024-b4e6-10f465caa164",
      "order": 4,
      "description": "Inhale and lower the barbell slowly to touch the lower part of your chest."
    },
    {
      "id": "551140f5-59ee-4685-ac73-af16d498a07d",
      "order": 5,
      "description": "Exhale and push the barbell back up to the starting position, fully extending your arms."
    }
  ],
  "variations": [
    {
      "id": "a1281637-139d-4864-903b-67d62037c16e",
      "name": "Incline Bench Press (Barbell)",
      "bodyPart": "Chest",
      "image": "..."
    },
    {
      "id": "b6707c01-285f-43a2-8c72-5ad3246e352a",
      "name": "Hex Press (Dumbbell)",
      "bodyPart": "Chest",
      "image": "..."
    },
    {
      "id": "c3eece11-94f5-49fc-9789-a03eb217e34b",
      "name": "Decline Bench Press (Barbell)",
      "bodyPart": "Chest",
      "image": "..."
    },
    {
      "id": "8a764a28-b2d8-496e-9d08-fa352280b178",
      "name": "Close Grip Bench Press (Barbell)",
      "bodyPart": "Arms",
      "image": "..."
    }
  ]
}
```
    """
    url = f"https://gym-fit.p.rapidapi.com/v1/exercises/{exercise_id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "gym-fit.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
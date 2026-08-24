import os
import requests

def getExerciseById(exercise_id):
    """
    :API_description: Retrieve detailed information about a specific exercise, including its name, targeted muscles, equipment required, and step-by-step instructions.
    :param exercise_id: The ID of the exercise to retrieve information for(eg:"0001" Exactly 4 characters).
    :response_schema: 
    ```json
  {
  "bodyPart": "waist",
  "equipment": "body weight",
  "id": "0001",
  "name": "3/4 sit-up",
  "target": "abs",
  "secondaryMuscles": [
    "hip flexors",
    "lower back"
  ],
  "instructions": [
    "Lie flat on your back with your knees bent and feet flat on the ground.",
    "Place your hands behind your head with your elbows pointing outwards.",
    "Engaging your abs, slowly lift your upper body off the ground, curling forward until your torso is at a 45-degree angle.",
    "Pause for a moment at the top, then slowly lower your upper body back down to the starting position.",
    "Repeat for the desired number of repetitions."
  ],
  "description": "The 3/4 sit-up is an abdominal exercise performed with body weight. It involves curling the torso up to a 45-degree angle, engaging the abs, hip flexors, and lower back. This movement is commonly used to build core strength and stability.",
  "difficulty": "beginner",
  "category": "strength"
}
```
    """
    url = f"https://exercisedb.p.rapidapi.com/exercises/exercise/{exercise_id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "exercisedb.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


import os
import requests

def listExercisesByEquipment(equipment,limit=10, offset=0):
    """
    :API_description: Retrieve a list of exercises tailored to a specific equipment type, including details like targeted body parts, GIF demonstrations, and step-by-step instructions.
    :param equipment: The equipment type for which to retrieve exercises, the allowed values are: assisted, band, barbell, body weight, bosu ball, cable, dumbbell, elliptical machine, ez barbell, hammer, kettlebell, leverage machine, medicine ball, olympic barbell,resistance band, roller, rope, skierg machine, sled machine, smith machine, stability ball, stationary bike, stepmill machine, tire, trap bar, upper body ergometer, weighted.
    :param limit: The maximum number of exercises to return.
    :param offset: The number of exercises to skip before starting to return results.
    :response_schema: 
    ```json
[
  {
    "bodyPart": "chest",
    "equipment": "assisted",
    "id": "1716",
    "name": "assisted seated pectoralis major stretch with stability ball",
    "target": "pectorals",
    "secondaryMuscles": [
      "shoulders",
      "triceps"
    ],
    "instructions": [
      "Sit on a stability ball with your feet flat on the ground and your back straight.",
      "Hold a stability ball with both hands and extend your arms straight out in front of you."
    ],
    "description": "...",
    "difficulty": "beginner",
    "category": "stretching"
  },
  {
    "bodyPart": "chest",
    "equipment": "assisted",
    "id": "1259",
    "name": "behind head chest stretch",
    "target": "pectorals",
    "secondaryMuscles": [
      "shoulders",
      "triceps"
    ],
    "instructions": [
      "Stand tall with your feet shoulder-width apart.",
      "Interlace your fingers behind your head with your elbows pointing outwards."
    ],
    "description": "...",
    "difficulty": "beginner",
    "category": "stretching"
  }
]
```
    """
    url = f"https://exercisedb.p.rapidapi.com/exercises/equipment/{equipment}"
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


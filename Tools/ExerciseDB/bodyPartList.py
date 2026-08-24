import os
import requests

def bodyPartList():
    """
    :API_description: Retrieve a list of exercises categorized by muscle groups, including details like exercise ID, name, type, targeted muscle group, equipment, difficulty, and instructions.
    :param None
    :response_schema: 
    ```json
[
  "back",
  "cardio",
  "chest",
  "lower arms",
  "lower legs",
  "neck",
  "shoulders",
  "upper arms",
  "upper legs",
  "waist"
]
    ```
    """
    url = "https://exercisedb.p.rapidapi.com/exercises/bodyPartList"
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
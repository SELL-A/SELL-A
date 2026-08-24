import os
import requests

def getMuscleById(id):
    """
    :API_description: Retrieve detailed information about a specific muscle, including its name, location, group, heads, and an image URL.
    :param id: The ID of the muscle to retrieve information for(depend on searchMuscles api).
    :response_schema: 
    ```json
{
  "id": "df03e634-d5d7-4d61-bc23-15b5e2f708bb",
  "name": "Adductor longus",
  "bodyPart": "Legs",
  "group": "Adductors",
  "heads": [],
  "images": {
    "front": "...",
    "back": "..."
  }
}
```
    """
    url = f"https://gym-fit.p.rapidapi.com/v1/muscles/{id}"
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



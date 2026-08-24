import os
import requests

def searchExercises(search, number):
    """
    :API_description: Retrieve a list of exercises, including their unique IDs, names, and targeted body parts.
    :param number: The number of exercises to retrieve.
    :param search: The search query for exercises(eg. "The partial or full exercise name").
    :response_schema: 
    ```json
{
  "results": [
    {
      "id": "c2b6fccf-2c2c-43e1-aca3-a3cb73caa78b",
      "name": "Bench Press (Barbell)",
      "bodyPart": "Chest",
      "image": "..."
    },
    {
      "id": "a1281637-139d-4864-903b-67d62037c16e",
      "name": "Incline Bench Press (Barbell)",
      "bodyPart": "Chest",
      "image": "..."
    },
    {
      "id": "c3eece11-94f5-49fc-9789-a03eb217e34b",
      "name": "Decline Bench Press (Barbell)",
      "bodyPart": "Chest",
      "image": "..."
    }
  ],
  "total": 3,
  "count": 3
}
```
    """
    url = "https://gym-fit.p.rapidapi.com/v1/exercises/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"number": number, "offset": 0, "search": search}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "gym-fit.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


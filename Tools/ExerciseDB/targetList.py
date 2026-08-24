import os
import requests

def targetList():
    """
    :API_description: Retrieve a list of muscle groups and cardiovascular system details, useful for fitness or medical applications.
    :param None
    :response_schema: 
    ```json
[
  "abductors",
  "abs",
  "adductors",
  "biceps",
  "calves",
  "cardiovascular system",
  "delts",
  "forearms"
]
```

    """
    url = "https://exercisedb.p.rapidapi.com/exercises/targetList"
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
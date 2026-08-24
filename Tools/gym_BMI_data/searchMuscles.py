import os
import requests

def searchMuscles(search, number):
    """
    :API_description: Retrieve a list of muscles based on body part, name, or number of results.
    :param search: The search query for muscles(eg. "The partial or full muscle name").
    :param number: The number of muscle records to retrieve.
    :response_schema: 
    ```json
{
  "results": [
    {
      "id": "22456832-adb8-4eef-bdf6-03c03ede89fa",
      "name": "Adductor brevis",
      "bodyPart": "Legs",
      "group": "Adductors"
    },
    {
      "id": "df03e634-d5d7-4d61-bc23-15b5e2f708bb",
      "name": "Adductor longus",
      "bodyPart": "Legs",
      "group": "Adductors"
    },
    {
      "id": "af4088f9-a989-4f23-9cd9-49558602c761",
      "name": "Adductor magnus",
      "bodyPart": "Legs",
      "group": "Adductors"
    }
  ],
  "total": 3,
  "count": 3
}
```
or
```json
{
  "results": [],
  "total": 0,
  "count": 0
}
```


    """
    url = "https://gym-fit.p.rapidapi.com/v1/muscles/search"
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


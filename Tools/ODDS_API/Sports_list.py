import os
import requests
def Sports_list():
    """
    :API_description: Get a list of all available sports.
    :param None
    :response_schema: 
    ```json
[
  {
    "id": 1,
    "name": "Football",
    "slug": "football"
  },
  {
    "id": 2,
    "name": "Tennis",
    "slug": "tennis"
  },
  {
    "id": 3,
    "name": "Basketball",
    "slug": "basketball"
  },
  {
    "id": 4,
    "name": "Hockey",
    "slug": "hockey"
  },
  {
    "id": 5,
    "name": "Baseball",
    "slug": "baseball"
  },
  {
    "id": 6,
    "name": "Volleyball",
    "slug": "volleyball"
  },
  {
    "id": 7,
    "name": "Esports",
    "slug": "esports"
  },
  {
    "id": 8,
    "name": "MMA",
    "slug": "mma"
  }
]
```
    """
    url = "https://odds-feed.p.rapidapi.com/api/v1/sports"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "odds-feed.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
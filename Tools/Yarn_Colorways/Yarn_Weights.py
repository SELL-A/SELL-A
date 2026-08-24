import os
import requests

def Yarn_Weights():
    """
    :API_description: Retrieve a list of yarn weights, including their names and unique identifiers, useful for filtering or matching yarn-related results.
    :param None
    :response_schema: 
    ```json
{
  "meta": {
    "total": 12
  },
  "data": [
    {
      "name": "Thread",
      "id": "t",
      "yarns": 3
    },
    {
      "name": "Cobweb",
      "id": "c",
      "yarns": 0
    },
    {
      "name": "Lace",
      "id": "l",
      "yarns": 7
    },
    {
      "name": "Light Fingering",
      "id": "lf",
      "yarns": 3
    },
    {
      "name": "Fingering",
      "id": "f",
      "yarns": 19
    },
    {
      "name": "Sport",
      "id": "s",
      "yarns": 31
    },
    {
      "name": "DK",
      "id": "d",
      "yarns": 86
    },
    {
      "name": "Worsted",
      "id": "w",
      "yarns": 58
    },
    {
      "name": "Aran",
      "id": "a",
      "yarns": 30
    },
    {
      "name": "Bulky",
      "id": "b",
      "yarns": 4
    },
    {
      "name": "Super Bulky",
      "id": "sb",
      "yarns": 14
    },
    {
      "name": "Jumbo",
      "id": "j",
      "yarns": 0
    }
  ]
}
    ```
    """
    url = "https://yarn-colorways.p.rapidapi.com/v3/weights"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yarn-colorways.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
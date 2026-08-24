import os
import requests

def GetAllCategories():
    """
    :API_description: Retrieve a list of plant categories, each described by a string value.
    :param None
    :response_schema: 
    ```json
[
  {
    "Category": "Dracaena"
  },
  {
    "Category": "Palm"
  },
  {
    "Category": "Anthurium"
  },
  {
    "Category": "Other"
  },
  {
    "Category": "Aglaonema"
  },
  {
    "Category": "Hanging"
  },
  {
    "Category": "Bromeliad"
  },
  {
    "Category": "Spathiphyllum"
  },
  {
    "Category": "Flower"
  },
  {
    "Category": "Aralia"
  },
  {
    "Category": "Ficus"
  },
  {
    "Category": "Sansevieria"
  },
  {
    "Category": "Foliage plant"
  },
  {
    "Category": "Dieffenbachia"
  },
  {
    "Category": "Philodendron"
  },
  {
    "Category": "Cactus & Succulent"
  },
  {
    "Category": "Schefflera"
  },
  {
    "Category": "Topiairy"
  },
  {
    "Category": "Fern"
  },
  {
    "Category": "Grass"
  },
  {
    "Category": "Ground Cover"
  }
]
```
    """
    url = "https://house-plants2.p.rapidapi.com/categories"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "house-plants2.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")



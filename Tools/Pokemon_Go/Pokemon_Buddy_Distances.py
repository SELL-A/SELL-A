import os
import requests

def Pokemon_Buddy_Distances():
    """
    :API_description: Retrieves distances required to gain candy for each Pokémon, including their ID, name, and form.
    :param None
    :response_schema: 
    ```json
{
  "1": [
    {
      "distance": 1,
      "form": "Normal",
      "pokemon_id": 10,
      "pokemon_name": "Caterpie"
    },
    {
      "distance": 1,
      "form": "Normal",
      "pokemon_id": 11,
      "pokemon_name": "Metapod"
    },
    {
      "distance": 1,
      "form": "Normal",
      "pokemon_id": 12,
      "pokemon_name": "Butterfree"
    }
  ],
  "3": [
    {
      "distance": 3,
      "form": "Fall_2019",
      "pokemon_id": 1,
      "pokemon_name": "Bulbasaur"
    },
    {
      "distance": 3,
      "form": "Normal",
      "pokemon_id": 1,
      "pokemon_name": "Bulbasaur"
    }
  ],
  "5": [
    {
      "distance": 5,
      "form": "Normal",
      "pokemon_id": 95,
      "pokemon_name": "Onix"
    },
    {
      "distance": 5,
      "form": "Normal",
      "pokemon_id": 106,
      "pokemon_name": "Hitmonlee"
    },
    {
      "distance": 5,
      "form": "Normal",
      "pokemon_id": 107,
      "pokemon_name": "Hitmonchan"
    }
  ],
  "20": [
    {
      "distance": 20,
      "form": "Galarian",
      "pokemon_id": 144,
      "pokemon_name": "Articuno"
    },
    {
      "distance": 20,
      "form": "Normal",
      "pokemon_id": 144,
      "pokemon_name": "Articuno"
    },
    {
      "distance": 20,
      "form": "Galarian",
      "pokemon_id": 145,
      "pokemon_name": "Zapdos"
    }
  ]
}
```
    """
    url = "https://pokemon-go1.p.rapidapi.com/pokemon_buddy_distances.json"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "pokemon-go1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")



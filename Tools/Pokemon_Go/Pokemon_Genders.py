import os
import requests

def Pokemon_Genders():
    """
    :API_description: This API provides detailed gender ratio information for Pokémon, categorizing them into '0M_1F', '1M_0F', and '1M_1F' based on their gender distribution.
    :param None
    :response_schema: 
    ```json
{
  "0M_1F": [
    {
      "form": "Diwali_2024",
      "gender": {
        "female_percent": 1
      },
      "pokemon_id": 25,
      "pokemon_name": "Pikachu"
    },
    {
      "form": "Doctor",
      "gender": {
        "female_percent": 1
      },
      "pokemon_id": 25,
      "pokemon_name": "Pikachu"
    }
  ],
  "1M_0F": [
    {
      "form": "Copy_2019",
      "gender": {
        "male_percent": 1
      },
      "pokemon_id": 25,
      "pokemon_name": "Pikachu"
    },
    {
      "form": "Fall_2019",
      "gender": {
        "male_percent": 1
      },
      "pokemon_id": 25,
      "pokemon_name": "Pikachu"
    },
    {
      "form": "Kurta",
      "gender": {
        "male_percent": 1
      },
      "pokemon_id": 25,
      "pokemon_name": "Pikachu"
    }
  ],
  "1M_1F": [
    {
      "form": "Normal",
      "gender": {
        "female_percent": 0.5,
        "male_percent": 0.5
      },
      "pokemon_id": 10,
      "pokemon_name": "Caterpie"
    },
    {
      "form": "Normal",
      "gender": {
        "female_percent": 0.5,
        "male_percent": 0.5
      },
      "pokemon_id": 11,
      "pokemon_name": "Metapod"
    },
    {
      "form": "Normal",
      "gender": {
        "female_percent": 0.5,
        "male_percent": 0.5
      },
      "pokemon_id": 12,
      "pokemon_name": "Butterfree"
    }
  ],
  "1M_3F": [
    {
      "gender": {
        "female_percent": 0.75,
        "male_percent": 0.25
      },
      "pokemon_id": 35,
      "pokemon_name": "Clefairy"
    },
    {
      "gender": {
        "female_percent": 0.75,
        "male_percent": 0.25
      },
      "pokemon_id": 36,
      "pokemon_name": "Clefable"
    },
    {
      "form": "Alola",
      "gender": {
        "female_percent": 0.75,
        "male_percent": 0.25
      },
      "pokemon_id": 37,
      "pokemon_name": "Vulpix"
    }
  ],
  "1M_7F": [
    {
      "gender": {
        "female_percent": 0.875,
        "male_percent": 0.125
      },
      "pokemon_id": 667,
      "pokemon_name": "Litleo"
    }
  ],
  "3M_1F": [
    {
      "form": "Hisuian",
      "gender": {
        "female_percent": 0.25,
        "male_percent": 0.75
      },
      "pokemon_id": 58,
      "pokemon_name": "Growlithe"
    },
    {
      "form": "Normal",
      "gender": {
        "female_percent": 0.25,
        "male_percent": 0.75
      },
      "pokemon_id": 58,
      "pokemon_name": "Growlithe"
    },
    {
      "form": "Hisuian",
      "gender": {
        "female_percent": 0.25,
        "male_percent": 0.75
      },
      "pokemon_id": 59,
      "pokemon_name": "Arcanine"
    }
  ],
  "7M_1F": [
    {
      "form": "Fall_2019",
      "gender": {
        "female_percent": 0.125,
        "male_percent": 0.875
      },
      "pokemon_id": 1,
      "pokemon_name": "Bulbasaur"
    },
    {
      "form": "Normal",
      "gender": {
        "female_percent": 0.125,
        "male_percent": 0.875
      },
      "pokemon_id": 1,
      "pokemon_name": "Bulbasaur"
    }
  ],
  "Genderless": [
    {
      "form": "Normal",
      "gender": {
        "genderless_percent": 1
      },
      "pokemon_id": 81,
      "pokemon_name": "Magnemite"
    },
    {
      "form": "Normal",
      "gender": {
        "genderless_percent": 1
      },
      "pokemon_id": 82,
      "pokemon_name": "Magneton"
    }
  ]
}
    """
    url = "https://pokemon-go1.p.rapidapi.com/pokemon_genders.json"
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
import os
import requests

def Pokemon_Rarity():
    """
    :API_description: This API categorizes Pokémon into three rarity types: Standard, Legendary, and Mythic, providing details such as Pokémon ID, name, and rarity for each category.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "Legendary": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "form": {
            "type": "string"
          },
          "pokemon_id": {
            "type": "integer"
          },
          "pokemon_name": {
            "type": "string"
          },
          "rarity": {
            "type": "string"
          }
        },
        "required": ["form", "pokemon_id", "pokemon_name", "rarity"]
      }
    },
    "Mythic": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "form": {
            "type": "string"
          },
          "pokemon_id": {
            "type": "integer"
          },
          "pokemon_name": {
            "type": "string"
          },
          "rarity": {
            "type": "string"
          }
        },
        "required": ["form", "pokemon_id", "pokemon_name", "rarity"]
      }
    },
    "Standard": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "form": {
            "type": "string"
          },
          "pokemon_id": {
            "type": "integer"
          },
          "pokemon_name": {
            "type": "string"
          },
          "rarity": {
            "type": "string"
          }
        },
        "required": ["form", "pokemon_id", "pokemon_name", "rarity"]
      }
    },
    "Ultra beast": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "form": {
            "type": "string"
          },
          "pokemon_id": {
            "type": "integer"
          },
          "pokemon_name": {
            "type": "string"
          },
          "rarity": {
            "type": "string"
          }
        },
        "required": ["form", "pokemon_id", "pokemon_name", "rarity"]
      }
    }
  },
  "required": ["Legendary", "Mythic", "Standard", "Ultra beast"]
}
```

    """
    url = "https://pokemon-go1.p.rapidapi.com/pokemon_rarity.json"
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
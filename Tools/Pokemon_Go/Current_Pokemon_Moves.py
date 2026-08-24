import os
import requests

def Current_Pokemon_Moves():
    """
    :API_description: Retrieves detailed information about Pokémon, including unique identifiers, names, forms, and associated moves (fast, charged, and elite).
    :param None
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "charged_moves": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of charged moves for the Pokémon."
      },
      "elite_charged_moves": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of elite charged moves for the Pokémon."
      },
      "elite_fast_moves": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of elite fast moves for the Pokémon."
      },
      "fast_moves": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "List of fast moves for the Pokémon."
      },
      "form": {
        "type": "string",
        "description": "Form of the Pokémon."
      },
      "pokemon_id": {
        "type": "integer",
        "description": "Unique identifier for the Pokémon."
      },
      "pokemon_name": {
        "type": "string",
        "description": "Name of the Pokémon."
      }
    },
    "required": [
      "charged_moves",
      "elite_charged_moves",
      "elite_fast_moves",
      "fast_moves",
      "form",
      "pokemon_id",
      "pokemon_name"
    ]
  }
}
```
    """
    url = "https://pokemon-go1.p.rapidapi.com/current_pokemon_moves.json"
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

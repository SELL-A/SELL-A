import os
import requests

def Pokemon_Evolutions():
    """
    :API_description: Retrieves detailed information about Pokemon evolutions, including base form, ID, name, and possible evolutions with their requirements.
    :param None
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "evolutions": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "candy_required": {
              "type": "integer",
              "description": "Number of candies required for evolution"
            },
            "form": {
              "type": "string",
              "description": "Form of the evolved Pokemon"
            },
            "pokemon_id": {
              "type": "integer",
              "description": "Unique identifier for the evolved Pokemon"
            },
            "pokemon_name": {
              "type": "string",
              "description": "Name of the evolved Pokemon"
            },
            "item_required": {
              "type": ["string", "null"],
              "description": "Item required for evolution, if any"
            },
            "priority": {
              "type": ["integer", "null"],
              "description": "Priority of the evolution, if any"
            },
            "no_candy_cost_if_traded": {
              "type": ["boolean", "null"],
              "description": "Indicates if no candy is required if the Pokemon is traded"
            },
            "lure_required": {
              "type": ["string", "null"],
              "description": "Lure required for evolution, if any"
            }
          },
          "required": ["candy_required", "form", "pokemon_id", "pokemon_name"]
        },
        "description": "List of evolutions for the Pokemon"
      },
      "form": {
        "type": "string",
        "description": "Form of the base Pokemon"
      },
      "pokemon_id": {
        "type": "integer",
        "description": "Unique identifier for the base Pokemon"
      },
      "pokemon_name": {
        "type": "string",
        "description": "Name of the base Pokemon"
      }
    },
    "required": ["evolutions", "form", "pokemon_id", "pokemon_name"]
  }
}
```

    """
    url = "https://pokemon-go1.p.rapidapi.com/pokemon_evolutions.json"
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
import os
import requests
def Pokemon_Names():
    """
    :API_description: This API provides detailed name ratio information for Pokémon.
    :param None
    :response_schema: 
    ```json
{
  "1": {
    "id": 1,
    "name": "Bulbasaur"
  },
  "2": {
    "id": 2,
    "name": "Ivysaur"
  },
  "3": {
    "id": 3,
    "name": "Venusaur"
  },
  "4": {
    "id": 4,
    "name": "Charmander"
  },
  "5": {
    "id": 5,
    "name": "Charmeleon"
  },
  "6": {
    "id": 6,
    "name": "Charizard"
  },
  "7": {
    "id": 7,
    "name": "Squirtle"
  },
  "8": {
    "id": 8,
    "name": "Wartortle"
  },
  "9": {
    "id": 9,
    "name": "Blastoise"
  },
  "10": {
    "id": 10,
    "name": "Caterpie"
  }
}

    ```
    """
    url = "https://pokemon-go1.p.rapidapi.com/pokemon_names.json"
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
import os
import requests

def Vegan_List_of_Foods():
    """
    :API_description: Retrieves a list of vegan recipes, each with an ID, title, difficulty level, and image URL.
    :param None
    :response_schema: 
    ```json
    {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "string",
            "description": "Unique identifier for the recipe."
          },
          "title": {
            "type": "string",
            "description": "Title of the recipe."
          },
          "difficulty": {
            "type": "string",
            "description": "Difficulty level of the recipe."
          },
          "image": {
            "type": "string",
            "description": "URL to the image of the recipe."
          }
        },
        "required": ["id", "title", "difficulty", "image"]
      }
    }
    ```
    """
    url = "https://the-vegan-recipes-db.p.rapidapi.com/"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "the-vegan-recipes-db.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


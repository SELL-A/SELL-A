import os
import requests

def Detailed_Food_Recipe_by_ID(recipe_id):
    """
    :API_description: Retrieves comprehensive details of a specific vegan recipe, including its title, difficulty, ingredients, and cooking instructions.
    :param recipe_id: The ID of the vegan recipe to retrieve(e.g. "45").
    :response_schema: 
    ```json
    {
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
        "portion": {
          "type": "string",
          "description": "Serving size of the recipe."
        },
        "time": {
          "type": "string",
          "description": "Total time required to prepare the recipe."
        },
        "description": {
          "type": "string",
          "description": "Detailed description of the recipe."
        },
        "ingredients": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of ingredients required for the recipe."
        },
        "method": {
          "type": "array",
          "items": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            }
          },
          "description": "Step-by-step instructions for preparing the recipe."
        },
        "image": {
          "type": "string",
          "format": "uri",
          "description": "URL to an image of the prepared recipe."
        }
      },
      "required": [
        "id",
        "title",
        "difficulty",
        "portion",
        "time",
        "description",
        "ingredients",
        "method",
        "image"
      ]
    }
    ```
    """
    url = f"https://the-vegan-recipes-db.p.rapidapi.com/{recipe_id}"
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
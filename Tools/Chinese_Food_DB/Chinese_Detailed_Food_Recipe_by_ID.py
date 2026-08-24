import os
import requests

def Chinese_Detailed_Food_Recipe_by_ID(food_id):
    """
    :API_description: Retrieve detailed information about a specific Chinese recipe, including its title, ingredients, and cooking instructions.
    :param food_id: The unique identifier for the Chinese food item.
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
      "description": "Number of servings the recipe provides."
    },
    "time": {
      "type": "string",
      "description": "Hands-on time required to prepare the recipe."
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
      "description": "Step-by-step cooking instructions for the recipe."
    },
    "image": {
      "type": "string",
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
    url = f"https://chinese-food-db.p.rapidapi.com/{food_id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "chinese-food-db.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
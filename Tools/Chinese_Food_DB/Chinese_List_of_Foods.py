import os
import requests

def Chinese_List_of_Foods():
    """
    :API_description: Retrieves a list of Chinese recipes, including their IDs, titles, difficulty levels, and image URLs.
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
            "description": "Difficulty level of the recipe, typically 'Easy' or 'Medium'."
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
    url = "https://chinese-food-db.p.rapidapi.com/"
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
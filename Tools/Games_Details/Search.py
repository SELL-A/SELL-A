import os
import requests

def Search(sugg):
    """
    :API_description: Searches for games and related digital content within the platform's store, returning matching items with details such as name, price, and image.
    :param sugg: The suggestion string used to search for game details.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "integer",
      "description": "HTTP status code indicating the response status"
    },
    "message": {
      "type": "string",
      "description": "Text message describing the response outcome"
    },
    "data": {
      "type": "object",
      "properties": {
        "search": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "description": "Unique identifier for the item (optional field)"
              },
              "name": {
                "type": "string",
                "description": "Name/title of the item"
              },
              "image": {
                "type": "string",
                "description": "URL to the item's thumbnail/image"
              },
              "price": {
                "type": "string",
                "description": "Price information (can be 'Free', price amount, or 'comming soon')"
              }
            },
            "required": ["name", "image", "price"]
          },
          "description": "Array of search results containing item details"
        },
        "total": {
          "type": "integer",
          "description": "Total number of search results returned"
        }
      },
      "required": ["search", "total"]
    }
  },
  "required": ["status", "message", "data"]
}
```
    """
    url = "https://games-details.p.rapidapi.com/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "sugg": sugg
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "games-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json().get('data', {})
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


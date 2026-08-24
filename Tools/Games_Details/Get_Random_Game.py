import os
import requests

def Get_Random_Game(page_no):
    """
    :API_description: Retrieves a paginated list of games or applications from a gaming platform catalog, including details such as ID, name, release date, pricing, and header images.
    :param page_no: The page number to retrieve game details from allowed values are 1, 2.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "integer",
      "description": "HTTP status code indicating the success or failure of the API request"
    },
    "message": {
      "type": "string",
      "description": "Human-readable message describing the result of the API call"
    },
    "data": {
      "type": "object",
      "properties": {
        "pages": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "description": "Unique identifier for the game/application (string representation)"
              },
              "name": {
                "type": "string",
                "description": "Name/title of the game or application"
              },
              "release_date": {
                "type": "string",
                "description": "Release date in abbreviated format (e.g., 'Mar 24, 2025')"
              },
              "price": {
                "type": "string",
                "description": "Price information, either monetary value or 'Free'"
              },
              "img": {
                "type": "string", 
                "description": "URL to the game/application header image hosted on Steam CDN"
              }
            },
            "required": ["id", "name", "release_date", "price", "img"]
          },
          "description": "Array of game/application objects with their details"
        },
        "current_page": {
          "type": "integer",
          "description": "Current page number in paginated results"
        },
        "total_page": {
          "type": "integer",
          "description": "Total number of pages available in paginated results"
        }
      },
      "required": ["pages", "current_page", "total_page"]
    }
  },
  "required": ["status", "message", "data"]
}
```
    """
    url = f"https://games-details.p.rapidapi.com/page/{page_no}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "games-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', {})
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")



import os
import requests

def Makes(direction="asc", sort="id"):
    """
    :API_description: Retrieve a list of automobile makes with their unique identifiers and names, along with metadata such as pagination details.
    :param direction: The direction of sorting, e.g., 'asc' for ascending.
    :param sort: The field by which to sort, e.g., 'id'.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "collection": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string",
          "description": "The URL endpoint used to fetch the data."
        },
        "count": {
          "type": "integer",
          "description": "The number of items in the current response."
        },
        "pages": {
          "type": "integer",
          "description": "The total number of pages available."
        },
        "total": {
          "type": "integer",
          "description": "The total number of items available."
        },
        "next": {
          "type": "string",
          "description": "The URL for the next page of results (if available)."
        },
        "prev": {
          "type": "string",
          "description": "The URL for the previous page of results (if available)."
        },
        "first": {
          "type": "string",
          "description": "The URL for the first page of results."
        },
        "last": {
          "type": "string",
          "description": "The URL for the last page of results (if available)."
        }
      },
      "required": ["url", "count", "pages", "total", "next", "prev", "first", "last"]
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the item."
          },
          "name": {
            "type": "string",
            "description": "Name of the item."
          }
        },
        "required": ["id", "name"]
      },
      "description": "List of items returned by the API."
    }
  },
  "required": ["collection", "data"]
}
```
    """
    url = "https://car-api2.p.rapidapi.com/api/makes"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"direction": direction, "sort": sort}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "car-api2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
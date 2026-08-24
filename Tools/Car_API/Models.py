import os
import requests

def Models(sort="id", direction="asc", year="2020", verbose="yes"):
    """
    :API_description: Retrieve a paginated list of car models with details like model ID, make ID, model name, and make details. Supports filtering by year, make, model, trim, or make_id.
    :param sort: The attribute to sort by (e.g., 'id').
    :param direction: The direction of sorting ('asc' or 'desc').
    :param year: The year of the car models to filter.
    :param verbose: Whether to include verbose details ('yes' or 'no').
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
          "description": "The URL used for the API request."
        },
        "count": {
          "type": "integer",
          "description": "The number of items returned in the current page."
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
          "description": "The URL for the next page of results."
        },
        "prev": {
          "type": "string",
          "description": "The URL for the previous page of results."
        },
        "first": {
          "type": "string",
          "description": "The URL for the first page of results."
        },
        "last": {
          "type": "string",
          "description": "The URL for the last page of results."
        }
      }
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the model."
          },
          "make_id": {
            "type": "integer",
            "description": "Unique identifier for the make of the model."
          },
          "name": {
            "type": "string",
            "description": "Name of the model."
          },
          "make": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer",
                "description": "Unique identifier for the make."
              },
              "name": {
                "type": "string",
                "description": "Name of the make."
              }
            }
          }
        }
      }
    }
  }
}
```
    """
    url = "https://car-api2.p.rapidapi.com/api/models"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"sort": sort, "direction": direction, "year": year, "verbose": verbose}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "car-api2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
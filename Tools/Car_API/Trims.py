import os
import requests

def Trims(direction, sort, year, verbose):
    """
    :API_description: Retrieve a paginated list of vehicle trims for the year 2020, including detailed specifications and pricing.
    :param direction: The direction of sorting, e.g., 'asc' or 'desc'.
    :param sort: The field by which to sort the results, e.g., 'id'.
    :param year: The year of the car trims to retrieve.
    :param verbose: Whether to include verbose information, e.g., 'yes' or 'no'.
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
          "description": "The URL of the API endpoint used to retrieve the data."
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
            "description": "Unique identifier for the trim."
          },
          "make_model_id": {
            "type": "integer",
            "description": "Unique identifier for the make and model."
          },
          "year": {
            "type": "integer",
            "description": "The year of the vehicle."
          },
          "name": {
            "type": "string",
            "description": "The name of the trim."
          },
          "description": {
            "type": "string",
            "description": "A description of the trim."
          },
          "msrp": {
            "type": "integer",
            "description": "Manufacturer's Suggested Retail Price."
          },
          "invoice": {
            "type": "integer",
            "description": "The invoice price of the vehicle."
          },
          "created": {
            "type": "string",
            "format": "date-time",
            "description": "The date and time when the record was created."
          },
          "modified": {
            "type": "string",
            "format": "date-time",
            "description": "The date and time when the record was last modified."
          },
          "make_model": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer",
                "description": "Unique identifier for the make and model."
              },
              "make_id": {
                "type": "integer",
                "description": "Unique identifier for the make."
              },
              "name": {
                "type": "string",
                "description": "The name of the make and model."
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
                    "description": "The name of the make."
                  }
                },
                "required": ["id", "name"]
              }
            },
            "required": ["id", "make_id", "name", "make"]
          }
        },
        "required": ["id", "make_model_id", "year", "name", "description", "msrp", "invoice", "created", "modified", "make_model"]
      }
    }
  },
  "required": ["collection", "data"]
}
    ```
    """
    url = "https://car-api2.p.rapidapi.com/api/trims"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"direction": direction, "sort": sort, "year": year, "verbose": verbose}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "car-api2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
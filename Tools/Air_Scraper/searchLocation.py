import os
import requests

def searchLocation(query):
    """
    :API_description: Retrieve a list of cities and airports with their hierarchical locations, coordinates, and unique identifiers for search or mapping applications.
    :param query: The search term used to find car locations.
    :response_schema: 
    ```json
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean",
          "description": "Indicates the status of the API response."
        },
        "timestamp": {
          "type": "integer",
          "description": "The timestamp when the API response was generated."
        },
        "data": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "hierarchy": {
                "type": "string",
                "description": "The hierarchical location of the entity, separated by '|'."
              },
              "location": {
                "type": "string",
                "description": "The geographical coordinates of the entity in the format 'latitude, longitude'."
              },
              "entity_name": {
                "type": "string",
                "description": "The name of the entity."
              },
              "highlight": {
                "type": "object",
                "properties": {
                  "entity_name": {
                    "type": "string",
                    "description": "The highlighted name of the entity."
                  },
                  "hierarchy": {
                    "type": "string",
                    "description": "The highlighted hierarchical location of the entity."
                  }
                },
                "description": "Contains the highlighted versions of the entity name and hierarchy."
              },
              "entity_id": {
                "type": "string",
                "description": "A unique identifier for the entity."
              },
              "class": {
                "type": "string",
                "description": "The class or type of the entity, such as 'City' or 'Airport'."
              }
            },
            "required": ["hierarchy", "location", "entity_name", "highlight", "entity_id", "class"]
          },
          "description": "An array of entities, each containing detailed information about a location."
        }
      },
      "required": ["status", "timestamp", "data"]
    }
    ```
    """
    url = "https://sky-scrapper.p.rapidapi.com/api/v1/cars/searchLocation"

    querystring = {"query": query}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
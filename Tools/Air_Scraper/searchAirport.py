import os
import requests

def searchAirport(query):
    """
    :API_description: Retrieves a list of airports and cities related to a specified location, providing detailed information for presentation and navigation.
    :param query: The search term for the airport. Name of the location where the Airport is situated.
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
          "description": "The timestamp of the API response in milliseconds since epoch."
        },
        "data": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "presentation": {
                "type": "object",
                "properties": {
                  "title": {
                    "type": "string",
                    "description": "The main title of the location."
                  },
                  "suggestionTitle": {
                    "type": "string",
                    "description": "A suggested title for the location, often including additional details."
                  },
                  "subtitle": {
                    "type": "string",
                    "description": "A subtitle providing additional context, typically the country."
                  }
                },
                "required": ["title", "suggestionTitle", "subtitle"]
              },
              "navigation": {
                "type": "object",
                "properties": {
                  "entityId": {
                    "type": "string",
                    "description": "A unique identifier for the entity."
                  },
                  "entityType": {
                    "type": "string",
                    "description": "The type of the entity, such as 'CITY' or 'AIRPORT'."
                  },
                  "localizedName": {
                    "type": "string",
                    "description": "The localized name of the entity."
                  },
                  "relevantFlightParams": {
                    "type": "object",
                    "properties": {
                      "skyId": {
                        "type": "string",
                        "description": "A unique identifier for flight-related parameters."
                      },
                      "entityId": {
                        "type": "string",
                        "description": "A unique identifier for the entity."
                      },
                      "flightPlaceType": {
                        "type": "string",
                        "description": "The type of place relevant to flights, such as 'CITY' or 'AIRPORT'."
                      },
                      "localizedName": {
                        "type": "string",
                        "description": "The localized name of the entity."
                      }
                    },
                    "required": ["skyId", "entityId", "flightPlaceType", "localizedName"]
                  },
                  "relevantHotelParams": {
                    "type": "object",
                    "properties": {
                      "entityId": {
                        "type": "string",
                        "description": "A unique identifier for the entity."
                      },
                      "entityType": {
                        "type": "string",
                        "description": "The type of the entity, such as 'CITY'."
                      },
                      "localizedName": {
                        "type": "string",
                        "description": "The localized name of the entity."
                      }
                    },
                    "required": ["entityId", "entityType", "localizedName"]
                  }
                },
                "required": ["entityId", "entityType", "localizedName", "relevantFlightParams", "relevantHotelParams"]
              }
            },
            "required": ["presentation", "navigation"]
          }
        }
      },
      "required": ["status", "timestamp", "data"]
    }
    ```
    """
    url = "https://sky-scrapper.p.rapidapi.com/api/v1/flights/searchAirport"

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


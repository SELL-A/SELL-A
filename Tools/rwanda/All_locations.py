import os
import requests

def All_locations():
    """
    :API_description: Retrieves a hierarchical structure of administrative divisions in Rwanda, including provinces, districts, sectors, cells, and villages.
    :param None
    :response_schema: 
    ```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "description": "Status of the API response, typically 'success' or 'error'."
    },
    "statusCode": {
      "type": "integer",
      "description": "HTTP status code of the response, typically 200 for success."
    },
    "message": {
      "type": "string",
      "description": "A descriptive message about the response, often providing context or details about the data returned."
    },
    "data": {
      "type": "array",
      "description": "An array containing hierarchical data representing provinces, districts, sectors, cells, and villages in Rwanda.",
      "items": {
        "type": "object",
        "properties": {
          "East": {
            "type": "array",
            "description": "An array of objects representing districts in the Eastern province of Rwanda.",
            "items": {
              "type": "object",
              "properties": {
                "Bugesera": {
                  "type": "array",
                  "description": "An array of objects representing sectors in the Bugesera district.",
                  "items": {
                    "type": "object",
                    "properties": {
                      "Gashora": {
                        "type": "array",
                        "description": "An array of objects representing cells in the Gashora sector.",
                        "items": {
                          "type": "object",
                          "properties": {
                            "Biryogo": {
                              "type": "array",
                              "description": "An array of strings representing villages in the Biryogo cell.",
                              "items": {
                                "type": "string"
                              }
                            },
                            "Kabuye": {
                              "type": "array",
                              "description": "An array of strings representing villages in the Kabuye cell.",
                              "items": {
                                "type": "string"
                              }
                            },
                            "Kagomasi": {
                              "type": "array",
                              "description": "An array of strings representing villages in the Kagomasi cell.",
                              "items": {
                                "type": "string"
                              }
                            },
                            "Mwendo": {
                              "type": "array",
                              "description": "An array of strings representing villages in the Mwendo cell.",
                              "items": {
                                "type": "string"
                              }
                            },
                            "Ramiro": {
                              "type": "array",
                              "description": "An array of strings representing villages in the Ramiro cell.",
                              "items": {
                                "type": "string"
                              }
                            }
                          },
                          "required": ["Biryogo", "Kabuye", "Kagomasi", "Mwendo", "Ramiro"]
                        }
                      }
                    },
                    "required": ["Gashora"]
                  }
                }
              },
              "required": ["Bugesera"]
            }
          }
        },
        "required": ["East"]
      }
    }
  },
  "required": ["status", "statusCode", "message", "data"]
}
```
    """
    url = "https://rwanda.p.rapidapi.com/"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "rwanda.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

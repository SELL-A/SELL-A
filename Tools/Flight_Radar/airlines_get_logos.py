import os
import requests

def airlines_get_logos():
    """
    :API_description: Retrieve detailed information about airline logos, including metadata such as file details and URLs.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "result": {
      "type": "object",
      "properties": {
        "request": {
          "type": "object",
          "properties": {
            "callback": {
              "type": "null"
            },
            "code": {
              "type": "null"
            },
            "format": {
              "type": "string"
            },
            "timestamp": {
              "type": "integer"
            },
            "type": {
              "type": "string"
            }
          },
          "required": ["callback", "code", "format", "timestamp", "type"]
        },
        "response": {
          "type": "object",
          "properties": {
            "airlines": {
              "type": "object",
              "properties": {
                "logotypes": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "file": {
                        "type": "object",
                        "properties": {
                          "modified": {
                            "type": "integer"
                          },
                          "name": {
                            "type": "string"
                          },
                          "size": {
                            "type": "integer"
                          },
                          "type": {
                            "type": "string"
                          },
                          "updated": {
                            "type": "boolean"
                          },
                          "url": {
                            "type": "string"
                          }
                        },
                        "required": ["modified", "name", "size", "type", "updated", "url"]
                      }
                    },
                    "required": ["file"]
                  }
                }
              },
              "required": ["logotypes"]
            }
          },
          "required": ["airlines"]
        }
      },
      "required": ["request", "response"]
    }
  },
  "required": ["result"]
}
```

    """
    url = "https://flight-radar1.p.rapidapi.com/airlines/get-logos"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "flight-radar1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
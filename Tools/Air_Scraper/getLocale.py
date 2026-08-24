import os
import requests

def getLocale():
    """
    :API_description: Retrieves a comprehensive list of languages with their respective codes and descriptions, useful for language selection or localization in web applications.
    :param: None
    :response_schema: 
    ```json
    {
      "type": "object",
      "properties": {
        "status": {
          "type": "boolean",
          "description": "Indicates the status of the API request, typically true for success."
        },
        "message": {
          "type": "string",
          "description": "A message providing additional information about the status of the request, typically 'Success' for successful requests."
        },
        "timestamp": {
          "type": "integer",
          "description": "A timestamp indicating when the response was generated, represented as a Unix epoch time in milliseconds."
        },
        "data": {
          "type": "array",
          "description": "An array of objects, each representing a language with its name and identifier.",
          "items": {
            "type": "object",
            "properties": {
              "text": {
                "type": "string",
                "description": "The name of the language."
              },
              "id": {
                "type": "string",
                "description": "The identifier of the language, typically in the format of a language code (e.g., 'en-US')."
              }
            },
            "required": ["text", "id"]
          }
        }
      },
      "required": ["status", "message", "timestamp", "data"]
    }
    ```
    """
    url = "https://sky-scrapper.p.rapidapi.com/api/v1/getLocale"
  
    
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "sky-scrapper.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
  

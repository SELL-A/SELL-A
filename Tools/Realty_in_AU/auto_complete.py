import os
import requests

def auto_complete(query):
    """
    :API_description: Retrieve location suggestions and property listings related to a given term or phrase, useful for integrating with property listing endpoints.
    :param query: The search query string for which auto-complete suggestions are needed.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "_embedded": {
      "type": "object",
      "properties": {
        "suggestions": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "display": {
                "type": "object",
                "properties": {
                  "subtext": {
                    "type": "string",
                    "description": "A brief description or category of the suggestion."
                  },
                  "text": {
                    "type": "string",
                    "description": "The main text of the suggestion, typically the name of a region, suburb, or property."
                  }
                },
                "required": ["subtext", "text"]
              },
              "id": {
                "type": "string",
                "description": "A unique identifier for the suggestion."
              },
              "source": {
                "type": "object",
                "properties": {
                  "atlasId": {
                    "type": "string",
                    "description": "A unique identifier for the source of the suggestion."
                  },
                  "name": {
                    "type": "string",
                    "description": "The name of the location or property."
                  },
                  "state": {
                    "type": "string",
                    "description": "The state where the location or property is situated."
                  },
                  "postcode": {
                    "type": "string",
                    "description": "The postcode of the location or property."
                  },
                  "channel": {
                    "type": "string",
                    "description": "The channel through which the property is listed (e.g., 'rent', 'buy')."
                  },
                  "image": {
                    "type": "string",
                    "description": "A URL template for the image of the property, with '{size}' as a placeholder for the image size."
                  },
                  "url": {
                    "type": "string",
                    "description": "The URL to the property listing."
                  }
                },
                "required": ["atlasId", "name"]
              },
              "type": {
                "type": "string",
                "description": "The type of suggestion (e.g., 'region', 'suburb', 'listing')."
              }
            },
            "required": ["display", "id", "source", "type"]
          }
        }
      },
      "required": ["suggestions"]
    },
    "count": {
      "type": "string",
      "description": "The number of suggestions returned in the response."
    }
  },
  "required": ["_embedded", "count"]
}
    ```
    """
    url = "https://realty-in-au.p.rapidapi.com/auto-complete"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"query": query}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "realty-in-au.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


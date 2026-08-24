import os
import requests

def Get_Player_Detail_by_Player_ID(playerid):
    """
    :API_description: Retrieves comprehensive profile information for a specific soccer player, including personal details, physical attributes, and career statistics.
    :param playerid: The ID of the player whose details are to be retrieved(eg. "671529").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "description": "API response status indicating success or failure"
    },
    "response": {
      "type": "object",
      "properties": {
        "detail": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "value": {
                "type": "object",
                "properties": {
                  "numberValue": {
                    "type": ["number", "null"],
                    "description": "Numeric value when applicable"
                  },
                  "dateValue": {
                    "type": ["string", "null"],
                    "description": "Date value in /Date()/ format"
                  },
                  "key": {
                    "type": ["string", "null"],
                    "description": "Key identifier for the value"
                  },
                  "fallback": {
                    "type": ["string", "number", "object"],
                    "description": "Fallback display value"
                  },
                  "options": {
                    "type": ["object", "null"],
                    "properties": {
                      "style": {"type": "string"},
                      "unit": {"type": "string"},
                      "unitDisplay": {"type": "string"}
                    }
                  }
                },
                "required": ["key", "fallback"]
              },
              "title": {
                "type": "string",
                "description": "Display title for the attribute"
              },
              "translationKey": {
                "type": "string",
                "description": "Key for internationalization"
              },
              "icon": {
                "type": ["object", "null"],
                "properties": {
                  "type": {"type": "string"},
                  "id": {"type": "string"}
                }
              },
              "countryCode": {
                "type": ["string", "null"],
                "description": "ISO country code"
              }
            },
            "required": ["value", "title", "translationKey"]
          }
        }
      },
      "required": ["detail"]
    }
  },
  "required": ["status", "response"]
}
    ```
    """
    url = "https://free-api-live-football-data.p.rapidapi.com/football-get-player-detail"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"playerid": playerid}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


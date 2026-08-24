import os
import requests

def Event_Markets(event_id):
    """
    :API_description: Get markets for a specific event.
    :param event_id: The ID of the event for which market data is to be retrieved.
    :response_schema: 
    ```JSON_schema
{
  "type": "object",
  "properties": {
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the data entry."
          },
          "event_id": {
            "type": "integer",
            "description": "Identifier for the associated event."
          },
          "period": {
            "type": "string",
            "description": "Period of the event (e.g., FULL_TIME_AND_OT)."
          },
          "bet_type": {
            "type": "string",
            "description": "Type of bet (e.g., BACK)."
          },
          "placing": {
            "type": "string",
            "description": "When the bet is placed (e.g., LIVE)."
          },
          "market_name": {
            "type": "string",
            "description": "Name of the betting market (e.g., 1X2)."
          },
          "value": {
            "type": "integer",
            "description": "Numerical value associated with the entry."
          },
          "market_books": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "market_book_id": {
                  "type": "integer",
                  "description": "Unique identifier for the market book."
                },
                "market_id": {
                  "type": "integer",
                  "description": "Identifier for the market."
                },
                "is_open": {
                  "type": "boolean",
                  "description": "Indicates if the market book is open for betting."
                },
                "book": {
                  "type": "string",
                  "description": "Name of the betting exchange (e.g., BETFAIR_EXCH)."
                },
                "outcome_0": {
                  "type": "integer",
                  "description": "Value for outcome 0 (e.g., odds or price)."
                },
                "outcome_1": {
                  "type": "integer",
                  "description": "Value for outcome 1 (e.g., odds or price)."
                },
                "outcome_2": {
                  "type": "integer",
                  "description": "Value for outcome 2 (e.g., odds or price)."
                },
                "volume_0": {
                  "type": "integer",
                  "description": "Volume or amount for outcome 0."
                },
                "volume_1": {
                  "type": "integer",
                  "description": "Volume or amount for outcome 1."
                },
                "volume_2": {
                  "type": "integer",
                  "description": "Volume or amount for outcome 2."
                }
              },
              "required": ["market_book_id", "market_id", "is_open", "book", "outcome_0", "outcome_1", "outcome_2", "volume_0", "volume_1", "volume_2"],
              "additionalProperties": false
            },
            "description": "List of market books containing detailed betting information for the market."
          }
        },
        "required": ["id", "event_id", "period", "bet_type", "placing", "market_name", "value", "market_books"],
        "additionalProperties": false
      },
      "description": "Array of data entries, each representing a betting market with associated details."
    }
  },
  "required": ["data"],
  "additionalProperties": false
}
```
    """
    url = "https://odds-feed.p.rapidapi.com/api/v1/events/markets"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"event_id": event_id}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "odds-feed.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


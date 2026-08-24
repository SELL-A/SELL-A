import os
import requests

def List_of_Archive_events(sport_id, page_num):
    """
    :API_description: Retrieve a list of archived soccer events, including start times, teams, and period-specific results. Supports pagination for large datasets.
    :param sport_id: The ID of the sport for which odds data is requested(e.g. 1). Minimum: 1,Maximum: 29.
    :param page_num: The page number of the archived data to retrieve.
    :response_schema: 
    ```json
    {
      "type": "object",
      "properties": {
        "sport_id": {
          "type": "integer",
          "description": "Unique identifier for the sport."
        },
        "sport_name": {
          "type": "string",
          "description": "Name of the sport."
        },
        "events": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "event_id": {
                "type": "integer",
                "description": "Unique identifier for the event."
              },
              "sport_id": {
                "type": "integer",
                "description": "Unique identifier for the sport associated with the event."
              },
              "league_id": {
                "type": "integer",
                "description": "Unique identifier for the league associated with the event."
              },
              "league_name": {
                "type": "string",
                "description": "Name of the league associated with the event."
              },
              "starts": {
                "type": "string",
                "format": "date-time",
                "description": "Start time of the event in ISO 8601 format."
              },
              "last": {
                "type": "integer",
                "description": "Timestamp indicating the last update time of the event."
              },
              "home": {
                "type": "string",
                "description": "Name of the home team."
              },
              "away": {
                "type": "string",
                "description": "Name of the away team."
              },
              "event_type": {
                "type": "string",
                "description": "Type of the event (e.g., 'prematch', 'live')."
              },
              "parent_id": {
                "type": ["integer", "null"],
                "description": "Unique identifier for the parent event, if applicable."
              },
              "resulting_unit": {
                "type": "string",
                "description": "Unit used for scoring (e.g., 'Regular', 'Corners')."
              },
              "is_have_odds": {
                "type": "boolean",
                "description": "Indicates whether odds are available for the event."
              },
              "period_results": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "number": {
                      "type": "integer",
                      "description": "Period number."
                    },
                    "status": {
                      "type": "integer",
                      "description": "Status of the period (e.g., 1 for active, 5 for settled)."
                    },
                    "settlement_id": {
                      "type": "integer",
                      "description": "Unique identifier for the settlement."
                    },
                    "settled_at": {
                      "type": "string",
                      "format": "date-time",
                      "description": "Timestamp indicating when the period was settled."
                    },
                    "team_1_score": {
                      "type": "integer",
                      "description": "Score of the home team for this period."
                    },
                    "team_2_score": {
                      "type": "integer",
                      "description": "Score of the away team for this period."
                    },
                    "cancellation_reason": {
                      "type": ["object", "null"],
                      "properties": {
                        "code": {
                          "type": "string",
                          "description": "Code indicating the reason for cancellation."
                        },
                        "details": {
                          "type": "object",
                          "description": "Additional details about the cancellation reason."
                        }
                      },
                      "description": "Reason for cancellation, if applicable."
                    }
                  },
                  "required": ["number", "status", "settlement_id", "settled_at", "team_1_score", "team_2_score", "cancellation_reason"]
                },
                "description": "List of results for each period of the event."
              }
            },
            "required": ["event_id", "sport_id", "league_id", "league_name", "starts", "last", "home", "away", "event_type", "parent_id", "resulting_unit", "is_have_odds", "period_results"]
          },
          "description": "List of events associated with the sport."
        }
      },
      "required": ["sport_id", "sport_name", "events"]
    }
    ```
    """
    url = "https://pinnacle-odds.p.rapidapi.com/kit/v1/archive"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"sport_id": sport_id, "page_num": page_num}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "pinnacle-odds.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
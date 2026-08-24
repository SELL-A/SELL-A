import os
import requests

def Get_All_Matches_by_League_ID(leagueid):
    """
    :API_description: Retrieves a comprehensive list of completed football matches for a specified league, including detailed team information, scores, match status, and timing data.
    :param leagueid: The ID of the league for which matches are to be retrieved(eg. "42").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "status": {
      "type": "string",
      "description": "API request status (e.g., 'success', 'error')"
    },
    "response": {
      "type": "object",
      "properties": {
        "matches": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "string",
                "description": "Unique match identifier"
              },
              "pageUrl": {
                "type": "string",
                "description": "URL path to match details page"
              },
              "opponent": {
                "type": "object",
                "properties": {
                  "id": {"type": "string"},
                  "name": {"type": "string"},
                  "score": {"type": "integer"}
                },
                "required": ["id", "name", "score"]
              },
              "home": {
                "type": "object",
                "properties": {
                  "id": {"type": "string"},
                  "name": {"type": "string"},
                  "score": {"type": "integer"}
                },
                "required": ["id", "name", "score"]
              },
              "away": {
                "type": "object",
                "properties": {
                  "id": {"type": "string"},
                  "name": {"type": "string"},
                  "score": {"type": "integer"}
                },
                "required": ["id", "name", "score"]
              },
              "displayTournament": {"type": "boolean"},
              "notStarted": {"type": "boolean"},
              "tournament": {
                "type": "object",
                "description": "Tournament information (empty in this dataset)"
              },
              "status": {
                "type": "object",
                "properties": {
                  "utcTime": {
                    "type": "string",
                    "format": "date-time",
                    "description": "Match time in UTC"
                  },
                  "finished": {"type": "boolean"},
                  "started": {"type": "boolean"},
                  "cancelled": {"type": "boolean"},
                  "awarded": {"type": "boolean"},
                  "scoreStr": {
                    "type": "string",
                    "description": "Formatted score string (e.g., '2 - 1')"
                  },
                  "reason": {
                    "type": "object",
                    "properties": {
                      "short": {"type": "string"},
                      "shortKey": {"type": "string"},
                      "long": {"type": "string"},
                      "longKey": {"type": "string"}
                    },
                    "required": ["short", "shortKey", "long", "longKey"]
                  }
                },
                "required": ["utcTime", "finished", "started", "cancelled", "awarded", "scoreStr", "reason"]
              }
            },
            "required": ["id", "pageUrl", "opponent", "home", "away", "displayTournament", "notStarted", "tournament", "status"]
          }
        }
      },
      "required": ["matches"]
    }
  },
  "required": ["status", "response"]
}
    ```
    """
    url = "https://free-api-live-football-data.p.rapidapi.com/football-get-all-matches-by-league"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"leagueid": leagueid}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
if __name__ == "__main__":
    leagueid = "42"
    matches = Get_All_Matches_by_League_ID(leagueid)
    print(matches)
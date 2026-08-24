import os
import requests

def Get_Top_Players_by_Goals(leagueid):
    """
    :API_description: Retrieves a ranked list of football players and their goal-scoring statistics for a specified league, including detailed player data, team affiliations, and visual styling information for display.
    :param leagueid: The ID of the league for which to retrieve the top players by goals(eg. "42").
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "players": [
      {
        "id": 737066,
        "name": "Erling Haaland",
        "teamId": 8456,
        "teamName": "Manchester City",
        "goals": 27,
        "value": 27,
        "stat": {
          "name": "goals",
          "value": 27,
          "format": "number",
          "fractions": 0
        },
        "teamColors": {
          "darkMode": "#76b4e5",
          "lightMode": "#69A8D8",
          "fontDarkMode": "rgba(29, 29, 29, 1.0)",
          "fontLightMode": "rgba(255, 255, 255, 1.0)"
        }
      },
      {
        "id": 1302005,
        "name": "Igor Thiago",
        "teamId": 9937,
        "teamName": "Brentford",
        "goals": 22,
        "value": 22,
        "stat": {
          "name": "goals",
          "value": 22,
          "format": "number",
          "fractions": 0
        },
        "teamColors": {
          "darkMode": "#C00808",
          "lightMode": "#C00808",
          "fontDarkMode": "rgba(255, 255, 255, 1.0)",
          "fontLightMode": "rgba(255, 255, 255, 1.0)"
        }
      },
      {
        "id": 933576,
        "name": "Antoine Semenyo",
        "teamId": 8456,
        "teamName": "Manchester City",
        "goals": 17,
        "value": 17,
        "stat": {
          "name": "goals",
          "value": 17,
          "format": "number",
          "fractions": 0
        },
        "teamColors": {
          "darkMode": "#76b4e5",
          "lightMode": "#69A8D8",
          "fontDarkMode": "rgba(29, 29, 29, 1.0)",
          "fontLightMode": "rgba(255, 255, 255, 1.0)"
        }
      }
    ]
  }
}
```
    """
    url = "https://free-api-live-football-data.p.rapidapi.com/football-get-top-players-by-goals"
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
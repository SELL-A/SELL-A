import os
import requests

def Get_NBA_Team_Detail_by_Team_ID(team_id):
    """
    :API_description: Retrieve detailed information about a specific NBA team, including current season details, record, standing, and coach information.
    :param team_id: The ID of the NBA team for which information is being requested(e.g. "13").
    :response_schema: 
    ```json{
  "status": "success",
  "response": {
    "teamDetail": {
      "id": "13",
      "guid": "2876e98b-b9bc-2920-4319-46e6943f8be4",
      "uid": "s:40~l:46~t:13",
      "slug": "los-angeles-lakers",
      "location": "Los Angeles",
      "name": "Lakers",
      "abbreviation": "LAL",
      "displayName": "Los Angeles Lakers",
      "shortDisplayName": "Lakers",
      "color": "552583",
      "alternateColor": "fdb927",
      "isActive": true,
      "isAllStar": false,
      "logos": [
        {
          "href": "https://a.espncdn.com/i/teamlogos/nba/500/lal.png",
          "width": 500,
          "height": 500,
          "alt": "",
          "rel": [
            "full",
            "default"
          ],
          "lastUpdated": "2024-06-25T21:17Z"
        },
        {
          "href": "https://a.espncdn.com/i/teamlogos/nba/500-dark/lal.png",
          "width": 500,
          "height": 500,
          "alt": "",
          "rel": [
            "full",
            "dark"
          ],
          "lastUpdated": "2024-06-25T21:13Z"
        },
        {
          "href": "https://a.espncdn.com/i/teamlogos/nba/500/scoreboard/lal.png",
          "width": 500,
          "height": 500,
          "alt": "",
          "rel": [
            "full",
            "scoreboard"
          ],
          "lastUpdated": "2024-06-25T21:18Z"
        }
      ]
    }
  }
}
```

    """
    url = "https://nba-api-free-data.p.rapidapi.com/nba-team-detail"
    
    querystring = {"id": team_id}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "nba-api-free-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
  
import os
import requests

def Get_Search_All_Players(search):
    """
    :API_description: Searches for football players by name, returning a ranked list of matching players with details including their ID, current team, coaching status, and a relevance score.
    :param search: The search term for finding football players(eg. "Messi").
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "suggestions": [
      {
        "type": "player",
        "id": "30981",
        "score": 301149,
        "name": "Lionel Messi",
        "isCoach": false,
        "teamId": 960720,
        "teamName": "Inter Miami CF"
      },
      {
        "type": "player",
        "id": "1003368",
        "score": 300020,
        "name": "Junior Messias",
        "isCoach": false,
        "teamId": 10233,
        "teamName": "Genoa"
      },
      {
        "type": "player",
        "id": "1635507",
        "score": 300014,
        "name": "Rayane Messi",
        "isCoach": false,
        "teamId": 1699505,
        "teamName": "Neom SC"
      },
      {
        "type": "player",
        "id": "898330",
        "score": 300006,
        "name": "Zakaria Messibah",
        "isCoach": false,
        "teamId": 277392,
        "teamName": "CS Constantine"
      }
    ]
  }
}
```

    """
    url = "https://free-api-live-football-data.p.rapidapi.com/football-players-search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"search": search}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "free-api-live-football-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

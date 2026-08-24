import os
import requests

def Get_Teams_All_List_by_League_ID(leagueid):
    """
    :API_description: Retrieves the complete standings table for a specified football/soccer league, including detailed team performance statistics such as matches played, wins, draws, losses, goals, points, and ranking position for each team.
    :param leagueid: The ID of the league for which to retrieve the list of teams(eg. "42").
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "list": [
      {
        "name": "Bayern München",
        "shortName": "Bayern München",
        "id": 9823,
        "deduction": null,
        "ongoing": null,
        "played": 34,
        "wins": 28,
        "draws": 5,
        "losses": 1,
        "scoresStr": "122-36",
        "goalConDiff": 86,
        "pts": 89,
        "idx": 1,
        "qualColor": "#2AD572",
        "logo": "https://images.fotmob.com/image_resources/logo/teamlogo/9823_large.png"
      },
      {
        "name": "Borussia Dortmund",
        "shortName": "Dortmund",
        "id": 9789,
        "deduction": null,
        "ongoing": null,
        "played": 34,
        "wins": 22,
        "draws": 7,
        "losses": 5,
        "scoresStr": "70-34",
        "goalConDiff": 36,
        "pts": 73,
        "idx": 2,
        "qualColor": "#2AD572",
        "logo": "https://images.fotmob.com/image_resources/logo/teamlogo/9789_large.png"
      }
    ]
  }
}
```
    """
    url = "https://free-api-live-football-data.p.rapidapi.com/football-get-list-all-team"
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
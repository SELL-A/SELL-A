import os
import requests

def Get_Northwest_Team_List():
    """
    :API_description: Retrieves detailed athlete profile information for NBA players including personal details, team information, and physical attributes. Provides comprehensive navigation links to various sections of the athlete's profile such as stats, game logs, news, and advanced statistics.
    :param None
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "teamList": [
      {
        "id": "7",
        "href": "...",
        "name": "Denver Nuggets",
        "shortName": "Nuggets",
        "abbrev": "den",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "16",
        "href": "...",
        "name": "Minnesota Timberwolves",
        "shortName": "Timberwolves",
        "abbrev": "min",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "25",
        "href": "...",
        "name": "Oklahoma City Thunder",
        "shortName": "Thunder",
        "abbrev": "okc",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "22",
        "href": "...",
        "name": "Portland Trail Blazers",
        "shortName": "Trail Blazers",
        "abbrev": "por",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "26",
        "href": "...",
        "name": "Utah Jazz",
        "shortName": "Jazz",
        "abbrev": "utah",
        "logo": "...",
        "logoDark": "..."
      }
    ]
  }
}
```
    """
    url = "https://nba-api-free-data.p.rapidapi.com/nba-northwest-team-list"
      
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "nba-api-free-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
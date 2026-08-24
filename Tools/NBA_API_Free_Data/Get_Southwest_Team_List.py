import os
import requests
def Get_Southwest_Team_List():
    """
    :API_description: This API retrieves detailed NBA player profiles including personal information, team affiliation with multiple logo variants, position details, player status, and navigation links to various player-related sections such as stats, game logs, news, bio, and advanced statistics.
    :param None
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "teamList": [
      {
        "id": "6",
        "href": "...",
        "name": "Dallas Mavericks",
        "shortName": "Mavericks",
        "abbrev": "dal",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "10",
        "href": "...",
        "name": "Houston Rockets",
        "shortName": "Rockets",
        "abbrev": "hou",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "29",
        "href": "...",
        "name": "Memphis Grizzlies",
        "shortName": "Grizzlies",
        "abbrev": "mem",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "3",
        "href": "...",
        "name": "New Orleans Pelicans",
        "shortName": "Pelicans",
        "abbrev": "no",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "24",
        "href": "...",
        "name": "San Antonio Spurs",
        "shortName": "Spurs",
        "abbrev": "sa",
        "logo": "...",
        "logoDark": "..."
      }
    ]
  }
}
```

    """
    url = "https://nba-api-free-data.p.rapidapi.com/nba-southwest-team-list"
      
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "nba-api-free-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
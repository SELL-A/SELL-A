import os
import requests

def Get_Southeast_Team_List():
    """
    :API_description: This API retrieves comprehensive NBA player profiles including personal details, team affiliations, positions, and status information. It provides rich metadata with player photos, team logos, and navigation links to stats, game logs, news, and biographical content on the ESPN platform.
    :param None
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "teamList": [
      {
        "id": "1",
        "href": "...",
        "name": "Atlanta Hawks",
        "shortName": "Hawks",
        "abbrev": "atl",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "30",
        "href": "...",
        "name": "Charlotte Hornets",
        "shortName": "Hornets",
        "abbrev": "cha",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "14",
        "href": "...",
        "name": "Miami Heat",
        "shortName": "Heat",
        "abbrev": "mia",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "19",
        "href": "...",
        "name": "Orlando Magic",
        "shortName": "Magic",
        "abbrev": "orl",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "27",
        "href": "...",
        "name": "Washington Wizards",
        "shortName": "Wizards",
        "abbrev": "wsh",
        "logo": "...",
        "logoDark": "..."
      }
    ]
  }
}
```
    """
    url = "https://nba-api-free-data.p.rapidapi.com/nba-southeast-team-list"
      
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "nba-api-free-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
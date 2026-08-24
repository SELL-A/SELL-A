import os
import requests

def Get_Atlantic_Team_List():
    """
    :API_description: This API retrieves detailed athlete profile information for NBA basketball players on the Atlanta Hawks team, including personal details, team information, position data, and navigation links to various player-related sections.
    :param None
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "teamList": [
      {
        "id": "2",
        "href": "...",
        "name": "Boston Celtics",
        "shortName": "Celtics",
        "abbrev": "bos",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "17",
        "href": "...",
        "name": "Brooklyn Nets",
        "shortName": "Nets",
        "abbrev": "bkn",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "18",
        "href": "...",
        "name": "New York Knicks",
        "shortName": "Knicks",
        "abbrev": "ny",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "20",
        "href": "...",
        "name": "Philadelphia 76ers",
        "shortName": "76ers",
        "abbrev": "phi",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "28",
        "href": "...",
        "name": "Toronto Raptors",
        "shortName": "Raptors",
        "abbrev": "tor",
        "logo": "...",
        "logoDark": "..."
      }
    ]
  }

}
```

    """
    url = "https://nba-api-free-data.p.rapidapi.com/nba-atlantic-team-list"
    

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "nba-api-free-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
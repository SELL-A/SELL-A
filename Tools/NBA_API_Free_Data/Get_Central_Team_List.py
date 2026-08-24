import os
import requests

def Get_Central_Team_List():
    """
    :API_description: This API retrieves detailed athlete profile information for NBA players including personal details, team affiliation, position, status, and navigation links to related content sections.
    :param None
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "teamList": [
      {
        "id": "4",
        "href": "...",
        "name": "Chicago Bulls",
        "shortName": "Bulls",
        "abbrev": "chi",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "5",
        "href": "...",
        "name": "Cleveland Cavaliers",
        "shortName": "Cavaliers",
        "abbrev": "cle",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "8",
        "href": "...",
        "name": "Detroit Pistons",
        "shortName": "Pistons",
        "abbrev": "det",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "11",
        "href": "...",
        "name": "Indiana Pacers",
        "shortName": "Pacers",
        "abbrev": "ind",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "15",
        "href": "...",
        "name": "Milwaukee Bucks",
        "shortName": "Bucks",
        "abbrev": "mil",
        "logo": "...",
        "logoDark": "..."
      }
    ]
  }
}
```

    """
    url = "https://nba-api-free-data.p.rapidapi.com/nba-central-team-list"
      
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "nba-api-free-data.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
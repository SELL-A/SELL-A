import os
import requests

def Get_NBA_Player_Detail_by_Player_ID(playerid):
    """
    :API_description: Retrieve detailed information about an NBA player using their unique player ID.
    :param playerid: The unique identifier for the NBA player(e.g. "4869342").
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "athlete": {
      "id": "4869342",
      "uid": "s:40~l:46~a:4869342",
      "guid": "7b066993-61be-35fd-9070-c1b9a57c7b31",
      "type": "basketball",
      "firstName": "Dyson",
      "lastName": "Daniels",
      "displayName": "Dyson Daniels",
      "fullName": "Dyson Daniels",
      "jersey": "5",
      "links": [
        {
          "language": "en",
          "rel": [
            "playercard",
            "desktop",
            "athlete"
          ],
          "href": "https://www.espn.com/nba/player/_/id/4869342/dyson-daniels",
          "text": "Player Card",
          "shortText": "Player Card",
          "isExternal": false,
          "isPremium": false
        },
        {
          "language": "en",
          "rel": [
            "stats",
            "desktop",
            "athlete"
          ],
          "href": "https://www.espn.com/nba/player/stats/_/id/4869342/dyson-daniels",
          "text": "Stats",
          "shortText": "Stats",
          "isExternal": false,
          "isPremium": false
        }
      ],
      "collegeAthlete": {
        "id": "4869342"
      },
      "headshot": {
        "href": "https://a.espncdn.com/i/headshots/nba/players/full/4869342.png",
        "alt": "Dyson Daniels"
      },
      "position": {
        "id": "3",
        "name": "Guard",
        "displayName": "Guard",
        "abbreviation": "G",
        "leaf": false,
        "slug": "guard"
      },
      "team": {
        "id": "1",
        "uid": "s:40~l:46~t:1",
        "guid": "15096a54-f015-c987-5ec8-55afedf6272f",
        "slug": "atlanta-hawks",
        "displayName": "Atlanta Hawks",
        "logos": [
          {
            "href": "https://a.espncdn.com/i/teamlogos/nba/500/atl.png",
            "width": 500,
            "height": 500,
            "rel": [
              "full",
              "default"
            ]
          },
          {
            "href": "https://a.espncdn.com/i/teamlogos/nba/500-dark/atl.png",
            "width": 500,
            "height": 500,
            "rel": [
              "full",
              "dark"
            ]
          }
        ]
      },
      "active": true,
      "status": {
        "id": "1",
        "name": "Active",
        "type": "active",
        "abbreviation": "Active"
      },
      "displayBirthPlace": "Bendigo, VIC",
      "displayHeight": "6' 7\"",
      "displayWeight": "199 lbs",
      "displayDOB": "17/3/2003",
      "age": 23,
      "displayJersey": "#5",
      "displayExperience": "3rd Season",
      "displayDraft": "2022: Rd 1, Pk 8 (NO)"
    }
  }
}
```
    """
    url = "https://nba-api-free-data.p.rapidapi.com/nba-player-info"
    
    querystring = {"playerid": playerid}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "nba-api-free-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
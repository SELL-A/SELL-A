import os
import requests

def Get_NBA_All_Players_by_Team_ID(teamid):
    """
    :API_description: Retrieve detailed information about all NBA players associated with a specific team, including personal details, career statistics, and contract status.
    
    :param teamid: The ID of the team for which to retrieve the player list(e.g. "13").
    :response_schema: 
    ```json{
  "status": "success",
  "response": {
    "PlayerList": [
      {
        "id": "4278129",
        "uid": "s:40~l:46~a:4278129",
        "guid": "9af41ea8-a24c-025f-a63f-8263fbf0ca66",
        "firstName": "Deandre",
        "lastName": "Ayton",
        "fullName": "Deandre Ayton",
        "displayWeight": "252 lbs",
        "displayHeight": "7' 0\"",
        "age": 27,
        "salary": 8104000,
        "image": "..."
      },
      {
        "id": "3945274",
        "uid": "s:40~l:46~a:3945274",
        "guid": "583794eb-0f38-9bbd-3e25-9dd33b7f83b8",
        "firstName": "Luka",
        "lastName": "Doncic",
        "fullName": "Luka Doncic",
        "displayWeight": "230 lbs",
        "displayHeight": "6' 8\"",
        "age": 27,
        "salary": 54126450,
        "image": "..."
      },
      {
        "id": "4066648",
        "uid": "s:40~l:46~a:4066648",
        "guid": "40c1bcf6-675b-f217-f97c-1d628073f927",
        "firstName": "Rui",
        "lastName": "Hachimura",
        "fullName": "Rui Hachimura",
        "displayWeight": "230 lbs",
        "displayHeight": "6' 8\"",
        "age": 28,
        "salary": 18259259,
        "image": "..."
      },
      {
        "id": "4397077",
        "uid": "s:40~l:46~a:4397077",
        "guid": "4cd92ac1-73ce-653d-c3b1-9c68e9c7a4d0",
        "firstName": "Jaxson",
        "lastName": "Hayes",
        "fullName": "Jaxson Hayes",
        "displayWeight": "220 lbs",
        "displayHeight": "7' 0\"",
        "age": 26,
        "salary": 3449324,
        "image": "..."
      }
    ]
  }
}
```
    """
    url = "https://nba-api-free-data.p.rapidapi.com/nba-player-list"
    
    querystring = {"teamid": teamid}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "nba-api-free-data.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
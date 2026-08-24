import os
import requests

def Get_Pacific_Team_List():
    """
    :API_description: This API retrieves comprehensive athlete profile information for sports professionals, including personal details, physical attributes, and professional career information.
    :param None
    :response_schema: 
    ```json
{
  "status": "success",
  "response": {
    "teamList": [
      {
        "id": "9",
        "href": "...",
        "name": "Golden State Warriors",
        "shortName": "Warriors",
        "abbrev": "gs",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "12",
        "href": "...",
        "name": "LA Clippers",
        "shortName": "Clippers",
        "abbrev": "lac",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "13",
        "href": "...",
        "name": "Los Angeles Lakers",
        "shortName": "Lakers",
        "abbrev": "lal",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "21",
        "href": "...",
        "name": "Phoenix Suns",
        "shortName": "Suns",
        "abbrev": "phx",
        "logo": "...",
        "logoDark": "..."
      },
      {
        "id": "23",
        "href": "...",
        "name": "Sacramento Kings",
        "shortName": "Kings",
        "abbrev": "sac",
        "logo": "...",
        "logoDark": "..."
      }
    ]
  }
}
    ```
    """
    url = "https://nba-api-free-data.p.rapidapi.com/nba-pacific-team-list"
      
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "nba-api-free-data.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
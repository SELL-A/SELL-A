import os
import requests

def Get_NBA_League_Info():
    """
    :API_description: Retrieves comprehensive information about the National Basketball Association (NBA) including league identifiers, naming details, organizational information, and logo assets for display purposes.
    :param None
    :response_schema: 
    ```json
{'status': 'success', 'response': {'id': '46', 'guid': '7b3729c9-7f69-308a-bf8a-ee15a6aba154', 'uid': 's:40~l:46', 'name': 'National Basketball Association', 'displayName': 'NBA', 'abbreviation': 'NBA', 'shortName': 'NBA', 'slug': 'nba', 'isTournament': False, 'logos': [{'href': 'https://a.espncdn.com/i/teamlogos/leagues/500/nba.png', 'width': 500, 'height': 500, 'alt': '', 'rel': ['full', 'default'], 'lastUpdated': '2018-06-05T12:07Z'}, {'href': 'https://a.espncdn.com/combiner/i?img=/i/teamlogos/leagues/500-dark/nba.png&w=500&h=500&transparent=true', 'width': 500, 'height': 500, 'alt': '', 'rel': ['full', 'dark'], 'lastUpdated': '2026-05-27T01:27Z'}], 'gender': 'MALE'}}
```
    """
    url = "https://nba-api-free-data.p.rapidapi.com/nba-leagues"
      
    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "nba-api-free-data.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

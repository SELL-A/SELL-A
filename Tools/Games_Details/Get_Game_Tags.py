import os
import requests

def Get_Game_Tags(id):
    """
    :API_description: Retrieves a list of descriptive tags that categorize and characterize a specific video game, such as its genre, gameplay style, and thematic elements.
    :param id: The unique identifier for the game(eg. "124").
    :response_schema: 
    ```json
{
  "status": 200,
  "message": "success",
  "data": {
    "tags": [
      "FPS",
      "Shooter",
      "Multiplayer",
      "Competitive",
      "Action",
      "Team-Based",
      "eSports",
      "Tactical",
      "First-Person",
      "PvP",
      "Online Co-Op",
      "Co-op",
      "Strategy",
      "Military",
      "War",
      "Difficult",
      "Trading",
      "Realistic",
      "Fast-Paced",
      "Moddable"
    ]
  }
}
    ```
    """
    url = f"https://games-details.p.rapidapi.com/gameinfo/tags/{id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "games-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
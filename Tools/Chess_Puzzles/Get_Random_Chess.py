import os
import requests

def Get_Random_Chess(number_of_puzzles):
    """
    :API_description: Get one or more random chess puzzles.
    :param number_of_puzzles: The number of chess puzzles to retrieve (e.g., "3").
    :response_schema: 
    ```json
    {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "fen": {"type": "string"},
                "moves": {"type": "array", "items": {"type": "string"}},
                "numberOfMoves": {"type": "string"},
                "rating": {"type": "string"},
                "ratingDeviation": {"type": "string"},
                "minRating": {"type": "string"},
                "maxRating": {"type": "string"},
                "themes": {"type": "string"},
                "openingFamily": {"type": "string"},
                "openingVariation": {"type": "string"}
            }
        }
    }
    ```
    """
    url = "https://chess-puzzles2.p.rapidapi.com/random"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"number_of_puzzles": number_of_puzzles}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "chess-puzzles2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


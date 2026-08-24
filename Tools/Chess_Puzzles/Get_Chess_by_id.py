import os
import requests
def Get_Chess_by_id(id):
    """
    :API_description: Get a specific chess puzzle by its unique ID.
    :param id: The unique identifier of the chess puzzle(e.g., "002VP").
    :response_schema: 
    ```json
    {
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "id": { "type": "string", "description": "Unique identifier of the puzzle" },
            "fen": { "type": "string", "description": "Chess board position in FEN notation" },
            "moves": {
              "type": "array",
              "items": { "type": "string" },
              "description": "Sequence of moves in algebraic notation representing the solution"
            },
            "numberOfMoves": { "type": "string", "description": "Number of moves in the solution (as string)" },
            "rating": { "type": "number", "description": "Rating of the puzzle difficulty" },
            "ratingDeviation": { "type": "number", "description": "Deviation of the rating" },
            "minRating": { "type": "number", "description": "Minimum possible rating" },
            "maxRating": { "type": "number", "description": "Maximum possible rating" },
            "themes": { "type": "string", "description": "Space-separated tags describing puzzle themes" },
            "openingFamily": { "type": "string", "description": "Chess opening family (or 'no data')" },
            "openingVariation": { "type": "string", "description": "Specific opening variation (or 'no data')" }
          },
          "required": ["id", "fen", "moves", "numberOfMoves", "rating", "ratingDeviation", "minRating", "maxRating", "themes", "openingFamily", "openingVariation"]
        }
      }
    }
    ```
    """
    url = f"https://chess-puzzles2.p.rapidapi.com/id/{id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "chess-puzzles2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


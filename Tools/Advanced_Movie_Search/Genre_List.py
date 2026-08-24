import os
import requests

def Genre_List():
    """
    :API_description: Retrieve a comprehensive list of movie genres, each defined by a unique ID and name.
    :param None
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "genres": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the genre"
          },
          "name": {
            "type": "string",
            "description": "Name of the genre"
          }
        },
        "required": ["id", "name"]
      }
    }
  },
  "required": ["genres"]
}
```
    """
    url = "https://advanced-movie-search.p.rapidapi.com/api/genre/movie/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "advanced-movie-search.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


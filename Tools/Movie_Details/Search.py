import os
import requests

def Search(title, page):
    """
    :API_description: This endpoint retrieves detailed information about movies and TV series based on the provided title, with optional pagination.
    :param title: The title of the content to search for.
    :param page: The page number for pagination.
    :response_schema: 
    ```json
    {
      "type": "object",
      "properties": {
        "page": {
          "type": "integer",
          "description": "The current page number of the results."
        },
        "results": {
          "type": "array",
          "description": "An array of movie or TV series objects.",
          "items": {
            "type": "object",
            "properties": {
              "genre": {
                "type": "array",
                "description": "An array of strings representing the genres of the movie or TV series.",
                "items": {
                  "type": "string"
                }
              },
              "imageurl": {
                "type": "array",
                "description": "An array of strings representing the URLs of the images associated with the movie or TV series.",
                "items": {
                  "type": "string"
                }
              },
              "imdbid": {
                "type": "string",
                "description": "The IMDb ID of the movie or TV series."
              },
              "released": {
                "type": "integer",
                "description": "The release year of the movie or TV series."
              },
              "synopsis": {
                "type": "string",
                "description": "A brief summary or description of the movie or TV series."
              },
              "title": {
                "type": "string",
                "description": "The title of the movie or TV series."
              },
              "type": {
                "type": "string",
                "description": "The type of the media, either 'movie' or 'tvSeries'."
              }
            },
            "required": ["genre", "imdbid", "released", "title", "type"]
          }
        }
      },
      "required": ["page", "results"]
    }
    ```
    """
    url = "https://ott-details.p.rapidapi.com/search"
 
    querystring = {"title": title, "page": page}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "ott-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
import os
import requests

def Advanced_Search(start_year, end_year, min_imdb, max_imdb, genre, language, type, sort):
    """
    :API_description: This endpoint facilitates the search for movies or TV shows using various filters like release year, IMDb rating, genre, and language.
    :param start_year: The starting year for the search range.
    :param end_year: The ending year for the search range.
    :param min_imdb: The minimum IMDb rating for the search.
    :param max_imdb: The maximum IMDb rating for the search.
    :param genre: The genre of the movie or TV show(e.g. "action, adventure, drama, fantasy, history, horror").
    :param language: The language of the movie or TV show(e.g. "english, german").
    :param type: The type of content, either 'movie' or 'show'.
    :param sort: The sorting order of the results Enter values highestrated , lowestrated , latest , oldest to sort results accodingly
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
          "items": {
            "type": "object",
            "properties": {
              "genre": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "List of genres associated with the movie."
              },
              "imageurl": {
                "type": "array",
                "items": {
                  "type": "string"
                },
                "description": "List of image URLs for the movie poster."
              },
              "imdbid": {
                "type": "string",
                "description": "IMDb ID of the movie."
              },
              "imdbrating": {
                "type": "number",
                "description": "IMDb rating of the movie."
              },
              "released": {
                "type": "integer",
                "description": "Year the movie was released."
              },
              "synopsis": {
                "type": "string",
                "description": "Brief summary of the movie's plot."
              },
              "title": {
                "type": "string",
                "description": "Title of the movie."
              },
              "type": {
                "type": "string",
                "description": "Type of the media, in this case, always 'movie'."
              }
            }
          },
          "description": "List of movie results."
        }
      }
    }
    ```
    """
    url = "https://ott-details.p.rapidapi.com/advancedsearch"
    querystring = {
        "start_year": start_year,
        "end_year": end_year,
        "min_imdb": min_imdb,
        "max_imdb": max_imdb,
        "genre": genre,
        "language": language,
        "type": type,
        "sort": sort
    }

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "ott-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
import os
import requests

def Search_By_Genre(with_genres):
    """
    :API_description: Retrieve a list of movies and TV shows filtered by genre, including details like title, release date, and ratings.
    :param with_genres: The genre ID to filter movies by.
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
          "description": "List of movie or TV show results.",
          "items": {
            "type": "object",
            "properties": {
              "adult": {
                "type": "boolean",
                "description": "Indicates if the content is for adults only."
              },
              "backdrop_path": {
                "type": "string",
                "description": "URL path to the backdrop image."
              },
              "genre_ids": {
                "type": "array",
                "description": "List of genre IDs associated with the content.",
                "items": {
                  "type": "integer"
                }
              },
              "id": {
                "type": "integer",
                "description": "Unique identifier for the content."
              },
              "original_language": {
                "type": "string",
                "description": "Original language of the content."
              },
              "original_title": {
                "type": "string",
                "description": "Original title of the content."
              },
              "overview": {
                "type": "string",
                "description": "Brief summary of the content."
              },
              "popularity": {
                "type": "number",
                "description": "Popularity score of the content."
              },
              "poster_path": {
                "type": "string",
                "description": "URL path to the poster image."
              },
              "release_date": {
                "type": "string",
                "description": "Release date of the content."
              },
              "title": {
                "type": "string",
                "description": "Title of the content."
              },
              "video": {
                "type": "boolean",
                "description": "Indicates if there is a video available for the content."
              },
              "vote_average": {
                "type": "number",
                "description": "Average rating of the content."
              },
              "vote_count": {
                "type": "integer",
                "description": "Number of votes for the content."
              }
            },
            "required": ["adult", "backdrop_path", "genre_ids", "id", "original_language", "original_title", "overview", "popularity", "poster_path", "release_date", "title", "video", "vote_average", "vote_count"]
          }
        },
        "total_pages": {
          "type": "integer",
          "description": "Total number of pages available."
        },
        "total_results": {
          "type": "integer",
          "description": "Total number of results available."
        }
      },
      "required": ["page", "results", "total_pages", "total_results"]
    }
    ```
    """
    url = "https://advanced-movie-search.p.rapidapi.com/api/discover/movie"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"with_genres": with_genres}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "advanced-movie-search.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
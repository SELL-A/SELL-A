import os
import requests


def Search_collections(query):
    """
    :API_description: Search for collections by their original, translated and alternative names.
    :param query: Search for collections by their original, translated and alternative names.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "page": {
          "type": "integer",
          "description": "The current page number."
        },
        "results": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "adult": {
                "type": "boolean",
                "description": "Indicates if the collection is for adults."
              },
              "backdrop_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Path to the backdrop image, can be null."
              },
              "id": {
                "type": "integer",
                "description": "The collection ID."
              },
              "name": {
                "type": "string",
                "description": "The name of the collection."
              },
              "original_language": {
                "type": "string",
                "description": "Original language code (e.g., 'en')."
              },
              "original_name": {
                "type": "string",
                "description": "Original name of the collection."
              },
              "overview": {
                "type": "string",
                "description": "Overview or description of the collection."
              },
              "poster_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Path to the poster image, can be null."
              }
            },
            "required": [
              "adult",
              "backdrop_path",
              "id",
              "name",
              "original_language",
              "original_name",
              "overview",
              "poster_path"
            ]
          },
          "description": "Array of collection search results."
        },
        "total_pages": {
          "type": "integer",
          "description": "Total number of pages."
        },
        "total_results": {
          "type": "integer",
          "description": "Total number of results."
        }
      },
      "required": [
        "page",
        "results",
        "total_pages",
        "total_results"
      ]
    }
    ```
    """
    if query is None:
        raise ValueError("`query` is required.")

    url = "https://api.themoviedb.org/3/search/collection"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    params = {"query": query}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

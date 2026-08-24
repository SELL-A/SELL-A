import os
import requests


def Search_company(query):
    """
    :API_description: Search for companies by their original and alternative names.
    :param query: Search for companies by their original and alternative names.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "page": {
          "type": "integer",
          "description": "Current page number"
        },
        "results": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer",
                "description": "Company ID"
              },
              "logo_path": {
                "type": [
                  "string",
                  "null"
                ],
                "description": "Path to company logo image"
              },
              "name": {
                "type": "string",
                "description": "Company name"
              },
              "origin_country": {
                "type": "string",
                "description": "Country code of origin"
              }
            },
            "required": [
              "id",
              "logo_path",
              "name",
              "origin_country"
            ]
          }
        },
        "total_pages": {
          "type": "integer",
          "description": "Total number of pages"
        },
        "total_results": {
          "type": "integer",
          "description": "Total number of results"
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

    url = "https://api.themoviedb.org/3/search/company"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    if not bearer_token:
        raise Exception("TMDB_BEARER_TOKEN is not set.")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    params = {}
    params["query"] = query

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

import os
import requests


def Get_company_details(company_id):
    """
    :API_description: Get the company details by ID.
    :param company_id: The ID of the company.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "description": {
          "type": "string",
          "description": "A brief description of the company."
        },
        "headquarters": {
          "type": "string",
          "description": "The headquarters location."
        },
        "homepage": {
          "type": "string",
          "description": "The company's homepage URL."
        },
        "id": {
          "type": "integer",
          "description": "The company ID."
        },
        "logo_path": {
          "type": "string",
          "description": "Path to the company logo image."
        },
        "name": {
          "type": "string",
          "description": "The company name."
        },
        "origin_country": {
          "type": "string",
          "description": "The origin country code (ISO 3166-1 alpha-2)."
        },
        "parent_company": {
          "type": [
            "object",
            "null"
          ],
          "additionalProperties": true,
          "description": "The parent company object, or null if none."
        }
      },
      "required": [
        "description",
        "headquarters",
        "homepage",
        "id",
        "logo_path",
        "name",
        "origin_country",
        "parent_company"
      ]
    }
    ```
    """
    if company_id is None:
        raise ValueError("`company_id` is required.")

    url = f"https://api.themoviedb.org/3/company/{company_id}"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    if not bearer_token:
        raise Exception("TMDB_BEARER_TOKEN is not set.")

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }

    params = None

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

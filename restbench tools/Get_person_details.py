import os
import requests


def Get_person_details(person_id):
    """
    :API_description: Get the person details by id.
    :param person_id: The ID of the person.
    :response_schema:
    ```json
    {
      "type": "object",
      "properties": {
        "adult": {
          "type": "boolean",
          "description": "Indicates if the person is an adult performer"
        },
        "also_known_as": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Alternate names or transliterations"
        },
        "biography": {
          "type": "string",
          "description": "Biographical text about the person"
        },
        "birthday": {
          "type": "string",
          "description": "Date of birth (YYYY-MM-DD format)"
        },
        "deathday": {
          "type": [
            "string",
            "null"
          ],
          "description": "Date of death (YYYY-MM-DD format), null if still alive"
        },
        "gender": {
          "type": "integer",
          "description": "Gender: 0=unspecified, 1=female, 2=male"
        },
        "homepage": {
          "type": [
            "string",
            "null"
          ],
          "description": "Official homepage URL, null if none"
        },
        "id": {
          "type": "integer",
          "description": "Unique person ID in TMDB"
        },
        "imdb_id": {
          "type": "string",
          "description": "IMDB identifier (e.g., nm0000158)"
        },
        "known_for_department": {
          "type": "string",
          "description": "Department the person is known for (e.g., Acting)"
        },
        "name": {
          "type": "string",
          "description": "Person's full name"
        },
        "place_of_birth": {
          "type": "string",
          "description": "Place of birth (city, state, country)"
        },
        "popularity": {
          "type": "number",
          "description": "Popularity score (float)"
        },
        "profile_path": {
          "type": [
            "string",
            "null"
          ],
          "description": "Path to the person's profile image on TMDB, null if none"
        }
      },
      "required": [
        "adult",
        "also_known_as",
        "biography",
        "birthday",
        "deathday",
        "gender",
        "homepage",
        "id",
        "imdb_id",
        "known_for_department",
        "name",
        "place_of_birth",
        "popularity",
        "profile_path"
      ]
    }
    ```
    """
    if person_id is None:
        raise ValueError("`person_id` is required.")

    url = f"https://api.themoviedb.org/3/person/{person_id}"
    bearer_token = os.getenv("TMDB_BEARER_TOKEN")
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {bearer_token}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

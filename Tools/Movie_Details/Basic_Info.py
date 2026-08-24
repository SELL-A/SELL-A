import os
import requests

def Basic_Info(peopleid):
    """
    :API_description: Retrieve detailed information about Robert Downey Jr., including biography, birth details, notable works, and professional roles.
    :param peopleid: The unique identifier for the person whose details are being requested(e.g. "nm0000375").
    :response_schema: 
    ```json
    {
      "type": "object",
      "properties": {
        "bio": {
          "type": "string",
          "description": "A detailed biography of Robert Downey Jr., including his early life, career milestones, personal struggles, and achievements."
        },
        "birthName": {
          "type": "string",
          "description": "The full birth name of Robert Downey Jr."
        },
        "birthYear": {
          "type": "string",
          "description": "The year of birth of Robert Downey Jr."
        },
        "born": {
          "type": "string",
          "description": "The date and place of birth of Robert Downey Jr."
        },
        "deathYear": {
          "type": "string",
          "description": "The year of death of Robert Downey Jr. (if applicable, otherwise a placeholder like '\\N' is used)."
        },
        "knownForTitles": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of IMDb title IDs for films and projects that Robert Downey Jr. is known for."
        },
        "name": {
          "type": "string",
          "description": "The name of Robert Downey Jr."
        },
        "peopleid": {
          "type": "string",
          "description": "The IMDb identifier for Robert Downey Jr."
        },
        "poster": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of URLs to posters or images associated with Robert Downey Jr."
        },
        "profession": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "A list of professions or roles associated with Robert Downey Jr., such as actor, producer, and soundtrack artist."
        }
      }
    }
    ```
    """
    url = "https://ott-details.p.rapidapi.com/getcastDetails"
  
    querystring = {"peopleid": peopleid}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "ott-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
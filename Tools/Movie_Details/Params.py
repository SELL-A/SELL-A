import os
import requests

def Params(param):
    """
    :API_description: Retrieve arrays of genres or languages for filtering media content in advanced searches.
    :param param: input 'genre' or 'language' to get array of genre or languages that can be used as filter in advanced search ..
    :response_schema: 
    ```json
    {
        "type": "array",
        "items": {
            "type": "string",
            "description": "Genre of a movie or TV show"
        }
    }
    ```
    """
    url = "https://ott-details.p.rapidapi.com/getParams"

    querystring = {"param": param}

    headers = {
        "x-rapidapi-key": "58a957b99emsh8c98d583eed0f4cp188259jsn6bfa77781fe2",
        "x-rapidapi-host": "ott-details.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
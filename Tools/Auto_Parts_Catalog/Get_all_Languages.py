import os
import requests

def Get_all_Languages():
    """
    :API_description: Retrieve a list of languages, each identified by a unique `lngId`, a two-letter ISO code `lngIso2`, and a descriptive name `lngDescription`.
    :param None
    :response_schema: 
    ```json
[
  {
    "lngId": "1",
    "lngIso2": "de",
    "lngDescription": "Deutsch"
  },
  {
    "lngId": "4",
    "lngIso2": "en",
    "lngDescription": "English (GB)"
  },
  {
    "lngId": "6",
    "lngIso2": "fr",
    "lngDescription": "Français"
  },
  {
    "lngId": "7",
    "lngIso2": "it",
    "lngDescription": "Italiano"
  },
  {
    "lngId": "8",
    "lngIso2": "es",
    "lngDescription": "Español"
  },
  {
    "lngId": "9",
    "lngIso2": "nl",
    "lngDescription": "Nederlands"
  },
  {
    "lngId": "10",
    "lngIso2": "da",
    "lngDescription": "Dansk"
  }
]
```
    """
    url = "https://auto-parts-catalog.p.rapidapi.com/languages/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "auto-parts-catalog.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


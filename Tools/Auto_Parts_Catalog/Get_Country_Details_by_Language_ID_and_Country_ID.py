import os
import requests

def Get_Country_Details_by_Language_ID_and_Country_ID(lang_id, country_filter_id):
    """
    :API_description: Retrieve detailed information about a country based on its language and country identifiers.
    :param lang_id: The language identifier for the request.
    :param country_filter_id: The country filter identifier for the request.
    :response_schema: 
    ```json
[
  {
    "id": 63,
    "couCode": "D",
    "countryName": "Germany"
  }
]
```
    """
    url = f"https://auto-parts-catalog.p.rapidapi.com/countries/get-country/lang-id/{lang_id}/country-filter-id/{country_filter_id}"
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
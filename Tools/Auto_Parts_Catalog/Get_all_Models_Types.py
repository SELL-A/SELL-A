import os
import requests

def Get_all_Models_Types(manufacturer_id, lang_id, country_filter_id, type_id):
    """
    :API_description: Retrieve detailed information about various automobile models, specifically focusing on the KIA CEE'D Hatchback (ED), including engine types and specifications.
    :param manufacturer_id: The ID of the manufacturer.
    :param lang_id: The language ID for the response.
    :param country_filter_id: The country filter ID.
    :param type_id: The type ID of the vehicle.
    :response_schema: 
    ```json
{
  "countModels": 130,
  "models": [
    {
      "modelId": 1,
      "modelName": "80 B4 Saloon (8C2)",
      "modelYearFrom": "1991-09-01",
      "modelYearTo": "1995-07-01"
    },
    {
      "modelId": 6,
      "modelName": "80 B4 Avant (8C5)",
      "modelYearFrom": "1991-09-01",
      "modelYearTo": "1996-01-01"
    },
    {
      "modelId": 10,
      "modelName": "100 C2 Saloon (431, 433, 434)",
      "modelYearFrom": "1976-06-01",
      "modelYearTo": "1984-08-01"
    },
    {
      "modelId": 13,
      "modelName": "100 C3 Saloon (443, 444)",
      "modelYearFrom": "1982-08-01",
      "modelYearTo": "1991-07-01"
    }
  ]
}
```
    """
    url = f"https://auto-parts-catalog.p.rapidapi.com/models/list/type-id/{type_id}/manufacturer-id/{manufacturer_id}/lang-id/{lang_id}/country-filter-id/{country_filter_id}"
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
  

import os
import requests

def Get_All_Countries():
    """
    :API_description: Retrieve a list of countries, each with a unique ID, country code, and name, useful for internationalization and global data processing.
    :param None
    :response_schema: 
    ```json
{
  "countries": [
    {
      "id": 1,
      "couCode": "A",
      "countryName": "Austria"
    },
    {
      "id": 2,
      "couCode": "ADN",
      "countryName": "Yemen (People's Democratic Republic)"
    },
    {
      "id": 3,
      "couCode": "AEU",
      "countryName": "Except Europe"
    },
    {
      "id": 4,
      "couCode": "AFG",
      "countryName": "Afghanistan"
    },
    {
      "id": 5,
      "couCode": "AIA",
      "countryName": "Anguilla"
    },
    {
      "id": 6,
      "couCode": "AK",
      "countryName": "Africa"
    },
    {
      "id": 7,
      "couCode": "AL",
      "countryName": "Albania"
    },
    {
      "id": 8,
      "couCode": "AM",
      "countryName": "Central America"
    },
    {
      "id": 9,
      "couCode": "AN",
      "countryName": "Netherlands Antilles"
    },
    {
      "id": 10,
      "couCode": "AND",
      "countryName": "Andorra"
    },
    {
      "id": 11,
      "couCode": "ANG",
      "countryName": "Angola"
    },
    {
      "id": 12,
      "couCode": "ANZ",
      "countryName": "Australia and New Zealand"
    },
    {
      "id": 13,
      "couCode": "APA",
      "countryName": "Asia/Pacific"
    },
    {
      "id": 14,
      "couCode": "AQ",
      "countryName": "Antarctica"
    },
    {
      "id": 15,
      "couCode": "ARM",
      "countryName": "Armenia"
    },
    {
      "id": 16,
      "couCode": "AS",
      "countryName": "South America"
    }
  ]
}
```
    """
    url = "https://auto-parts-catalog.p.rapidapi.com/countries/list"
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
import os
import requests

def Get_Microsite_Locations(micrositeShortName, location, locale, operation, locationId):
    """
    :API_description: Retrieve detailed information about provinces and municipalities in a specified region, useful for geographical or administrative data retrieval.
    :param micrositeShortName: The short name of the microsite(e.g., "sumainmobiliaria").Microsite ShortName is the identifier of every real estate profile. You may find it in the URL: idealista.com/pro/sierra-blanca-estates-realty/
    :param location: The location code(e.g., "One of the following values: es|pt|it").
    :param locale: The locale code(Language: es|it|pt|en|ca|de|fr|nl|nb).
    :param operation: The type of operation (e.g., sale).
    :param locationId: The ID of the location(e.g., "0-EU-ES-28").
    :response_schema: 
    ```json
{
  "provinces": [
    {
      "locationId": "0-EU-ES-28",
      "locationName": "Madrid",
      "divisible": true,
      "total": 17
    }
  ],
  "municipalities": [
    {
      "locationId": "0-EU-ES-28-01-008-504",
      "locationName": "Ciudalcampo, Madrid",
      "divisible": false,
      "total": 2
    },
    {
      "locationId": "0-EU-ES-28-01-007-502",
      "locationName": "La Moraleja, Madrid",
      "divisible": true,
      "total": 8
    },
    {
      "locationId": "0-EU-ES-28-07-001-079",
      "locationName": "Madrid, Madrid",
      "divisible": true,
      "total": 7
    }
  ]
}
```
    """
    url = "https://idealista7.p.rapidapi.com/getmicrositelocations"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "micrositeShortName": micrositeShortName,
        "location": location,
        "locale": locale,
        "operation": operation,
        "locationId": locationId
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "idealista7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
import os
import requests

def Search_airports_by_query(q, limit=10):
    """
    :API_description: This API searches for airports based on a text query and returns a list of matching results, allowing control over the maximum number of airports returned.
    :param q: The search term for the airport.
    :param limit: The maximum number of results to return.
    :response_schema: 
    ```json
{
  "searchBy": "new york",
  "count": 2,
  "items": [
    {
      "icao": "KJFK",
      "iata": "JFK",
      "name": "New York John F Kennedy",
      "shortName": "John F Kennedy",
      "municipalityName": "New York",
      "location": {
        "lat": 40.6398,
        "lon": -73.7789
      },
      "countryCode": "US",
      "timeZone": "America/New_York"
    },
    {
      "icao": "KLGA",
      "iata": "LGA",
      "name": "New York La Guardia",
      "shortName": "La Guardia",
      "municipalityName": "New York",
      "location": {
        "lat": 40.7772,
        "lon": -73.8726
      },
      "countryCode": "US",
      "timeZone": "America/New_York"
    }
  ]
}
    ```
    """
    url = f"https://aerodatabox.p.rapidapi.com/airports/search/term"

    querystring = {
        "q": q,
        "limit": limit,
    }

    headers = {
        "x-rapidapi-key": "9cda500e54mshe688ef1d857bd6bp1f9040jsn59b82e309f42",
        "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


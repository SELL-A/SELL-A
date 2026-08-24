import os
import requests

def Search_airports_by_location(lat, lon, radiusKm, limit):
    """
    :API_description: This API searches for airports within a specified radius of a given geographic coordinate, returning a list of matching airports with their details.
    :param lat: Latitude of the location to search around.
    :param lon: Longitude of the location to search around.
    :param radiusKm: Radius of search around specified location in kilometers (max. 1000 km)
    :param limit: Maximum number of results to return.
    :response_schema: 
    ```json
    {
  "searchBy": {
    "lat": 40.688812,
    "lon": -74.04437
  },
  "count": 7,
  "items": [
    {
      "icao": "KEWR",
      "iata": "EWR",
      "name": "Newark Liberty",
      "shortName": "Liberty",
      "municipalityName": "Newark",
      "location": {
        "lat": 40.6925,
        "lon": -74.1687
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
    },
    {
      "icao": "KTEB",
      "iata": "TEB",
      "name": "Teterboro",
      "shortName": "Teterboro",
      "municipalityName": "Teterboro",
      "location": {
        "lat": 40.8501,
        "lon": -74.0608
      },
      "countryCode": "US",
      "timeZone": "America/New_York"
    },
    {
      "icao": "KLDJ",
      "iata": "LDJ",
      "name": "Linden",
      "shortName": "Linden",
      "municipalityName": "Linden",
      "location": {
        "lat": 40.6174,
        "lon": -74.2446
      },
      "countryCode": "US",
      "timeZone": "America/New_York"
    },
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
      "icao": "KCDW",
      "iata": "CDW",
      "name": "Caldwell Essex County",
      "shortName": "Essex County",
      "municipalityName": "Caldwell",
      "location": {
        "lat": 40.8752,
        "lon": -74.2814
      },
      "countryCode": "US",
      "timeZone": "America/New_York"
    },
    {
      "icao": "KMMU",
      "iata": "MMU",
      "name": "Morristown Municipal",
      "shortName": "Municipal",
      "municipalityName": "Morristown",
      "location": {
        "lat": 40.7994,
        "lon": -74.4149
      },
      "countryCode": "US",
      "timeZone": "America/New_York"
    }
  ]
}
```
    """
    url = f"https://aerodatabox.p.rapidapi.com/airports/search/location"
    querystring = {
        "lat": lat,
        "lon": lon,
        "radiusKm": radiusKm,
        "limit": limit,
        "withFlightInfoOnly": False
    }

    headers = {
        "x-rapidapi-key": "9cda500e54mshe688ef1d857bd6bp1f9040jsn59b82e309f42",
        "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    if response.status_code == 204:
        return {}
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


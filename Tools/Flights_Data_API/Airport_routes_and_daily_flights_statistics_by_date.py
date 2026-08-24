import os
import requests

def Airport_routes_and_daily_flights_statistics_by_date(codeType, code, dateLocal):
    """
    :API_description: Retrieves detailed route information and flight statistics for a specified airport on a given local date and time.
    :param codeType: The type of code used to identify the airport (e.g., iata, icao).
    :param code: The specific code of the airport(If codeType is:
    icao, then this field must be a 4-character ICAO-code of the airport (e.g.: EHAM, KLAX, UUEE, etc.);iata, then this field must be a 3-character IATA-code of the airport (e.g.: AMS, SFO, LAX, etc.).).
    :param dateLocal: The local date for which the statistics are requested (e.g., "2025-11-15" Date (yyyy-mm-dd)).
    :response_schema: 
    ```json
{
  "routes": [
    {
      "destination": {
        "icao": "CYYC",
        "iata": "YYC",
        "name": "Calgary",
        "shortName": "Calgary",
        "municipalityName": "Calgary",
        "location": {
          "lat": 51.1139,
          "lon": -114.02
        },
        "countryCode": "CA",
        "timeZone": "America/Edmonton"
      },
      "averageDailyFlights": 32.86,
      "operators": [
        {
          "name": "Air Canada",
          "iata": "AC",
          "icao": "ACA"
        },
        {
          "name": "Morningstar Air Express",
          "icao": "MAL"
        },
        {
          "name": "WestJet",
          "iata": "WS",
          "icao": "WJA"
        },
        {
          "name": "Flair Airlines",
          "iata": "F8",
          "icao": "FLE"
        },
        {
          "name": "Porter Airlines",
          "iata": "PD",
          "icao": "POE"
        },
        {
          "name": "Chartright Air",
          "icao": "HRT"
        }
      ]
    },
    {
      "destination": {
        "icao": "CYVR",
        "iata": "YVR",
        "name": "Vancouver",
        "shortName": "Vancouver",
        "municipalityName": "Vancouver",
        "location": {
          "lat": 49.1939,
          "lon": -123.184
        },
        "countryCode": "CA",
        "timeZone": "America/Vancouver"
      },
      "averageDailyFlights": 32.71,
      "operators": [
        {
          "name": "Air Canada",
          "iata": "AC",
          "icao": "ACA"
        },
        {
          "name": "WestJet",
          "iata": "WS",
          "icao": "WJA"
        },
        {
          "name": "Porter Airlines",
          "iata": "PD",
          "icao": "POE"
        },
        {
          "name": "Flair Airlines",
          "iata": "F8",
          "icao": "FLE"
        },
        {
          "name": "Skyservice Business Aviation",
          "icao": "SYB"
        },
        {
          "name": "Morningstar Air Express",
          "icao": "MAL"
        }
      ]
    },
    {
      "destination": {
        "icao": "CYUL",
        "iata": "YUL",
        "name": "Montreal Trudeau",
        "shortName": "Trudeau",
        "municipalityName": "Montreal",
        "location": {
          "lat": 45.4706,
          "lon": -73.7408
        },
        "countryCode": "CA",
        "timeZone": "America/Toronto"
      },
      "averageDailyFlights": 28.43,
      "operators": [
        {
          "name": "United Airlines",
          "iata": "UA",
          "icao": "UAL"
        },
        {
          "name": "Air Canada",
          "iata": "AC",
          "icao": "ACA"
        },
        {
          "name": "Porter Airlines",
          "iata": "PD",
          "icao": "POE"
        },
        {
          "name": "WestJet",
          "iata": "WS",
          "icao": "WJA"
        },
        {
          "name": "Royal Jordanian",
          "iata": "RJ",
          "icao": "RJA"
        },
        {
          "name": "Air Transat",
          "iata": "TS",
          "icao": "TSC"
        },
        {
          "name": "Skyservice Business Aviation",
          "icao": "SYB"
        }
      ]
    }
  ]
}
```
    """
    url = f"https://aerodatabox.p.rapidapi.com/airports/{codeType}/{code}/stats/routes/daily/{dateLocal}"
    headers = {
        "x-rapidapi-key": "9cda500e54mshe688ef1d857bd6bp1f9040jsn59b82e309f42",
        "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    if response.status_code == 204:
        return {}
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")






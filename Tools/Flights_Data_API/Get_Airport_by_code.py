import os
import requests

def Get_Airport_by_code(codeType, code):
    """
    :API_description: Retrieves detailed information about a specific airport by searching for its iata (3-character) or icao (4-character) airport code.
    :param codeType: The type of code used to identify the airport (e.g., iata, icao).
    :param code: The actual code of the airport
    (If codeType is: icao, then this field must be a 4-character ICAO-code of the airport (e.g.: EHAM, KLAX, UUEE, etc.);iata, then this field must be a 3-character IATA-code of the airport (e.g.: AMS, SFO, LAX, etc.).).
    :response_schema: 
    ```json
   {
  "icao": "EGLL",
  "iata": "LHR",
  "shortName": "Heathrow",
  "fullName": "London Heathrow",
  "municipalityName": "London",
  "location": {
    "lat": 51.4706,
    "lon": -0.461941
  },
  "elevation": {
    "meter": 25.3,
    "km": 0.03,
    "mile": 0.02,
    "nm": 0.01,
    "feet": 83
  },
  "country": {
    "code": "GB",
    "name": "United Kingdom"
  },
  "continent": {
    "code": "EU",
    "name": "Europe"
  },
  "timeZone": "Europe/London",
  "urls": {
    "webSite": "http://www.heathrow.com/",
    "wikipedia": "https://en.wikipedia.org/wiki/London_Heathrow_Airport",
    "twitter": "https://x.com/HeathrowAirport",
    "flightRadar": "https://www.flightradar24.com/51.47,-0.46/14",
    "googleMaps": "https://www.google.com/maps/@51.470600,-0.461941,14z"
  }
}```
    """
    url = f"https://aerodatabox.p.rapidapi.com/airports/{codeType}/{code}"
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


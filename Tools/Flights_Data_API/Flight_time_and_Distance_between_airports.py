import os
import requests

def Flight_time_and_Distance_between_airports(codeType, codeFrom, codeTo, flightTimeModel="Standard"):
    """
    :API_description: This API calculates the estimated flight time and distance between two specified airports. It supports both iata (3-character) and icao (4-character) airport code formats.
    :param codeType: The type of code used for the airports (e.g., iata, icao).
    :param codeFrom: The code of the departure airport(If codeType is:
    icao, then this field must be a 4-character ICAO-code of the origin airport (e.g.: EHAM, KLAX, UUEE, etc.);
    iata, then this field must be a 3-character IATA-code of the origin airport (e.g.: AMS, SFO, LAX, etc.).).
    :param codeTo: The code of the destination airport.
    :param flightTimeModel: The model used to estimate flight time (default is "Standard").
    :response_schema: 
    ```json
{
  "from": {
    "icao": "EGLL",
    "iata": "LHR",
    "name": "London Heathrow",
    "shortName": "Heathrow",
    "municipalityName": "London",
    "location": {
      "lat": 51.4706,
      "lon": -0.461941
    },
    "countryCode": "GB",
    "timeZone": "Europe/London"
  },
  "to": {
    "icao": "KLAX",
    "iata": "LAX",
    "name": "Los Angeles",
    "shortName": "Los Angeles",
    "municipalityName": "Los Angeles",
    "location": {
      "lat": 33.9425,
      "lon": -118.408
    },
    "countryCode": "US",
    "timeZone": "America/Los_Angeles"
  },
  "greatCircleDistance": {
    "meter": 8780646.41,
    "km": 8780.65,
    "mile": 5456.04,
    "nm": 4741.17,
    "feet": 28807895.05
  },
  "approxFlightTime": "14:05:00"
}
    ```
    """
    url = f"https://aerodatabox.p.rapidapi.com/airports/{codeType}/{codeFrom}/distance-time/{codeTo}?flightTimeModel={flightTimeModel}"
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

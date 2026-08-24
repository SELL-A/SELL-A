import os
import requests

def Airport_delays_by_date(codeType, code, dateLocal):
    """
    :API_description: Retrieves flight delay information for a specific airport on a given date and time.
    :param codeType: The type of code used to identify the airport (e.g., iata, icao).
    :param code: The specific code of the airport(If codeType is:
    icao, then this field must be a 4-character ICAO-code of the airport (e.g.: EHAM, KLAX, UUEE, etc.);iata, then this field must be a 3-character IATA-code of the airport (e.g.: AMS, SFO, LAX, etc.).).
    :param dateLocal: The local date for which delay information is requested (e.g., "2025-11-15T09:00").
    :response_schema: 
    ```json
{
  "airportIcao": "KLAX",
  "from": {
    "utc": "2025-11-15 15:00Z",
    "local": "2025-11-15 07:00-08:00"
  },
  "to": {
    "utc": "2025-11-15 17:00Z",
    "local": "2025-11-15 09:00-08:00"
  },
  "departuresDelayInformation": {
    "numTotal": 98,
    "numQualifiedTotal": 89,
    "numCancelled": 0,
    "medianDelay": "00:29:00",
    "delayIndex": 1.61
  },
  "arrivalsDelayInformation": {
    "numTotal": 85,
    "numQualifiedTotal": 73,
    "numCancelled": 0,
    "medianDelay": "-00:17:00",
    "delayIndex": 0
  }
}
```
    """
    url = f"https://aerodatabox.p.rapidapi.com/airports/{codeType}/{code}/delays/{dateLocal}"
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


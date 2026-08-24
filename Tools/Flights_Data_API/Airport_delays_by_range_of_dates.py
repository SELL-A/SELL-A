import os
import requests

def Airport_delays_by_range_of_dates(codeType, code, dateLocal, dateToLocal):
    """
    :API_description: Retrieves historical delay information for a specific airport over a defined time period, providing details on arrival and departure delays.
    :param codeType: The type of code used to identify the airport (e.g., iata, icao).
    :param code: The actual code of the airport(If codeType is:
    icao, then this field must be a 4-character ICAO-code of the airport (e.g.: EHAM, KLAX, UUEE, etc.);iata, then this field must be a 3-character IATA-code of the airport (e.g.: AMS, SFO, LAX, etc.).).
    :param dateLocal: The start date for the delay information in local time (e.g., "2025-11-15T09:00").
    :param dateToLocal: The end date for the delay information in local time (e.g., "2025-11-20T18:00").
    :note: The duration of the requested period of time should be positive and should not be more than 12 hours in duration.
    :response_schema: 
    ```json
[
  {
    "airportIcao": "KLAX",
    "from": {
      "utc": "2026-06-03 17:00Z",
      "local": "2026-06-03 10:00-07:00"
    },
    "to": {
      "utc": "2026-06-03 19:00Z",
      "local": "2026-06-03 12:00-07:00"
    },
    "departuresDelayInformation": {
      "numTotal": 99,
      "numQualifiedTotal": 91,
      "numCancelled": 0,
      "medianDelay": "00:14:00",
      "delayIndex": 0.78
    },
    "arrivalsDelayInformation": {
      "numTotal": 88,
      "numQualifiedTotal": 79,
      "numCancelled": 0,
      "medianDelay": "-00:20:00",
      "delayIndex": 0
    }
  },
  {
    "airportIcao": "KLAX",
    "from": {
      "utc": "2026-06-03 17:15Z",
      "local": "2026-06-03 10:15-07:00"
    },
    "to": {
      "utc": "2026-06-03 19:15Z",
      "local": "2026-06-03 12:15-07:00"
    },
    "departuresDelayInformation": {
      "numTotal": 90,
      "numQualifiedTotal": 82,
      "numCancelled": 0,
      "medianDelay": "00:14:00",
      "delayIndex": 0.78
    },
    "arrivalsDelayInformation": {
      "numTotal": 89,
      "numQualifiedTotal": 78,
      "numCancelled": 0,
      "medianDelay": "-00:19:00",
      "delayIndex": 0
    }
  },
  {
    "airportIcao": "KLAX",
    "from": {
      "utc": "2026-06-03 17:30Z",
      "local": "2026-06-03 10:30-07:00"
    },
    "to": {
      "utc": "2026-06-03 19:30Z",
      "local": "2026-06-03 12:30-07:00"
    },
    "departuresDelayInformation": {
      "numTotal": 90,
      "numQualifiedTotal": 81,
      "numCancelled": 0,
      "medianDelay": "00:14:00",
      "delayIndex": 0.78
    },
    "arrivalsDelayInformation": {
      "numTotal": 85,
      "numQualifiedTotal": 74,
      "numCancelled": 0,
      "medianDelay": "-00:19:00",
      "delayIndex": 0
    }
  },
  {
    "airportIcao": "KLAX",
    "from": {
      "utc": "2026-06-03 17:45Z",
      "local": "2026-06-03 10:45-07:00"
    },
    "to": {
      "utc": "2026-06-03 19:45Z",
      "local": "2026-06-03 12:45-07:00"
    },
    "departuresDelayInformation": {
      "numTotal": 89,
      "numQualifiedTotal": 78,
      "numCancelled": 0,
      "medianDelay": "00:14:00",
      "delayIndex": 0.81
    },
    "arrivalsDelayInformation": {
      "numTotal": 88,
      "numQualifiedTotal": 77,
      "numCancelled": 0,
      "medianDelay": "-00:19:00",
      "delayIndex": 0
    }
  }
]
    ```
    """
    url = f"https://aerodatabox.p.rapidapi.com/airports/{codeType}/{code}/delays/{dateLocal}/{dateToLocal}"
    headers = {
        "x-rapidapi-key": "9cda500e54mshe688ef1d857bd6bp1f9040jsn59b82e309f42",
        "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    if response.status_code == 204:
        return []
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
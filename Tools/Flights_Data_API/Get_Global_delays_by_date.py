import os
import requests

def Get_Global_delays_by_date(dateTimeUtc):
    """
    :API_description: Get Global Worldwide delays. How many flights are delayed or canceled right now or in the past? Delay statistics and delay index at an airport now and back then.
    :param dateTimeUtc: The UTC date and time in ISO 8601 format (e.g., "2023-01-01T12:00:00").
    :response_schema: 
    ```
[
  {
    "airportIcao": "LYTV",
    "from": {
      "utc": "2025-06-21 10:00Z",
      "local": "2025-06-21 12:00+02:00"
    },
    "to": {
      "utc": "2025-06-21 12:00Z",
      "local": "2025-06-21 14:00+02:00"
    },
    "departuresDelayInformation": {
      "numTotal": 6,
      "numQualifiedTotal": 6,
      "numCancelled": 0,
      "medianDelay": "02:07:00",
      "delayIndex": 5
    },
    "arrivalsDelayInformation": {
      "numTotal": 1,
      "numQualifiedTotal": 1,
      "numCancelled": 0
    }
  },
  {
    "airportIcao": "ZSSS",
    "from": {
      "utc": "2025-06-21 10:00Z",
      "local": "2025-06-21 18:00+08:00"
    },
    "to": {
      "utc": "2025-06-21 12:00Z",
      "local": "2025-06-21 20:00+08:00"
    },
    "departuresDelayInformation": {
      "numTotal": 55,
      "numQualifiedTotal": 52,
      "numCancelled": 1,
      "medianDelay": "00:57:00",
      "delayIndex": 3.28
    },
    "arrivalsDelayInformation": {
      "numTotal": 52,
      "numQualifiedTotal": 50,
      "numCancelled": 0,
      "medianDelay": "-01:28:00",
      "delayIndex": 0
    }
  },
  {
    "airportIcao": "LGZA",
    "from": {
      "utc": "2025-06-21 10:00Z",
      "local": "2025-06-21 13:00+03:00"
    },
    "to": {
      "utc": "2025-06-21 12:00Z",
      "local": "2025-06-21 15:00+03:00"
    },
    "departuresDelayInformation": {
      "numTotal": 8,
      "numQualifiedTotal": 6,
      "numCancelled": 0,
      "medianDelay": "00:57:00",
      "delayIndex": 3.17
    },
    "arrivalsDelayInformation": {
      "numTotal": 5,
      "numQualifiedTotal": 3,
      "numCancelled": 0
    }
  },
  {
    "airportIcao": "ZSPD",
    "from": {
      "utc": "2025-06-21 10:00Z",
      "local": "2025-06-21 18:00+08:00"
    },
    "to": {
      "utc": "2025-06-21 12:00Z",
      "local": "2025-06-21 20:00+08:00"
    },
    "departuresDelayInformation": {
      "numTotal": 131,
      "numQualifiedTotal": 131,
      "numCancelled": 5,
      "medianDelay": "00:49:00",
      "delayIndex": 2.89
    },
    "arrivalsDelayInformation": {
      "numTotal": 108,
      "numQualifiedTotal": 108,
      "numCancelled": 2,
      "medianDelay": "-01:55:00",
      "delayIndex": 0
    }
  },
  {
    "airportIcao": "LGAV",
    "from": {
      "utc": "2025-06-21 10:00Z",
      "local": "2025-06-21 13:00+03:00"
    },
    "to": {
      "utc": "2025-06-21 12:00Z",
      "local": "2025-06-21 15:00+03:00"
    },
    "departuresDelayInformation": {
      "numTotal": 46,
      "numQualifiedTotal": 46,
      "numCancelled": 0,
      "medianDelay": "00:37:00",
      "delayIndex": 2.06
    },
    "arrivalsDelayInformation": {
      "numTotal": 47,
      "numQualifiedTotal": 47,
      "numCancelled": 0,
      "medianDelay": "00:14:00",
      "delayIndex": 0.78
    }
  },
  {
    "airportIcao": "DTNH",
    "from": {
      "utc": "2025-06-21 10:00Z",
      "local": "2025-06-21 11:00+01:00"
    },
    "to": {
      "utc": "2025-06-21 12:00Z",
      "local": "2025-06-21 13:00+01:00"
    },
    "departuresDelayInformation": {
      "numTotal": 5,
      "numQualifiedTotal": 5,
      "numCancelled": 1,
      "delayIndex": 2.83
    },
    "arrivalsDelayInformation": {
      "numTotal": 1,
      "numQualifiedTotal": 1,
      "numCancelled": 0
    }
  }
]
    ```
    """
    url = f"https://aerodatabox.p.rapidapi.com/airports/delays/{dateTimeUtc}"
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
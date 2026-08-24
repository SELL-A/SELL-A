from ast import If
import os
import requests

def Get_Flight_history_and_Schedule(flightid, dateFromLocal, dateToLocal):
    """
    :API_description: Returns the data over a range of dates, thus allowing to get insights on the flight history or schedule within the specified range.
    :param flightid: The flight identifier/number, e.g. KL1395, Klm 1395
    :param dateFromLocal: The start date in local time. YYYY-MM-DD, e.g.: 2025-08-29
    :param dateToLocal: The end date in local time.YYYY-MM-DD, e.g.: 2025-08-30
     :note: The duration of the requested period of time should be positive and should not be more than 12 hours in duration.
    :response_schema: 
    ```json
[
  {
    "greatCircleDistance": {
      "meter": 5863339.83,
      "km": 5863.34,
      "mile": 3643.31,
      "nm": 3165.95,
      "feet": 19236679.22
    },
    "departure": {
      "airport": {
        "icao": "EHAM",
        "iata": "AMS",
        "name": "Amsterdam Schiphol",
        "shortName": "Schiphol",
        "municipalityName": "Amsterdam",
        "location": {
          "lat": 52.3086,
          "lon": 4.763889
        },
        "countryCode": "NL",
        "timeZone": "Europe/Amsterdam"
      },
      "scheduledTime": {
        "utc": "2026-01-01 07:55Z",
        "local": "2026-01-01 08:55+01:00"
      },
      "revisedTime": {
        "utc": "2026-01-01 08:42Z",
        "local": "2026-01-01 09:42+01:00"
      },
      "runwayTime": {
        "utc": "2026-01-01 08:57Z",
        "local": "2026-01-01 09:57+01:00"
      },
      "terminal": "2",
      "checkInDesk": "9-16",
      "gate": "D7",
      "runway": "24",
      "quality": [
        "Basic",
        "Live"
      ]
    },
    "arrival": {
      "airport": {
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
      "scheduledTime": {
        "utc": "2026-01-01 16:40Z",
        "local": "2026-01-01 11:40-05:00"
      },
      "predictedTime": {
        "utc": "2026-01-01 16:57Z",
        "local": "2026-01-01 11:57-05:00"
      },
      "terminal": "4",
      "quality": [
        "Basic"
      ]
    },
    "lastUpdatedUtc": "2026-01-01 09:22Z",
    "number": "DL 47",
    "callSign": "DAL47",
    "status": "Departed",
    "codeshareStatus": "IsOperator",
    "isCargo": false,
    "aircraft": {
      "reg": "N817NW",
      "modeS": "AB249E",
      "model": "Airbus A330"
    },
    "airline": {
      "name": "Delta Air Lines",
      "iata": "DL",
      "icao": "DAL"
    }
  },
  {
    "greatCircleDistance": {
      "meter": 5863339.83,
      "km": 5863.34,
      "mile": 3643.31,
      "nm": 3165.95,
      "feet": 19236679.22
    },
    "departure": {
      "airport": {
        "icao": "EHAM",
        "iata": "AMS",
        "name": "Amsterdam Schiphol",
        "shortName": "Schiphol",
        "municipalityName": "Amsterdam",
        "location": {
          "lat": 52.3086,
          "lon": 4.763889
        },
        "countryCode": "NL",
        "timeZone": "Europe/Amsterdam"
      },
      "scheduledTime": {
        "utc": "2026-01-02 07:50Z",
        "local": "2026-01-02 08:50+01:00"
      },
      "revisedTime": {
        "utc": "2026-01-02 07:50Z",
        "local": "2026-01-02 08:50+01:00"
      },
      "terminal": "2",
      "checkInDesk": "9-16",
      "gate": "E6",
      "quality": [
        "Basic",
        "Live"
      ]
    },
    "arrival": {
      "airport": {
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
      "scheduledTime": {
        "utc": "2026-01-02 16:35Z",
        "local": "2026-01-02 11:35-05:00"
      },
      "terminal": "4",
      "quality": [
        "Basic"
      ]
    },
    "lastUpdatedUtc": "2026-01-02 13:28Z",
    "number": "DL 47",
    "status": "Canceled",
    "codeshareStatus": "IsOperator",
    "isCargo": false,
    "aircraft": {
      "reg": "N827NW",
      "modeS": "AB4C1D",
      "model": "Airbus A330-300"
    },
    "airline": {
      "name": "Delta Air Lines",
      "iata": "DL",
      "icao": "DAL"
    }
  },
  {
    "greatCircleDistance": {
      "meter": 5863339.83,
      "km": 5863.34,
      "mile": 3643.31,
      "nm": 3165.95,
      "feet": 19236679.22
    },
    "departure": {
      "airport": {
        "icao": "EHAM",
        "iata": "AMS",
        "name": "Amsterdam Schiphol",
        "shortName": "Schiphol",
        "municipalityName": "Amsterdam",
        "location": {
          "lat": 52.3086,
          "lon": 4.763889
        },
        "countryCode": "NL",
        "timeZone": "Europe/Amsterdam"
      },
      "scheduledTime": {
        "utc": "2026-01-03 07:55Z",
        "local": "2026-01-03 08:55+01:00"
      },
      "revisedTime": {
        "utc": "2026-01-03 08:26Z",
        "local": "2026-01-03 09:26+01:00"
      },
      "runwayTime": {
        "utc": "2026-01-03 09:13Z",
        "local": "2026-01-03 10:13+01:00"
      },
      "terminal": "2",
      "checkInDesk": "9-16",
      "gate": "E19",
      "runway": "36C",
      "quality": [
        "Basic",
        "Live"
      ]
    },
    "arrival": {
      "airport": {
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
      "scheduledTime": {
        "utc": "2026-01-03 16:40Z",
        "local": "2026-01-03 11:40-05:00"
      },
      "revisedTime": {
        "utc": "2026-01-03 17:38Z",
        "local": "2026-01-03 12:38-05:00"
      },
      "runwayTime": {
        "utc": "2026-01-03 17:38Z",
        "local": "2026-01-03 12:38-05:00"
      },
      "terminal": "4",
      "quality": [
        "Basic",
        "Live"
      ]
    },
    "lastUpdatedUtc": "2026-01-03 17:39Z",
    "number": "DL 47",
    "callSign": "DAL9887",
    "status": "Arrived",
    "codeshareStatus": "IsOperator",
    "isCargo": false,
    "aircraft": {
      "reg": "N807NW",
      "modeS": "AAFD1F",
      "model": "Airbus A330"
    },
    "airline": {
      "name": "Delta Air Lines",
      "iata": "DL",
      "icao": "DAL"
    }
  }
]
    ```
    """
    url = f"https://aerodatabox.p.rapidapi.com/flights/Number/{flightid}/{dateFromLocal}/{dateToLocal}?dateLocalRole=Both"
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

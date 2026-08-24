import os
import requests

def Get_Flight_status(flightid: str):
    """
    :API_description: Retrieves comprehensive status and operational details for a specific flight, including airline information, arrival/departure data, aircraft details, and codeshare partner information.
    :param flightid: The flight number identifier then then this field should be Flight number (with or without spaces, IATA or ICAO, any case formats are acceptable, e.g. KL1395, Klm1395).
    :response_schema: 
    ```json
[
  {
    "greatCircleDistance": {
      "meter": 204586.42,
      "km": 204.59,
      "mile": 127.12,
      "nm": 110.47,
      "feet": 671215.29
    },
    "departure": {
      "airport": {
        "icao": "KSEA",
        "iata": "SEA",
        "name": "Seattle Tacoma",
        "shortName": "Tacoma",
        "municipalityName": "Seattle",
        "location": {
          "lat": 47.449,
          "lon": -122.309
        },
        "countryCode": "US",
        "timeZone": "America/Los_Angeles"
      },
      "scheduledTime": {
        "utc": "2026-01-03 23:45Z",
        "local": "2026-01-03 15:45-08:00"
      },
      "revisedTime": {
        "utc": "2026-01-04 00:22Z",
        "local": "2026-01-03 16:22-08:00"
      },
      "runwayTime": {
        "utc": "2026-01-04 00:22Z",
        "local": "2026-01-03 16:22-08:00"
      },
      "quality": [
        "Basic",
        "Live"
      ]
    },
    "arrival": {
      "airport": {
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
      "scheduledTime": {
        "utc": "2026-01-04 00:45Z",
        "local": "2026-01-03 16:45-08:00"
      },
      "revisedTime": {
        "utc": "2026-01-04 00:59Z",
        "local": "2026-01-03 16:59-08:00"
      },
      "predictedTime": {
        "utc": "2026-01-04 01:16Z",
        "local": "2026-01-03 17:16-08:00"
      },
      "terminal": "M",
      "gate": "E88",
      "baggageBelt": "34",
      "quality": [
        "Basic",
        "Live"
      ]
    },
    "flightPlan": {
      "flightRules": "IFR",
      "revisionNo": 0,
      "status": "Active",
      "route": "DCT PAE GRIZZ8",
      "altitude": {
        "requested": {
          "meter": 4876.8,
          "km": 4.88,
          "mile": 3.03,
          "nm": 2.63,
          "feet": 16000
        }
      },
      "airspeed": {
        "requested": {
          "kt": 361,
          "kmPerHour": 669,
          "miPerHour": 415,
          "meterPerSecond": 186
        }
      },
      "remarks": "TCAS EQUIPPED",
      "lastUpdatedUtc": "2026-01-03 21:51Z"
    },
    "lastUpdatedUtc": "2026-01-04 00:24Z",
    "number": "AS 2223",
    "callSign": "QXE2223",
    "status": "EnRoute",
    "codeshareStatus": "IsOperator",
    "isCargo": false,
    "aircraft": {
      "reg": "N632QX",
      "modeS": "A8469E",
      "model": "Embraer 175"
    },
    "airline": {
      "name": "Alaska Airlines",
      "iata": "AS",
      "icao": "ASA"
    },
    "location": {
      "pressureAltitude": {
        "meter": 5013.96,
        "km": 5.01,
        "mile": 3.12,
        "nm": 2.71,
        "feet": 16450
      },
      "altitude": {
        "meter": 5013.96,
        "km": 5.01,
        "mile": 3.12,
        "nm": 2.71,
        "feet": 16450
      },
      "pressure": {
        "hPa": 0,
        "inHg": 0,
        "mmHg": 0
      },
      "groundSpeed": {
        "kt": 389,
        "kmPerHour": 720,
        "miPerHour": 448,
        "meterPerSecond": 200
      },
      "trueTrack": {
        "deg": 348,
        "rad": 6.073745796940266
      },
      "reportedAtUtc": "2026-01-04 00:35Z",
      "lat": 48.347397,
      "lon": -122.40206
    }
  },
  {
    "greatCircleDistance": {
      "meter": 204586.42,
      "km": 204.59,
      "mile": 127.12,
      "nm": 110.47,
      "feet": 671215.29
    },
    "departure": {
      "airport": {
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
      "scheduledTime": {
        "utc": "2026-01-04 01:45Z",
        "local": "2026-01-03 17:45-08:00"
      },
      "revisedTime": {
        "utc": "2026-01-04 01:49Z",
        "local": "2026-01-03 17:49-08:00"
      },
      "terminal": "M",
      "checkInDesk": "222-228",
      "gate": "E88",
      "quality": [
        "Basic",
        "Live"
      ]
    },
    "arrival": {
      "airport": {
        "icao": "KSEA",
        "iata": "SEA",
        "name": "Seattle Tacoma",
        "shortName": "Tacoma",
        "municipalityName": "Seattle",
        "location": {
          "lat": 47.449,
          "lon": -122.309
        },
        "countryCode": "US",
        "timeZone": "America/Los_Angeles"
      },
      "scheduledTime": {
        "utc": "2026-01-04 02:50Z",
        "local": "2026-01-03 18:50-08:00"
      },
      "predictedTime": {
        "utc": "2026-01-04 03:05Z",
        "local": "2026-01-03 19:05-08:00"
      },
      "quality": [
        "Basic"
      ]
    },
    "lastUpdatedUtc": "2026-01-04 00:24Z",
    "number": "AS 2223",
    "status": "Expected",
    "codeshareStatus": "Unknown",
    "isCargo": false,
    "aircraft": {
      "model": "Embraer 175"
    },
    "airline": {
      "name": "Alaska Airlines",
      "iata": "AS",
      "icao": "ASA"
    }
  }
]
```
    """
    url = f"https://aerodatabox.p.rapidapi.com/flights/Number/{flightid}"
    headers = {
        "x-rapidapi-key": "9cda500e54mshe688ef1d857bd6bp1f9040jsn59b82e309f42",
        "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
    }
    querystring = {"dateLocalRole":"Both","withAircraftImage":"false","withLocation":"false","withFlightPlan":"false"}
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    if response.status_code == 204:
        return []
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

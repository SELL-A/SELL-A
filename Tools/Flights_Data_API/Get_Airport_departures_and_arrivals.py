import os
import requests

def Get_Airport_departures_and_arrivals(codeType, code, fromLocal, toLocal):
    """
    :API_description: Retrieves a list of scheduled flight departures and arrivals for a specified airport within a given local time range.
    :param codeType: The type of code used to identify the airport (e.g., iata, icao).
    :param code: The actual code of the airport.
    :param fromLocal: The start time for the flight data in local time (e.g., 2023-11-15T09:00).
    :param toLocal: The end time for the flight data in local time (e.g., 2023-11-20T18:00).
    :note: The duration of the requested period of time should be positive and should not be more than 12 hours in duration.
    :response_schema: 
    ```json
{
  "departures": [
    {
      "departure": {
        "scheduledTime": {
          "utc": "2026-04-04 23:55Z",
          "local": "2026-04-04 19:55-04:00"
        },
        "revisedTime": {
          "utc": "2026-04-05 00:04Z",
          "local": "2026-04-04 20:04-04:00"
        },
        "runwayTime": {
          "utc": "2026-04-05 00:04Z",
          "local": "2026-04-04 20:04-04:00"
        },
        "terminal": "C",
        "runway": "13",
        "quality": [
          "Basic",
          "Live"
        ]
      },
      "arrival": {
        "airport": {
          "icao": "KMIA",
          "iata": "MIA",
          "name": "Miami",
          "countryCode": "us",
          "timeZone": "America/New_York"
        },
        "scheduledTime": {
          "utc": "2026-04-05 03:18Z",
          "local": "2026-04-04 23:18-04:00"
        },
        "revisedTime": {
          "utc": "2026-04-05 02:30Z",
          "local": "2026-04-04 22:30-04:00"
        },
        "runwayTime": {
          "utc": "2026-04-05 02:30Z",
          "local": "2026-04-04 22:30-04:00"
        },
        "runway": "09",
        "quality": [
          "Basic",
          "Live"
        ]
      },
      "number": "DL 2382",
      "callSign": "DAL2382",
      "status": "Departed",
      "codeshareStatus": "IsOperator",
      "isCargo": false,
      "aircraft": {
        "reg": "N397DN",
        "modeS": "A49D22",
        "model": "Airbus A321"
      },
      "airline": {
        "name": "Delta Air Lines",
        "iata": "DL",
        "icao": "DAL"
      }
    },
    {
      "departure": {
        "scheduledTime": {
          "utc": "2026-04-05 00:10Z",
          "local": "2026-04-04 20:10-04:00"
        },
        "revisedTime": {
          "utc": "2026-04-05 00:10Z",
          "local": "2026-04-04 20:10-04:00"
        },
        "runwayTime": {
          "utc": "2026-04-05 00:10Z",
          "local": "2026-04-04 20:10-04:00"
        },
        "quality": [
          "Basic",
          "Live"
        ]
      },
      "arrival": {
        "airport": {
          "icao": "KBKL",
          "iata": "BKL",
          "name": "Cleveland",
          "countryCode": "us",
          "timeZone": "America/New_York"
        },
        "scheduledTime": {
          "utc": "2026-04-05 01:05Z",
          "local": "2026-04-04 21:05-04:00"
        },
        "revisedTime": {
          "utc": "2026-04-05 01:05Z",
          "local": "2026-04-04 21:05-04:00"
        },
        "quality": [
          "Basic",
          "Live"
        ]
      },
      "number": "LN 171AR",
      "callSign": "LN171AR",
      "status": "Departed",
      "codeshareStatus": "IsOperator",
      "isCargo": false,
      "aircraft": {
        "reg": "N171AR",
        "modeS": "A11CF4",
        "model": "Bombardier Learjet 31"
      },
      "airline": {
        "name": "Libyan Airlines",
        "iata": "LN",
        "icao": "LAA"
      }
    },
    {
      "departure": {
        "scheduledTime": {
          "utc": "2026-04-05 00:10Z",
          "local": "2026-04-04 20:10-04:00"
        },
        "revisedTime": {
          "utc": "2026-04-05 00:12Z",
          "local": "2026-04-04 20:12-04:00"
        },
        "runwayTime": {
          "utc": "2026-04-05 00:12Z",
          "local": "2026-04-04 20:12-04:00"
        },
        "terminal": "C",
        "quality": [
          "Basic",
          "Live"
        ]
      },
      "arrival": {
        "airport": {
          "name": "Minneapolis"
        },
        "quality": []
      },
      "number": "DL 1362",
      "callSign": "DAL2086",
      "status": "Departed",
      "codeshareStatus": "IsOperator",
      "isCargo": false,
      "aircraft": {
        "reg": "N918DU",
        "modeS": "ACB4C1",
        "model": "Boeing 737"
      },
      "airline": {
        "name": "Delta Air Lines",
        "iata": "DL",
        "icao": "DAL"
      }
    },
    {
      "departure": {
        "scheduledTime": {
          "utc": "2026-04-05 00:25Z",
          "local": "2026-04-04 20:25-04:00"
        },
        "revisedTime": {
          "utc": "2026-04-05 00:21Z",
          "local": "2026-04-04 20:21-04:00"
        },
        "runwayTime": {
          "utc": "2026-04-05 00:22Z",
          "local": "2026-04-04 20:22-04:00"
        },
        "terminal": "B",
        "quality": [
          "Basic",
          "Live"
        ]
      },
      "arrival": {
        "airport": {
          "name": "Chicago"
        },
        "quality": []
      },
      "number": "UA 686",
      "callSign": "UAL3883",
      "status": "Departed",
      "codeshareStatus": "IsOperator",
      "isCargo": false,
      "aircraft": {
        "reg": "N665UA",
        "modeS": "A8C88F",
        "model": "Boeing 767-300"
      },
      "airline": {
        "name": "United",
        "iata": "UA",
        "icao": "UAL"
      }
    }
      "departure": {
        "scheduledTime": {
          "utc": "2026-04-05 01:15Z",
          "local": "2026-04-04 21:15-04:00"
        },
        "revisedTime": {
          "utc": "2026-04-05 00:26Z",
          "local": "2026-04-04 20:26-04:00"
        },
        "runwayTime": {
          "utc": "2026-04-05 00:26Z",
          "local": "2026-04-04 20:26-04:00"
        },
        "terminal": "B",
        "quality": [
          "Basic",
          "Live"
        ]
      },
      "arrival": {
        "airport": {
          "name": "Boston"
        },
        "quality": []
      },
      "number": "AA 4346",
      "callSign": "AAL198",
      "status": "Departed",
      "codeshareStatus": "IsOperator",
      "isCargo": false,
      "aircraft": {
        "reg": "N780AN",
        "modeS": "AA9093",
        "model": "Boeing 777-200"
      },
      "airline": {
        "name": "American",
        "iata": "AA",
        "icao": "AAL"
      }
      },
      {
        "departure": {
          "scheduledTime": {
            "utc": "2026-04-05 00:25Z",
            "local": "2026-04-04 20:25-04:00"
          },
          "revisedTime": {
            "utc": "2026-04-05 00:33Z",
            "local": "2026-04-04 20:33-04:00"
          },
          "runwayTime": {
            "utc": "2026-04-05 00:33Z",
            "local": "2026-04-04 20:33-04:00"
          },
          "terminal": "B",
          "quality": [
            "Basic",
            "Live"
          ]
        },
        "arrival": {
          "airport": {
            "icao": "KORD",
            "iata": "ORD",
            "name": "Chicago",
            "countryCode": "us",
            "timeZone": "America/Chicago"
          },
          "scheduledTime": {
            "utc": "2026-04-05 03:17Z",
            "local": "2026-04-04 22:17-05:00"
          },
          "revisedTime": {
            "utc": "2026-04-05 02:34Z",
            "local": "2026-04-04 21:34-05:00"
          },
          "runwayTime": {
            "utc": "2026-04-05 02:34Z",
            "local": "2026-04-04 21:34-05:00"
          },
          "terminal": "3",
          "quality": [
            "Basic",
            "Live"
          ]
        },
        "number": "AA 4466",
        "callSign": "RPA4466",
        "status": "Departed",
        "codeshareStatus": "IsOperator",
        "isCargo": false,
        "aircraft": {
          "reg": "N445YX",
          "modeS": "A55F6C",
          "model": "Embraer 175"
        },
        "airline": {
          "name": "American",
          "iata": "AA",
          "icao": "AAL"
        }
      },
      {
        "departure": {
          "scheduledTime": {
            "utc": "2026-04-05 00:30Z",
            "local": "2026-04-04 20:30-04:00"
          },
          "revisedTime": {
            "utc": "2026-04-05 00:38Z",
            "local": "2026-04-04 20:38-04:00"
          },
          "runwayTime": {
            "utc": "2026-04-05 00:38Z",
            "local": "2026-04-04 20:38-04:00"
          },
          "terminal": "B",
          "runway": "13",
          "quality": [
            "Basic",
            "Live"
          ]
        },
        "arrival": {
          "airport": {
            "icao": "KPBI",
            "iata": "PBI",
            "name": "West Palm Beach",
            "countryCode": "us",
            "timeZone": "America/New_York"
          },
          "scheduledTime": {
            "utc": "2026-04-05 03:28Z",
            "local": "2026-04-04 23:28-04:00"
          },
          "revisedTime": {
            "utc": "2026-04-05 02:56Z",
            "local": "2026-04-04 22:56-04:00"
          },
          "runwayTime": {
            "utc": "2026-04-05 02:56Z",
            "local": "2026-04-04 22:56-04:00"
          },
          "quality": [
            "Basic",
            "Live"
          ]
        },
        "number": "B6 761",
        "callSign": "JBU761",
        "status": "Departed",
        "codeshareStatus": "IsOperator",
        "isCargo": false,
        "aircraft": {
          "reg": "N952JB",
          "modeS": "AD3CDF",
          "model": "Airbus A321"
        },
        "airline": {
          "name": "JetBlue",
          "iata": "B6",
          "icao": "JBU"
        }
      }
  ]
}
```
    """
    url = f"https://aerodatabox.p.rapidapi.com/flights/airports/{codeType}/{code}/{fromLocal}/{toLocal}"
    querystring = {
        "withLeg": "true",
        "direction": "Both",
        "withCancelled": "true",
        "withCodeshared": "true",
        "withCargo": "true",
        "withPrivate": "true",
        "withLocation": "false"
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
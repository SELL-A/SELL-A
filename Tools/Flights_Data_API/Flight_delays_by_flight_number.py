import os
import requests

def Flight_delays_by_flight_number(number):
    """
    :API_description: This API retrieves historical flight delay statistics for a specified flight number, providing detailed analysis of departure and arrival performance including percentile-based delays, median times, and distribution across delay brackets for various time periods.
    :param number: The flight number for which delay information is requested(Flight number (with or without spaces, IATA or ICAO, any case formats are acceptable, e.g. KL1395, Klm 1395)).
    :response_schema: 
    ```json
{
  "number": "DL 47",
  "origins": [
    {
      "airportIcao": "EHAM",
      "class": "FlightAndHour",
      "scheduledHourUtc": 7,
      "medianDelay": "00:00:00",
      "delayPercentiles": [
        {
          "percentile": 5,
          "delay": "-00:03:00"
        },
        {
          "percentile": 10,
          "delay": "00:00:00"
        },
        {
          "percentile": 15,
          "delay": "00:00:00"
        },
        {
          "percentile": 20,
          "delay": "00:00:00"
        },
        {
          "percentile": 25,
          "delay": "00:00:00"
        },
        {
          "percentile": 30,
          "delay": "00:00:00"
        },
        {
          "percentile": 35,
          "delay": "00:00:00"
        },
        {
          "percentile": 40,
          "delay": "00:00:00"
        },
        {
          "percentile": 45,
          "delay": "00:00:00"
        },
        {
          "percentile": 50,
          "delay": "00:00:00"
        }
      ],
      "numConsideredFlights": 75,
      "numFlightsDelayedBrackets": [
        {
          "delayedTo": "-02:00:00",
          "num": 0,
          "percentage": 0
        },
        {
          "delayedFrom": "-02:00:00",
          "delayedTo": "-01:00:00",
          "num": 0,
          "percentage": 0
        },
        {
          "delayedFrom": "-01:00:00",
          "delayedTo": "-00:30:00",
          "num": 0,
          "percentage": 0
        },
        {
          "delayedFrom": "-00:30:00",
          "delayedTo": "-00:15:00",
          "num": 0,
          "percentage": 0
        },
        {
          "delayedFrom": "-00:15:00",
          "delayedTo": "00:15:00",
          "num": 60,
          "percentage": 0.8
        }
      ],
      "fromUtc": "2025-12-28 07:55",
      "toUtc": "2026-03-28 07:55"
    },
    {
      "airportIcao": "EHAM",
      "class": "FlightAndHour",
      "scheduledHourUtc": 8,
      "medianDelay": "00:00:00",
      "delayPercentiles": [
        {
          "percentile": 5,
          "delay": "00:00:00"
        },
        {
          "percentile": 10,
          "delay": "00:00:00"
        },
        {
          "percentile": 15,
          "delay": "00:00:00"
        },
        {
          "percentile": 20,
          "delay": "00:00:00"
        }
      ],
      "numConsideredFlights": 54,
      "numFlightsDelayedBrackets": [
        {
          "delayedTo": "-02:00:00",
          "num": 0,
          "percentage": 0
        },
        {
          "delayedFrom": "-02:00:00",
          "delayedTo": "-01:00:00",
          "num": 0,
          "percentage": 0
        },
        {
          "delayedFrom": "-01:00:00",
          "delayedTo": "-00:30:00",
          "num": 0,
          "percentage": 0
        }
      ],
      "fromUtc": "2026-02-22 08:10",
      "toUtc": "2026-05-23 08:10"
    }
  ],
  "destinations": [
    {
      "airportIcao": "KJFK",
      "class": "FlightAndHour",
      "scheduledHourUtc": 16,
      "medianDelay": "-00:08:00",
      "delayPercentiles": [
        {
          "percentile": 5,
          "delay": "-00:41:00"
        },
        {
          "percentile": 10,
          "delay": "-00:37:00"
        },
        {
          "percentile": 15,
          "delay": "-00:31:00"
        },
        {
          "percentile": 20,
          "delay": "-00:23:00"
        },
        {
          "percentile": 25,
          "delay": "-00:20:00"
        }
      ],
      "numConsideredFlights": 69,
      "numFlightsDelayedBrackets": [
        {
          "delayedTo": "-02:00:00",
          "num": 0,
          "percentage": 0
        },
        {
          "delayedFrom": "-02:00:00",
          "delayedTo": "-01:00:00",
          "num": 0,
          "percentage": 0
        },
        {
          "delayedFrom": "-01:00:00",
          "delayedTo": "-00:30:00",
          "num": 11,
          "percentage": 0.1594
        },
        {
          "delayedFrom": "-00:30:00",
          "delayedTo": "-00:15:00",
          "num": 14,
          "percentage": 0.2029
        }
      ],
      "fromUtc": "2026-03-10 16:25",
      "toUtc": "2026-06-08 16:25"
    }
  ]
}
    ```
    """
    url = f"https://aerodatabox.p.rapidapi.com/flights/{number}/delays"
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
import os
import requests

def Get_Flight_departure_dates(flightid, fromLocal, toLocal):
    """
    :API_description: This API retrieves an array of consecutive departure dates for a specified flight within an optional date range, typically used for checking flight schedules or availability.
    :param flightid: The flight number identifier then then this field should be Flight number (with or without spaces, IATA or ICAO, any case formats are acceptable, e.g. KL1395, Klm 1395).
    :param fromLocal: The start date for the flight information in local time (e.g., 2023-11-15).
    :param toLocal: The end date for the flight information in local time (e.g., 2023-11-20).
    :note: The duration of the requested period of time should be positive and should not be more than 12 hours in duration.
    :response_schema: 
    ```json
[
  "2025-07-01",
  "2025-07-02",
  "2025-07-03",
  "2025-07-04",
  "2025-07-05",
  "2025-07-06",
  "2025-07-07",
  "2025-07-08",
  "2025-07-09",
  "2025-07-10"
]
```
    """
    url = f"https://aerodatabox.p.rapidapi.com/flights/number/{flightid}/dates/{fromLocal}/{toLocal}"
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

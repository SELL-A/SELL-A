import os
import requests

def Get_single_aircraft(searchBy, searchParam):
    """
    :API_description: Get aircraft (aircraft information by aircraft tail number / registration or 24-bit ICAO Mode-S address)
    :param searchBy: The field to search by (e.g., reg, icao24).
    :param searchParam: The search value for the specified field.Value of the search criteria. If searchBy is: reg: then this field should be aircraft registration (with or without spaces or dashes, any case formats are acceptable, e.g.PH-BXO, DeMhJ);
icao24, then this field should be aircraft ICAO 24-bit Mode-S address specified in hexadecimal format (e.g. 484161, 483EFD).
    :response_schema: 
    ```json
{
  "id": 1,
  "reg": "PH-BXO",
  "active": true,
  "serial": "29599",
  "hexIcao": "48418A",
  "airlineId": "3ea023e6-565d-481e-b23e-15932077d9a7",
  "airlineName": "KLM",
  "iataCodeShort": "73J",
  "iataCodeLong": "B739",
  "model": "737",
  "modelCode": "B737-9K2WIN.",
  "numSeats": 170,
  "rolloutDate": "2001-05-21T00:00:00",
  "firstFlightDate": "2001-06-01T00:00:00",
  "deliveryDate": "2001-06-29T00:00:00",
  "registrationDate": "2001-06-29T00:00:00",
  "typeName": "Boeing 737-900 (winglets)",
  "numEngines": 2,
  "engineType": "Jet",
  "isFreighter": false,
  "productionLine": "Boeing 737 NG",
  "ageYears": 18.2,
  "verified": true
}
```
    """
    url = f"https://aerodatabox.p.rapidapi.com/aircrafts/{searchBy}/{searchParam}"
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

if __name__ == "__main__":
    print(Get_single_aircraft("reg", "VP-BZP"))
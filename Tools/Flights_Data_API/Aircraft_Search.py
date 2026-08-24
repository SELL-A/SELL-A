import os
import requests

def Aircraft_Search(q):
    """
    :API_description: Search Aircraft Tail Numbers By Term (lookup active aircraft tail numbers by term - useful for implmenting auto-complete features)
    :param q: The search term to query for aircraft.
    :response_schema: 
    ```json
{
  "searchBy": "PH-T",
  "count": 5,
  "items": [
    {
      "id": 120,
      "reg": "PH-TCM",
      "active": true,
      "serial": "043",
      "airlineName": "Vliegschool Hilversum",
      "iataCodeShort": "XSR",
      "icaoCode": "SIRA",
      "model": "P2002JF",
      "modelCode": "SIRA",
      "numSeats": 2,
      "typeName": "Tecnam P2002JF Sierra ",
      "numEngines": 1,
      "engineType": "Piston",
      "isFreighter": false,
      "productionLine": "Tecnam P2002",
      "verified": true,
      "numRegistrations": 1
    },
    {
      "id": 748,
      "reg": "PH-TCN",
      "active": true,
      "serial": "1089",
      "hexIcao": "4843C7",
      "airlineName": "Unknown/Private owner",
      "model": "P-180",
      "modelCode": "P180",
      "registrationDate": "2017-03-29",
      "typeName": "Piaggio P.180 Avanti",
      "isFreighter": false,
      "verified": true,
      "numRegistrations": 1
    },
    {
      "id": 20844,
      "reg": "PH-TAX",
      "active": true,
      "serial": "50.C.A.A.009",
      "hexIcao": "486398",
      "airlineName": "Unknown/Private owner",
      "model": "DA50",
      "modelCode": "DA50C",
      "numSeats": 5,
      "deliveryDate": "2021-10-29",
      "typeName": "Diamond DA50RG",
      "isFreighter": false,
      "ageYears": 4.6,
      "verified": true,
      "numRegistrations": 1
    },
    {
      "id": 65450,
      "reg": "PH-TAK",
      "active": true,
      "hexIcao": "4844D9",
      "airlineName": "Unknown/Private owner",
      "typeName": "Diamond DA42",
      "isFreighter": false,
      "verified": false,
      "numRegistrations": 1
    },
    {
      "id": 101691,
      "reg": "PH-TBR",
      "active": true,
      "hexIcao": "484609",
      "airlineName": "Unknown/Private owner",
      "typeName": "North American AT-6A Texan",
      "isFreighter": false,
      "verified": false,
      "numRegistrations": 1
    }
  ]
}
    ```
    """
    url = "https://aerodatabox.p.rapidapi.com/aircrafts/search/term"
    querystring = {"q": q}

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

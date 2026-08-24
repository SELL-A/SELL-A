import os
import requests

def Get_Airport_runways(codeType, code):
    """
    :API_description: Returns: Collection of runway data items.
    :param codeType: The type of airport code,Type of code to search airport by (iata or icao).
    :param code: The airport code value. If codeType is:
    icao, then this field must be a 4-character ICAO-code of the airport (e.g.: EHAM, KLAX, UUEE, etc.);
    iata, then this field must be a 3-character IATA-code of the airport (e.g.: AMS, SFO, LAX, etc.).
    :response_schema: 
    ```json
[
  {
    "name": "04",
    "trueHdg": 41.1,
    "length": {
      "meter": 2022.04,
      "km": 2.02,
      "mile": 1.26,
      "nm": 1.09,
      "feet": 6634
    },
    "width": {
      "meter": 45.11,
      "km": 0.05,
      "mile": 0.03,
      "nm": 0.02,
      "feet": 148
    },
    "isClosed": false,
    "location": {
      "lat": 52.300358,
      "lon": 4.783485
    },
    "surface": "Asphalt",
    "displacedThreshold": {
      "meter": 0,
      "km": 0,
      "mile": 0,
      "nm": 0,
      "feet": 0
    },
    "hasLighting": true
  },
  {
    "name": "06",
    "trueHdg": 57.9,
    "length": {
      "meter": 3439.06,
      "km": 3.44,
      "mile": 2.14,
      "nm": 1.86,
      "feet": 11283
    },
    "width": {
      "meter": 45.11,
      "km": 0.05,
      "mile": 0.03,
      "nm": 0.02,
      "feet": 148
    },
    "isClosed": false,
    "location": {
      "lat": 52.28792,
      "lon": 4.7341533
    },
    "surface": "Asphalt",
    "displacedThreshold": {
      "meter": 250,
      "km": 0.25,
      "mile": 0.16,
      "nm": 0.13,
      "feet": 820.21
    },
    "hasLighting": true
  },
  {
    "name": "09",
    "trueHdg": 86.8,
    "length": {
      "meter": 3446.07,
      "km": 3.45,
      "mile": 2.14,
      "nm": 1.86,
      "feet": 11306
    },
    "width": {
      "meter": 45.11,
      "km": 0.05,
      "mile": 0.03,
      "nm": 0.02,
      "feet": 148
    },
    "isClosed": false,
    "location": {
      "lat": 52.316628,
      "lon": 4.7463284
    },
    "surface": "Asphalt",
    "displacedThreshold": {
      "meter": 89,
      "km": 0.09,
      "mile": 0.06,
      "nm": 0.05,
      "feet": 291.99
    },
    "hasLighting": true
  },
  {
    "name": "18C",
    "trueHdg": 183.2,
    "length": {
      "meter": 3301.9,
      "km": 3.3,
      "mile": 2.05,
      "nm": 1.78,
      "feet": 10833
    },
    "width": {
      "meter": 45.11,
      "km": 0.05,
      "mile": 0.03,
      "nm": 0.02,
      "feet": 148
    },
    "isClosed": false,
    "location": {
      "lat": 52.331394,
      "lon": 4.740041
    },
    "surface": "Asphalt",
    "displacedThreshold": {
      "meter": 0,
      "km": 0,
      "mile": 0,
      "nm": 0,
      "feet": 0
    },
    "hasLighting": true
  },
  {
    "name": "18L",
    "trueHdg": 183.2,
    "length": {
      "meter": 3397.91,
      "km": 3.4,
      "mile": 2.11,
      "nm": 1.83,
      "feet": 11148
    },
    "width": {
      "meter": 45.11,
      "km": 0.05,
      "mile": 0.03,
      "nm": 0.02,
      "feet": 148
    },
    "isClosed": false,
    "location": {
      "lat": 52.321293,
      "lon": 4.7801604
    },
    "surface": "Asphalt",
    "displacedThreshold": {
      "meter": 574,
      "km": 0.57,
      "mile": 0.36,
      "nm": 0.31,
      "feet": 1883.2
    },
    "hasLighting": true
  },
  {
    "name": "18R",
    "trueHdg": 183.2,
    "length": {
      "meter": 3799.94,
      "km": 3.8,
      "mile": 2.36,
      "nm": 2.05,
      "feet": 12467
    },
    "width": {
      "meter": 60.05,
      "km": 0.06,
      "mile": 0.04,
      "nm": 0.03,
      "feet": 197
    },
    "isClosed": false,
    "location": {
      "lat": 52.362667,
      "lon": 4.7119555
    },
    "surface": "Asphalt",
    "displacedThreshold": {
      "meter": 270,
      "km": 0.27,
      "mile": 0.17,
      "nm": 0.15,
      "feet": 885.83
    },
    "hasLighting": true
  },
  {
    "name": "22",
    "trueHdg": 221.1,
    "length": {
      "meter": 2022.04,
      "km": 2.02,
      "mile": 1.26,
      "nm": 1.09,
      "feet": 6634
    },
    "width": {
      "meter": 45.11,
      "km": 0.05,
      "mile": 0.03,
      "nm": 0.02,
      "feet": 148
    },
    "isClosed": false,
    "location": {
      "lat": 52.31404,
      "lon": 4.8030405
    },
    "surface": "Asphalt",
    "displacedThreshold": {
      "meter": 0,
      "km": 0,
      "mile": 0,
      "nm": 0,
      "feet": 0
    },
    "hasLighting": true
  },
  {
    "name": "24",
    "trueHdg": 237.9,
    "length": {
      "meter": 3439.06,
      "km": 3.44,
      "mile": 2.14,
      "nm": 1.86,
      "feet": 11283
    },
    "width": {
      "meter": 45.11,
      "km": 0.05,
      "mile": 0.03,
      "nm": 0.02,
      "feet": 148
    },
    "isClosed": false,
    "location": {
      "lat": 52.304356,
      "lon": 4.776933
    },
    "surface": "Asphalt",
    "displacedThreshold": {
      "meter": 0,
      "km": 0,
      "mile": 0,
      "nm": 0,
      "feet": 0
    },
    "hasLighting": true
  },
  {
    "name": "27",
    "trueHdg": 266.8,
    "length": {
      "meter": 3446.07,
      "km": 3.45,
      "mile": 2.14,
      "nm": 1.86,
      "feet": 11306
    },
    "width": {
      "meter": 45.11,
      "km": 0.05,
      "mile": 0.03,
      "nm": 0.02,
      "feet": 148
    },
    "isClosed": false,
    "location": {
      "lat": 52.31837,
      "lon": 4.7969036
    },
    "surface": "Asphalt",
    "displacedThreshold": {
      "meter": 0,
      "km": 0,
      "mile": 0,
      "nm": 0,
      "feet": 0
    },
    "hasLighting": true
  },
  {
    "name": "36C",
    "trueHdg": 3.2,
    "length": {
      "meter": 3301.9,
      "km": 3.3,
      "mile": 2.05,
      "nm": 1.78,
      "feet": 10833
    },
    "width": {
      "meter": 45.11,
      "km": 0.05,
      "mile": 0.03,
      "nm": 0.02,
      "feet": 148
    },
    "isClosed": false,
    "location": {
      "lat": 52.301777,
      "lon": 4.737321
    },
    "surface": "Asphalt",
    "displacedThreshold": {
      "meter": 450,
      "km": 0.45,
      "mile": 0.28,
      "nm": 0.24,
      "feet": 1476.38
    },
    "hasLighting": true
  },
  {
    "name": "36L",
    "trueHdg": 3.2,
    "length": {
      "meter": 3799.94,
      "km": 3.8,
      "mile": 2.36,
      "nm": 2.05,
      "feet": 12467
    },
    "width": {
      "meter": 60.05,
      "km": 0.06,
      "mile": 0.04,
      "nm": 0.03,
      "feet": 197
    },
    "isClosed": false,
    "location": {
      "lat": 52.328575,
      "lon": 4.70885
    },
    "surface": "Asphalt",
    "displacedThreshold": {
      "meter": 0,
      "km": 0,
      "mile": 0,
      "nm": 0,
      "feet": 0
    },
    "hasLighting": true
  },
  {
    "name": "36R",
    "trueHdg": 3.2,
    "length": {
      "meter": 3397.91,
      "km": 3.4,
      "mile": 2.11,
      "nm": 1.83,
      "feet": 11148
    },
    "width": {
      "meter": 45.11,
      "km": 0.05,
      "mile": 0.03,
      "nm": 0.02,
      "feet": 148
    },
    "isClosed": false,
    "location": {
      "lat": 52.29081,
      "lon": 4.7773438
    },
    "surface": "Asphalt",
    "displacedThreshold": {
      "meter": 0,
      "km": 0,
      "mile": 0,
      "nm": 0,
      "feet": 0
    },
    "hasLighting": true
  }
]
```
    """
    url = f"https://aerodatabox.p.rapidapi.com/airports/{codeType}/{code}/runways"
    headers = {
        "x-rapidapi-key": "9cda500e54mshe688ef1d857bd6bp1f9040jsn59b82e309f42",
        "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
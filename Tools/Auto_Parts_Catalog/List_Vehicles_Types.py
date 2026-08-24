import os
import requests

def List_Vehicles_Types():
    """
    :API_description: Retrieves a list of vehicle types, each identified by a unique integer `id` and categorized by a string `vehicleType`.
    :param None
    :response_schema: 
    ```json
[
  {
    "id": 1,
    "vehicleType": "PC"
  },
  {
    "id": 2,
    "vehicleType": "CV"
  },
  {
    "id": 3,
    "vehicleType": "Motorcycle"
  },
  {
    "id": 4,
    "vehicleType": "LCV"
  },
  {
    "id": 5,
    "vehicleType": "DriverCab"
  },
  {
    "id": 6,
    "vehicleType": "Axle"
  },
  {
    "id": 7,
    "vehicleType": "Engine"
  },
  {
    "id": 8,
    "vehicleType": "Bus"
  },
  {
    "id": 9,
    "vehicleType": "Aftermarket"
  },
  {
    "id": 10,
    "vehicleType": "Tractor"
  },
  {
    "id": 11,
    "vehicleType": "Virtual OEM"
  }
]
```
    """
    url = "https://auto-parts-catalog.p.rapidapi.com/types/list-vehicles-type"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "auto-parts-catalog.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
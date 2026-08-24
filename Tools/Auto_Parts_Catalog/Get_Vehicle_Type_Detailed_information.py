import os
import requests

def Get_Vehicle_Type_Detailed_information(vehicleId, lang_id, country_filter_id, type_id):
    """
    :API_description: Retrieve comprehensive technical specifications of a specific vehicle model, including brand, model type, engine details, and other technical attributes.
    :param vehicleId: The ID of the vehicle model.
    :param lang_id: The language ID for the response.
    :param country_filter_id: The country filter ID to apply.
    :param type_id: The type ID of the vehicle.
    :response_schema: 
    ```json
{
  "vehicleTypeDetails": {
    "manufacturerName": "KIA",
    "modelType": "CEE'D Hatchback (ED)",
    "typeEngineName": "1.6 CRDi 115",
    "constructionIntervalStart": "2006-12-01",
    "constructionIntervalEnd": "2012-12-01",
    "powerKw": "85.0000",
    "powerPs": "115.0000",
    "capacityTax": null,
    "capacityLt": "1.6000",
    "capacityTech": "1582.0000",
    "abs": 0,
    "asr": 0,
    "numberOfCylinders": 4,
    "numberOfValves": 4,
    "bodyType": "Hatchback",
    "engineType": "Diesel",
    "gearType": null,
    "driveType": "Front-Wheel Drive",
    "brakeSystem": null,
    "brakeType": null,
    "fuelType": "Diesel",
    "catalysatorType": "with diesel oxidation catalytic converter",
    "fuelMixture": "Direct Injection",
    "engCodes": "D4FB",
    "engId": 19228
  }
}
    ```
    """
    url = f"https://auto-parts-catalog.p.rapidapi.com/types/type-id/{type_id}/vehicle-type-details/{vehicleId}/lang-id/{lang_id}/country-filter-id/{country_filter_id}"
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
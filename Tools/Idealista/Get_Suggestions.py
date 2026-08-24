import os
import requests

def Get_Suggestions(prefix, location, propertyType, operation):
    """
    :API_description: Retrieve detailed information about geographical locations based on provided criteria.
    :param prefix: The prefix for the property search (e.g., madrid).
    :param location: The location code (e.g., One of the following values: es|pt|it).
    :param propertyType: The type of property (e.g., homes, apartments).
    :param operation: The operation type (e.g., sale, rent).
    :response_schema: 
    ```json
{
  "locations": [
    {
      "name": "Madrid, Madrid",
      "locationId": "0-EU-ES-28-07-001-079",
      "divisible": true,
      "type": "location",
      "suggestedLocationId": 28643,
      "subTypeText": "Municipio",
      "total": 16860
    },
    {
      "name": "Madrid",
      "locationId": "0-EU-ES-28",
      "divisible": true,
      "type": "location",
      "suggestedLocationId": 30090,
      "subTypeText": "Provincia",
      "total": 29706
    },
    {
      "name": "Las Rozas de Madrid, Madrid",
      "locationId": "0-EU-ES-28-02-005-127",
      "divisible": true,
      "type": "location",
      "suggestedLocationId": 24770,
      "subTypeText": "Municipio",
      "total": 491
    },
    {
      "name": "Humanes de Madrid, Madrid",
      "locationId": "0-EU-ES-28-04-008-073",
      "divisible": false,
      "type": "location",
      "suggestedLocationId": 24773,
      "subTypeText": "Municipio",
      "total": 57
    },
    {
      "name": "Zona Avda. de Madrid, Logroño",
      "locationId": "0-EU-ES-26-01-001-089-13",
      "divisible": false,
      "type": "location",
      "suggestedLocationId": 294678,
      "subTypeText": "Distrito",
      "total": 45
    },
    {
      "name": "Avda de Madrid - Pº de la Estación, Jaén",
      "locationId": "0-EU-ES-23-07-001-050-05",
      "divisible": false,
      "type": "location",
      "suggestedLocationId": 33233,
      "subTypeText": "Distrito",
      "total": 36
    },
    {
      "name": "Madridejos, Toledo",
      "locationId": "0-EU-ES-45-08-001-087",
      "divisible": false,
      "type": "location",
      "suggestedLocationId": 29749,
      "subTypeText": "Municipio",
      "total": 40
    },
    {
      "name": "Madridanos, Zamora",
      "locationId": "0-EU-ES-49-02-001-103",
      "divisible": false,
      "type": "location",
      "suggestedLocationId": 25050,
      "subTypeText": "Municipio",
      "total": 1
    },
    {
      "name": "Rivas-Vaciamadrid, Madrid",
      "locationId": "0-EU-ES-28-05-001-123",
      "divisible": true,
      "type": "location",
      "suggestedLocationId": 24837,
      "subTypeText": "Municipio",
      "total": 209
    },
    {
      "name": "Miramadrid, Paracuellos de Jarama",
      "locationId": "0-EU-ES-28-01-016-104-04",
      "divisible": false,
      "type": "location",
      "suggestedLocationId": 31714,
      "subTypeText": "Distrito",
      "total": 36
    }
  ],
  "total": 10
}
```
    """
    url = "https://idealista7.p.rapidapi.com/getsuggestions"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "prefix": prefix,
        "location": location,
        "propertyType": propertyType,
        "operation": operation
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "idealista7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


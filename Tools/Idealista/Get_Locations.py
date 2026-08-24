import os
import requests

def Get_Locations(locationId, location, propertyType, operation):
    """
    :API_description: Retrieve a list of sublocations within Madrid, Spain, categorized by types like 'Comarca' and 'Municipio', including details such as name, identifier, and subtype.
    :param locationId: The ID of the location to retrieve data for(e.g., "0-EU-ES-28").
    :param location: The location code (e.g., One of the following values: es|pt|it).
    :param propertyType: The type of property (e.g., 'homes') Changes the 'total' field which indicates the number of properties of this type. Note: bedrooms only works with rent operation.
    :param operation: The type of operation (e.g., 'sale' ,'').
    :response_schema: 
    ```json
{
  "locations": [
    {
      "name": "Corredor del Henares, Madrid",
      "locationId": "0-EU-ES-28-06",
      "divisible": true,
      "type": "location",
      "suggestedLocationId": 30582,
      "subTypeText": "Comarca",
      "total": 1581
    },
    {
      "name": "Madrid, Madrid",
      "locationId": "0-EU-ES-28-07-001-079",
      "divisible": true,
      "type": "location",
      "suggestedLocationId": 28643,
      "subTypeText": "Municipio",
      "total": 16858
    },
    {
      "name": "Zona noroeste, Madrid",
      "locationId": "0-EU-ES-28-02",
      "divisible": true,
      "type": "location",
      "suggestedLocationId": 30580,
      "subTypeText": "Comarca",
      "total": 3617
    },
    {
      "name": "Zona norte, Madrid",
      "locationId": "0-EU-ES-28-01",
      "divisible": true,
      "type": "location",
      "suggestedLocationId": 30581,
      "subTypeText": "Comarca",
      "total": 2359
    },
    {
      "name": "Zona sur, Madrid",
      "locationId": "0-EU-ES-28-04",
      "divisible": true,
      "type": "location",
      "suggestedLocationId": 30584,
      "subTypeText": "Comarca",
      "total": 3263
    },
    {
      "name": "Zona sureste, Madrid",
      "locationId": "0-EU-ES-28-05",
      "divisible": true,
      "type": "location",
      "suggestedLocationId": 30583,
      "subTypeText": "Comarca",
      "total": 1221
    },
    {
      "name": "Zona suroeste, Madrid",
      "locationId": "0-EU-ES-28-03",
      "divisible": true,
      "type": "location",
      "suggestedLocationId": 30579,
      "subTypeText": "Comarca",
      "total": 803
    }
  ],
  "total": 7
}
```
    """
    url = "https://idealista7.p.rapidapi.com/getlocations"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "locationId": locationId,
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

if __name__ == "__main__":
    print(Get_Locations("0-EU-ES-28", "es", "homes", "sale"))


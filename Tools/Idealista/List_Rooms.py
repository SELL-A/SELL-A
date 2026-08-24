import os
import requests

def List_Rooms(order, locationId, location, locale):
    """
    :API_description: Retrieve detailed listings of rental rooms in Madrid, Spain, including property details, pricing, and amenities.
    :param order: The order in which results are sorted (e.g., relevance) Order by one of the followings: relevance|lowestprice|highestprice|mostrecent|leastrecent|highestpricereduction|lowestpricem2|highestpricem2|biggest|smallest|highestfloors|lowestfloors.
    :param locationId: The unique identifier for the location(e.g., "0-EU-ES-28-07-001-079").
    :param location: The country code for the location ("One of the following values: es|pt|it").
    :param locale: The language locale for the results(e.g., "es").
    :response_schema: 
    ```json
{
  "elementList": [
    {
      "propertyCode": "string",
      "thumbnail": "string",
      "externalReference": "string",
      "numPhotos": "integer",
      "floor": "string",
      "price": "number",
      "priceInfo": {
        "price": {
          "amount": "number",
          "currencySuffix": "string",
          "priceDropInfo": {
            "formerPrice": "number",
            "priceDropValue": "number",
            "priceDropPercentage": "number"
          }
        }
      },
      "propertyType": "string",
      "operation": "string",
      "size": "number",
      "rooms": "integer",
      "bathrooms": "integer",
      "address": "string",
      "province": "string",
      "municipality": "string",
      "district": "string",
      "country": "string",
      "neighborhood": "string",
      "locationId": "string",
      "latitude": "number",
      "longitude": "number",
      "showAddress": "boolean",
      "url": "string",
      "description": "string",
      "hasVideo": "boolean",
      "firstActivationDate": "integer",
      "newDevelopment": "boolean",
      "favourite": "boolean",
      "newProperty": "boolean",
      "tenantNumber": "integer",
      "flatMatesNumber": "integer",
      "tenantGender": "string",
      "multimedia": {
        "images": [
          {
            "url": "string",
            "tag": "string"
          }
        ]
      },
      "contactInfo": {
        "commercialName": "string",
        "phone1": {
          "phoneNumber": "string",
          "formattedPhone": "string",
          "prefix": "string",
          "phoneNumberForMobileDialing": "string",
          "nationalNumber": "boolean"
        },
        "contactName": "string",
        "userType": "string",
        "agencyLogo": "string",
        "contactMethod": "string",
        "micrositeShortName": "string",
        "totalAds": "integer"
      },
      "hasLift": "boolean",
      "isSmokingAllowed": "boolean",
      "priceByArea": "number",
      "features": {
        "hasAirConditioning": "boolean"
      },
      "detailedType": {
        "typology": "string"
      },
      "suggestedTexts": {
        "subtitle": "string",
        "title": "string"
      },
      "hasPlan": "boolean",
      "has3DTour": "boolean",
      "has360": "boolean",
      "hasStaging": "boolean",
      "isOnlineBookingActive": "boolean",
      "ribbons": [
        {
          "name": "string",
          "text": "string"
        }
      ],
      "preferenceHighlight": "boolean",
      "topNewDevelopment": "boolean",
      "topPlus": "boolean",
      "urgentVisualHighlight": "boolean",
      "visualHighlight": "boolean",
      "topHighlight": "boolean"
    }
  ]
}
```
    """
    url = "https://idealista7.p.rapidapi.com/listrooms"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "order": order,
        "locationId": locationId,
        "numPage": 1,
        "maxItems": 30,
        "location": location,
        "locale": locale
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
    print(List_Rooms("relevance", "0-EU-ES-28-07-001-079", "es", "es"))
import os
import requests

def List_Commercial_Properties(order, operation, locationId, location, locale):
    """
    :API_description: Retrieve detailed listings of commercial properties, including property details, pricing, and contact information.
    :param order: The order in which results are sorted (e.g., relevance).
    :param operation: The type of operation (e.g., sale,rent).
    :param locationId: The ID of the location to search within(e.g., "0-EU-ES-28-07-001-079").
    :param location: The country code (e.g., "One of the following values: es|pt|it").
    :param locale: The language code for the response (e.g., en for English).
    :response_schema: 
    ```json
{
  "elementList": [
    {
      "propertyCode": "109656100",
      "thumbnail": "",
      "externalReference": "215664",
      "numPhotos": 27,
      "floor": "bj",
      "price": 490000,
      "priceInfo": {
        "price": {
          "amount": 490000,
          "currencySuffix": "€"
        },
        "mainPrice": "price"
      },
      "propertyType": "premise",
      "operation": "sale",
      "size": 247,
      "bathrooms": 0,
      "address": "Local en Calle de Martínez de la Riva, 13, San Diego, Madrid",
      "province": "Madrid",
      "municipality": "Madrid",
      "district": "Puente de Vallecas",
      "country": "es",
      "neighborhood": "San Diego",
      "locationId": "0-EU-ES-28-07-001-079-13-002",
      "latitude": 40.3951743,
      "longitude": -3.6672687,
      "showAddress": true,
      "url": "https://www.idealista.com/inmueble/109656100/",
      "description": "",
      "hasVideo": true,
      "status": "good",
      "newDevelopment": false,
      "favourite": false,
      "newProperty": false,
      "multimedia": {
        "images": [
          {
            "url": "",
            "tag": "details"
          },
          {
            "url": "",
            "tag": "details"
          }
        ],
        "videos": [
          {
            "url": "https://st3v.idealista.com/20/5a/0c/1382025709.mp4",
            "thumbnail": "https://st3v.idealista.com/20/5a/0c/1382025709.jpg",
            "multimediaId": 1382025709,
            "hasExternalVideoPlayer": false
          }
        ],
        "virtual3DTours": [
          {
            "url": "",
            "thumbnail": "",
            "category": "3d"
          }
        ]
      },
      "contactInfo": {
        "commercialName": "Gilmar Locales e Inversiones",
        "phone1": {
          "phoneNumber": "919386579",
          "formattedPhone": "919 38 65 79",
          "prefix": "34",
          "phoneNumberForMobileDialing": "+34919386579",
          "nationalNumber": true
        },
        "contactName": "locales e inversiones",
        "userType": "professional",
        "agencyLogo": "",
        "contactMethod": "all",
        "micrositeShortName": "gilmar-inversiones",
        "totalAds": 0,
        "needLoginForContact": false,
        "needLoginForPhone": false
      },
      "priceByArea": 1984,
      "features": {
        "hasAirConditioning": false
      },
      "detailedType": {
        "typology": "premise",
        "subTypology": "commercialProperty",
        "transfer": false
      },
      "suggestedTexts": {
        "title": "Local en Calle de Martínez de la Riva, 13, San Diego, Madrid"
      },
      "hasPlan": true,
      "has3DTour": true,
      "has360": false,
      "hasStaging": false,
      "highlight": {
        "groupDescription": "Top"
      },
      "savedAd": {},
      "ribbons": [],
      "ubicationInfo": {
        "key": "onTheStreet",
        "text": "A pie de calle"
      },
      "notes": [],
      "newDevelopmentHighlight": false,
      "topPlus": false,
      "topNewDevelopment": false,
      "preferenceHighlight": false,
      "topHighlight": true,
      "urgentVisualHighlight": false,
      "visualHighlight": false
    }
  ],
  "total": 2196,
  "totalPages": 74,
  "actualPage": 1,
  "itemsPerPage": 30,
  "numPaginations": 0,
  "summary": [
    "Comprar locales o naves en Madrid",
    "Todos los precios",
    "Todos los tamaños"
  ],
  "filter": {
    "locationName": "Madrid"
  },
  "alertName": "Locales o naves en Madrid",
  "totalAppliedFilters": 0,
  "searchTitle": "Madrid",
  "lowerRangePosition": 0,
  "upperRangePosition": 30,
  "paginable": true
}
```
    """
    url = "https://idealista7.p.rapidapi.com/listcommercialproperties"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "order": order,
        "operation": operation,
        "locationId": locationId,
        "maxItems": 30,
        "numPage": 1,
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

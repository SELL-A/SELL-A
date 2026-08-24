import os
import requests

def List_New_Homes(order, operation, locationId, location, locale):
    """
    :API_description: Retrieve a list of new real estate properties for sale in Madrid, Spain, with detailed information including property code, price, location, and multimedia content.
    :param order: The order in which results are sorted (e.g., relevance)Order by one of the followings: relevance|lowestprice|highestprice|mostrecent|leastrecent|highestpricereduction|lowestpricem2|highestpricem2|biggest|smallest|highestfloors|lowestfloors
    Default is relevance.
    :param operation: The type of operation (e.g., sale,rent).
    :param locationId: The ID of the location to search within(e.g., "0-EU-ES-28-07-001-079").
    :param location: The country code of the location ("One of the following values: es|pt|it").
    :param locale: The language locale for the results(e.g., "es").
    :response_schema: 
    ```json
{
  "elementList": [
    {
      "propertyCode": "110934108",
      "thumbnail": "",
      "numPhotos": 47,
      "price": 1750000,
      "priceInfo": {
        "price": {
          "amount": 1750000,
          "currencySuffix": "€"
        }
      },
      "propertyType": "newDevelopment",
      "operation": "sale",
      "address": "Calle Gerda Taro, 9, El Plantío, Madrid",
      "province": "Madrid",
      "municipality": "Madrid",
      "district": "Moncloa",
      "country": "es",
      "neighborhood": "El Plantío",
      "locationId": "0-EU-ES-28-07-001-079-09-006",
      "latitude": 40.4701159,
      "longitude": -3.8218606,
      "showAddress": true,
      "url": "",
      "description": "",
      "hasVideo": false,
      "newDevelopment": true,
      "favourite": false,
      "newProperty": false,
      "multimedia": {
        "images": [
          {
            "url": "",
            "tag": "livingRoom"
          },
          {
            "url": "",
            "tag": "views"
          },
          {
            "url": "",
            "tag": "facade"
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
        "commercialName": "HOMING VILLA",
        "phone1": {
          "phoneNumber": "919388539",
          "formattedPhone": "919 38 85 39",
          "prefix": "34",
          "phoneNumberForMobileDialing": "+34919388539",
          "nationalNumber": true
        },
        "contactName": "Homing Properties",
        "userType": "professional",
        "agencyLogo": "https://st3.idealista.com/95/fe/5f/homing-villa.gif",
        "contactMethod": "all",
        "micrositeShortName": "homing-villa",
        "totalAds": 0,
        "needLoginForContact": false,
        "needLoginForPhone": false
      },
      "newDevelopmentFinished": true,
      "detailedType": {
        "typology": "newDevelopment"
      },
      "suggestedTexts": {
        "description": "Chalets adosados de 4 habitaciones",
        "title": "Calle Gerda Taro, 9, El Plantío, Madrid"
      },
      "isRentToOwn": false,
      "hasPlan": false,
      "has3DTour": true,
      "has360": false,
      "hasStaging": false,
      "promoName": "Homing Villa 19",
      "highlight": {
        "groupDescription": "Top"
      },
      "savedAd": {},
      "ribbons": [
        {
          "name": "newDevelopmentFinished",
          "text": "Obra nueva terminada"
        }
      ],
      "notes": [],
      "topNewDevelopment": true,
      "newDevelopmentHighlight": false,
      "topPlus": false,
      "preferenceHighlight": false,
      "topHighlight": false,
      "urgentVisualHighlight": false,
      "visualHighlight": false
    },
    {
      "propertyCode": "111003192",
      "thumbnail": "",
      "numPhotos": 7,
      "price": 373000,
      "priceInfo": {
        "price": {
          "amount": 373000,
          "currencySuffix": "€"
        }
      },
      "propertyType": "newDevelopment",
      "operation": "sale",
      "address": "Calle de Bustillo del Oro, 22, Berruguete, Madrid",
      "province": "Madrid",
      "municipality": "Madrid",
      "district": "Tetuán",
      "country": "es",
      "neighborhood": "Berruguete",
      "locationId": "0-EU-ES-28-07-001-079-06-006",
      "latitude": 40.4610438,
      "longitude": -3.7077252,
      "showAddress": true,
      "url": "",
      "description": "",
      "hasVideo": false,
      "newDevelopment": true,
      "favourite": false,
      "newProperty": false,
      "multimedia": {
        "images": [
          {
            "url": "",
            "tag": "unknown"
          },
          {
            "url": "",
            "tag": "views"
          }
        ]
      },
      "contactInfo": {
        "commercialName": "ARGIS Living",
        "phone1": {
          "phoneNumber": "919382863",
          "formattedPhone": "919 38 28 63",
          "prefix": "34",
          "phoneNumberForMobileDialing": "+34919382863",
          "nationalNumber": true
        },
        "contactName": "ARGIS",
        "userType": "professional",
        "agencyLogo": "https://st3.idealista.com/49/7e/b3/argis-urban-nature-iii.gif",
        "contactMethod": "all",
        "micrositeShortName": "argis-urban-nature-iii",
        "totalAds": 0,
        "needLoginForContact": false,
        "needLoginForPhone": false
      },
      "newDevelopmentFinished": false,
      "detailedType": {
        "typology": "newDevelopment"
      },
      "suggestedTexts": {
        "description": "Pisos y áticos de 1 habitaciones y locales",
        "title": "Calle de Bustillo del Oro, 22, Berruguete, Madrid"
      },
      "isRentToOwn": false,
      "hasPlan": false,
      "has3DTour": false,
      "has360": false,
      "hasStaging": false,
      "promoName": "ARGIS Urban Nature III",
      "highlight": {
        "groupDescription": "Top"
      },
      "savedAd": {},
      "ribbons": [],
      "notes": [],
      "topNewDevelopment": true,
      "newDevelopmentHighlight": false,
      "topPlus": false,
      "preferenceHighlight": false,
      "topHighlight": false,
      "urgentVisualHighlight": false,
      "visualHighlight": false
    }
  ],
  "total": 253,
  "totalPages": 9,
  "actualPage": 1,
  "itemsPerPage": 30,
  "numPaginations": 0,
  "summary": [
    "Comprar promociones de obra nueva en Madrid",
    "Todos los precios"
  ],
  "filter": {
    "locationName": "Madrid"
  },
  "alertName": "Obra nueva en Madrid",
  "totalAppliedFilters": 0,
  "searchTitle": "Madrid",
  "lowerRangePosition": 0,
  "upperRangePosition": 30,
  "paginable": true
}
```
    """
    url = "https://idealista7.p.rapidapi.com/listnewhomes"
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
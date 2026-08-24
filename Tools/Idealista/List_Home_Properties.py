import os
import requests

def List_Home_Properties(order, operation, locationId, location, locale):
    """
    :API_description: Retrieve detailed listings of flats for sale in Madrid, Spain, with options to filter by various property features and order results by relevance or other criteria.
    :param order: The order in which results are sorted (e.g., relevance).
    :param operation: The type of operation (e.g., sale,rent).
    :param locationId: The ID of the location to search within(e.g., "0-EU-ES-28-07-001-079").
    :param location: The country code of the location(e.g., "es").
    :param locale: The locale for the results(e.g., "es").
    :response_schema: 
    ```json
{
  "elementList": [
    {
      "propertyCode": "111040108",
      "thumbnail": "",
      "externalReference": "PV9692I",
      "numPhotos": 56,
      "price": 1290000,
      "priceInfo": {
        "price": {
          "amount": 1290000,
          "currencySuffix": "€",
          "priceDropInfo": {
            "formerPrice": 1349000,
            "priceDropValue": 59000,
            "priceDropPercentage": 4
          }
        }
      },
      "propertyType": "chalet",
      "operation": "sale",
      "size": 234,
      "rooms": 5,
      "bathrooms": 4,
      "address": "Chalet adosado en Calle Riaza, Aravaca, Madrid",
      "province": "Madrid",
      "municipality": "Madrid",
      "district": "Moncloa",
      "country": "es",
      "neighborhood": "Aravaca",
      "locationId": "0-EU-ES-28-07-001-079-09-007",
      "latitude": 40.4573098,
      "longitude": -3.784414,
      "showAddress": false,
      "url": "",
      "description": "",
      "hasVideo": true,
      "status": "renew",
      "newDevelopment": false,
      "priceDropValue": 59000,
      "dropDate": 1779780983000,
      "favourite": false,
      "newProperty": false,
      "multimedia": {
        "images": [
          {
            "url": "",
            "tag": "garden"
          },
          {
            "url": "",
            "tag": "garden"
          }
        ],
        "videos": [
          {
            "url": "https://st3v.idealista.com/3d/e1/bd/1423650232.mp4",
            "thumbnail": "https://st3v.idealista.com/3d/e1/bd/1423650232.jpg",
            "multimediaId": 1423650232,
            "hasExternalVideoPlayer": false
          }
        ],
        "virtual3DTours": [
          {
            "url": "",
            "thumbnail": "",
            "category": "3d"
          }
        ],
        "homestagings": [
          {
            "original": {
              "url": "",
              "tag": "livingRoom",
              "localizedName": "Salón",
              "multimediaId": 1423716921
            },
            "rendered": {
              "url": "",
              "tag": "livingRoom",
              "localizedName": "Salón",
              "multimediaId": 1434044215
            }
          }
        ]
      },
      "contactInfo": {
        "commercialName": "Promora Aravaca",
        "phone1": {
          "phoneNumber": "919385884",
          "formattedPhone": "919 38 58 84",
          "prefix": "34",
          "phoneNumberForMobileDialing": "+34919385884",
          "nationalNumber": true
        },
        "contactName": "Promora Aravaca",
        "userType": "professional",
        "agencyLogo": "https://st3.idealista.com/37/6e/75/promoraaravaca.gif",
        "contactMethod": "all",
        "micrositeShortName": "promoraaravaca",
        "totalAds": 0,
        "needLoginForContact": false,
        "needLoginForPhone": false
      },
      "parkingSpace": {
        "hasParkingSpace": true,
        "isParkingSpaceIncludedInPrice": true
      },
      "priceDropPercentage": 4,
      "priceByArea": 5513,
      "features": {
        "hasAirConditioning": true,
        "hasBoxRoom": false
      },
      "detailedType": {
        "typology": "chalet",
        "subTypology": "terracedHouse"
      },
      "suggestedTexts": {
        "title": "Chalet adosado en Calle Riaza, Aravaca, Madrid"
      },
      "hasPlan": true,
      "has3DTour": true,
      "has360": false,
      "hasStaging": true,
      "highlight": {
        "groupDescription": "Top+"
      },
      "savedAd": {},
      "ribbons": [],
      "notes": [],
      "preferenceHighlight": false,
      "topHighlight": false,
      "topNewDevelopment": false,
      "newDevelopmentHighlight": false,
      "topPlus": true,
      "urgentVisualHighlight": false,
      "visualHighlight": false
    }
  ],
  "total": 16861,
  "totalPages": 563,
  "actualPage": 1,
  "itemsPerPage": 30,
  "numPaginations": 0,
  "summary": [
    "Comprar casas y pisos en Madrid",
    "Todos los precios",
    "Todos los tamaños"
  ],
  "filter": {
    "locationName": "Madrid"
  },
  "alertName": "Viviendas en Madrid",
  "totalAppliedFilters": 0,
  "searchTitle": "Madrid",
  "geoReach": {
    "allowed": true,
    "listingPosition": 14
  },
  "upperRangePosition": 30,
  "lowerRangePosition": 0,
  "paginable": true
}
    ```
    """
    url = "https://idealista7.p.rapidapi.com/listhomes"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "order": order,
        "operation": operation,
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
import os
import requests

def properties_v2_list(locationValue, locationIdentifier, sortOrder, page):
    """
    :API_description: Retrieve a detailed list of residential property listings for sale in Oxford, Oxfordshire, including property addresses, agent details, pricing, and images.
    :param locationValue: The name of the location to search properties in(e.g., Oxford, Oxfordshire). he value of geoLabel field returned in auto-complete endpoint with listings as search_type.
    :param locationIdentifier: A unique identifier for the location.(e.g., "Oxford")The value of geoIdentifier field returned in auto-complete endpoint with listings as search_type.
    :param sortOrder: The order in which to sort the listings (e.g., 'newest_listings').
    :param page: The page number for paginated results(default 1).
    :response_schema: 
    ```json
{
  "success": true,
  "data": {
    "analyticsTaxonomy": {
      "activity": "listing_search",
      "areaName": "Oxford",
      "bedsMax": null,
      "bedsMin": null,
      "brand": "zoopla",
      "countryCode": "",
      "countyAreaName": "Oxfordshire",
      "currencyCode": "",
      "expandedResultsCount": 0,
      "geoIdentifier": "oxford",
      "listingsCategory": "residential",
      "outcode": "",
      "outcodes": [],
      "page": "/for-sale/results/",
      "postalArea": "",
      "priceMax": null,
      "priceMin": null,
      "radius": null,
      "regionName": "South East England",
      "resultsSort": "newest_listings",
      "searchGuid": "",
      "searchIdentifier": "db054e4d42587bf8ea29fd6a7d8923d443756983e189c845bfed0693a4d61804",
      "searchLocation": null,
      "searchResultsCount": 0,
      "section": "for-sale",
      "totalResults": 0,
      "url": "/api/search/mobile/?version=v2&category=residential&page=1&location.identifier=oxford&location.value=Oxford%2C+Oxfordshire&section=for-sale&sortOrder=newest_listings&chainFree=true&reducedPriceOnly=true&includeRetirementHomes=true&includeSharedOwnership=true&includeSold=true&isAuction=true&includeSharedAccommodation=true&includeRented=true&billsIncluded=true&petsAllowed=true&newHomes=exclude&excludeRadius=true&furnishedState=Any",
      "viewType": "List"
    },
    "listings": {
      "regular": [],
      "extended": null,
      "featured": null
    },
    "geoData": {
      "polygon": {
        "coordinates": [
          [
            [
              -1.33105,
              51.72861
            ],
            [
              -1.30843,
              51.73172
            ],
            [
              -1.29843,
              51.73606
            ],
            [
              -1.27215,
              51.72711
            ],
            [
              -1.2711,
              51.72568
            ],
            [
              -1.27942,
              51.72264
            ],
            [
              -1.27743,
              51.72079
            ],
            [
              -1.26553,
              51.72067
            ],
            [
              -1.25489,
              51.71717
            ],
            [
              -1.25137,
              51.71122
            ],
            [
              -1.24176,
              51.70633
            ],
            [
              -1.21704,
              51.70654
            ],
            [
              -1.19953,
              51.70377
            ],
            [
              -1.1906,
              51.70761
            ],
            [
              -1.19338,
              51.71404
            ],
            [
              -1.16801,
              51.72988
            ],
            [
              -1.16634,
              51.74583
            ],
            [
              -1.17756,
              51.75759
            ],
            [
              -1.17718,
              51.76319
            ],
            [
              -1.19061,
              51.76992
            ],
            [
              -1.23146,
              51.77567
            ],
            [
              -1.25104,
              51.78363
            ],
            [
              -1.26004,
              51.79413
            ],
            [
              -1.2718,
              51.79688
            ],
            [
              -1.27371,
              51.79504
            ],
            [
              -1.27621,
              51.79769
            ],
            [
              -1.28759,
              51.80025
            ],
            [
              -1.29617,
              51.79961
            ],
            [
              -1.29617,
              51.79388
            ],
            [
              -1.29239,
              51.78814
            ],
            [
              -1.30407,
              51.77859
            ],
            [
              -1.30407,
              51.77391
            ],
            [
              -1.3003,
              51.76462
            ],
            [
              -1.30478,
              51.76774
            ],
            [
              -1.31474,
              51.76413
            ],
            [
              -1.31611,
              51.75903
            ],
            [
              -1.30794,
              51.75333
            ],
            [
              -1.3162,
              51.75023
            ],
            [
              -1.31985,
              51.75125
            ],
            [
              -1.32459,
              51.7474
            ],
            [
              -1.32093,
              51.7455
            ],
            [
              -1.3306,
              51.73909
            ],
            [
              -1.33105,
              51.72861
            ]
          ]
        ],
        "type": "Polygon"
      },
      "polyenc": [],
      "radius": null,
      "geoIdentifier": "oxford",
      "geoType": "post_town",
      "coordinates": [
        -1.22692587247685,
        51.7477879344573
      ],
      "label": "Oxford"
    },
    "pagination": {
      "totalResults": 0,
      "totalResultsWasLimited": false
    }
  }
}
    """
    url = "https://zoopla.p.rapidapi.com/properties/v2/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "locationValue": locationValue,
        "locationIdentifier": locationIdentifier,
        "sortOrder": sortOrder,
        "page": page
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "zoopla.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


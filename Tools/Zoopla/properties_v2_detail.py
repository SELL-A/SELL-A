import os
import requests

def properties_v2_detail(listingId):
    """
    :API_description: Retrieve detailed information about a specific property listing, including its description, pricing, and associated metadata.
    :param listingId: The unique identifier for the property listing(The value of listingId field returned in properties_v2_list endpoint).
    :response_schema: 
    ```json
{
  "data": {
    "listingDetails": {
      "listingId": "64576476",
      "administrationFees": null,
      "analyticsTaxonomy": {
        "areaName": "Marston, Oxford",
        "bedsMax": 4,
        "bedsMin": 4,
        "branchId": 13802,
        "branchLogoUrl": "https://st.zoocdn.com/zoopla_static_agent_logo_(487497).png",
        "branchName": "Chancellors - Headington",
        "brandName": "Chancellors",
        "chainFree": true,
        "companyId": 688,
        "countryCode": "gb",
        "countyAreaName": "Oxfordshire",
        "currencyCode": "GBP",
        "displayAddress": "Old Marston, Oxford OX3",
        "furnishedState": "",
        "groupId": 155,
        "hasEpc": true,
        "hasFloorplan": true,
        "incode": "0QS",
        "isRetirementHome": false,
        "isSharedOwnership": false,
        "listingCondition": "pre-owned",
        "listingId": 64576476,
        "listingsCategory": "residential",
        "listingStatus": "sold",
        "location": "Marston",
        "memberType": "agent",
        "numBaths": 2,
        "numBeds": 4,
        "numImages": 10,
        "numRecepts": 2,
        "outcode": "OX3",
        "postalArea": "OX",
        "postTownName": "Oxford",
        "priceActual": 480000,
        "price": 480000,
        "priceMax": 500000,
        "priceMin": 475000,
        "priceQualifier": "offers_over",
        "propertyHighlight": "",
        "propertyType": "detached",
        "regionName": "South East England",
        "section": "for-sale",
        "sizeSqFeet": "1722",
        "tenure": "freehold",
        "uuid": "bc71a7fa-07af-4e5f-8f6f-dbb8a5c70f2f",
        "zindex": 357343
      },
      "tenure": "freehold",
      "detailedDescription": "",
      "metaTitle": "Old Marston, Oxford OX3, 4 bed detached house for sale, £480,000 - Zoopla",
      "metaDescription": "",
      "category": "residential",
      "listingUris": {
        "detail": "/for-sale/details/64576476/",
        "contact": "/for-sale/contact/64576476/"
      },
      "title": "4 bed detached house for sale",
      "publicationStatus": "Expired",
      "ingested": null,
      "counts": {
        "numBedrooms": 4,
        "numBathrooms": 2,
        "numLivingRooms": 2
      },
      "viewCount": {
        "viewCount30day": 0
      },
      "ntsInfo": [
        {
          "title": "Tenure",
          "key": "tenure",
          "value": "Freehold",
          "description": ""
        }
      ],
      "additionalNtsInfo": [
        {
          "title": "Water",
          "key": "water",
          "value": "Ask agent",
          "description": ""
        }
      ],
      "derivedEPC": {
        "efficiencyRating": "D"
      },
      "derived": {
        "buyerIncentives": null
      },
      "branchV2": {
        "branchDetailsUri": "/find-agents/branch/chancellors-headington-oxford-13802/",
        "branchId": 13802,
        "branchName": "Chancellors - Headington",
        "isDeveloper": null,
        "logoUrl": "https://st.zoocdn.com/zoopla_static_agent_logo_(487497).png",
        "redirectPhone": "01865 680525",
        "redirectLettingsPhone": "01865 360073"
      },
      "adTargeting": {
        "areaName": "Marston, Oxford",
        "bedsMax": 4,
        "bedsMin": 4,
        "branchId": 13802,
        "branchLogoUrl": "https://st.zoocdn.com/zoopla_static_agent_logo_(487497).png",
        "branchName": "Chancellors - Headington",
        "brandName": "Chancellors",
        "chainFree": true,
        "companyId": 688,
        "countryCode": "gb",
        "countyAreaName": "Oxfordshire",
        "currencyCode": "GBP",
        "displayAddress": "Old Marston, Oxford OX3",
        "furnishedState": "",
        "groupId": 155,
        "hasEpc": true,
        "hasFloorplan": true,
        "incode": "0QS",
        "isRetirementHome": false,
        "isSharedOwnership": false,
        "listingCondition": "pre-owned",
        "listingId": 64576476,
        "listingsCategory": "residential",
        "listingStatus": "sold",
        "location": "Marston",
        "memberType": "agent",
        "numBaths": 2,
        "numBeds": 4,
        "numImages": 10,
        "numRecepts": 2,
        "outcode": "OX3",
        "postalArea": "OX",
        "postTownName": "Oxford",
        "priceActual": 480000,
        "price": 480000,
        "priceMax": 500000,
        "priceMin": 475000,
        "priceQualifier": "offers_over",
        "propertyHighlight": "",
        "propertyType": "detached",
        "regionName": "South East England",
        "section": "for-sale",
        "sizeSqFeet": "1722",
        "tenure": "freehold",
        "uuid": "bc71a7fa-07af-4e5f-8f6f-dbb8a5c70f2f",
        "zindex": 357343
      },
      "analyticsEcommerce": {
        "brand": "Chancellors",
        "category": "for-sale/resi/agent/pre-owned/gb",
        "id": 64576476,
        "name": "FS_Contact",
        "price": 1,
        "quantity": 1,
        "variant": "premium"
      },
      "pricing": {
        "isAuction": false,
        "qualifier": "offers_over",
        "priceQualifierLabel": "Offers over",
        "internalValue": 480000,
        "rentFrequencyLabel": null,
        "valueLabel": "£480,000",
        "currencyCode": "GBP",
        "originalCurrencyPrice": null,
        "pricePerFloorAreaUnit": {
          "internalValue": 279,
          "rentFrequencyLabel": null,
          "unitsLabel": "sq. ft",
          "label": "£279/sq. ft",
          "valueLabel": "£279",
          "currencyCode": null
        },
        "alternateRentFrequencyPrice": null,
        "label": "£480,000"
      },
      "epc": {
        "image": [
          {
            "caption": "EPC",
            "filename": "e7fba7614450e1592afe8e9ba5ac7fcaaeda74be.jpg"
          }
        ],
        "pdf": null
      },
      "features": {
        "bullets": [
          "Sold with no onward chain",
          "Driveway parking",
          "Single garage",
          "Two shower rooms",
          "Two reception rooms",
          "Well presented throughout",
          "Photos were taken pre-tenancy"
        ],
        "flags": {
          "furnishedState": null,
          "studentFriendly": false,
          "tenure": {
            "name": "freehold",
            "label": "Freehold"
          },
          "availableFromDate": null
        },
        "highlights": null
      },
      "floorPlan": {
        "image": [
          {
            "filename": "622cd5d507f149743e6ba8a8c6a0f4b9e7329405.png",
            "caption": "Floor Plan"
          }
        ],
        "links": null,
        "pdf": null
      },
      "floorArea": {
        "label": "1,722 sq. ft",
        "range": null,
        "units": "sq_feet",
        "unitsLabel": "sq. ft",
        "value": 1722
      },
      "content": {
        "virtualTour": null,
        "floorPlan": [
          {
            "original": "https://lc.zoocdn.com/622cd5d507f149743e6ba8a8c6a0f4b9e7329405.png",
            "caption": "Floor Plan",
            "url": null,
            "filename": "622cd5d507f149743e6ba8a8c6a0f4b9e7329405.png",
            "type": "floor_plan"
          }
        ],
        "audioTour": null
      },
      "propertyImage": [
        {
          "original": "https://lc.zoocdn.com/f5b74099ede8b5afaf014a3e9bbf0952544efc7d.jpg",
          "caption": "External Front",
          "url": null,
          "filename": "f5b74099ede8b5afaf014a3e9bbf0952544efc7d.jpg",
          "type": "property_image"
        }
      ],
      "additionalLinks": [
        {
          "original": "https://www.chancellors.co.uk/properties/r/5006534?utm_source=Marketing&utm_medium=Web&utm_campaign=Sales",
          "caption": "More Details From Chancellors",
          "url": null,
          "filename": null,
          "type": "document"
        }
      ],
      "location": {
        "coordinates": {
          "isApproximate": false,
          "latitude": 51.777378,
          "longitude": -1.23808
        },
        "postalCode": "OX3 0QS",
        "streetName": "Old Marston",
        "countryCode": "GB",
        "propertyNumberOrName": "14 HARLOW WAY",
        "townOrCity": "Oxford",
        "uprn": "100120820763"
      },
      "embeddedContent": {
        "videos": null,
        "tours": null,
        "links": null
      },
      "pointsOfInterest": [
        {
          "title": "Meadowbrook College",
          "address": "The Harlow Centre, Raymund Road, Old Marston",
          "type": "uk_school_primary_and_secondary",
          "latitude": 51.771549,
          "longitude": -1.240355,
          "distanceMiles": 0.4
        }
      ],
      "priceHistory": {
        "firstPublished": null,
        "priceChanges": null
      },
      "displayAddress": "Old Marston, Oxford OX3",
      "section": "for-sale",
      "branch": {
        "logoUrl": "https://st.zoocdn.com/zoopla_static_agent_logo_(487497).png",
        "name": "Chancellors - Headington"
      },
      "featurePreview": [
        {
          "iconId": "bed",
          "content": 4
        }
      ],
      "imagePreview": {
        "caption": "External Front",
        "src": "https://lid.zoocdn.com/645/430/f5b74099ede8b5afaf014a3e9bbf0952544efc7d.jpg"
      },
      "tags": [
        {
          "label": "Chain free"
        },
        {
          "label": "Freehold"
        }
      ],
      "transports": [
        {
          "distanceInMiles": 3.3,
          "poiType": "national_rail_station",
          "title": "Islip"
        }
      ],
      "publishedOn": "2023-05-09T10:56:52",
      "numberOfImages": 10,
      "statusSummary": {
        "label": "Sold subject to contract"
      },
      "staticWidgets": []
    }
  },
  "extensions": {
    "requestId": "4314019b-77e4-4efa-bc8e-bea92efef22d"
  }
}
    """
    url = "https://zoopla.p.rapidapi.com/properties/v2/detail"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"listingId": listingId}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "zoopla.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
import os
import requests

def Business_Details(business_id, region):
    """
    :API_description: Retrieves comprehensive business profile information from Google Maps or Google Business, including contact details, operational hours, location data, reviews, and photos.
    :param business_id: The unique identifier for the business.
    :param region: The region where the business is located(e.g., "us").
    :response_schema: 
    ```json
{
  "status": "OK",
  "request_id": "03022853-2e6c-45c3-8786-4377b83d9ade",
  "parameters": {
    "business_id": "0x880fd393d427a591:0x8cba02d713a995ed",
    "language": "en",
    "region": "us",
    "coordinates": "37.09024,-95.712891",
    "extract_emails_and_contacts": true,
    "extract_share_link": false
  },
  "data": [
    {
      "business_id": "0x880fd393d427a591:0x8cba02d713a995ed",
      "google_id": "0x880fd393d427a591:0x8cba02d713a995ed",
      "place_id": "ChIJkaUn1JPTD4gR7ZWpE9cCuow",
      "google_mid": "/g/11hzfpv2st",
      "phone_number": "+17732196071",
      "name": "Rescue Plumbing",
      "latitude": 41.9214708,
      "longitude": -87.6574208,
      "full_address": "Rescue Plumbing, 1137 W Webster Ave, Chicago, IL 60614",
      "review_count": 1534,
      "rating": 4.9,
      "timezone": "America/Chicago",
      "opening_status": "Open 24 hours",
      "working_hours": {
        "Monday": [
          "Open 24 hours"
        ],
        "Tuesday": [
          "Open 24 hours"
        ],
        "Wednesday": [
          "Open 24 hours"
        ],
        "Thursday": [
          "Open 24 hours"
        ],
        "Friday": [
          "Open 24 hours"
        ],
        "Saturday": [
          "Open 24 hours"
        ],
        "Sunday": [
          "Open 24 hours"
        ]
      },
      "opening_date": null,
      "website": "https://www.myrescueplumbing.com",
      "tld": "myrescueplumbing.com",
      "verified": true,
      "place_link": "...",
      "cid": "10140420633749198317",
      "reviews_link": "...",
      "owner_id": "115585709876694632889",
      "owner_link": "...",
      "owner_name": "Rescue Plumbing",
      "booking_link": "...",
      "reservations_link": null,
      "business_status": "OPEN",
      "type": "Plumber",
      "subtypes": [
        "Plumber",
        "Drainage service"
      ],
      "photos_sample": [
        {
          "photo_id": "CIHM0ogKEICAgICyt5TI2AE",
          "photo_url": "...",
          "photo_url_large": "...",
          "video_thumbnail_url": null,
          "latitude": 41.921224699999996,
          "longitude": -87.65736620000001,
          "type": "photo",
          "photo_datetime_utc": "2021-03-16T00:00:00.000Z",
          "photo_timestamp": 1615852800
        }
      ],
      "global_plus_code": "86HJW8CV+H2",
      "compound_plus_code": "W8CV+H2 Chicago, Illinois",
      "reviews_per_rating": {
        "1": 38,
        "2": 10,
        "3": 9,
        "4": 13,
        "5": 1464
      },
      "photo_count": 1622,
      "about": {
        "summary": "Here at Rescue Plumbing, we strive to set a new standard of professionalism!",
        "details": null
      },
      "address": "1137 W Webster Ave, Chicago, IL 60614",
      "menu_link": null,
      "order_link": null,
      "price_level": null,
      "district": "Sheffield Neighbors",
      "street_address": "1137 W Webster Ave",
      "city": "Chicago",
      "zipcode": "60614",
      "state": "Illinois",
      "country": "US",
      "business_services": {
        "Plumber": [
          "Drain cleaning",
          "Faucet installation",
          "Faucet repair"
        ]
      },
      "posts_sample": [
        {
          "post_id": "CIHM0ogKEJ3IopjQ0qfeygE",
          "post_link": "...",
          "post_datetime_utc": "2026-05-28T22:08:07.000Z",
          "post_timestamp": 1780006087,
          "post_text": "Under Sink Valve Repair & Plumbing Service",
          "post_links": [
            {
              "url": "https://www.myrescueplumbing.com/plumbing-services/leak-repair/",
              "caption": "Learn more"
            }
          ],
          "post_photos": [
            "..."
          ]
        }
      ],
      "posts_link": "...",
      "emails_and_contacts": null,
      "requested_business_id": "0x880fd393d427a591:0x8cba02d713a995ed"
    }
  ]
}
    ```
    """
    url = "https://api.openwebninja.com/local-business-data/business-details"

    querystring = {
        "business_id": business_id,
        "region": region
    }

    headers = {
        "X-API-Key": "ak_2a42z3zdrr3rnxcapzcpfplyqqohqtgk8n0rsxjtvftpre3"
        }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

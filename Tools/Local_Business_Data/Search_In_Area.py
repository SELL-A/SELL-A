import os
import requests

def Search_In_Area(query, lat, lng, zoom):
    """
    :API_description: This API performs a keyword-based search for locations within a specified geographic area, with optional biasing towards a central coordinate point.
    :param query: The search query for the local business.
    :param lat: The latitude of the area to search in.
    :param lng: The longitude of the area to search in.
    :param zoom: The zoom level for the search area.
    :response_schema: 
    ```json
{
  "status": "OK",
  "request_id": "48778e41-dcbf-4f93-ae16-f139d6d8ce49",
  "parameters": {
    "query": "pizza",
    "language": "en",
    "region": "us",
    "lat": 37.359428,
    "lng": -121.925337,
    "zoom": 13,
    "limit": 20,
    "extract_emails_and_contacts": false
  },
  "data": [
    {
      "business_id": "0x808fcdf48ffa61f3:0xab7236e6429eb4c9",
      "google_id": "0x808fcdf48ffa61f3:0xab7236e6429eb4c9",
      "place_id": "ChIJ82H6j_TNj4ARybSeQuY2cqs",
      "google_mid": "/g/11l1h5r4gl",
      "phone_number": "+16694994800",
      "name": "Mountain Mike's Pizza",
      "latitude": 37.335961499999996,
      "longitude": -121.8878108,
      "full_address": "Mountain Mike's Pizza, 29 S Third St, San Jose, CA 95113",
      "review_count": 96,
      "rating": 4.1,
      "timezone": "America/Los_Angeles",
      "opening_status": "Open · Closes 4 AM · Reopens 9 AM",
      "working_hours": {
        "Thursday": [
          "9 AM–4 AM"
        ],
        "Friday": [
          "9 AM–4 AM"
        ],
        "Saturday": [
          "9 AM–4 AM"
        ],
        "Sunday": [
          "9 AM–4 AM"
        ],
        "Monday": [
          "9 AM–4 AM"
        ],
        "Tuesday": [
          "9 AM–4 AM"
        ],
        "Wednesday": [
          "9 AM–4 AM"
        ]
      },
      "opening_date": null,
      "website": "...",
      "tld": "mountainmikespizza.com",
      "verified": true,
      "place_link": "...",
      "cid": "...",
      "reviews_link": "...",
      "owner_id": "...",
      "owner_link": "...",
      "owner_name": "Mountain Mike's Pizza",
      "booking_link": "...",
      "reservations_link": null,
      "business_status": "OPEN",
      "type": "Pizza restaurant",
      "subtypes": [
        "Pizza restaurant",
        "Buffet restaurant",
        "Chicken wings restaurant",
        "Family restaurant",
        "Pizza delivery",
        "Pizza Takeout"
      ],
      "subtype_gcids": [
        "pizza_restaurant",
        "buffet_restaurant",
        "chicken_wings_restaurant",
        "deliveries",
        "eatery"
      ],
      "photos_sample": [
        {
          "photo_id": "...",
          "photo_url": "...",
          "photo_url_large": "...",
          "video_thumbnail_url": null,
          "latitude": 37.3363569,
          "longitude": -121.8878962,
          "type": "photo",
          "photo_datetime_utc": "2023-05-27T00:00:00.000Z",
          "photo_timestamp": 1685145600
        }
      ],
      "reviews_per_rating": {
        "1": 16,
        "2": 1,
        "3": 6,
        "4": 8,
        "5": 65
      },
      "photo_count": 248,
      "about": {
        "summary": "Casual pizza chain featuring traditional pies, gluten-free crust & assorted appetizers.",
        "details": {
          "Accessibility": {
            "Wheelchair accessible entrance": true,
            "Wheelchair accessible parking lot": true,
            "Wheelchair accessible restroom": true,
            "Wheelchair accessible seating": true
          }
        }
      },
      "address": "29 S Third St, San Jose, CA 95113",
      "order_link": "...",
      "price_level": "$20–30",
      "district": "Central San Jose",
      "street_address": "29 S Third St",
      "city": "San Jose",
      "zipcode": "95113",
      "state": "California",
      "country": "US",
      "hotel_price_for_dates": "Family-friendly pizzeria chain"
    },
    {
      "business_id": "0x808fcd00229637f1:0xbfe5bdb6b39d5c65",
      "google_id": "0x808fcd00229637f1:0xbfe5bdb6b39d5c65",
      "place_id": "ChIJ8TeWIgDNj4ARZVyds7a95b8",
      "google_mid": "/g/11yp5cph5s",
      "phone_number": "+16692928620",
      "name": "PIZZETTA",
      "latitude": 37.3551284,
      "longitude": -121.8880624,
      "full_address": "PIZZETTA, 703 N 13th St, San Jose, CA 95112",
      "review_count": 12,
      "rating": 5,
      "timezone": "America/Los_Angeles",
      "opening_status": "Closed · Opens 6 PM",
      "working_hours": {
        "Friday": [
          "6–11:30 PM"
        ],
        "Saturday": [
          "6–11:30 PM"
        ],
        "Sunday": [
          "6–11:30 PM"
        ],
        "Monday": [
          "Closed"
        ],
        "Tuesday": [
          "5:30–11:30 PM"
        ],
        "Wednesday": [
          "6–11:30 PM"
        ],
        "Thursday": [
          "6–11:30 PM"
        ]
      },
      "opening_date": null,
      "website": null,
      "verified": true,
      "place_link": "...",
      "cid": "...",
      "reviews_link": "...",
      "owner_id": "100087767235817751002",
      "owner_link": "...",
      "owner_name": "PIZZETTA",
      "booking_link": null,
      "reservations_link": null,
      "business_status": "OPEN",
      "type": "Pizza restaurant",
      "subtypes": [
        "Pizza restaurant"
      ],
      "subtype_gcids": [
        "pizza_restaurant",
        "eatery",
        "establishment",
        "establishment_poi"
      ],
      "photos_sample": [
        {
          "photo_id": "...",
          "photo_url": "...",
          "photo_url_large": "...",
          "video_thumbnail_url": null,
          "latitude": 37.3552295,
          "longitude": -121.88792129999999,
          "type": "photo",
          "photo_datetime_utc": "2026-01-21T00:00:00.000Z",
          "photo_timestamp": 1768953600
        }
      ],
      "reviews_per_rating": {
        "1": 0,
        "2": 0,
        "3": 0,
        "4": 0,
        "5": 12
      },
      "photo_count": 10,
      "about": {
        "summary": null,
        "details": {
          "Accessibility": {
            "Wheelchair accessible entrance": true,
            "Wheelchair accessible parking lot": true
          }
        }
      },
      "address": "703 N 13th St, San Jose, CA 95112",
      "order_link": null,
      "price_level": "$10–20",
      "district": "Central San Jose",
      "street_address": "703 N 13th St",
      "city": "San Jose",
      "zipcode": "95112",
      "state": "California",
      "country": "US"
    }
  ]
}
```
    """
    url = "https://api.openwebninja.com/local-business-data/search-in-area"
    querystring = {
        "query": query,
        "lat": lat,
        "lng": lng,
        "zoom": zoom
    }
    headers = {
        "X-API-Key": "ak_2a42z3zdrr3rnxcapzcpfplyqqohqtgk8n0rsxjtvftpre3"
        }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
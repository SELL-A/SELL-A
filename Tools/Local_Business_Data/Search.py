import os
import requests

def Search(query):
    """
    :API_description: This API performs location-based searches using a query string, with optional parameters to bias results towards specific geographic coordinates or regions.
    :param query: The search term for the local business.
    :response_schema: 
    ```json
{
  "status": "OK",
  "request_id": "...",
  "parameters": {
    "query": "Hotels in San Francisco, USA",
    "language": "en",
    "region": "us",
    "lat": 37.359428,
    "lng": -121.925337,
    "zoom": 13,
    "limit": 2,
    "offset": 0,
    "extract_emails_and_contacts": false
  },
  "data": [
    {
      "business_id": "0x8085808636673e71:0xebc2cf7c5bf2d655",
      "google_id": "0x8085808636673e71:0xebc2cf7c5bf2d655",
      "place_id": "ChIJcT5nNoaAhYARVdbyW3zPwus",
      "google_mid": "/m/03c9s02",
      "phone_number": "+14158961600",
      "name": "San Francisco Marriott Marquis",
      "latitude": 37.7853366,
      "longitude": -122.40440679999999,
      "full_address": "San Francisco Marriott Marquis, 780 Mission St, San Francisco, CA 94103",
      "review_count": 10190,
      "rating": 4.3,
      "timezone": "America/Los_Angeles",
      "opening_status": null,
      "working_hours": {},
      "website": "...",
      "tld": "marriott.com",
      "verified": true,
      "place_link": "...",
      "cid": "16988368877420467797",
      "reviews_link": "...",
      "owner_id": "116211684039937392083",
      "owner_link": "...",
      "owner_name": "San Francisco Marriott Marquis",
      "booking_link": null,
      "reservations_link": null,
      "business_status": "OPEN",
      "type": "Hotel",
      "subtypes": [
        "Hotel",
        "Meeting planning service",
        "Wedding venue"
      ],
      "subtype_gcids": [
        "hotel",
        "business_related",
        "business_service"
      ],
      "photos_sample": [
        {
          "photo_id": "CIABIhD-NLnkxkDZDB_gfiFg7Owi",
          "photo_url": "...",
          "photo_url_large": "...",
          "video_thumbnail_url": null,
          "latitude": 37.7848997,
          "longitude": -122.4038217,
          "type": "photo",
          "photo_datetime_utc": "2026-04-07T00:00:00.000Z",
          "photo_timestamp": 1775520000
        }
      ],
      "reviews_per_rating": {
        "1": 408,
        "2": 233,
        "3": 791,
        "4": 2945,
        "5": 5813
      },
      "photo_count": 15971,
      "about": {
        "summary": "...",
        "details": null
      },
      "address": "780 Mission St, San Francisco, CA 94103",
      "order_link": null,
      "price_level": null,
      "district": "SoMa",
      "street_address": "780 Mission St",
      "city": "San Francisco",
      "zipcode": "94103",
      "state": "California",
      "country": "US",
      "hotel_location_rating": null,
      "hotel_amenities": null,
      "hotel_stars": 4,
      "hotel_review_summary": null,
      "hotel_price_for_dates": "$189",
      "hotel_booking_options": null,
      "hotel_results_from_web": null
    },
    {
      "business_id": "0x808580614d1f605f:0x84660c500c409d2b",
      "google_id": "0x808580614d1f605f:0x84660c500c409d2b",
      "place_id": "ChIJX2AfTWGAhYARK51ADFAMZoQ",
      "google_mid": "/m/0b6f64b",
      "phone_number": "+14157881234",
      "name": "Hyatt Regency San Francisco",
      "latitude": 37.794216899999995,
      "longitude": -122.39566629999999,
      "full_address": "Hyatt Regency San Francisco, 5 Embarcadero Ctr, San Francisco, CA 94111",
      "review_count": 7250,
      "rating": 4.4,
      "timezone": "America/Los_Angeles",
      "opening_status": null,
      "working_hours": {},
      "website": "...",
      "tld": "hyatt.com",
      "verified": true,
      "place_link": "...",
      "cid": "9540326398573452587",
      "reviews_link": "...",
      "owner_id": "115079196767241965887",
      "owner_link": "...",
      "owner_name": "Hyatt Regency San Francisco",
      "booking_link": null,
      "reservations_link": null,
      "business_status": "OPEN",
      "type": "Hotel",
      "subtypes": [
        "Hotel"
      ],
      "subtype_gcids": [
        "hotel",
        "establishment",
        "establishment_poi",
        "feature",
        "indoor_lodging",
        "lodging",
        "public_api_establishment",
        "travel",
        "vacances"
      ],
      "photos_sample": [
        {
          "photo_id": "CIHM0ogKEICAgICa6qy-iwE",
          "photo_url": "...",
          "photo_url_large": "...",
          "video_thumbnail_url": null,
          "latitude": 37.7945917,
          "longitude": -122.3963792,
          "type": "photo",
          "photo_datetime_utc": "2021-08-28T00:00:00.000Z",
          "photo_timestamp": 1630108800
        }
      ],
      "reviews_per_rating": {
        "1": 223,
        "2": 158,
        "3": 514,
        "4": 1894,
        "5": 4461
      },
      "photo_count": 18241,
      "about": {
        "summary": "...",
        "details": null
      },
      "address": "5 Embarcadero Ctr, San Francisco, CA 94111",
      "order_link": null,
      "price_level": null,
      "district": "Financial District",
      "street_address": "5 Embarcadero Ctr",
      "city": "San Francisco",
      "zipcode": "94111",
      "state": "California",
      "country": "US",
      "hotel_location_rating": null,
      "hotel_amenities": {
        "Free Wi-Fi": true
      },
      "hotel_stars": 4,
      "hotel_review_summary": null,
      "hotel_price_for_dates": "$224",
      "hotel_booking_options": null,
      "hotel_results_from_web": null
    }
  ]
}
```
    """
    url = "https://api.openwebninja.com/local-business-data/search"
    querystring = {
        "query": query,
    }
    headers = {
        "X-API-Key": "ak_2a42z3zdrr3rnxcapzcpfplyqqohqtgk8n0rsxjtvftpre3"
        }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


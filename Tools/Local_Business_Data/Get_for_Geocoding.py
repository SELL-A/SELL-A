import os
import requests

def Get_for_Geocoding(lat, lng):
    """
    :API_description: This API performs geocoding by searching for locations based on provided latitude and longitude coordinates, which are used to bias the search results towards a specific geographic area.
    :param lat: Latitude of the location.
    :param lng: Longitude of the location.
    :response_schema: 
    ```json
{
  "status": "OK",
  "request_id": "4c37e6d3-fbaf-4dae-bb9e-cd33ce1bb1cc",
  "parameters": {
    "language": "en",
    "region": "us",
    "lat": 40.6958453,
    "lng": -73.9799119
  },
  "data": [
    {
      "business_id": "0x89c25bca7cf7c659:0xe153fe5bf602367f",
      "google_id": "0x89c25bca7cf7c659:0xe153fe5bf602367f",
      "place_id": "ChIJWcb3fMpbwokRfzYC9lv-U-E",
      "google_mid": "/g/11c1jy3gzq",
      "phone_number": null,
      "name": "8 Monument Walk",
      "latitude": 40.6958276,
      "longitude": -73.979916,
      "full_address": "8 Monument Walk, Brooklyn, NY 11205",
      "review_count": 0,
      "rating": null,
      "timezone": "America/New_York",
      "opening_status": null,
      "working_hours": null,
      "website": null,
      "verified": true,
      "place_link": "...",
      "cid": "16236600752523589247",
      "reviews_link": null,
      "owner_id": null,
      "owner_link": null,
      "owner_name": null,
      "booking_link": null,
      "reservations_link": null,
      "business_status": "OPEN",
      "type": "Building",
      "subtypes": [
        "Building"
      ],
      "photos_sample": [
        {
          "photo_id": "TR5VjpA41kYBHkF92OxdyQ",
          "photo_url": "...",
          "photo_url_large": null,
          "video_thumbnail_url": null,
          "latitude": 40.695847399870864,
          "longitude": -73.9802580338202,
          "type": "street_view",
          "photo_datetime_utc": "2024-12-14T00:00:00.000Z",
          "photo_timestamp": 1734134400
        }
      ],
      "reviews_per_rating": null,
      "photo_count": 1,
      "about": null,
      "address": "8 Monument Walk, Brooklyn, NY 11205",
      "order_link": null,
      "price_level": null,
      "district": "Fort Greene",
      "street_address": "8 Monument Walk",
      "city": "Brooklyn",
      "zipcode": "11205",
      "state": "New York",
      "country": "US"
    }
  ]
}
    ```
    """
    url = "https://api.openwebninja.com/local-business-data/reverse-geocoding"
    querystring = {
        "lat": lat,
        "lng": lng
    }
    headers = {
        "X-API-Key": "ak_2a42z3zdrr3rnxcapzcpfplyqqohqtgk8n0rsxjtvftpre3"
        }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
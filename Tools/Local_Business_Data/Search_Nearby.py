import os
import requests

def Search_Nearby(query, lat, lng):
    """
    :API_description: Search businesses near by specific geographic coordinates. To see it in action, right click on a specific point in the map on Google Maps and select "Search nearby", enter a query and search.
    :param query: The search term for nearby businesses.
    :param lat: Latitude of the location to search around.
    :param lng: Longitude of the location to search around.
    :response_schema: 
    ```json
{
  "status": "string",
  "request_id": "string",
  "parameters": {
    "query": "string",
    "language": "string",
    "region": "string",
    "lat": "number",
    "lng": "number",
    "limit": "integer",
    "extract_emails_and_contacts": "boolean"
  },
  "data": [
    {
      "business_id": "string",
      "google_id": "string",
      "place_id": "string",
      "google_mid": "string",
      "phone_number": "string | null",
      "name": "string",
      "latitude": "number",
      "longitude": "number",
      "full_address": "string",
      "review_count": "integer",
      "rating": "number",
      "timezone": "string",
      "opening_status": "string",
      "working_hours": {
        "Sunday": ["string"],
        "Monday": ["string"],
        "Tuesday": ["string"],
        "Wednesday": ["string"],
        "Thursday": ["string"],
        "Friday": ["string"],
        "Saturday": ["string"]
      },
      "opening_date": "string | null",
      "website": "string | null",
      "tld": "string",
      "verified": "boolean",
      "place_link": "string",
      "cid": "string",
      "reviews_link": "string",
      "owner_id": "string",
      "owner_link": "string",
      "owner_name": "string",
      "booking_link": "string | null",
      "reservations_link": "string | null",
      "business_status": "string",
      "type": "string",
      "subtypes": ["string"],
      "subtype_gcids": ["string"],
      "photos_sample": [
        {
          "photo_id": "string",
          "photo_url": "string",
          "photo_url_large": "string",
          "video_thumbnail_url": "string | null",
          "latitude": "number",
          "longitude": "number",
          "type": "string",
          "photo_datetime_utc": "string (ISO 8601)",
          "photo_timestamp": "integer (Unix timestamp)"
        }
      ],
      "reviews_per_rating": {
        "1": "integer",
        "2": "integer",
        "3": "integer",
        "4": "integer",
        "5": "integer"
      },
      "photo_count": "integer",
      "about": {
        "summary": "string | null",
        "details": {
          "Accessibility": {
            "Wheelchair accessible restroom": "boolean",
            "Wheelchair accessible seating": "boolean",
            "Assistive hearing loop": "boolean",
            "Wheelchair accessible entrance": "boolean",
            "Wheelchair accessible parking lot": "boolean"
          }
        }
      } | null,
      "address": "string",
      "order_link": "string | null",
      "price_level": "string | null",
      "district": "string",
      "street_address": "string",
      "city": "string",
      "zipcode": "string",
      "state": "string",
      "country": "string",
      "business_services": {
        "Plumber": ["string"],
        "Gasfitter": ["string"],
        "Drainage service": ["string"],
        "Water filter supplier": ["string"],
        "Gas installation service": ["string"],
        "Water treatment supplier": ["string"],
        "Hot water system supplier": ["string"]
      }
    }
  ]
}
```
    """
    url = "https://api.openwebninja.com/local-business-data/search-nearby"
    querystring = {
        "query": query,
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
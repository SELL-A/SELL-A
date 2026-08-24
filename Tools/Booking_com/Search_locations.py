import os
import requests

def Search_locations(name):
    """
    :API_description: This API searches for destination locations, such as cities, districts, airports, and landmarks, based on a query string and returns detailed information including geographic coordinates, hotel counts, and booking constraints for each matching result.
    :param name: The name of the location to search for hotels.
    :response_schema: 
    ```json
[
  {
    "name": "Berlin",
    "b_max_los_data": {
      "experiment": "long_stays_android_extend_los_2",
      "default_los": 45,
      "extended_los": 90,
      "has_extended_los": 1,
      "max_allowed_los": 90,
      "is_fullon": 0
    },
    "longitude": 13.376818,
    "region": "Berlin Federal State",
    "lc": "en",
    "label": "Berlin, Berlin Federal State, Germany",
    "timezone": "Europe/Berlin",
    "image_url": "...",
    "city_name": "Berlin",
    "rtl": 0,
    "latitude": 52.516212,
    "roundtrip": "...",
    "country": "Germany",
    "cc1": "de",
    "dest_type": "city",
    "hotels": 2662,
    "city_ufi": null,
    "dest_id": "-1746443",
    "type": "ci",
    "nr_hotels": 2662
  },
  {
    "b_max_los_data": {
      "is_fullon": 0,
      "has_extended_los": 1,
      "max_allowed_los": 90,
      "default_los": 45,
      "extended_los": 90,
      "experiment": "long_stays_android_extend_los_2"
    },
    "name": "Berlin City Centre",
    "longitude": 13.374681,
    "region": "Berlin Federal State",
    "lc": "en",
    "timezone": "Europe/Berlin",
    "label": "Berlin City Centre, Berlin, Berlin Federal State, Germany",
    "city_name": "Berlin",
    "image_url": "...",
    "roundtrip": "...",
    "latitude": 52.517666,
    "rtl": 0,
    "dest_type": "district",
    "cc1": "de",
    "country": "Germany",
    "type": "di",
    "dest_id": "2285",
    "city_ufi": -1746443,
    "hotels": 356,
    "nr_hotels": 356
  },
  {
    "dest_type": "airport",
    "cc1": "de",
    "country": "Germany",
    "roundtrip": "GhA5YTQyNjkyOWIyYzkwMTMyIAIoATICZW46BkJlcmxpbkAASgBQAA==",
    "latitude": 52.363,
    "rtl": 0,
    "nr_hotels": 117,
    "type": "ai",
    "dest_id": "7944",
    "city_ufi": -1746443,
    "hotels": 117,
    "region": "Berlin Federal State",
    "longitude": 13.51,
    "lc": "en",
    "b_max_los_data": {
      "extended_los": 90,
      "default_los": 45,
      "experiment": "long_stays_android_extend_los_2",
      "is_fullon": 0,
      "max_allowed_los": 90,
      "has_extended_los": 1
    },
    "name": "Berlin Brandenburg Airport Willy Brandt",
    "city_name": "Berlin",
    "image_url": "https://cf.bstatic.com/static/img/plane-100.jpg",
    "timezone": "Europe/Berlin",
    "label": "Berlin Brandenburg Airport Willy Brandt, Berlin, Berlin Federal State, Germany"
  },
  {
    "label": "Berlin Central Station, Berlin, Berlin Federal State, Germany",
    "timezone": "Europe/Berlin",
    "image_url": "...",
    "roundtrip": "...",
    "latitude": 52.52504,
    "city_name": "Berlin",
    "name": "Berlin Central Station",
    "b_max_los_data": {
      "has_extended_los": 1,
      "max_allowed_los": 90,
      "is_fullon": 0,
      "experiment": "long_stays_android_extend_los_2",
      "extended_los": 90,
      "default_los": 45
    },
    "longitude": 13.369533,
    "region": "Berlin Federal State",
    "lc": "en",
    "city_ufi": -1746443,
    "dest_id": "11155",
    "hotels": 111,
    "type": "la",
    "nr_hotels": 111,
    "latitude": 52.52504,
    "rtl": 0,
    "roundtrip": "...",
    "landmark_type": 2,
    "country": "Germany",
    "dest_type": "landmark",
    "cc1": "de"
  }
]
```
    """
    url = "https://booking-com.p.rapidapi.com/v1/hotels/locations"
    querystring = {
        "name": name,
        "locale": "en-us"
    }

    headers = {
        "x-rapidapi-key": "8337d89e37msh71c9e40b4a00012p119156jsnd38901b956f2",
        "x-rapidapi-host": "booking-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

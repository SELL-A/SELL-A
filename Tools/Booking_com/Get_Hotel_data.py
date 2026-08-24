import os
import requests

def Get_Hotel_data(hotel_id):
    """
    :API_description: Retrieves comprehensive details for a specific hotel property, including its identification, location, amenities, policies, descriptions, photos, pricing, and customer reviews.
    :param hotel_id: The unique identifier for the hotel.
    :response_schema: 
    ```json
{
  "city": "Berlin",
  "hotel_facilities_filtered": "3,5,6,7,8,11,15,16,22,25,28,48,51,64,75,80,91,108,109,117,163,181,184,185,186,203,219,253,305,418,420,422,423,425,435,436,439,440,443,445,446,447,448,449,450,451,453,455,456,457,458,459,460,461,462,464,465,466,467,468,478,483,485,486,489,492,493,494,495,496,506,522",
  "hoteltype_id": 204,
  "description_translations": [
    {
      "languagecode": "en-gb",
      "description": "...",
      "descriptiontype_id": 6
    },
    {
      "description": "...",
      "descriptiontype_id": 6,
      "languagecode": "en-us"
    },
    {
      "descriptiontype_id": 7,
      "description": "...",
      "languagecode": "en-gb"
    }
  ],
  "class": 4,
  "hotel_facilities": "...",
  "city_id": -1746443,
  "email": "",
  "checkin": {
    "from": "15:00",
    "to": "23:30",
    "24_hour_available": 0
  },
  "preferred": 1,
  "district": null,
  "district_id": 5844,
  "main_photo_id": 54629815,
  "ranking": 16379420,
  "entrance_photo_url": "...",
  "location": {
    "latitude": 52.5002932226084,
    "longitude": 13.3467457829422
  },
  "currencycode": "EUR",
  "preferred_plus": 0,
  "review_nr": 12334,
  "class_is_estimated": 1,
  "hotel_id": 1377073,
  "countrycode": "de",
  "zip": "10777",
  "country": "Germany",
  "languages_spoken": {
    "languagecode": [
      "ar",
      "de",
      "en-gb",
      "es",
      "fr",
      "it"
    ]
  },
  "url": "https://www.booking.com/hotel/de/riu-plaza-berlin.html",
  "booking_home": {
    "quality_class": null,
    "is_single_unit_property": 0,
    "is_aparthotel": 0,
    "is_vacation_rental": 0,
    "is_single_type_property": 0,
    "group": "hotels_and_others",
    "segment": 0,
    "is_booking_home": 0
  },
  "main_photo_url": "...",
  "review_score": "8.5",
  "review_score_word": "Very Good",
  "address": "Martin-Luther-Strasse 1",
  "is_vacation_rental": 0,
  "checkout": {
    "from": "00:30",
    "to": "12:00",
    "24_hour_available": 0
  },
  "is_single_unit_vr": 0,
  "name": "Riu Plaza Berlin"
}
    ```
    """
    url = "https://booking-com.p.rapidapi.com/v1/hotels/data"
    querystring = {
        "hotel_id": hotel_id,
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


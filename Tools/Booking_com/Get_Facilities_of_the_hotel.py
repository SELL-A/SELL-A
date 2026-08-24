import os
import requests

def Get_Facilities_of_the_hotel(hotel_id):
    """
    :API_description: Get hotel amenities (Restaurant, Room service, Breakfast, etc.).
    :param hotel_id: The ID of the hotel to query.
    :response_schema: 
    ```
JSON[
  {
    "hotel_id": 1676161,
    "facilitytype_name": "Food & Drink",
    "is_common_room_facility": 0,
    "hotelfacilitytype_id": 3,
    "roomfacilitytype_id": "",
    "facilitytype_id": 7,
    "kind": "boolean",
    "facility_name": "Restaurant",
    "value": 1
  },
  {
    "facilitytype_name": "General",
    "hotel_id": 1676161,
    "is_common_room_facility": 0,
    "hotelfacilitytype_id": 5,
    "roomfacilitytype_id": "",
    "facility_name": "Room service",
    "kind": "boolean",
    "facilitytype_id": 1,
    "value": 1
  },
  {
    "facilitytype_id": 27,
    "kind": "free_or_paid",
    "facility_name": "Meeting/banquet facilities (additional charge)",
    "value": 5,
    "paid": 1,
    "roomfacilitytype_id": "",
    "is_common_room_facility": 0,
    "hotelfacilitytype_id": 6,
    "hotel_id": 1676161,
    "facilitytype_name": "Business facilities"
  },
  {
    "hotel_id": 1676161,
    "facilitytype_name": "Food & Drink",
    "is_common_room_facility": 0,
    "hotelfacilitytype_id": 7,
    "roomfacilitytype_id": "",
    "facilitytype_id": 7,
    "kind": "boolean",
    "facility_name": "Bar",
    "value": 1
  },
  {
    "facilitytype_name": "Reception services",
    "hotel_id": 1676161,
    "hotelfacilitytype_id": 8,
    "is_common_room_facility": 0,
    "roomfacilitytype_id": "",
    "value": 1,
    "facility_name": "24-hour front desk",
    "kind": "boolean",
    "facilitytype_id": 23
  },
  {
    "hotel_id": 1676161,
    "facilitytype_name": "Activities",
    "hotelfacilitytype_id": 10,
    "is_common_room_facility": 0,
    "roomfacilitytype_id": "",
    "value": 4,
    "free": 1,
    "facilitytype_id": 2,
    "kind": "free_or_paid",
    "facility_name": "Sauna"
  },
  {
    "is_common_room_facility": 0,
    "hotelfacilitytype_id": 11,
    "hotel_id": 1676161,
    "facilitytype_name": "Activities",
    "facilitytype_id": 2,
    "kind": "free_or_paid",
    "facility_name": "Fitness centre",
    "value": 4,
    "free": 1,
    "roomfacilitytype_id": ""
  },
  {
    "facilitytype_name": "Outdoors",
    "hotel_id": 1676161,
    "hotelfacilitytype_id": 15,
    "is_common_room_facility": 0,
    "roomfacilitytype_id": "",
    "value": 1,
    "facility_name": "Terrace",
    "facilitytype_id": 13,
    "kind": "boolean"
  },
  {
    "hotelfacilitytype_id": 16,
    "is_common_room_facility": 0,
    "facilitytype_name": "General",
    "hotel_id": 1676161,
    "value": 1,
    "facility_name": "Non-smoking rooms",
    "kind": "boolean",
    "facilitytype_id": 1,
    "roomfacilitytype_id": ""
  },
  {
    "hotel_id": 1676161,
    "facilitytype_name": "Business facilities",
    "is_common_room_facility": 0,
    "hotelfacilitytype_id": 20,
    "roomfacilitytype_id": "",
    "paid": 1,
    "facilitytype_id": 27,
    "kind": "free_or_paid",
    "facility_name": "Business centre (additional charge)",
    "value": 5
  },
  {
    "facilitytype_name": "Cleaning services",
    "hotel_id": 1676161,
    "hotelfacilitytype_id": 22,
    "is_common_room_facility": 0,
    "paid": 1,
    "roomfacilitytype_id": "",
    "value": 5,
    "facility_name": "Laundry (additional charge)",
    "facilitytype_id": 26,
    "kind": "free_or_paid"
  },
  {
    "value": 5,
    "facility_name": "Dry cleaning (additional charge)",
    "facilitytype_id": 26,
    "kind": "free_or_paid",
    "paid": 1,
    "roomfacilitytype_id": "",
    "hotelfacilitytype_id": 23,
    "is_common_room_facility": 0,
    "facilitytype_name": "Cleaning services",
    "hotel_id": 1676161
  },
  {
    "value": 1,
    "facility_name": "Facilities for disabled guests",
    "facilitytype_id": 1,
    "kind": "boolean",
    "roomfacilitytype_id": "",
    "hotelfacilitytype_id": 25,
    "is_common_room_facility": 0,
    "facilitytype_name": "General",
    "hotel_id": 1676161
  }
]
    ```
    """
    url = "https://booking-com.p.rapidapi.com/v1/hotels/facilities"
    querystring = {
        "locale": "en-us",
        "hotel_id": hotel_id
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
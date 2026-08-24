import os
import requests
from datetime import datetime, date

def Search_hotels(checkin_date, checkout_date, dest_type, dest_id, order_by, room_number, filter_by_currency):
    """
    :API_description: This API searches for hotel accommodations based on destination, dates, and guest details, returning comprehensive results including pricing, reviews, facilities, and location information.
    :param checkin_date: Check-in date (e.g., "2026-11-15")  the time must be in the future or present, now time is 2026-6-13.
    :param checkout_date: Check-out date (e.g., "2026-11-20")
    :param dest_type: Destination type (e.g., city, region, country, hotel, airport)
    :param dest_id: Destination ID ,use Search locations API to find a place, field dest_id and dest_type
    :param order_by: Order preference (e.g., popularity, price, distance)
    :param room_number: Number of rooms
    :param filter_by_currency: Currency filter (e.g., USD, EUR)
    :response_schema: 
    ```json
{
  "primary_count": 5,
  "count": 5,
  "room_distribution": [
    {
      "adults": "2",
      "children": [
        1,
        1
      ]
    }
  ],
  "map_bounding_box": {
    "ne_long": 14.6137006742745,
    "sw_long": 14.308751,
    "ne_lat": 50.152601,
    "sw_lat": 49.9600355
  },
  "total_count_with_filters":5,
  "unfiltered_count": 4200,
  "extended_count": 0,
  "unfiltered_primary_count": 4200,
  "search_radius": 0,
  "sort": [
    {
      "name": "Distance From Downtown",
      "id": "distance"
    },
    {
      "name": "Popularity",
      "id": "popularity"
    },
    {
      "id": "class_descending",
      "name": "Stars (5 to 0)"
    },
    {
      "name": "Stars (0 to 5)",
      "id": "class_ascending"
    },
    {
      "id": "bayesian_review_score",
      "name": "Guest Review Score"
    },
    {
      "name": "Price (low to high)",
      "id": "price"
    }
  ],
  "result": [
    {
      "distances": [
        {
          "text": "Prague 9  5.6 km from downtown",
          "icon_name": "bui_geo_pin",
          "icon_set": null
        }
      ],
      "preferred_plus": 0,
      "ufi": -553173,
      "is_no_prepayment_block": 0,
      "city_in_trans": "in Prague",
      "genius_discount_percentage": 0,
      "class": 4,
      "min_total_price": 8580.96,
      "default_language": "en",
      "district_id": 263,
      "badges": [],
      "updated_checkout": null,
      "preferred": 1,
      "id": "property_card_7696424",
      "review_score": 9.4,
      "cant_book": 0,
      "property_cribs_availability": 2,
      "in_best_district": 0,
      "review_nr": 17741,
      "review_recommendation": "",
      "review_score_word": "Wonderful",
      "hotel_has_vb_boost": 0,
      "distance": "5.63",
      "hotel_name": "STAGES HOTEL Prague, a Tribute Portfolio Hotel",
      "city_name_en": "Prague",
      "default_wishlist_name": "Prague",
      "is_beach_front": 0,
      "is_geo_rate": "",
      "currency_code": "CZK",
      "countrycode": "cz",
      "address_trans": "Ceskomoravska 19a",
      "composite_price_breakdown": {
        "all_inclusive_amount_hotel_currency": {
          "amount_rounded": "8,581 Kč",
          "currency": "CZK",
          "value": 8580.96,
          "amount_unrounded": "8,580.96 Kč"
        },
        "excluded_amount": {
          "amount_rounded": "0 Kč",
          "currency": "CZK",
          "value": 0,
          "amount_unrounded": "0 Kč"
        },
        "all_inclusive_amount": {
          "amount_rounded": "8,581 Kč",
          "currency": "CZK",
          "value": 8580.96,
          "amount_unrounded": "8,580.96 Kč"
        },
        "gross_amount_hotel_currency": {
          "value": 8580.96,
          "currency": "CZK",
          "amount_unrounded": "8,580.96 Kč",
          "amount_rounded": "8,581 Kč"
        },
        "gross_amount_per_night": {
          "amount_unrounded": "8,580.96 Kč",
          "value": 8580.96,
          "currency": "CZK",
          "amount_rounded": "8,581 Kč"
        },
        "gross_amount": {
          "amount_unrounded": "8,580.96 Kč",
          "value": 8580.96,
          "currency": "CZK",
          "amount_rounded": "8,581 Kč"
        },
        "charges_details": {
          "translated_copy": "Includes taxes and fees",
          "amount": {
            "value": 0,
            "currency": "CZK"
          },
          "mode": "all_included"
        },
        "charges": {},
        "items": [
          {
            "base": {
              "kind": "per_person_per_night",
              "base_amount": 50
            },
            "inclusion_type": "included",
            "item_amount": {
              "amount_rounded": "200 Kč",
              "amount_unrounded": "200 Kč",
              "value": 200,
              "currency": "CZK"
            },
            "details": "City tax",
            "name": "City tax",
            "kind": "charge"
          },
          {
            "item_amount": {
              "amount_rounded": "898 Kč",
              "amount_unrounded": "897.96 Kč",
              "currency": "CZK",
              "value": 897.96
            },
            "inclusion_type": "included",
            "base": {
              "kind": "percentage",
              "percentage": 12
            },
            "kind": "charge",
            "name": "VAT",
            "details": "12 % VAT"
          }
        ],
        "net_amount": {
          "amount_rounded": "7,483 Kč",
          "amount_unrounded": "7,483 Kč",
          "value": 7483,
          "currency": "CZK"
        },
        "price_display_config": [
          {
            "value": 0,
            "key": "use_nightly_prices"
          },
          {
            "value": 0,
            "key": "use_nightly_as_dominant"
          },
          {
            "value": 1,
            "key": "use_js_tracking"
          }
        ],
        "included_taxes_and_charges_amount": {
          "currency": "CZK",
          "value": 1097.96,
          "amount_unrounded": "1,097.96 Kč",
          "amount_rounded": "1,098 Kč"
        },
        "benefits": []
      },
      "native_ads_cpc": 0,
      "cc1": "cz",
      "bwallet": {
        "hotel_eligibility": 0
      },
      "soldout": 0,
      "type": "property_card",
      "price_breakdown": {
        "has_incalculable_charges": null,
        "has_tax_exceptions": null,
        "sum_excluded_raw": null,
        "gross_price": null,
        "has_fine_print_charges": null,
        "currency": null,
        "all_inclusive_price": null
      },
      "crib_guaranteed": "",
      "checkin": {
        "until": "00:00",
        "from": "15:00"
      },
      "class_is_estimated": 0,
      "urgency_room_msg": "Connecting Family Room",
      "wishlist_count": 0,
      "price_is_final": 1,
      "native_ad_id": "",
      "is_mobile_deal": 0,
      "currencycode": "CZK",
      "is_smart_deal": 0,
      "distance_to_cc": "5.65",
      "zip": "CZ-19000",
      "latitude": 50.104384958882,
      "mobile_discount_percentage": 0,
      "cc_required": 1,
      "district": "Prague 9",
      "block_ids": [
        "769642411_334772528_4_1_0"
      ],
      "ribbon_text": "Breakfast included",
      "native_ads_tracking": "",
      "hotel_id": 7696424,
      "children_not_allowed": 0,
      "is_city_center": 0,
      "accommodation_type_name": "Hotel",
      "is_genius_deal": 0,
      "matching_units_configuration": {
        "matching_units_common_config": {
          "unit_type_id": 13,
          "localized_area": null
        }
      },
      "updated_checkin": null,
      "main_photo_url": "...",
      "hotel_facilities": "...",
      "main_photo_id": 430825435,
      "hotel_name_trans": "STAGES HOTEL Prague, a Tribute Portfolio Hotel",
      "city": "Prague",
      "longitude": 14.4953591788171,
      "city_trans": "Prague",
      "accommodation_type": 204,
      "timezone": "Europe/Prague",
      "distance_to_cc_formatted": "5.6 km",
      "url": "https://www.booking.com/hotel/cz/stages-prague-a-portfolio.html",
      "districts": "263",
      "is_tpi_exclusive_property": 0,
      "address": "Ceskomoravska 19a",
      "is_free_cancellable": 0,
      "selected_review_topic": null,
      "checkout": {
        "until": "12:00",
        "from": "06:00"
      },
      "extended": 0,
      "country_trans": "Czech Republic",
      "max_photo_url": "...",
      "max_1440_photo_url": "..."
    },
    {
      "default_wishlist_name": "Prague",
      "is_beach_front": 0,
      "countrycode": "cz",
      "is_geo_rate": "",
      "currency_code": "EUR",
      "address_trans": "Teplicka 492",
      "composite_price_breakdown": {
        "benefits": [
          {
            "details": "This property is offering a discount on select stays between Mar 26 and Sep 30 2026.",
            "identifier": "getaway-2021",
            "kind": "badge",
            "name": "Getaway Deal",
            "icon": null,
            "badge_variant": "constructive"
          }
        ],
        "included_taxes_and_charges_amount": {
          "amount_rounded": "€ 30",
          "amount_unrounded": "€ 29.74",
          "currency": "EUR",
          "value": 29.7432
        },
        "price_display_config": [
          {
            "value": 0,
            "key": "use_nightly_prices"
          },
          {
            "value": 0,
            "key": "use_nightly_as_dominant"
          },
          {
            "key": "use_js_tracking",
            "value": 1
          }
        ],
        "net_amount": {
          "amount_unrounded": "€ 213.53",
          "currency": "EUR",
          "value": 213.5268,
          "amount_rounded": "€ 214"
        },
        "items": [
          {
            "inclusion_type": "included",
            "item_amount": {
              "amount_rounded": "€ 4",
              "amount_unrounded": "€ 4.12",
              "currency": "EUR",
              "value": 4.12
            },
            "base": {
              "base_amount": 2.06,
              "kind": "per_person_per_night"
            },
            "name": "City tax",
            "kind": "charge",
            "details": "City tax"
          },
          {
            "base": {
              "percentage": 12,
              "kind": "percentage"
            },
            "inclusion_type": "included",
            "item_amount": {
              "amount_rounded": "€ 26",
              "amount_unrounded": "€ 25.62",
              "value": 25.6232,
              "currency": "EUR"
            },
            "details": "12 % VAT",
            "kind": "charge",
            "name": "VAT"
          },
          {
            "details": "This property is offering a discount on stays between Mar 26 and Sep 30 2026.",
            "name": "Getaway Deal",
            "identifier": "campaign_38",
            "kind": "discount",
            "item_amount": {
              "amount_unrounded": "€ 42.93",
              "currency": "EUR",
              "value": 42.93,
              "amount_rounded": "€ 43"
            },
            "base": {
              "kind": "rate"
            }
          },
          {
            "details": "You’ll get a reduced rate when you pay online because Booking.com will pay part of the price.",
            "identifier": "BSB",
            "kind": "discount",
            "name": "Booking.com pays",
            "item_amount": {
              "amount_rounded": "€ 17",
              "amount_unrounded": "€ 17.13",
              "value": 17.13,
              "currency": "EUR"
            },
            "base": {
              "kind": "total"
            }
          }
        ],
        "charges_details": {
          "translated_copy": "Includes taxes and fees",
          "amount": {
            "value": 0,
            "currency": "EUR"
          },
          "mode": "all_included"
        },
        "charges": {},
        "gross_amount": {
          "amount_unrounded": "€ 226.14",
          "currency": "EUR",
          "value": 226.14,
          "amount_rounded": "€ 226"
        },
        "strikethrough_amount": {
          "currency": "EUR",
          "value": 286.2,
          "amount_unrounded": "€ 286.20",
          "amount_rounded": "€ 286"
        },
        "gross_amount_per_night": {
          "amount_unrounded": "€ 226.14",
          "value": 226.14,
          "currency": "EUR",
          "amount_rounded": "€ 226"
        },
        "gross_amount_hotel_currency": {
          "amount_rounded": "€ 226",
          "amount_unrounded": "€ 226.14",
          "currency": "EUR",
          "value": 226.14
        },
        "discounted_amount": {
          "currency": "EUR",
          "value": 60.06,
          "amount_unrounded": "€ 60.06",
          "amount_rounded": "€ 60"
        },
        "all_inclusive_amount": {
          "amount_rounded": "€ 226",
          "currency": "EUR",
          "value": 226.14,
          "amount_unrounded": "€ 226.14"
        },
        "excluded_amount": {
          "currency": "EUR",
          "value": 0,
          "amount_unrounded": "€ 0",
          "amount_rounded": "€ 0"
        },
        "strikethrough_amount_per_night": {
          "amount_rounded": "€ 286",
          "value": 286.2,
          "currency": "EUR",
          "amount_unrounded": "€ 286.20"
        },
        "all_inclusive_amount_hotel_currency": {
          "amount_rounded": "€ 226",
          "amount_unrounded": "€ 226.14",
          "value": 226.14,
          "currency": "EUR"
        }
      },
      "native_ads_cpc": 0,
      "review_score": 8.4,
      "id": "property_card_77320",
      "cant_book": 0,
      "property_cribs_availability": 2,
      "in_best_district": 0,
      "review_nr": 11857,
      "hotel_has_vb_boost": 0,
      "review_score_word": "Very Good",
      "review_recommendation": "",
      "distance": "6.38",
      "city_name_en": "Prague",
      "hotel_name": "Hotel Duo & Wellness",
      "genius_discount_percentage": 0,
      "class": 4,
      "min_total_price": 226.14,
      "default_language": "en",
      "district_id": 263,
      "badges": [
        {
          "text": "Getaway Deal",
          "id": "Getaway 2021 Deals",
          "badge_variant": "constructive"
        }
      ],
      "updated_checkout": null,
      "preferred": 1,
      "distances": [
        {
          "text": "Prague 9  6.4 km from downtown",
          "icon_name": "bui_geo_pin",
          "icon_set": null
        }
      ],
      "preferred_plus": 1,
      "has_swimming_pool": 1,
      "ufi": -553173,
      "is_no_prepayment_block": 0,
      "city_in_trans": "in Prague",
      "accommodation_type": 204,
      "timezone": "Europe/Prague",
      "distance_to_cc_formatted": "6.4 km",
      "districts": "263",
      "url": "https://www.booking.com/hotel/cz/duo.html",
      "is_tpi_exclusive_property": 0,
      "address": "Teplicka 492",
      "is_free_cancellable": 0,
      "selected_review_topic": null,
      "checkout": {
        "until": "11:00",
        "from": ""
      },
      "extended": 0,
      "country_trans": "Czech Republic",
      "native_ads_tracking": "",
      "hotel_include_breakfast": 0,
      "hotel_id": 77320,
      "children_not_allowed": 0,
      "is_city_center": 0,
      "accommodation_type_name": "Hotel",
      "is_genius_deal": 0,
      "updated_checkin": null,
      "matching_units_configuration": {
        "matching_units_common_config": {
          "localized_area": null,
          "unit_type_id": 5
        }
      },
      "hotel_name_trans": "Hotel Duo & Wellness",
      "main_photo_url": "...",
      "main_photo_id": 493721137,
      "hotel_facilities": "27,16,91,484,81,526,441,457,451,127,121,502,53,462,532,448,458,421,496,184,459,2,449,4,6,160,505,75,163,17,500,460,517,530,241,465,535,404,463,47,533,136,467,461,531,15,14,77,422,253,220,7,436,64,501,468,44,442,25,80,423,242,425,51,143,512,140,186,420,494,222,22,443,453,3,455,445,177,440,524,486,450,506,101,107,522,8,78,224,437,109,54,492,110,108,439,244,514,466,124,189,454,176,520,444,523,188,187,210,489,424,490,305,11,493,488,209,96,495,426,217,529,301,198,185,28,205,527,219,10,521,203,499,485,218,63,133,135,400,23,418,534,5,117,111,435,48,118,433,20,103",
      "longitude": 14.485929608345,
      "city": "Prague",
      "city_trans": "Prague",
      "is_smart_deal": 0,
      "distance_to_cc": "6.40",
      "zip": "19000",
      "latitude": 50.1267585266021,
      "mobile_discount_percentage": 0,
      "cc_required": 1,
      "district": "Prague 9",
      "block_ids": [
        "7732047_91906602_2_1_0"
      ],
      "cc1": "cz",
      "soldout": 0,
      "bwallet": {
        "hotel_eligibility": 0
      },
      "type": "property_card",
      "price_breakdown": {
        "has_fine_print_charges": null,
        "currency": null,
        "all_inclusive_price": null,
        "has_incalculable_charges": null,
        "has_tax_exceptions": null,
        "gross_price": null,
        "sum_excluded_raw": null
      },
      "crib_guaranteed": "",
      "class_is_estimated": 0,
      "checkin": {
        "until": "",
        "from": "15:00"
      },
      "urgency_room_msg": "Junior Suite",
      "wishlist_count": 0,
      "native_ad_id": "",
      "price_is_final": 1,
      "is_mobile_deal": 0,
      "currencycode": "EUR",
      "max_photo_url": "...",
      "max_1440_photo_url": "..."
    }
  ]
}
    ```
    """
    url = "https://booking-com.p.rapidapi.com/v1/hotels/search"
    querystring = {
        "adults_number": 2,
        "units": "metric",
        "checkin_date": checkin_date,
        "checkout_date": checkout_date,
        "dest_type": dest_type,
        "dest_id": dest_id,
        "order_by": order_by,
        "room_number": room_number,
        "filter_by_currency": filter_by_currency,
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
        return {"error": f"Request failed with status code {response.status_code}"}

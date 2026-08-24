import os
import requests

def Search_hotels_by_coordinates(checkout_date, checkin_date, latitude, room_number, order_by, longitude, filter_by_currency):
    """
    :API_description: This API searches for available hotels based on geographic coordinates, check-in/check-out dates, and other filters, returning a list of properties sorted by the specified criteria.
    :param checkout_date: The date of checkout e.g., "2026-09-19". the time must be in the future or present, now time is 2026-6-13.
    :param checkin_date: The date of check-in e.g., "2026-09-18".
    :param latitude: The latitude coordinate for the search Default: 65.9667.
    :param room_number: The number of rooms required, Default: 1.
    :param order_by: The order in which results should be sorted. Default: "price".
    :param longitude: The longitude coordinate for the search Default: -18.5333.
    :param filter_by_currency: Currency filter (e.g., "USD","AED")
    :response_schema: 
    ```json
{

  "type": "object",
  "properties": {
    "primary_count": {"type": "integer"},
    "count": {"type": "integer"},
    "room_distribution": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "adults": {"type": "string"},
          "children": {
            "type": "array",
            "items": {"type": "integer"}
          }
        },
        "required": ["adults", "children"]
      }
    },
    "map_bounding_box": {
      "type": "object",
      "properties": {
        "sw_lat": {"type": "number"},
        "ne_lat": {"type": "number"},
        "ne_long": {"type": "number"},
        "sw_long": {"type": "number"}
      },
      "required": ["sw_lat", "ne_lat", "ne_long", "sw_long"]
    },
    "total_count_with_filters": {"type": "integer"},
    "unfiltered_count": {"type": "integer"},
    "extended_count": {"type": "integer"},
    "unfiltered_primary_count": {"type": "integer"},
    "search_radius": {"type": "integer"},
    "sort": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {"type": "string"},
          "name": {"type": "string"}
        },
        "required": ["id", "name"]
      }
    },
    "result": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "district": {"type": "string"},
          "is_genius_deal": {"type": "integer"},
          "url": {"type": "string"},
          "is_beach_front": {"type": "integer"},
          "review_score_word": {"type": "string"},
          "default_language": {"type": "string"},
          "currencycode": {"type": "string"},
          "soldout": {"type": "integer"},
          "is_no_prepayment_block": {"type": "integer"},
          "is_smart_deal": {"type": "integer"},
          "property_cribs_availability": {"type": "integer"},
          "review_score": {"type": "integer"},
          "hotel_id": {"type": "integer"},
          "city_trans": {"type": "string"},
          "accommodation_type_name": {"type": "string"},
          "hotel_include_breakfast": {"type": "integer"},
          "block_ids": {
            "type": "array",
            "items": {"type": "string"}
          },
          "longitude": {"type": "number"},
          "in_best_district": {"type": "integer"},
          "city_name_en": {"type": "string"},
          "countrycode": {"type": "string"},
          "distance": {"type": "string"},
          "has_free_parking": {"type": "integer"},
          "hotel_facilities": {"type": "string"},
          "type": {"type": "string"},
          "main_photo_url": {"type": "string"},
          "accommodation_type": {"type": "integer"},
          "matching_units_configuration": {
            "type": "object",
            "properties": {
              "matching_units_common_config": {
                "type": "object",
                "properties": {
                  "localized_area": {"type": "string"},
                  "unit_type_id": {"type": "integer"}
                },
                "required": ["localized_area", "unit_type_id"]
              }
            },
            "required": ["matching_units_common_config"]
          },
          "booking_home": {
            "type": "object",
            "properties": {
              "is_single_unit_property": {"type": "string"},
              "group": {"type": "string"},
              "segment": {"type": "integer"},
              "is_booking_home": {"type": "integer"},
              "quality_class": {"type": "integer"}
            },
            "required": ["is_single_unit_property", "group", "segment", "is_booking_home", "quality_class"]
          },
          "is_free_cancellable": {"type": "integer"},
          "native_ads_tracking": {"type": "string"},
          "currency_code": {"type": "string"},
          "urgency_room_msg": {"type": "string"},
          "is_tpi_exclusive_property": {"type": "integer"},
          "country_trans": {"type": "string"},
          "address": {"type": "string"},
          "main_photo_id": {"type": "integer"},
          "crib_guaranteed": {"type": "string"},
          "min_total_price": {"type": "integer"},
          "zip": {"type": "string"},
          "native_ads_cpc": {"type": "integer"},
          "id": {"type": "string"},
          "review_recommendation": {"type": "string"},
          "address_trans": {"type": "string"},
          "wishlist_count": {"type": "integer"},
          "price_breakdown": {
            "type": "object",
            "properties": {
              "has_fine_print_charges": {"type": "integer"},
              "all_inclusive_price": {"type": "integer"},
              "gross_price": {"type": "string"},
              "has_tax_exceptions": {"type": "integer"},
              "has_incalculable_charges": {"type": "integer"},
              "currency": {"type": "string"},
              "sum_excluded_raw": {"type": "string"}
            },
            "required": ["has_fine_print_charges", "all_inclusive_price", "gross_price", "has_tax_exceptions", "has_incalculable_charges", "currency", "sum_excluded_raw"]
          },
          "timezone": {"type": "string"},
          "updated_checkin": {"type": "null"},
          "cc_required": {"type": "integer"},
          "is_mobile_deal": {"type": "integer"},
          "default_wishlist_name": {"type": "string"},
          "bwallet": {
            "type": "object",
            "properties": {
              "hotel_eligibility": {"type": "integer"}
            },
            "required": ["hotel_eligibility"]
          },
          "distances": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "icon_set": {"type": "null"},
                "text": {"type": "string"},
                "icon_name": {"type": "string"}
              },
              "required": ["icon_set", "text", "icon_name"]
            }
          },
          "mobile_discount_percentage": {"type": "number"},
          "district_id": {"type": "integer"},
          "latitude": {"type": "number"},
          "composite_price_breakdown": {
            "type": "object",
            "properties": {
              "strikethrough_amount": {
                "type": "object",
                "properties": {
                  "amount_unrounded": {"type": "string"},
                  "value": {"type": "integer"},
                  "currency": {"type": "string"},
                  "amount_rounded": {"type": "string"}
                },
                "required": ["amount_unrounded", "value", "currency", "amount_rounded"]
              },
              "price_display_config": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "key": {"type": "string"},
                    "value": {"type": "integer"}
                  },
                  "required": ["key", "value"]
                }
              },
              "excluded_amount": {
                "type": "object",
                "properties": {
                  "amount_rounded": {"type": "string"},
                  "value": {"type": "integer"},
                  "currency": {"type": "string"},
                  "amount_unrounded": {"type": "string"}
                },
                "required": ["amount_rounded", "value", "currency", "amount_unrounded"]
              },
              "gross_amount_per_night": {
                "type": "object",
                "properties": {
                  "amount_unrounded": {"type": "string"},
                  "value": {"type": "integer"},
                  "currency": {"type": "string"},
                  "amount_rounded": {"type": "string"}
                },
                "required": ["amount_unrounded", "value", "currency", "amount_rounded"]
              },
              "items": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "name": {"type": "string"},
                    "kind": {"type": "string"},
                    "inclusion_type": {"type": "string"},
                    "details": {"type": ["string", "null"]},
                    "base": {
                      "type": "object",
                      "properties": {
                        "base_amount": {"type": "number"},
                        "kind": {"type": "string"},
                        "percentage": {"type": "integer"}
                      }
                    },
                    "item_amount": {
                      "type": "object",
                      "properties": {
                        "amount_rounded": {"type": "string"},
                        "amount_unrounded": {"type": "string"},
                        "value": {"type": "number"},
                        "currency": {"type": "string"}
                      },
                      "required": ["amount_rounded", "amount_unrounded", "value", "currency"]
                    },
                    "identifier": {"type": "string"}
                  },
                  "required": ["name", "kind", "inclusion_type", "details", "base", "item_amount", "identifier"]
                }
              },
              "charges_details": {
                "type": "object",
                "properties": {
                  "translated_copy": {"type": "string"},
                  "mode": {"type": "string"},
                  "amount": {
                    "type": "object",
                    "properties": {
                      "value": {"type": "integer"},
                      "currency": {"type": "string"}
                    },
                    "required": ["value", "currency"]
                  }
                },
                "required": ["translated_copy", "mode", "amount"]
              },
              "benefits": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "icon": {"type": "null"},
                    "identifier": {"type": "string"},
                    "details": {"type": "string"},
                    "badge_variant": {"type": "string"},
                    "name": {"type": "string"},
                    "kind": {"type": "string"}
                  },
                  "required": ["icon", "identifier", "details", "badge_variant", "name", "kind"]
                }
              },
              "gross_amount_hotel_currency": {
                "type": "object",
                "properties": {
                  "value": {"type": "integer"},
                  "currency": {"type": "string"},
                  "amount_unrounded": {"type": "string"},
                  "amount_rounded": {"type": "string"}
                },
                "required": ["value", "currency", "amount_unrounded", "amount_rounded"]
              },
              "included_taxes_and_charges_amount": {
                "type": "object",
                "properties": {
                  "amount_unrounded": {"type": "string"},
                  "currency": {"type": "string"},
                  "value": {"type": "number"},
                  "amount_rounded": {"type": "string"}
                },
                "required": ["amount_unrounded", "currency", "value", "amount_rounded"]
              },
              "discounted_amount": {
                "type": "object",
                "properties": {
                  "amount_rounded": {"type": "string"},
                  "currency": {"type": "string"},
                  "value": {"type": "integer"},
                  "amount_unrounded": {"type": "string"}
                },
                "required": ["amount_rounded", "currency", "value", "amount_unrounded"]
              },
              "strikethrough_amount_per_night": {
                "type": "object",
                "properties": {
                  "value": {"type": "integer"},
                  "currency": {"type": "string"},
                  "amount_unrounded": {"type": "string"},
                  "amount_rounded": {"type": "string"}
                },
                "required": ["value", "currency", "amount_unrounded", "amount_rounded"]
              },
              "product_price_breakdowns": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "all_inclusive_amount": {
                      "type": "object",
                      "properties": {
                        "value": {"type": "integer"},
                        "currency": {"type": "string"},
                        "amount_unrounded": {"type": "string"},
                        "amount_rounded": {"type": "string"}
                      },
                      "required": ["value", "currency", "amount_unrounded", "amount_rounded"]
                    },
                    "all_inclusive_amount_hotel_currency": {
                      "type": "object",
                      "properties": {
                        "currency": {"type": "string"},
                        "value": {"type": "integer"},
                        "amount_unrounded": {"type": "string"},
                        "amount_rounded": {"type": "string"}
                      },
                      "required": ["currency", "value", "amount_unrounded", "amount_rounded"]
                    },
                    "gross_amount": {
                      "type": "object",
                      "properties": {
                        "amount_unrounded": {"type": "string"},
                        "currency": {"type": "string"},
                        "value": {"type": "integer"},
                        "amount_rounded": {"type": "string"}
                      },
                      "required": ["amount_unrounded", "currency", "value", "amount_rounded"]
                    },
                    "net_amount": {
                      "type": "object",
                      "properties": {
                        "amount_unrounded": {"type": "string"},
                        "currency": {"type": "string"},
                        "value": {"type": "number"},
                        "amount_rounded": {"type": "string"}
                      },
                      "required": ["amount_unrounded", "currency", "value", "amount_rounded"]
                    },
                    "strikethrough_amount_per_night": {
                      "type": "object",
                      "properties": {
                        "amount_rounded": {"type": "string"},
                        "value": {"type": "integer"},
                        "currency": {"type": "string"},
                        "amount_unrounded": {"type": "string"}
                      },
                      "required": ["amount_rounded", "value", "currency", "amount_unrounded"]
                    },
                    "discounted_amount": {
                      "type": "object",
                      "properties": {
                        "amount_rounded": {"type": "string"},
                        "currency": {"type": "string"},
                        "value": {"type": "integer"},
                        "amount_unrounded": {"type": "string"}
                      },
                      "required": ["amount_rounded", "currency", "value", "amount_unrounded"]
                    },
                    "benefits": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "icon": {"type": "null"},
                          "badge_variant": {"type": "string"},
                          "details": {"type": "string"},
                          "identifier": {"type": "string"},
                          "kind": {"type": "string"},
                          "name": {"type": "string"}
                        },
                        "required": ["icon", "badge_variant", "details", "identifier", "kind", "name"]
                      }
                    },
                    "gross_amount_hotel_currency": {
                      "type": "object",
                      "properties": {
                        "amount_rounded": {"type": "string"},
                        "currency": {"type": "string"},
                        "value": {"type": "integer"},
                        "amount_unrounded": {"type": "string"}
                      },
                      "required": ["amount_rounded", "currency", "value", "amount_unrounded"]
                    },
                    "included_taxes_and_charges_amount": {
                      "type": "object",
                      "properties": {
                        "amount_rounded": {"type": "string"},
                        "value": {"type": "number"},
                        "currency": {"type": "string"},
                        "amount_unrounded": {"type": "string"}
                      },
                      "required": ["amount_rounded", "value", "currency", "amount_unrounded"]
                    },
                    "gross_amount_per_night": {
                      "type": "object",
                      "properties": {
                        "currency": {"type": "string"},
                        "value": {"type": "integer"},
                        "amount_unrounded": {"type": "string"},
                        "amount_rounded": {"type": "string"}
                      },
                      "required": ["currency", "value", "amount_unrounded", "amount_rounded"]
                    },
                    "items": {
                      "type": "array",
                      "items": {
                        "type": "object",
                        "properties": {
                          "name": {"type": "string"},
                          "kind": {"type": "string"},
                          "inclusion_type": {"type": "string"},
                          "details": {"type": ["string", "null"]},
                          "base": {
                            "type": "object",
                            "properties": {
                              "kind": {"type": "string"},
                              "base_amount": {"type": "number"},
                              "percentage": {"type": "integer"}
                            }
                          },
                          "item_amount": {
                            "type": "object",
                            "properties": {
                              "amount_rounded": {"type": "string"},
                              "currency": {"type": "string"},
                              "value": {"type": "number"},
                              "amount_unrounded": {"type": "string"}
                            },
                            "required": ["amount_rounded", "currency", "value", "amount_unrounded"]
                          },
                          "identifier": {"type": "string"}
                        },
                        "required": ["name", "kind", "inclusion_type", "details", "base", "item_amount", "identifier"]
                      }
                    },
                    "charges_details": {
                      "type": "object",
                      "properties": {
                        "amount": {
                          "type": "object",
                          "properties": {
                            "currency": {"type": "string"},
                            "value": {"type": "integer"}
                          },
                          "required": ["currency", "value"]
                        },
                        "translated_copy": {"type": "string"},
                        "mode": {"type": "string"}
                      },
                      "required": ["amount", "translated_copy", "mode"]
                    },
              ```
              """
    url = "https://booking-com.p.rapidapi.com/v1/hotels/search-by-coordinates"
    querystring = {
        "adults_number": 2,
        "units": "metric",
        "latitude": latitude,
        "longitude": longitude,
        "checkin_date": checkin_date,
        "checkout_date": checkout_date,
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



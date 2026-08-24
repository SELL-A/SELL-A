import os
import requests

def Get_Policies_of_the_hotel(hotel_id):
    """
    :API_description: Retrieves detailed policy information for a specified hotel, including rules for children, extra beds, internet, parking, pets, age restrictions, and curfew, with multilingual support.
    :param hotel_id: The unique identifier for the hotel.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "hotel_id": {
      "type": "integer",
      "description": "Unique identifier for the hotel"
    },
    "policy": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "policy_id": {
            "type": ["string", "integer"],
            "description": "Policy identifier, can be numeric or empty string"
          },
          "content": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "languagecode": {
                  "type": "string",
                  "description": "Language code for the policy content"
                },
                "allow_children": {
                  "type": "integer",
                  "description": "Flag indicating if children are allowed (0 or 1)",
                  "optional": true
                },
                "cribs_and_extra_beds": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "highlight": {
                        "type": "integer",
                        "description": "Highlight flag (0 or 1)"
                      },
                      "text": {
                        "type": "string",
                        "description": "Policy text content"
                      }
                    },
                    "required": ["highlight", "text"]
                  },
                  "optional": true
                },
                "ruleset": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "name": {
                        "type": "string",
                        "description": "Name of the rule set"
                      },
                      "type": {
                        "type": "string",
                        "description": "Type identifier for the rule set"
                      },
                      "rule": {
                        "type": "array",
                        "items": {
                          "type": "object",
                          "properties": {
                            "content": {
                              "type": "string",
                              "description": "Rule content text"
                            },
                            "b_connection": {
                              "type": "string",
                              "description": "Connection type (e.g., wireless)",
                              "optional": true
                            },
                            "b_good_rule": {
                              "type": "integer",
                              "description": "Good rule indicator",
                              "optional": true
                            }
                          },
                          "required": ["content"]
                        }
                      }
                    },
                    "required": ["type", "rule"]
                  }
                },
                "type": {
                  "type": "string",
                  "description": "Policy type identifier"
                },
                "children_at_the_property": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "highlight": {
                        "type": "integer",
                        "description": "Highlight flag (0 or 1)"
                      },
                      "text": {
                        "type": "string",
                        "description": "Text about children policy"
                      }
                    },
                    "required": ["highlight", "text"]
                  },
                  "optional": true
                },
                "name": {
                  "type": "string",
                  "description": "Name of the policy"
                },
                "age_intervals": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "max_age": {
                        "type": "integer",
                        "description": "Maximum age for this interval"
                      },
                      "crib": {
                        "type": "object",
                        "properties": {
                          "price_type": {
                            "type": "string",
                            "description": "Type of pricing (free, fixed)"
                          },
                          "price_mode_n": {
                            "type": "integer",
                            "description": "Price mode numeric code"
                          },
                          "price_mode": {
                            "type": "string",
                            "description": "Price mode description"
                          },
                          "price": {
                            "type": ["integer", "string"],
                            "description": "Price amount"
                          },
                          "id": {
                            "type": "integer",
                            "description": "Unique identifier"
                          },
                          "guaranteed": {
                            "type": "integer",
                            "description": "Guaranteed availability flag"
                          },
                          "price_type_n": {
                            "type": "integer",
                            "description": "Price type numeric code"
                          }
                        },
                        "required": ["price_type", "price_mode", "price", "id"]
                      },
                      "min_age": {
                        "type": "integer",
                        "description": "Minimum age for this interval"
                      },
                      "group_by_price": {
                        "type": "object",
                        "description": "Price grouping by bed types"
                      },
                      "extra_bed": {
                        "type": "object",
                        "properties": {
                          "price_type": {
                            "type": "string",
                            "description": "Type of pricing"
                          },
                          "price_mode_n": {
                            "type": "integer",
                            "description": "Price mode numeric code"
                          },
                          "id": {
                            "type": "integer",
                            "description": "Unique identifier"
                          },
                          "price_mode": {
                            "type": "string",
                            "description": "Price mode description"
                          },
                          "price": {
                            "type": "string",
                            "description": "Price amount with currency"
                          },
                          "price_type_n": {
                            "type": "integer",
                            "description": "Price type numeric code"
                          }
                        },
                        "required": ["price_type", "price_mode", "price", "id"]
                      },
                      "types_by_price": {
                        "type": "array",
                        "items": {
                          "type": "array",
                          "items": {
                            "type": "string"
                          }
                        },
                        "description": "Bed types organized by price"
                      }
                    },
                    "required": ["max_age", "min_age"]
                  },
                  "optional": true
                }
              },
              "required": ["languagecode", "ruleset", "type", "name"]
            }
          },
          "type": {
            "type": "string",
            "description": "Policy category type"
          }
        },
        "required": ["content", "type"]
      }
    },
    "policygroup_id": {
      "type": "integer",
      "description": "Policy group identifier"
    },
    "name": {
      "type": "string",
      "description": "Name of the policy group"
    },
    "active_since": {
      "type": "string",
      "description": "Timestamp when the policy became active"
    },
    "policygroup_type_id": {
      "type": "integer",
      "description": "Policy group type identifier"
    }
  },
  "required": ["hotel_id", "policy", "policygroup_id", "name", "active_since", "policygroup_type_id"]
}
    ```
    """
    url = "https://booking-com.p.rapidapi.com/v1/hotels/policies"
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


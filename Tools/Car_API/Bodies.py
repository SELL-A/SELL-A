import os
import requests

def Bodies(sort="id", verbose="yes", direction="asc"):
    """
    :API_description: Retrieve detailed information about vehicle bodies, including dimensions, weight, and cargo capacity, with options to filter by year, make, model, and trim.
    :param sort: The attribute to sort the car bodies by(eg:id).
    :param verbose: Whether to include verbose information in the response(eg:yes).
    :param direction: The direction of sorting, either ascending or descending(eg:asc).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "collection": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string",
          "description": "The URL of the API endpoint."
        },
        "count": {
          "type": "integer",
          "description": "The number of items in the current page."
        },
        "pages": {
          "type": "integer",
          "description": "The total number of pages available."
        },
        "total": {
          "type": "integer",
          "description": "The total number of items available."
        },
        "next": {
          "type": "string",
          "description": "The URL for the next page of results."
        },
        "prev": {
          "type": "string",
          "description": "The URL for the previous page of results."
        },
        "first": {
          "type": "string",
          "description": "The URL for the first page of results."
        },
        "last": {
          "type": "string",
          "description": "The URL for the last page of results."
        }
      },
      "required": ["url", "count", "pages", "total", "next", "prev", "first", "last"]
    },
    "data": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "id": {
            "type": "integer",
            "description": "Unique identifier for the vehicle body."
          },
          "make_model_trim_id": {
            "type": "integer",
            "description": "Unique identifier for the vehicle make, model, and trim."
          },
          "type": {
            "type": "string",
            "description": "Type of the vehicle body (hidden for non-paying users)."
          },
          "doors": {
            "type": "integer",
            "description": "Number of doors in the vehicle."
          },
          "length": {
            "type": "string",
            "description": "Length of the vehicle."
          },
          "width": {
            "type": "string",
            "description": "Width of the vehicle."
          },
          "seats": {
            "type": "integer",
            "description": "Number of seats in the vehicle."
          },
          "height": {
            "type": "string",
            "description": "Height of the vehicle."
          },
          "wheel_base": {
            "type": "string",
            "description": "Wheel base of the vehicle."
          },
          "front_track": {
            "type": ["null", "string"],
            "description": "Front track of the vehicle."
          },
          "rear_track": {
            "type": ["null", "string"],
            "description": "Rear track of the vehicle."
          },
          "ground_clearance": {
            "type": "string",
            "description": "Ground clearance of the vehicle."
          },
          "cargo_capacity": {
            "type": "string",
            "description": "Cargo capacity of the vehicle."
          },
          "max_cargo_capacity": {
            "type": ["null", "string"],
            "description": "Maximum cargo capacity of the vehicle."
          },
          "curb_weight": {
            "type": "integer",
            "description": "Curb weight of the vehicle."
          },
          "gross_weight": {
            "type": ["null", "integer"],
            "description": "Gross weight of the vehicle."
          },
          "max_payload": {
            "type": ["null", "integer"],
            "description": "Maximum payload capacity of the vehicle."
          },
          "max_towing_capacity": {
            "type": ["null", "integer"],
            "description": "Maximum towing capacity of the vehicle."
          },
          "make_model_trim": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer",
                "description": "Unique identifier for the vehicle make, model, and trim."
              },
              "make_model_id": {
                "type": "integer",
                "description": "Unique identifier for the vehicle make and model."
              },
              "year": {
                "type": "integer",
                "description": "Year of the vehicle model."
              },
              "name": {
                "type": "string",
                "description": "Name of the vehicle model (hidden for non-paying users)."
              },
              "description": {
                "type": "string",
                "description": "Description of the vehicle model (hidden for non-paying users)."
              },
              "msrp": {
                "type": "integer",
                "description": "Manufacturer's Suggested Retail Price (MSRP) of the vehicle."
              },
              "invoice": {
                "type": "integer",
                "description": "Invoice price of the vehicle."
              },
              "created": {
                "type": "string",
                "format": "date-time",
                "description": "Timestamp when the vehicle model was created."
              },
              "modified": {
                "type": "string",
                "format": "date-time",
                "description": "Timestamp when the vehicle model was last modified."
              },
              "make_model": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Unique identifier for the vehicle make and model."
                  },
                  "make_id": {
                    "type": "integer",
                    "description": "Unique identifier for the vehicle make."
                  },
                  "name": {
                    "type": "string",
                    "description": "Name of the vehicle make and model (hidden for non-paying users)."
                  },
                  "make": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Unique identifier for the vehicle make."
                      },
                      "name": {
                        "type": "string",
                        "description": "Name of the vehicle make."
                      }
                    },
                    "required": ["id", "name"]
                  }
                },
                "required": ["id", "make_id", "name", "make"]
              },
              "__message": {
                "type": "string",
                "description": "Message indicating data limitations for non-paying users."
              }
            },
            "required": ["id", "make_model_id", "year", "name", "description", "msrp", "invoice", "created", "modified", "make_model", "__message"]
          },
          "__message": {
            "type": "string",
            "description": "Message indicating data limitations for non-paying users."
          }
        },
        "required": ["id", "make_model_trim_id", "type", "doors", "length", "width", "seats", "height", "wheel_base", "front_track", "rear_track", "ground_clearance", "cargo_capacity", "max_cargo_capacity", "curb_weight", "gross_weight", "max_payload", "max_towing_capacity", "make_model_trim", "__message"]
      }
    }
  },
  "required": ["collection", "data"]
}
    ```
    """
    url = "https://car-api2.p.rapidapi.com/api/bodies"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"sort": sort, "verbose": verbose, "direction": direction}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "car-api2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
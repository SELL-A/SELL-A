import os
import requests

def Trim_View(id):
    """
    :API_description: Retrieves comprehensive vehicle specifications including pricing, mileage, engine details, and make/model information.
    :param id: The unique identifier for the car trim.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "description": "Unique identifier for the vehicle."
    },
    "make_model_id": {
      "type": "integer",
      "description": "Unique identifier for the make and model combination."
    },
    "year": {
      "type": "integer",
      "description": "Year of the vehicle."
    },
    "name": {
      "type": "string",
      "description": "Name of the vehicle (hidden)."
    },
    "description": {
      "type": "string",
      "description": "Description of the vehicle (hidden)."
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
      "description": "Timestamp when the record was created."
    },
    "modified": {
      "type": "string",
      "format": "date-time",
      "description": "Timestamp when the record was last modified."
    },
    "make_model_trim_interior_colors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of interior colors available for the vehicle (hidden)."
    },
    "make_model_trim_exterior_colors": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "List of exterior colors available for the vehicle (hidden)."
    },
    "make_model_trim_mileage": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "make_model_trim_id": {
          "type": "integer"
        },
        "fuel_tank_capacity": {
          "type": "string"
        },
        "combined_mpg": {
          "type": "integer"
        },
        "epa_city_mpg": {
          "type": "integer"
        },
        "epa_highway_mpg": {
          "type": "integer"
        },
        "range_city": {
          "type": "integer"
        },
        "range_highway": {
          "type": "integer"
        },
        "battery_capacity_electric": {
          "type": "null"
        },
        "epa_time_to_charge_hr_240v_electric": {
          "type": "null"
        },
        "epa_kwh_100_mi_electric": {
          "type": "null"
        },
        "range_electric": {
          "type": "null"
        },
        "epa_highway_mpg_electric": {
          "type": "null"
        },
        "epa_city_mpg_electric": {
          "type": "null"
        },
        "epa_combined_mpg_electric": {
          "type": "null"
        }
      },
      "description": "Mileage and fuel-related details of the vehicle."
    },
    "make_model_trim_engine": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "make_model_trim_id": {
          "type": "integer"
        },
        "engine_type": {
          "type": "string"
        },
        "fuel_type": {
          "type": "string"
        },
        "cylinders": {
          "type": "string"
        },
        "size": {
          "type": "string"
        },
        "horsepower_hp": {
          "type": "integer"
        },
        "horsepower_rpm": {
          "type": "integer"
        },
        "torque_ft_lbs": {
          "type": "integer"
        },
        "torque_rpm": {
          "type": "integer"
        },
        "valves": {
          "type": "integer"
        },
        "valve_timing": {
          "type": "string"
        },
        "cam_type": {
          "type": "string"
        },
        "drive_type": {
          "type": "string"
        },
        "transmission": {
          "type": "string"
        }
      },
      "description": "Engine specifications of the vehicle."
    },
    "make_model_trim_body": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "make_model_trim_id": {
          "type": "integer"
        },
        "type": {
          "type": "string"
        },
        "doors": {
          "type": "integer"
        },
        "length": {
          "type": "string"
        },
        "width": {
          "type": "string"
        },
        "seats": {
          "type": "integer"
        },
        "height": {
          "type": "string"
        },
        "wheel_base": {
          "type": "string"
        },
        "front_track": {
          "type": "null"
        },
        "rear_track": {
          "type": "null"
        },
        "ground_clearance": {
          "type": "string"
        },
        "cargo_capacity": {
          "type": "string"
        },
        "max_cargo_capacity": {
          "type": "null"
        },
        "curb_weight": {
          "type": "integer"
        },
        "gross_weight": {
          "type": "null"
        },
        "max_payload": {
          "type": "null"
        },
        "max_towing_capacity": {
          "type": "null"
        }
      },
      "description": "Body specifications of the vehicle."
    },
    "make_model": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "make_id": {
          "type": "integer"
        },
        "name": {
          "type": "string"
        },
        "make": {
          "type": "object",
          "properties": {
            "id": {
              "type": "integer"
            },
            "name": {
              "type": "string"
            }
          }
        }
      },
      "description": "Details about the make and model of the vehicle."
    },
    "__message": {
      "type": "string",
      "description": "Message regarding data access limitations."
    }
  },
  "required": [
    "id",
    "make_model_id",
    "year",
    "name",
    "description",
    "msrp",
    "invoice",
    "created",
    "modified",
    "make_model_trim_interior_colors",
    "make_model_trim_exterior_colors",
    "make_model_trim_mileage",
    "make_model_trim_engine",
    "make_model_trim_body",
    "make_model",
    "__message"
  ]
}
```
    """
    url = f"https://car-api2.p.rapidapi.com/api/trims/{id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "car-api2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
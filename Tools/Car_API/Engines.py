import os
import requests

def Engines(verbose="yes", direction="asc", sort="id"):
    """
    :API_description: Retrieve detailed information about vehicle engines, including specifications and performance metrics. The response can be customized with optional parameters for filtering and pagination.
    :param verbose: Specifies whether to include detailed information in the response.
    :param direction: Specifies the direction of sorting, either ascending or descending.
    :param sort: Specifies the field by which the results should be sorted.
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
          "description": "The URL endpoint for the API request."
        },
        "count": {
          "type": "integer",
          "description": "The number of items returned in the current page."
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
            "description": "Unique identifier for the engine."
          },
          "make_model_trim_id": {
            "type": "integer",
            "description": "Unique identifier for the make, model, and trim combination."
          },
          "engine_type": {
            "type": "string",
            "description": "Type of the engine (hidden for non-paying users)."
          },
          "fuel_type": {
            "type": "string",
            "description": "Type of fuel used by the engine (hidden for non-paying users)."
          },
          "cylinders": {
            "type": "string",
            "description": "Number of cylinders in the engine (hidden for non-paying users)."
          },
          "size": {
            "type": "string",
            "description": "Size of the engine in liters."
          },
          "horsepower_hp": {
            "type": "integer",
            "description": "Horsepower of the engine."
          },
          "horsepower_rpm": {
            "type": "integer",
            "description": "RPM at which the engine produces maximum horsepower."
          },
          "torque_ft_lbs": {
            "type": "integer",
            "description": "Torque of the engine in foot-pounds."
          },
          "torque_rpm": {
            "type": "integer",
            "description": "RPM at which the engine produces maximum torque."
          },
          "valves": {
            "type": "integer",
            "description": "Number of valves in the engine."
          },
          "valve_timing": {
            "type": "string",
            "description": "Valve timing mechanism (hidden for non-paying users)."
          },
          "cam_type": {
            "type": "string",
            "description": "Type of camshaft (hidden for non-paying users)."
          },
          "drive_type": {
            "type": "string",
            "description": "Type of drive system (hidden for non-paying users)."
          },
          "transmission": {
            "type": "string",
            "description": "Type of transmission (hidden for non-paying users)."
          },
          "make_model_trim": {
            "type": "object",
            "properties": {
              "id": {
                "type": "integer",
                "description": "Unique identifier for the make, model, and trim combination."
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
                "description": "Name of the trim (hidden for non-paying users)."
              },
              "description": {
                "type": "string",
                "description": "Description of the trim (hidden for non-paying users)."
              },
              "msrp": {
                "type": "integer",
                "description": "Manufacturer's suggested retail price."
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
              "make_model": {
                "type": "object",
                "properties": {
                  "id": {
                    "type": "integer",
                    "description": "Unique identifier for the make and model combination."
                  },
                  "make_id": {
                    "type": "integer",
                    "description": "Unique identifier for the make."
                  },
                  "name": {
                    "type": "string",
                    "description": "Name of the model (hidden for non-paying users)."
                  },
                  "make": {
                    "type": "object",
                    "properties": {
                      "id": {
                        "type": "integer",
                        "description": "Unique identifier for the make."
                      },
                      "name": {
                        "type": "string",
                        "description": "Name of the make."
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
        "required": ["id", "make_model_trim_id", "engine_type", "fuel_type", "cylinders", "size", "horsepower_hp", "horsepower_rpm", "torque_ft_lbs", "torque_rpm", "valves", "valve_timing", "cam_type", "drive_type", "transmission", "make_model_trim", "__message"]
      }
    }
  },
  "required": ["collection", "data"]
}
    ```
    """
    url = "https://car-api2.p.rapidapi.com/api/engines"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"verbose": verbose, "direction": direction, "sort": sort}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "car-api2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
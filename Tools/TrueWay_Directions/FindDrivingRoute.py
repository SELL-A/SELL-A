import os
import requests

def FindDrivingRoute(stops):
    """
    :API_description: Find the best driving route between multiple stops, with options to optimize, avoid specific road types, and specify geometry format.
    :param stops: A string representing the coordinates of the stops in the format "lat1,lon1;lat2,lon2;...".
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "route": {
      "type": "object",
      "properties": {
        "distance": {
          "type": "integer",
          "description": "Total distance of the route in meters."
        },
        "duration": {
          "type": "integer",
          "description": "Total duration of the route in seconds."
        },
        "bounds": {
          "type": "object",
          "properties": {
            "south": {
              "type": "number",
              "description": "Southernmost latitude of the route bounds."
            },
            "west": {
              "type": "number",
              "description": "Westernmost longitude of the route bounds."
            },
            "north": {
              "type": "number",
              "description": "Northernmost latitude of the route bounds."
            },
            "east": {
              "type": "number",
              "description": "Easternmost longitude of the route bounds."
            }
          },
          "required": ["south", "west", "north", "east"]
        },
        "geometry": {
          "type": "object",
          "properties": {
            "coordinates": {
              "type": "array",
              "items": {
                "type": "array",
                "items": [
                  {
                    "type": "number",
                    "description": "Latitude of a point on the route."
                  },
                  {
                    "type": "number",
                    "description": "Longitude of a point on the route."
                  }
                ]
              },
              "description": "List of coordinate pairs representing the route geometry."
            }
          },
          "required": ["coordinates"]
        }
      },
      "required": ["distance", "duration", "bounds", "geometry"]
    },
    "legs": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "distance": {
            "type": "integer",
            "description": "Distance of the leg in meters."
          },
          "duration": {
            "type": "integer",
            "description": "Duration of the leg in seconds."
          },
          "start_point_index": {
            "type": "integer",
            "description": "Index of the starting point in the route's coordinates array."
          },
          "start_point": {
            "type": "object",
            "properties": {
              "lat": {
                "type": "number",
                "description": "Latitude of the starting point."
              },
              "lng": {
                "type": "number",
                "description": "Longitude of the starting point."
              }
            },
            "required": ["lat", "lng"]
          },
          "end_point_index": {
            "type": "integer",
            "description": "Index of the ending point in the route's coordinates array."
          },
          "end_point": {
            "type": "object",
            "properties": {
              "lat": {
                "type": "number",
                "description": "Latitude of the ending point."
              },
              "lng": {
                "type": "number",
                "description": "Longitude of the ending point."
              }
            },
            "required": ["lat", "lng"]
          },
          "bounds": {
            "type": "object",
            "properties": {
              "south": {
                "type": "number",
                "description": "Southernmost latitude of the leg bounds."
              },
              "west": {
                "type": "number",
                "description": "Westernmost longitude of the leg bounds."
              },
              "north": {
                "type": "number",
                "description": "Northernmost latitude of the leg bounds."
              },
              "east": {
                "type": "number",
                "description": "Easternmost longitude of the leg bounds."
              }
            },
            "required": ["south", "west", "north", "east"]
          },
          "steps": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "distance": {
                  "type": "integer",
                  "description": "Distance of the step in meters."
                },
                "duration": {
                  "type": "integer",
                  "description": "Duration of the step in seconds."
                },
                "start_point_index": {
                  "type": "integer",
                  "description": "Index of the starting point in the route's coordinates array."
                },
                "start_point": {
                  "type": "object",
                  "properties": {
                    "lat": {
                      "type": "number",
                      "description": "Latitude of the starting point."
                    },
                    "lng": {
                      "type": "number",
                      "description": "Longitude of the starting point."
                    }
                  },
                  "required": ["lat", "lng"]
                },
                "end_point_index": {
                  "type": "integer",
                  "description": "Index of the ending point in the route's coordinates array."
                },
                "end_point": {
                  "type": "object",
                  "properties": {
                    "lat": {
                      "type": "number",
                      "description": "Latitude of the ending point."
                    },
                    "lng": {
                      "type": "number",
                      "description": "Longitude of the ending point."
                    }
                  },
                  "required": ["lat", "lng"]
                },
                "bounds": {
                  "type": "object",
                  "properties": {
                    "south": {
                      "type": "number",
                      "description": "Southernmost latitude of the step bounds."
                    },
                    "west": {
                      "type": "number",
                      "description": "Westernmost longitude of the step bounds."
                    },
                    "north": {
                      "type": "number",
                      "description": "Northernmost latitude of the step bounds."
                    },
                    "east": {
                      "type": "number",
                      "description": "Easternmost longitude of the step bounds."
                    }
                  },
                  "required": ["south", "west", "north", "east"]
                },
                "maneuver": {
                  "type": "string",
                  "description": "Type of maneuver to be performed at the end of the step (e.g., 'turn right', 'turn left')."
                }
              },
              "required": ["distance", "duration", "start_point_index", "start_point", "end_point_index", "end_point", "bounds"]
            }
          }
        },
        "required": ["distance", "duration", "start_point_index", "start_point", "end_point_index", "end_point", "bounds", "steps"]
      }
    }
  },
  "required": ["route", "legs"]
}
    ```
    """
    url = "https://trueway-directions2.p.rapidapi.com/FindDrivingRoute"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"stops": stops}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "trueway-directions2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


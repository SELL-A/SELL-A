import os
import requests

def FindDrivingPath(origin, destination):
    """
    :API_description: Find the best driving route between an origin and a destination, with options to include waypoints, avoid certain road types, and specify travel start time.
    :param origin: The starting point of the route in "latitude,longitude" format(e.g., 40.629041,-74.025606).
    :param destination: The endpoint of the route in "latitude,longitude" format(e.g., 40.712822,-74.005942).
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
              "description": "Array of coordinate pairs representing the route path."
            }
          },
          "required": ["coordinates"]
        },
        "steps": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "distance": {
                "type": "integer",
                "description": "Distance of this step in meters."
              },
              "duration": {
                "type": "integer",
                "description": "Duration of this step in seconds."
              },
              "start_point_index": {
                "type": "integer",
                "description": "Index of the starting point in the coordinates array."
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
                "description": "Index of the ending point in the coordinates array."
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
                    "description": "Southernmost latitude of this step's bounds."
                  },
                  "west": {
                    "type": "number",
                    "description": "Westernmost longitude of this step's bounds."
                  },
                  "north": {
                    "type": "number",
                    "description": "Northernmost latitude of this step's bounds."
                  },
                  "east": {
                    "type": "number",
                    "description": "Easternmost longitude of this step's bounds."
                  }
                },
                "required": ["south", "west", "north", "east"]
              },
              "maneuver": {
                "type": "string",
                "description": "Type of maneuver required at the end of this step (e.g., 'turn right', 'turn left')."
              }
            },
            "required": ["distance", "duration", "start_point_index", "start_point", "end_point_index", "end_point", "bounds"]
          },
          "description": "Array of steps along the route, each describing a segment of the journey."
        }
      },
      "required": ["distance", "duration", "bounds", "geometry", "steps"]
    }
  },
  "required": ["route"]
}
    ```
    """
    url = "https://trueway-directions2.p.rapidapi.com/FindDrivingPath"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"origin": origin, "destination": destination}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "trueway-directions2.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


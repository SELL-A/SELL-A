import os
import requests

def ReverseGeocoding(lat, lon, zoom=10, addressdetails=1, namedetails=0, accept_language='en', format='json', polygon_text=0, polygon_kml=0, polygon_svg=0, polygon_geojson=0, polygon_threshold=0.0, limit=1):
    """
    :API_description: Retrieve detailed address and geographical information based on latitude and longitude coordinates.
    :param lat: Latitude of the location(eg. "52.520000").
    :param lon: Longitude of the location(eg. "13.405000").
    :param zoom: Level of detail required in the response(eg. "10").
    :param addressdetails: Include address details in the response(eg. "1").
    :param namedetails: Include name details in the response(eg. "0").
    :param accept_language: Language of the response(eg. "en").
    :param format: Format of the response(eg. "json").
    :param polygon_text: Include polygon text in the response(eg. "0").
    :param polygon_kml: Include polygon KML in the response(eg. "0").
    :param polygon_svg: Include polygon SVG in the response(eg. "0").
    :param polygon_geojson: Include polygon GeoJSON in the response(eg. "0").
    :param polygon_threshold: Threshold for polygon simplification(eg. "0.0").
    :param limit: Limit the number of results(eg. "1").
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "licence": {
      "type": "string",
      "description": "The license under which the data is distributed."
    },
    "osm_id": {
      "type": "integer",
      "description": "Unique identifier for the OpenStreetMap entity."
    },
    "address": {
      "type": "object",
      "properties": {
        "state": {
          "type": "string",
          "description": "The state where the location is situated."
        },
        "country_code": {
          "type": "string",
          "description": "The ISO 3166-1 alpha-2 country code."
        },
        "country": {
          "type": "string",
          "description": "The name of the country."
        },
        "city": {
          "type": "string",
          "description": "The city where the location is situated."
        },
        "ISO3166-2-lvl4": {
          "type": "string",
          "description": "The ISO 3166-2 code for the sub-national entity."
        },
        "county": {
          "type": "string",
          "description": "The county where the location is situated."
        }
      },
      "description": "Detailed address information."
    },
    "osm_type": {
      "type": "string",
      "description": "The type of OpenStreetMap entity (e.g., relation, node, way)."
    },
    "boundingbox": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Array of latitude and longitude values defining the bounding box of the location."
    },
    "place_id": {
      "type": "integer",
      "description": "Unique identifier for the place."
    },
    "lat": {
      "type": "string",
      "description": "Latitude of the location."
    },
    "lon": {
      "type": "string",
      "description": "Longitude of the location."
    },
    "display_name": {
      "type": "string",
      "description": "Human-readable name of the location."
    }
  },
  "required": ["licence", "osm_id", "address", "osm_type", "boundingbox", "place_id", "lat", "lon", "display_name"]
}
```
    """
    url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/reverse"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "lat": lat,
        "lon": lon,
        "zoom": zoom,
        "addressdetails": addressdetails,
        "namedetails": namedetails,
        "accept-language": accept_language,
        "format": format,
        "polygon_text": polygon_text,
        "polygon_kml": polygon_kml,
        "polygon_svg": polygon_svg,
        "polygon_geojson": polygon_geojson,
        "polygon_threshold": polygon_threshold,
        "limit": limit
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "forward-reverse-geocoding.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
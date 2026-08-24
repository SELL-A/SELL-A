import os
import requests

def ForwardGeocoding(format, street, city, state, postalcode, country, addressdetails, accept_language, namedetails, limit, bounded, polygon_text, polygon_kml, polygon_svg, polygon_geojson, polygon_threshold):
    """
    :API_description: Convert an address into geographical coordinates (latitude and longitude) for mapping or geolocation services.
    :param format: The format of the response, e.g., 'json'.
    :param street: The street address.
    :param city: The city name.
    :param state: The state code(eg. "CA").
    :param postalcode: The postal code(eg. "10011").
    :param country: The country name.
    :param addressdetails: Whether to include address details in the response(eg. "1").
    :param accept_language: The language for the response(eg. "en").
    :param namedetails: Whether to include name details in the response(eg. "0").
    :param limit: The maximum number of results to return.
    :param bounded: Whether the search should be bounded.
    :param polygon_text: Whether to include polygon text in the response(eg. "0").
    :param polygon_kml: Whether to include polygon KML in the response(eg. "0").
    :param polygon_svg: Whether to include polygon SVG in the response(eg. "0").
    :param polygon_geojson: Whether to include polygon GeoJSON in the response(eg. "0").
    :param polygon_threshold: The threshold for polygon simplification(eg. "0.0").
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "importance": {
        "type": "number",
        "description": "A numerical value indicating the importance of the location."
      },
      "licence": {
        "type": "string",
        "description": "The license under which the data is distributed."
      },
      "class": {
        "type": "string",
        "description": "The class of the location, typically indicating its type (e.g., 'amenity')."
      },
      "address": {
        "type": "object",
        "properties": {
          "road": {
            "type": "string",
            "description": "The name of the road where the location is situated."
          },
          "state": {
            "type": "string",
            "description": "The state where the location is located."
          },
          "ISO3166-2-lvl4": {
            "type": "string",
            "description": "The ISO 3166-2 code for the state or region."
          },
          "county": {
            "type": "string",
            "description": "The county where the location is located."
          },
          "country_code": {
            "type": "string",
            "description": "The country code of the location."
          },
          "house_number": {
            "type": "string",
            "description": "The house number of the location."
          },
          "city": {
            "type": "string",
            "description": "The city where the location is located."
          },
          "suburb": {
            "type": "string",
            "description": "The suburb where the location is located."
          },
          "country": {
            "type": "string",
            "description": "The country where the location is located."
          },
          "neighbourhood": {
            "type": "string",
            "description": "The neighbourhood where the location is located."
          },
          "amenity": {
            "type": "string",
            "description": "The type of amenity at the location."
          },
          "postcode": {
            "type": "string",
            "description": "The postal code of the location."
          }
        },
        "required": [
          "road",
          "state",
          "ISO3166-2-lvl4",
          "county",
          "country_code",
          "house_number",
          "city",
          "suburb",
          "country",
          "neighbourhood",
          "amenity",
          "postcode"
        ]
      },
      "osm_id": {
        "type": "integer",
        "description": "The OpenStreetMap ID of the location."
      },
      "display_name": {
        "type": "string",
        "description": "A human-readable name for the location."
      },
      "osm_type": {
        "type": "string",
        "description": "The type of OpenStreetMap object (e.g., 'node')."
      },
      "lon": {
        "type": "string",
        "description": "The longitude of the location."
      },
      "place_id": {
        "type": "integer",
        "description": "The unique identifier for the location in the OpenStreetMap database."
      },
      "boundingbox": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "An array of strings representing the bounding box coordinates of the location."
      },
      "lat": {
        "type": "string",
        "description": "The latitude of the location."
      },
      "type": {
        "type": "string",
        "description": "The type of the location (e.g., 'cinema')."
      }
    },
    "required": [
      "importance",
      "licence",
      "class",
      "address",
      "osm_id",
      "display_name",
      "osm_type",
      "lon",
      "place_id",
      "boundingbox",
      "lat",
      "type"
    ]
  }
}
```
    """
    url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/forward"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "format": format,
        "street": street,
        "city": city,
        "state": state,
        "postalcode": postalcode,
        "country": country,
        "addressdetails": addressdetails,
        "accept-language": accept_language,
        "namedetails": namedetails,
        "limit": limit,
        "bounded": bounded,
        "polygon_text": polygon_text,
        "polygon_kml": polygon_kml,
        "polygon_svg": polygon_svg,
        "polygon_geojson": polygon_geojson,
        "polygon_threshold": polygon_threshold
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

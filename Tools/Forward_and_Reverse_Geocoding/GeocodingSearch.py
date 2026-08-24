import os
import requests

def GeocodingSearch(q, format="json", addressdetails="1", namedetails="0", accept_language="en", limit="5", bounded="0", polygon_text="0", polygon_svg="0", polygon_kml="0", polygon_geojson="0", polygon_threshold="0.0"):
    """
    :API_description: Provides detailed location information including coordinates, addresses, and administrative boundaries sourced from OpenStreetMap.
    :param q: The query string for the location search (e.g., "New York City NY USA").
    :param format: The format of the response (default is "json").
    :param addressdetails: Include address details in the response (default is "1").
    :param namedetails: Include name details in the response (default is "0").
    :param accept_language: Language for the response (default is "en").
    :param limit: Limit the number of results (default is "5").
    :param bounded: Whether the search is bounded (default is "0").
    :param polygon_text: Include polygon text in the response (default is "0").
    :param polygon_svg: Include polygon SVG in the response (default is "0").
    :param polygon_kml: Include polygon KML in the response (default is "0").
    :param polygon_geojson: Include polygon GeoJSON in the response (default is "0").
    :param polygon_threshold: Threshold for polygon inclusion (default is "0.0").
    :response_schema: 
    ```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "importance": {
        "type": "number",
        "description": "A numerical value indicating the importance or relevance of the location."
      },
      "licence": {
        "type": "string",
        "description": "The license under which the data is distributed."
      },
      "class": {
        "type": "string",
        "description": "The class of the location, such as 'boundary' or 'leisure'."
      },
      "address": {
        "type": "object",
        "properties": {
          "city": {
            "type": "string",
            "description": "The city where the location is situated."
          },
          "country": {
            "type": "string",
            "description": "The country where the location is situated."
          },
          "country_code": {
            "type": "string",
            "description": "The ISO 3166-1 alpha-2 country code."
          },
          "ISO3166-2-lvl4": {
            "type": "string",
            "description": "The ISO 3166-2 code for the subdivision (level 4)."
          },
          "state": {
            "type": "string",
            "description": "The state or province where the location is situated."
          },
          "road": {
            "type": "string",
            "description": "The road name where the location is situated."
          },
          "town": {
            "type": "string",
            "description": "The town where the location is situated."
          },
          "county": {
            "type": "string",
            "description": "The county where the location is situated."
          },
          "postcode": {
            "type": "string",
            "description": "The postal code of the location."
          },
          "leisure": {
            "type": "string",
            "description": "The type of leisure activity associated with the location."
          }
        },
        "description": "The address details of the location."
      },
      "osm_id": {
        "type": "integer",
        "description": "The OpenStreetMap ID of the location."
      },
      "display_name": {
        "type": "string",
        "description": "The human-readable name of the location."
      },
      "osm_type": {
        "type": "string",
        "description": "The type of OpenStreetMap object (e.g., 'relation', 'way')."
      },
      "lon": {
        "type": "string",
        "description": "The longitude of the location."
      },
      "place_id": {
        "type": "integer",
        "description": "The unique identifier for the place."
      },
      "boundingbox": {
        "type": "array",
        "items": {
          "type": "string"
        },
        "description": "The bounding box coordinates of the location."
      },
      "lat": {
        "type": "string",
        "description": "The latitude of the location."
      },
      "type": {
        "type": "string",
        "description": "The type of the location, such as 'administrative' or 'garden'."
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
    url = "https://forward-reverse-geocoding.p.rapidapi.com/v1/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "q": q,
        "format": format,
        "addressdetails": addressdetails,
        "namedetails": namedetails,
        "accept-language": accept_language,
        "limit": limit,
        "bounded": bounded,
        "polygon_text": polygon_text,
        "polygon_svg": polygon_svg,
        "polygon_kml": polygon_kml,
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
        


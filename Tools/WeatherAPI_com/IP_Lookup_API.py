import os
import requests

def IP_Lookup_API(q:str):
    """
    :API_description: The IP Lookup API provides detailed geolocation information for an IP address, including continent, country, city, region, latitude, longitude, timezone, and local time.
    :param q: e.g: q=auto:ip IP address (IPv4 and IPv6 supported) e.g: q=100.0.0.1
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "ip": {
      "type": "string",
      "description": "The IP address of the client making the request."
    },
    "type": {
      "type": "string",
      "description": "The type of IP address (e.g., 'ipv4')."
    },
    "continent_code": {
      "type": "string",
      "description": "The code representing the continent associated with the IP address."
    },
    "continent_name": {
      "type": "string",
      "description": "The name of the continent associated with the IP address."
    },
    "country_code": {
      "type": "string",
      "description": "The ISO 3166-1 alpha-2 country code associated with the IP address."
    },
    "country_name": {
      "type": "string",
      "description": "The name of the country associated with the IP address."
    },
    "is_eu": {
      "type": "string",
      "description": "Indicates whether the country is a member of the European Union ('true' or 'false')."
    },
    "geoname_id": {
      "type": "integer",
      "description": "The GeoName ID associated with the location."
    },
    "city": {
      "type": "string",
      "description": "The name of the city associated with the IP address."
    },
    "region": {
      "type": "string",
      "description": "The name of the region (state or province) associated with the IP address."
    },
    "lat": {
      "type": "number",
      "description": "The latitude of the location associated with the IP address."
    },
    "lon": {
      "type": "number",
      "description": "The longitude of the location associated with the IP address."
    },
    "tz_id": {
      "type": "string",
      "description": "The timezone ID associated with the location."
    },
    "localtime_epoch": {
      "type": "integer",
      "description": "The local time in epoch format."
    },
    "localtime": {
      "type": "string",
      "description": "The local time in ISO 8601 format."
    }
  },
  "required": [
    "ip",
    "type",
    "continent_code",
    "continent_name",
    "country_code",
    "country_name",
    "is_eu",
    "geoname_id",
    "city",
    "region",
    "lat",
    "lon",
    "tz_id",
    "localtime_epoch",
    "localtime"
  ]
}
```
    """
    url = "https://weatherapi-com.p.rapidapi.com/ip.json"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    params = {
        "q": q
    }
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "weatherapi-com.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

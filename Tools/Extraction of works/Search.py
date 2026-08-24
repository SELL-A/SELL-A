import os
import requests

def Search(query):
    """
    :API_description: Retrieve a list of works related to blood, including metadata like DOI, title, and author information.
    :param query: The search query string (required).
    :response_schema: 
    ```json
{
  "status": "string",
  "message-type": "string",
  "message-version": "string",
  "message": {
    "facets": {},
    "total-results": "integer",
    "items": [
      {
        "indexed": {
          "date-parts": [["integer"]],
          "date-time": "string",
          "timestamp": "integer",
          "version": "string"
        },
        "reference-count": "integer",
        "publisher": "string",
        "isbn-type": [
          {
            "value": "string",
            "type": "string"
          }
        ],
        "content-domain": {
          "domain": ["string"],
          "crossmark-restriction": "boolean"
        },
        "published-print": {
          "date-parts": [["integer"]]
        },
        "abstract": "string",
        "DOI": "string",
        "type": "string",
        "created": {
          "date-parts": [["integer"]],
          "date-time": "string",
          "timestamp": "integer"
        },
        "page": "string",
        "source": "string",
        "is-referenced-by-count": "integer",
        "title": ["string"],
        "prefix": "string",
        "author": [
          {
            "given": "string",
            "family": "string",
            "sequence": "string",
            "affiliation": []
          }
        ],
        "member": "string",
        "published-online": {
          "date-parts": [["integer"]]
        },
        "container-title": ["string"],
        "original-title": ["string"],
        "language": "string",
        "deposited": {
          "date-parts": [["integer"]],
          "date-time": "string",
          "timestamp": "integer"
        },
        "score": "number",
        "resource": {
          "primary": {
            "URL": "string"
          }
        },
        "issued": {
          "date-parts": [["integer"]]
        },
        "ISBN": ["string"],
        "references-count": "integer",
        "URL": "string",
        "published": {
          "date-parts": [["integer"]]
        },
        "standards-body": {
          "name": "string",
          "acronym": "string"
        },
        "description": "string",
        "license": [
          {
            "start": {
              "date-parts": [["integer"]],
              "date-time": "string",
              "timestamp": "integer"
            },
            "content-version": "string",
            "delay-in-days": "integer",
            "URL": "string"
          }
        ],
        "posted": {
          "date-parts": [["integer"]]
        },
        "publisher-location": "string",
        "issue": "string",
        "link": [
          {
            "URL": "string",
            "content-type": "string",
            "content-version": "string",
            "intended-application": "string"
          }
        ],
        "subtype": "string"
      }
    ]
  }
}
```
    """
    url = "https://crossref.p.rapidapi.com/"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"query": query}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "crossref.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
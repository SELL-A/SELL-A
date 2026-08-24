import os
import requests

def auto_complete(query):
    """
    :API_description: Provides auto-complete suggestions
    :param query: The search query string for which auto-complete suggestions are needed.
    :response_schema: 
'''json
{
  "people": [
    {
      "id": 51516124,
      "type": "user",
      "score": 1108.6741,
      "url": "/user/51516124",
      "name": "Tim <b>Apple</b>",
      "slug": "tim-apple",
      "image_url": "..."
    },
    {
      "id": 2806791,
      "type": "user",
      "score": 571.4988,
      "url": "/user/2806791",
      "name": "<b>Apple53</b>",
      "slug": "apple53",
      "image_url": "..."
    },
    {
      "id": 30855475,
      "type": "user",
      "score": 568.0078,
      "url": "/user/30855475",
      "name": "<b>Apple</b> Eye",
      "slug": "apple-eye",
      "image_url": "..."
    }
  ],
  "symbols": [
    {
      "id": 146,
      "type": "symbol",
      "score": 32228.525,
      "url": "/symbol/AAPL",
      "name": "AAPL",
      "content": "<b>Apple</b> Inc.",
      "slug": "aapl",
      "image": {
        "light": "https://static.seekingalpha.com/cdn/s3/company_logos/mark_vector_light/AAPL.svg",
        "dark": "https://static.seekingalpha.com/cdn/s3/company_logos/mark_vector_dark/AAPL.svg"
      }
    },
    {
      "id": 513836,
      "type": "symbol",
      "score": 21158.102,
      "url": "/symbol/APLE",
      "name": "APLE",
      "content": "<b>Apple</b> Hospitality REIT, Inc.",
      "slug": "aple",
      "image": {
        "light": "https://static.seekingalpha.com/cdn/s3/company_logos/mark_vector_light/APLE.svg",
        "dark": "https://static.seekingalpha.com/cdn/s3/company_logos/mark_vector_dark/APLE.svg"
      }
    },
    {
      "id": 764528,
      "type": "symbol",
      "score": 15964.588,
      "url": "/symbol/AAPL:CA",
      "name": "AAPL:CA",
      "content": "<b>Apple</b> Inc.",
      "slug": "aapl:ca",
      "image": {
        "light": "https://static.seekingalpha.com/cdn/s3/company_logos/mark_vector_light/AAPL:CA.svg",
        "dark": "https://static.seekingalpha.com/cdn/s3/company_logos/mark_vector_dark/AAPL:CA.svg"
      }
    }
  ],
  "pages": [
    {
      "id": 332,
      "type": "page",
      "score": 2520.3064,
      "url": "comparison/9e-FAANG-Stocks",
      "name": "FAANG Stocks Comparison"
    }
  ]


}'''
    """
    url = "https://seeking-alpha.p.rapidapi.com/v2/auto-complete"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"query": query}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "seeking-alpha.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")



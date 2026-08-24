import os
import requests

def News_Topics():
    """
    :API_description: Retrieve trending news stories grouped by topics, ordered by popularity. Topics and stories update hourly.
    :param None
    :response_schema: 
    ```json
{
  "figure_of_the_day": "...",
  "market_summary": "...",
  "most_important_story": {
    "domain": "yahoo.com",
    "hash": "p9z6v8",
    "headline": "...",
    "id": "4cc86b9bee2642ba",
    "img": {
      "s": "4cc86b9bee2642ba_s.webp",
      "sq": "4cc86b9bee2642ba_sq.webp"
    },
    "snippet": "...",
    "url": "..."
  },
  "most_negative_story": {
    "domain": "reuters.com",
    "hash": "pvnqqb",
    "id": "5e98181ecc3b2102",
    "img": {
      "s": "5e98181ecc3b2102_s.webp",
      "sq": "5e98181ecc3b2102_sq.webp"
    },
    "snippet": "...",
    "title": "...",
    "url": "..."
  },
  "most_positive_story": {
    "domain": "cnbc.com",
    "hash": "prxuoc",
    "id": "ce86a671f42cef73",
    "img": {
      "s": "ce86a671f42cef73_s.webp",
      "sq": "ce86a671f42cef73_sq.webp"
    },
    "snippet": "...",
    "title": "...",
    "url": "..."
  },
  "news_cluster": [
    [
      {
        "domain": "yahoo.com",
        "hash": "pp7oqs",
        "id": "4cc86b9bee2642ba",
        "img": {
          "s": "4cc86b9bee2642ba_s.webp",
          "sq": "4cc86b9bee2642ba_sq.webp"
        },
        "summary": "...",
        "title": "...",
        "url": "..."
      },
      {
        "domain": "abcnews.com",
        "hash": "p5djf3",
        "id": "c96449c32349f64e",
        "img": {
          "s": "c96449c32349f64e_s.webp",
          "sq": "c96449c32349f64e_sq.webp"
        },
        "summary": "...",
        "title": "...",
        "url": "..."
      }
    ],
    [
      {
        "domain": "cnbc.com",
        "hash": "pthds0",
        "id": "d2934f035555c2ca",
        "img": {
          "s": "d2934f035555c2ca_s.webp",
          "sq": "d2934f035555c2ca_sq.webp"
        },
        "summary": "...",
        "title": "...",
        "url": "..."
      },
      {
        "domain": "breakingthenews.net",
        "hash": "pkqiod",
        "id": "e65ff5c2a4dd51e2",
        "img": {
          "s": "e65ff5c2a4dd51e2_s.webp",
          "sq": "e65ff5c2a4dd51e2_sq.webp"
        },
        "summary": "...",
        "title": "...",
        "url": "..."
      }
    ]
  ],
  "policy_changes": "...",
  "quote_of_the_day": {
    "quote": "“Blaming AI for layoffs is a lazy excuse.”",
    "speaker": "Jensen Huang, Nvidia CEO"
  },
  "timestamp": "Thu, 28 May 2026 05:51:19 GMT",
  "version": 1
}
```

    """
    url = "https://biztoc.p.rapidapi.com/news/topics"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "biztoc.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
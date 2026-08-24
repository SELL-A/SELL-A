import os
import requests

def News_Source(source_id):
    """
    :API_description: Retrieve the latest news articles from a specified source, ordered by publication date.
    :param source_id: The ID of the news source to retrieve articles from ,the allowed value are tfswallst,abc,apnews,abnormalreturns,asiafinancial,blockworks,bbc,axios,marketbeat,barrons,cbc,cbs,cnn,reddit.
    :response_schema: 
    ```json
[
  {
    "body": "...",
    "img": {
      "s": "...",
      "sq": "..."
    },
    "published": "Thu, 28 May 2026 06:44:47 GMT",
    "title": "The £5 coffee that tells a story of global economic turmoil",
    "url": "..."
  },
  {
    "body": "...",
    "img": {
      "s": "...",
      "sq": "..."
    },
    "published": "Thu, 28 May 2026 04:30:00 GMT",
    "title": "Oil prices jump after US launches new attacks on Iran",
    "url": "..."
  }
]
```

    """
    url = f"https://biztoc.p.rapidapi.com/news/source/{source_id}"
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

import os
import requests

def News_Latest():
    """
    :API_description: Retrieve a list of the latest news articles, including titles, sources, publication dates, and URLs.
    :param None
    :response_schema: 
    ```json
[
  {
    "body": "...",
    "domain": "roadandtrack.com",
    "img": {
      "s": "...",
      "sq": "..."
    },
    "published": "Thu, 28 May 2026 06:34:25 GMT",
    "title": "Ferrari Luce Designer Mark Newson Explains the EV's Radically Unconventional Looks",
    "uid": "7e1fc07d13fb4fbe",
    "url": "..."
  },
  {
    "body": "...",
    "domain": "investing.com",
    "img": {
      "s": "...",
      "sq": "..."
    },
    "published": "Thu, 28 May 2026 06:34:21 GMT",
    "title": "Asia stocks retreat after fresh US strikes on Iran; PCE inflation on tap",
    "uid": "a29aeaf083200e95",
    "url": "..."
  },
  {
    "body_preview": "",
    "domain": "reuters.com",
    "img": null,
    "published": "Thu, 28 May 2026 06:31:33 GMT",
    "title": "DR Congo say World Cup delegation compliant with US Ebola protocols",
    "uid": "c38051ec1d7a8d48",
    "url": "..."
  },
  
]
```
    """
    url = "https://biztoc.p.rapidapi.com/news/latest"
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

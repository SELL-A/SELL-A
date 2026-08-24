import os
import requests

def Search(q):
    """
    :API_description: Retrieve a list of news articles related to Apple from the last 14 days, including details like content, source, date, and relevance score.
    :param q: The search query string.
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
    "score": 3.767899761336516,
    "title": "Ferrari Luce Designer Mark Newson Explains the EV's Radically Unconventional Looks",
    "url": "..."
  },
  {
    "body": "...",
    "domain": "abcnews.com",
    "img": {
      "s": "...",
      "sq": "..."
    },
    "published": "Thu, 28 May 2026 05:17:10 GMT",
    "score": 2.5128205128205128,
    "title": "Financial app for managing Trump Accounts set to launch Thursday - ABC News",
    "url": "..."
  }
]
```
    """
    url = "https://biztoc.p.rapidapi.com/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"q": q}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "biztoc.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")



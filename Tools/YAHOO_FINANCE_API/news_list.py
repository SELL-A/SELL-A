import os
import requests

def news_list(snippetCount,region):
    """
    :API_description: This API retrieves a paginated feed of financial news, analyst reports, and market content, including detailed metadata such as article information, publication dates, image thumbnails, content providers, and associated stock tickers.
    :param snippetCount: The number of news items to retrieve (e.g., 30).
    :param region: The region code (e.g., 'US') AR, AU, BR, CA, CN, FR, DE, HK, IN, IT, MX, NZ, SG, KR, ES, TW, GB, US
    :response_schema: 
    ```json
{
  "data": {
    "ntk": {
      "stream": [
        {
          "id": "b23bfb27-07ae-3b36-8c3a-648ff9333ec5",
          "editorialContent": {
            "id": "b23bfb27-07ae-3b36-8c3a-648ff9333ec5",
            "title": "UK households face £200 energy bill rise amid Iran war",
            "publishTime": "2026-05-25T09:21:11Z",
            "thumbnail": {
              "resolutions": [
                {
                  "height": 720,
                  "width": 1280,
                  "url": "...",
                  "tag": "original"
                },
                {
                  "height": 140,
                  "width": 140,
                  "url": "...",
                  "tag": "140x140"
                },
                {
                  "height": 768,
                  "width": 768,
                  "url": "...",
                  "tag": "768x768"
                },
                {
                  "height": 640,
                  "width": 640,
                  "url": "...",
                  "tag": "640x640"
                }
              ]
            },
            "content": {
              "id": "b23bfb27-07ae-3b36-8c3a-648ff9333ec5",
              "contentType": "STORY",
              "title": "UK households face £200 energy bill rise amid Iran war",
              "isHosted": true,
              "canonicalUrl": {
                "url": "..."
              },
              "clickThroughUrl": {
                "url": "..."
              },
              "providerContentUrl": "...",
              "displayTime": "2026-05-25T09:21:11Z",
              "previewUrl": null,
              "pubDate": "2026-05-25T09:21:11Z",
              "duration": 0,
              "thumbnail": {
                "resolutions": [
                  {
                    "height": 720,
                    "width": 1280,
                    "url": "...",
                    "tag": "original"
                  },
                  {
                    "height": 140,
                    "width": 140,
                    "url": "...",
                    "tag": "140x140"
                  },
                  {
                    "height": 768,
                    "width": 768,
                    "url": "...",
                    "tag": "768x768"
                  },
                  {
                    "height": 640,
                    "width": 640,
                    "url": "...",
                    "tag": "640x640"
                  }
                ]
              },
              "provider": {
                "displayName": "The Independent UK Finance",
                "url": "https://www.independent.co.uk/"
              },
              "liveBlogStatus": null,
              "liveVideo": null,
              "finance": {
                "stockTickers": null,
                "premiumFinance": {
                  "isPremiumNews": false,
                  "isPremiumFreeNews": false
                }
              },
              "summary": "Ofgem will on Wednesday reveal the level of the annual energy price cap for July to September."
            }
          }
        }
      ],
      "nextPage": true,
      "remainingCount": 72,
      "pagination": {
        "uuids": "paginationString={\"pageInfo\":{\"count\":20,\"hasNextPage\":true,\"hasPreviousPage\":false,\"start\":0,\"totalCount\":92}}"
      }
    },
    "main": {
      "stream": [],
      "nextPage": false,
      "pagination": {
        "uuids": "..."
      },
      "remainingCount": 0
    }
  },
  "status": "OK"
}
```
    """
    url = "https://yahoo-finance166.p.rapidapi.com/api/news/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"snippetCount": snippetCount,"region": region}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yahoo-finance166.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
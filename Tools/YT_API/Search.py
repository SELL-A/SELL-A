import os
import requests

def Search(query):
    """
    :API_description: The Search API retrieves a list of cat-themed videos and shorts, including detailed metadata such as titles, channel information, and view counts. It supports pagination and various filters for refining search results.
    :param query: The search term to query YouTube.
    :response_schema: 
    ```json
{
  "continuation": "string",
  "estimatedResults": "746",
  "data": [
    {
      "type": "ad",
      "slotId": "1779779744644643:150361126:453279308:1",
      "slotType": "SLOT_TYPE_IN_FEED",
      "slotPhysicalPosition": 1,
      "layoutId": "aNeYXNBdZFOQSMnB",
      "layoutType": "LAYOUT_TYPE_DISPLAY_COMPACT_LANDSCAPE_NO_BUTTON",
      "ad": {
        "thumbnail": [
          {
            "url": "...",
            "width": 2402,
            "height": 1256
          }
        ],
        "title": "Aus Österreich & Deutschland",
        "description": "THE GOODSTUFF setzt auf viel frisches Fleisch und regional verfügbare Zutaten.",
        "websiteText": "THE GOODSTUFF",
        "url": "",
        "aboutThisAd": "..."
      }
    },
    {
      "type": "video",
      "videoId": "DFQk9MYgerg",
      "title": "Live 🔴Mama Cat And Kitten ✨Funny Cat | Kucing 🌻 Cat Videos 😿 Cute Cat | Meow Meow",
      "channelTitle": "RICK_GARRY",
      "channelId": "UCY1ziw18DwltkFu2dP2SZzA",
      "channelHandle": "@RICK_GARRY",
      "channelThumbnail": [
        {
          "url": "...",
          "width": 68,
          "height": 68
        }
      ],
      "channelAvatar": [
        {
          "url": "...",
          "width": 68,
          "height": 68
        }
      ],
      "description": "...",
      "viewCountText": "62 watching",
      "viewCount": "62",
      "publishedTimeText": null,
      "lengthText": "LIVE",
      "isLive": true,
      "badges": [
        "LIVE",
        "New"
      ],
      "thumbnail": [
        {
          "url": "...",
          "width": 360,
          "height": 202
        },
        {
          "url": "...",
          "width": 720,
          "height": 404
        }
      ],
      "richThumbnail": null
    }
  ],
  "msg": ""
}
    ```
    """
    url = "https://yt-api.p.rapidapi.com/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"query": query}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
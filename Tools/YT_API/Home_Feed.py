import os
import requests

def Home_Feed():
    """
    :API_description: Retrieve categorized content feeds with optional pagination and regional filtering.
    :param None
    :response_schema: 
    ```json
{
  "filters": [
    {
      "filter": "All"
    },
    {
      "filter": "Music",
      "continuation": "..."
    },
    {
      "filter": "Music of Romania",
      "continuation": "..."
    },
    {
      "filter": "Music of Iran",
      "continuation": "..."
    }
  ],
  "continuation": "...",
  "data": [
    {
      "type": "ad",
      "slotId": "1779736424551070:24445959:1612767799:2",
      "slotType": "SLOT_TYPE_IN_FEED",
      "slotPhysicalPosition": 1,
      "layoutId": "g07Moa4rtevrBWr7",
      "layoutType": "LAYOUT_TYPE_VIDEO_DISPLAY_BUTTON_GROUP"
    },
    {
      "type": "shorts_listing",
      "title": "Shorts",
      "subtitle": null,
      "data": [
        {
          "type": "shorts",
          "videoId": "iHTp2Ny7vlM",
          "title": "Cute Funny Cat Moments 🥺😹 | Funniest Cat Short Ever#funny",
          "viewCountText": "2.4M views",
          "thumbnail": [
            {
              "url": "https://i.ytimg.com/vi/iHTp2Ny7vlM/frame0.jpg",
              "width": 1080,
              "height": 1920
            }
          ],
          "isOriginalAspectRatio": true,
          "params": "CAUwAroBGFVDdmxZelVDNGNxTDhZY0MwZWNRVENfUQ%3D%3D",
          "playerParams": "8AEBoAMByAMkuAQFogYVAdeaJRO3D9t0qLLMqz4fEDlT468xkAcC",
          "sequenceParams": "CgtpSFRwMk55N3ZsTSoCGAVQGWgA"
        },
        {
          "type": "shorts",
          "videoId": "ADWJppw24nA",
          "title": "Ranking The BEST Breakup Glow Ups! Part 10",
          "viewCountText": "544K views",
          "thumbnail": [
            {
              "url": "https://i.ytimg.com/vi/ADWJppw24nA/frame0.jpg",
              "width": 1080,
              "height": 1920
            }
          ],
          "isOriginalAspectRatio": true,
          "params": "CAUwAroBGFVDTFlvelU5Q3ZYTUItZUpiN3M0WFQwQQ%3D%3D",
          "playerParams": "8AEBoAMByAMkuAQFugUEEgJlbqIGFQHXmiUT_6FaHpUCRq82MmaUC_6yDpAHAg%3D%3D",
          "sequenceParams": "CgtBRFdKcHB3MjRuQSoCGAVQGWgA"
        }
      ]
    },
    {
      "type": "video",
      "videoId": "85h2xmyhQPY",
      "title": "Music for Cats 😽 Good Sleep Music and Stress Relief Music for cats, Music that cats like",
      "publishedTimeText": "Streamed 2y ago",
      "publishDate": "1969-12-31",
      "publishedAt": "1969-12-31T00:00:00Z",
      "description": "",
      "thumbnail": [
        {
          "url": "https://i.ytimg.com/vi/85h2xmyhQPY/hq720.jpg?sqp=-oaymwEcCOgCEMoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCPZRMZVWpqBkm2NIdqpGefg6LzXw",
          "width": 360,
          "height": 202
        },
        {
          "url": "https://i.ytimg.com/vi/85h2xmyhQPY/hq720.jpg?sqp=-oaymwEcCNAFEJQDSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLAp4cXypITT9TrsKOdywaZzzD8yRQ",
          "width": 720,
          "height": 404
        }
      ],
      "lengthText": "11:54:56"
    }
  ],
  "msg": ""
}
```
    """
    url = "https://yt-api.p.rapidapi.com/home"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
import os
import requests

def Hashtag(tag):
    """
    :API_description: Retrieves a list of video data related to a specified hashtag, including metadata and pagination options.
    :param tag: The hashtag for which data is to be retrieved(e.g., "viral").
    :response_schema: 
    ```json
{
  "meta": {
    "hashtag": "#viral",
    "hashtagInfoText": "789M videos • 52M channels"
  },
  "continuation": "...",
  "data": [
    {
      "type": "shorts",
      "videoId": "uTzcSyJzy1s",
      "title": "Viral Videos You Didn't Realize Were Fake",
      "channelTitle": "Sambucha",
      "channelId": "UCWBWgCD4oAqT3hUeq40SCUw",
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
      "channelBadges": [
        "Verified"
      ],
      "isVerifiedChannel": true,
      "description": "",
      "viewCountText": "16,463,308 views",
      "viewCount": "16463308",
      "publishedTimeText": "2 years ago",
      "publishDate": "2024-05-26",
      "publishedAt": "2024-05-26T00:00:00Z",
      "lengthText": "0:57",
      "thumbnail": [
        {
          "url": "...",
          "width": 168,
          "height": 94
        },
        {
          "url": "...",
          "width": 196,
          "height": 110
        }
      ],
      "richThumbnail": [
        {
          "url": "https://i.ytimg.com/an_webp/uTzcSyJzy1s/mqdefault_6s.webp?du=3000&sqp=CLyU19AG&rs=AOn4CLDbQhCIJYze-wZ8E2LLC8_LmsUQWA",
          "width": 320,
          "height": 180
        }
      ],
      "isOriginalAspectRatio": true,
      "params": "CBUwAroBAA%3D%3D",
      "playerParams": "8AEBoAMFyAMkuAQVogYVAdeaJRPl_TPIdIyo1si7KfE3-RhXkAcC",
      "sequenceParams": "Cgt1VHpjU3lKenkxcyoCGBU%3D"
    },
    {
      "type": "shorts",
      "videoId": "nle5f7MRUHM",
      "title": "Viral Video | Monkeys Scroll Through Social Media Like An Everyday Activity | #trending",
      "channelTitle": "CNN-News18",
      "channelId": "UCef1-8eOpJgud7szVPlZQAQ",
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
      "channelBadges": [
        "Verified"
      ],
      "isVerifiedChannel": true,
      "description": "",
      "viewCountText": "1,129,131 views",
      "viewCount": "1129131",
      "publishedTimeText": "3 years ago",
      "publishDate": "2023-05-26",
      "publishedAt": "2023-05-26T00:00:00Z",
      "lengthText": "0:09",
      "thumbnail": [
        {
          "url": "...",
          "width": 168,
          "height": 94
        },
        {
          "url": "...",
          "width": 196,
          "height": 110
        },
        {
          "url": "...",
          "width": 246,
          "height": 138
        }
      ],
      "richThumbnail": null,
      "isOriginalAspectRatio": true,
      "params": "CBUwAroBAA%3D%3D",
      "playerParams": "8AEBoAMFyAMkuAQVogYVAdeaJROradBQnl7Mp0C1V4cXBWBvkAcC",
      "sequenceParams": "CgtubGU1ZjdNUlVITSoCGBU%3D"
    }

  ],
  "msg": ""
}
```
    """
    url = "https://yt-api.p.rapidapi.com/hashtag"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"tag": tag}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
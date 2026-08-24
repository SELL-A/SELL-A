import os
import requests

def Trending(geo: str):
    """
    :API_description: Retrieves a list of trending videos and shorts, including detailed metadata such as title, view count, and publication date, tailored to a specific region and language.
    :param geo: The geographical location code (e.g., 'US' for the United States ISO 3166-2 country code of the region for which you want the trending data. Like US (default), GB, CA, IN, etc.).
    :response_schema: 
    ```json
{
  "data": [
    {
      "type": "video",
      "videoId": "XelMqi0jlvk",
      "title": "...",
      "channelTitle": "Christmas Songs and Carols - Love to Sing",
      "channelId": "UCn0JHLJWiO3_Y5xfNPcF_Ug",
      "channelThumbnail": null,
      "description": "...",
      "viewCount": "316056",
      "likeCount": "1117",
      "commentCount": "61",
      "publishedAt": "2025-12-09T11:30:38Z",
      "publishedTimeText": "6 months ago",
      "lengthText": "2:07:14",
      "thumbnail": [
        {
          "url": "https://i.ytimg.com/vi/XelMqi0jlvk/default.jpg",
          "width": 120,
          "height": 90
        },
        {
          "url": "https://i.ytimg.com/vi/XelMqi0jlvk/mqdefault.jpg",
          "width": 320,
          "height": 180
        }
      ],
      "richThumbnail": null
    },
    {
      "type": "video",
      "videoId": "VnzCyRyPugM",
      "title": "...",
      "channelTitle": "The Official Pokémon YouTube channel",
      "channelId": "UCFctpiB_Hnlk3ejWfHqSm6Q",
      "channelThumbnail": null,
      "description": "...",
      "viewCount": "529246",
      "likeCount": "24301",
      "commentCount": "2419",
      "publishedAt": "2025-12-09T14:02:40Z",
      "publishedTimeText": "6 months ago",
      "lengthText": "2:12",
      "thumbnail": [
        {
          "url": "https://i.ytimg.com/vi/VnzCyRyPugM/default.jpg",
          "width": 120,
          "height": 90
        }
      ],
      "richThumbnail": null
    }
  ],
  "msg": ""
}
```
    """
    url = "https://yt-api.p.rapidapi.com/trending"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"geo": geo}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
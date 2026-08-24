import os
import requests

def Discover(keywords: str, region="us", count=10):
    """
    :API_description: Retrieve a list of trending videos with specific hashtags for a specified region, providing detailed metadata for each video.
    :param keywords: The keywords to search for.
    :param region: The region code to filter the content(e.g. "us"s).
    :param count: The number of videos to return Default: 10.
    :response_schema: 
    ```json
{
  "code": 0,
  "msg": "success",
  "processed_time": 0.8001,
  "data": {
    "videos": [
      {
        "aweme_id": "v15044gf0000d6lb2cvog65nvo6jctt0",
        "video_id": "7614092899642330398",
        "region": "US",
        "title": "##foryoupage# fyp",
        "content_desc": [],
        "cover": "...",
        "ai_dynamic_cover": "...",
        "origin_cover": "...",
        "duration": 10,
        "play": "...",
        "wmplay": "...",
        "size": 1354097,
        "wm_size": 1233293,
        "music": "...",
        "music_info": {
          "id": "7614092821179534111",
          "title": "original sound - u.s.a.cilap123",
          "play": "...",
          "cover": "...",
          "author": "u.s.a.cilap123",
          "original": true,
          "duration": 10,
          "album": ""
        },
        "play_count": 1751239,
        "digg_count": 17267,
        "comment_count": 465,
        "share_count": 3461,
        "download_count": 2225,
        "create_time": 1772794169,
        "anchors": null,
        "anchors_extras": "",
        "is_ad": false,
        "commerce_info": {
          "auction_ad_invited": false,
          "with_comment_filter_words": false,
          "adv_promotable": false,
          "branded_content_type": 0,
          "organic_log_extra": "{\"req_id\":\"20260517144610794C4DEECAA2956DB3BB\"}",
          "is_diversion_ad": 0
        },
        "commercial_video_info": "",
        "item_comment_settings": 0,
        "mentioned_users": "",
        "author": {
          "id": "7608233038564082702",
          "unique_id": "u.s.a.cilap123",
          "nickname": "u.s.a.cilap123",
          "avatar": "..."
        },
        "is_top": 0
      },
      {
        "aweme_id": "v15044gf0000d7400bnog65uceb9koj0",
        "video_id": "7622342677903838495",
        "region": "US",
        "title": "#vairalvideos_tik_tok🌿🙂🥰👇👈 ",
        "content_desc": [],
        "cover": "...",
        "ai_dynamic_cover": "...",
        "origin_cover": "...",
        "duration": 71,
        "play": "...",
        "wmplay": "...",
        "size": 9222128,
        "wm_size": 0,
        "music": "...",
        "music_info": {
          "id": "7622342694848809758",
          "title": "original sound - english0492",
          "play": "...",
          "cover": "...",
          "author": "English Hub",
          "original": true,
          "duration": 71,
          "album": ""
        },
        "play_count": 1317711,
        "digg_count": 8310,
        "comment_count": 161,
        "share_count": 678,
        "download_count": 32,
        "create_time": 1774714972,
        "anchors": null,
        "anchors_extras": "",
        "is_ad": false,
        "commerce_info": {
          "auction_ad_invited": false,
          "with_comment_filter_words": false,
          "adv_promotable": false,
          "branded_content_type": 0,
          "organic_log_extra": "{\"req_id\":\"20260517144610794C4DEECAA2956DB3BB\"}",
          "is_diversion_ad": 0
        },
        "commercial_video_info": "",
        "item_comment_settings": 0,
        "mentioned_users": "",
        "author": {
          "id": "7606265726516626446",
          "unique_id": "english0492",
          "nickname": "English Hub",
          "avatar": "..."
        },
        "is_top": 0
      }
    ],
    "cursor": 2,
    "hasMore": true
  }
}
    ```
    """
    url = "https://tiktok-scraper7.p.rapidapi.com/feed/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"keywords": keywords, "region": region, "count": count}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "tiktok-scraper7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

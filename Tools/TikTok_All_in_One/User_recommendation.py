import os
import requests

def User_recommendation(user_id: str):
    """
    :API_description: Retrieve a list of popular users based on the specified user_id, providing detailed user information including profile details and media content.
    :param user_id: The unique identifier of the TikTok user(e.g. "107955").
    :response_schema: 
    ```json
{
  "code": 0,
  "msg": "success",
  "processed_time": 0.815,
  "data": {
    "videos": [
      {
        "aweme_id": "v15044gf0000d724vbfog65ugaj79100",
        "video_id": "7621307384165666079",
        "region": "US",
        "title": "the way I FaceTimed my friends like I’m getting engaged…it’s just a podcast 🤣 ",
        "content_desc": [],
        "cover": "...",
        "ai_dynamic_cover": "...",
        "origin_cover": "...",
        "duration": 124,
        "play": "...",
        "wmplay": "...",
        "size": 14319755,
        "wm_size": 13199748,
        "music": "...",
        "music_info": {
          "id": "7621307427723447071",
          "title": "original sound - thecarterb",
          "play": "...",
          "cover": "...",
          "author": "Carter Gregory",
          "original": true,
          "duration": 124,
          "album": ""
        },
        "play_count": 92640,
        "digg_count": 5360,
        "comment_count": 322,
        "share_count": 240,
        "download_count": 24,
        "collect_count": 325,
        "create_time": 1774473919,
        "anchors": null,
        "anchors_extras": "",
        "is_ad": false,
        "commerce_info": {
          "adv_promotable": false,
          "auction_ad_invited": false,
          "branded_content_type": 0,
          "is_diversion_ad": 0,
          "organic_log_extra": "{\"req_id\":\"20260405133508AA81F41410782FB3183A\"}",
          "with_comment_filter_words": false
        },
        "commercial_video_info": "",
        "item_comment_settings": 0,
        "mentioned_users": "",
        "author": {
          "id": "6756295321263490053",
          "unique_id": "thecarterb",
          "nickname": "Carter Gregory",
          "avatar": "..."
        },
        "is_top": 0
      },
      {
        "aweme_id": "v15044gf0000d6tdoefog65ivoab3cfg",
        "video_id": "7618646098588044574",
        "region": "US",
        "title": "@Gabby can confirm to @Delaney Rowe: blondes do infact have more fun #VFOscars",
        "content_desc": [],
        "cover": "...",
        "ai_dynamic_cover": "...",
        "origin_cover": "...",
        "duration": 43,
        "play": "...",
        "wmplay": "...",
        "size": 6910905,
        "wm_size": 6423758,
        "music": "...",
        "music_info": {
          "id": "7618646145178307359",
          "title": "original sound - vanityfair",
          "play": "...",
          "cover": "...",
          "author": "Vanity Fair",
          "original": true,
          "duration": 43,
          "album": ""
        },
        "play_count": 42315,
        "digg_count": 980,
        "comment_count": 15,
        "share_count": 21,
        "download_count": 4,
        "collect_count": 35,
        "create_time": 1773854308,
        "anchors": null,
        "anchors_extras": "",
        "is_ad": true,
        "commerce_info": {
          "ad_source": 1,
          "adv_promotable": true,
          "auction_ad_invited": false,
          "branded_content_type": 0,
          "is_diversion_ad": 0,
          "organic_log_extra": "{\"req_id\":\"20260405133508AA81F41410782FB3183A\"}",
          "with_comment_filter_words": false
        },
        "commercial_video_info": "",
        "item_comment_settings": 0,
        "mentioned_users": "6805944441938838533,6839379691784045573",
        "author": {
          "id": "7015709895425721349",
          "unique_id": "vanityfair",
          "nickname": "Vanity Fair",
          "avatar": "..."
        },
        "is_top": 0
      }
    ],
    "cursor": "10",
    "hasMore": true
  }
}
    ```
    """
    url = "https://tiktok-scraper7.p.rapidapi.com/user/reposts"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"user's id": user_id}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "tiktok-scraper7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


import os
import requests

def Users_videos(user_id: str):
    """
    :API_description: Retrieve detailed information about TikTok videos uploaded by a specific user, including metadata about the associated music and author profiles.
    :param user_id: The unique identifier of the TikTok user.
    :response_schema: 
    ```json
{
  "code": 0,
  "msg": "success",
  "processed_time": 2.567,
  "data": {
    "videos": [
      {
        "aweme_id": "",
        "video_id": "7640602632368803094",
        "region": "AT",
        "title": "",
        "content_desc": [],
        "cover": "...",
        "ai_dynamic_cover": "...",
        "origin_cover": "...",
        "duration": 0,
        "play": "",
        "wmplay": "...",
        "size": 0,
        "wm_size": 0,
        "music": "...",
        "music_info": {
          "id": "7637894029987941128",
          "title": "original sound - mniemils",
          "play": "...",
          "cover": "...",
          "author": "𝗠𝗻𝗶𝗲𝗺𝗶𝗹𝘀 𐌀",
          "original": true,
          "duration": 8,
          "album": ""
        },
        "play_count": 4496,
        "digg_count": 238,
        "comment_count": 0,
        "share_count": 1,
        "download_count": 0,
        "collect_count": 0,
        "create_time": 1778966438,
        "anchors": [
          {
            "actions": [
              {
                "action_type": 1,
                "icon": {
                  "height": 720,
                  "uri": "tiktok-obj/28px_primary_create_onDark3x.png",
                  "url_list": [
                    "...",
                    "..."
                  ],
                  "url_prefix": null,
                  "width": 720
                },
                "schema": "shoot"
              }
            ],
            "anchor_strong": null,
            "component_key": "anchor_effect",
            "description": "Effects",
            "extra": "{\"effect_post_publish_count\":299826,\"effect_source\":1,\"is_commerce\":0,\"resource_id\":7482816265279509009}",
            "icon": {
              "height": 720,
              "uri": "tiktok-obj/20px_anchor_effect3x.png",
              "url_list": [
                "...",
                "..."
              ],
              "url_prefix": null,
              "width": 720
            },
            "id": "1999002120",
            "keyword": "mori berry",
            "log_extra": "{\"anchor_id\":\"1999002378\",\"anchor_name\":\"mori berry\",\"anchor_type\":\"prop\",\"has_friends_info\":\"0\"}",
            "thumbnail": {
              "height": 64,
              "uri": "e6bc6975d26a5bde438b5f26683dba52",
              "url_list": [
                "...",
                "..."
              ],
              "url_prefix": null,
              "width": 64
            },
            "type": 28
          }
        ],
        "anchors_extras": "",
        "is_ad": false,
        "commerce_info": {
          "adv_promotable": false,
          "auction_ad_invited": false,
          "branded_content_type": 0,
          "is_diversion_ad": 0,
          "organic_log_extra": "{\"req_id\":\"202605171513506C507372A31486A51E67\"}",
          "with_comment_filter_words": false
        },
        "commercial_video_info": "",
        "item_comment_settings": 3,
        "mentioned_users": "",
        "author": {
          "id": "7128593328456041478",
          "unique_id": "isi.cos",
          "nickname": "twitch.tv/isiicos",
          "avatar": "..."
        },
        "images": [
            "..."
        ],
        "is_top": 0
      },
      {
        "aweme_id": "v24044gl0000d84el27og65pa1ctk3hg",
        "video_id": "7640614679856844054",
        "region": "AT",
        "title": "",
        "content_desc": [],
        "cover": "...",
        "ai_dynamic_cover": "...",
        "origin_cover": "...",
        "duration": 15,
        "play": "...",
        "wmplay": "...",
        "size": 1958302,
        "wm_size": 2043880,
        "music": "",
        "music_info": {
          "id": "7640614681408801558",
          "title": "original sound - isi.cos",
          "play": "",
          "cover": "...",
          "author": "twitch.tv/isiicos",
          "original": true,
          "duration": 15,
          "album": ""
        },
        "play_count": 4132,
        "digg_count": 298,
        "comment_count": 0,
        "share_count": 5,
        "download_count": 0,
        "collect_count": 0,
        "create_time": 1778969242,
        "anchors": null,
        "anchors_extras": "",
        "is_ad": false,
        "commerce_info": {
          "adv_promotable": false,
          "auction_ad_invited": false,
          "branded_content_type": 0,
          "is_diversion_ad": 0,
          "organic_log_extra": "{\"req_id\":\"202605171513506C507372A31486A51E67\"}",
          "with_comment_filter_words": false
        },
        "commercial_video_info": "",
        "item_comment_settings": 3,
        "mentioned_users": "",
        "author": {
          "id": "7128593328456041478",
          "unique_id": "isi.cos",
          "nickname": "twitch.tv/isiicos",
          "avatar": "..."
        },
        "is_top": 0
      }
    ],
    "cursor": "1779029606462",
    "hasMore": true
  }
}
```
    """
    url = "https://tiktok-scraper7.p.rapidapi.com/user/story"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"user_id": user_id}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "tiktok-scraper7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
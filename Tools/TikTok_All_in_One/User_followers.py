import os
import requests

def User_followers(user_id: str, count=50):
    """
    :API_description: Retrieve a list of followers for a specified user, with optional pagination using a timestamp from a previous request.
    :param user_id: The unique identifier of the TikTok user(e.g. "6774419827379389445").
    :param count: The number of followers to return Default: 50.
    :response_schema: 
    ```json
{
  "code": 0,
  "msg": "success",
  "processed_time": 0.2394,
  "data": {
    "followers": [
      {
        "id": "7100432298936878082",
        "region": "MM",
        "sec_uid": "...",
        "unique_id": "nangnaychilin",
        "nickname": "LENG❤️‍🔥",
        "signature": "ချီးထုပ်...🙄🤍🤍@♡KEVIN♡🌪️",
        "avatar": "...",
        "verified": false,
        "secret": false,
        "aweme_count": 581,
        "following_count": 583,
        "follower_count": 3506,
        "favoriting_count": 117582,
        "total_favorited": 95488,
        "ins_id": "",
        "youtube_channel_title": "",
        "youtube_channel_id": "",
        "twitter_name": "",
        "twitter_id": ""
      },
      {
        "id": "7639494383029896213",
        "region": "ID",
        "sec_uid": "...",
        "unique_id": "dian.harianto735",
        "nickname": "Dian Harianto",
        "signature": "",
        "avatar": "...",
        "verified": false,
        "secret": false,
        "aweme_count": 1,
        "following_count": 1,
        "follower_count": 0,
        "favoriting_count": 102,
        "total_favorited": 4,
        "ins_id": "",
        "youtube_channel_title": "",
        "youtube_channel_id": "",
        "twitter_name": "",
        "twitter_id": ""
      },
      {
        "id": "7463776125644620817",
        "region": "BD",
        "sec_uid": "...",
        "unique_id": "djshuvoj87",
        "nickname": "❌DJSHUVOJ❌",
        "signature": "10.000K",
        "avatar": "...",
        "verified": false,
        "secret": false,
        "aweme_count": 297,
        "following_count": 2568,
        "follower_count": 3678,
        "favoriting_count": 109200,
        "total_favorited": 64054,
        "ins_id": "",
        "youtube_channel_title": "shuvoj Mia",
        "youtube_channel_id": "UCDkjH0ZcAH-4ZjuGQBbdvjQ",
        "twitter_name": "",
        "twitter_id": ""
      }
    ],
    "total": 94104619,
    "time": 1779029234,
    "hasMore": true
  }
}
```
    """
    url = "https://tiktok-scraper7.p.rapidapi.com/user/followers"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"user_id": user_id, "count": count}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "tiktok-scraper7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
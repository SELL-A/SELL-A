import os
import requests
def User_info(user_id):
    """
    :API_description: Retrieve detailed user profile information, including avatar images, social media links, and follower counts.
    :param user_id: The unique identifier of the TikTok user(e.g. "107955").
    :response_schema: 
    ```json
{
  "code": 0,
  "msg": "success",
  "processed_time": 0.7088,
  "data": {
    "user": {
      "id": "107955",
      "uniqueId": "tiktok",
      "nickname": "TikTok",
      "avatarThumb": "...",
      "avatarMedium": "...",
      "avatarLarger": "...",
      "signature": "One TikTok can make a big impact",
      "verified": true,
      "secUid": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
      "secret": false,
      "ftc": false,
      "relation": 0,
      "openFavorite": false,
      "commentSetting": null,
      "duetSetting": null,
      "stitchSetting": null,
      "privateAccount": false,
      "isADVirtual": false,
      "isUnderAge18": false,
      "ins_id": "",
      "twitter_id": "",
      "youtube_channel_title": "",
      "youtube_channel_id": "",
      "UserStoryStatus": 0,
      "createTime": 1425144149,
      "bioLink": {
        "link": "linktr.ee/tiktok"
      }
    },
    "stats": {
      "followingCount": 3,
      "followerCount": 94102921,
      "heartCount": 458097000,
      "videoCount": 1511,
      "diggCount": 0,
      "heart": 458097000
    }
  }
}
```
    """
    url = "https://tiktok-scraper7.p.rapidapi.com/user/info"
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
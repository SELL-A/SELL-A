import os
import requests
def User_following(user_id: str, count=50):
    """
    :API_description: Retrieve the list of users a specific user is following, including detailed user profiles.
    :param user_id: The unique identifier of the TikTok user(e.g. "107955").
    :param count: The number of users to return Default: 50.
    :response_schema: 
    ```json
{
  "code": 0,
  "msg": "success",
  "processed_time": 0.8425,
  "data": {
    "followings": [
      {
        "id": "6551237489917432832",
        "region": "US",
        "sec_uid": "MS4wLjABAAAAXqqA-cLDC0hfQPIrS5APYNsg04zkl-socWCkqkI3UIOaEe6_Qnokg0GcWpLnMNQP",
        "unique_id": "tiktokcreators",
        "nickname": "tiktok creators",
        "signature": "The official account for TikTok Creators who inspire creativity and bring joy ✨\n\n⬇️ Creator Growth Challenge 💰⬇️",
        "avatar": "...",
        "verified": true,
        "secret": false,
        "aweme_count": 1052,
        "following_count": 559,
        "follower_count": 7857318,
        "favoriting_count": 1785,
        "total_favorited": 28452200,
        "ins_id": "",
        "youtube_channel_title": "",
        "youtube_channel_id": "",
        "twitter_name": "",
        "twitter_id": ""
      }
    ],
    "total": 2,
    "time": 1447292191,
    "hasMore": false
  }
}
    ```
    """
    url = "https://tiktok-scraper7.p.rapidapi.com/user/following"
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

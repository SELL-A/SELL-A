import os
import requests

def Comments(video_id):
    """
    :API_description: Retrieves detailed information about comments on a video, including metadata such as comment ID, author details, text, publication date, likes, and replies.
    :param video_id: The ID of the YouTube video for which comments are to be retrieved(Example: "1gxf6flnvNA").
    :response_schema: 
    ```json
{
  "commentsCount": "1643",
  "continuation": "...",
  "data": [
    {
      "commentId": "Ugwq5-FSu3zt7iVrMyp4AaABAg",
      "authorText": "@allaboutroofing2",
      "authorChannelId": "UC1oyzRrNZ4YkJL3EufJkZEw",
      "authorThumbnail": [
        {
          "url": "...",
          "width": 88,
          "height": 88
        }
      ],
      "textDisplay": "Costco would sell a lot more large screen 4K TVs  if they had this playing instead of those stupid parrots and lizards.  THIS is why we have 4K tv.",
      "publishedTimeText": "7 years ago",
      "publishDate": "2019-05-26",
      "publishedAt": "2019-05-26T00:00:00Z",
      "likesCount": "2.3K",
      "replyCount": "18",
      "replyToken": "...",
      "authorIsChannelOwner": false,
      "isVerified": false,
      "isArtist": false,
      "isCreator": false
    },
    {
      "commentId": "UgyvtOeavGohYbGB0F54AaABAg",
      "authorText": "@santosh9909",
      "authorChannelId": "UCKKtMBwUn5YMDmCv8Bg3LSA",
      "authorThumbnail": [
        {
          "url": "...", 
          "width": 88,
          "height": 88
        }
      ],
      "textDisplay": "00:39 beautiful",
      "publishedTimeText": "1 year ago",
      "publishDate": "2025-05-26",
      "publishedAt": "2025-05-26T00:00:00Z",
      "likesCount": "0",
      "replyCount": "0",
      "authorIsChannelOwner": false,
      "isVerified": false,
      "isArtist": false,
      "isCreator": false
    },
    {
      "commentId": "UgzQui0aNzMc22NjSIp4AaABAg",
      "authorText": "@SATO_FD2R",
      "authorChannelId": "UCsPx0UkCuY2_JIe5O7DBoXA",
      "authorThumbnail": [
        {
          "url": "...", 
          "width": 88,
          "height": 88
        }
      ],
      "textDisplay": "Always my go to when I buy a new tv. Used it about 4 times now! 🔥🔥🔥 What a time to be alive",
      "publishedTimeText": "1 year ago",
      "publishDate": "2025-05-26",
      "publishedAt": "2025-05-26T00:00:00Z",
      "likesCount": "4",
      "replyCount": "0",
      "authorIsChannelOwner": false,
      "isVerified": false,
      "isArtist": false,
      "isCreator": false
    },
    {
      "commentId": "UgxbAHLBt6tyH_ZKLx54AaABAg",
      "authorText": "@cristopherlopezpaniagua3112",
      "authorChannelId": "UC-DpLMOAyyETUiFHnGxttwQ",
      "authorThumbnail": [
        {
          "url": "https://yt3.ggpht.com/ytc/AIdro_mfL6YVOFOl0JNfPj0eeTYecgLJk-0QHcVBHiKjbGh07JMC=s88-c-k-c0x00ffffff-no-rj",
          "width": 88,
          "height": 88
        }
      ],
      "textDisplay": "2025. Checking in...",
      "publishedTimeText": "1 year ago",
      "publishDate": "2025-05-26",
      "publishedAt": "2025-05-26T00:00:00Z",
      "likesCount": "3",
      "replyCount": "0",
      "authorIsChannelOwner": false,
      "isVerified": false,
      "isArtist": false,
      "isCreator": false
    }
  ],
  "msg": ""
}
    ```
    """
    url = "https://yt-api.p.rapidapi.com/comments"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"id": video_id}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
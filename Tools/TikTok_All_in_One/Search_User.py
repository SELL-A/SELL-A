import os
import requests

def Search_User(keywords: str, count=10):
    """
    :API_description: Retrieve a list of users.
    :param keywords: The search term used to find TikTok users.
    :param count: The number of results to return.
    :response_schema: 
    ```JSON_schema
{
  "type": "object",
  "properties": {
    "code": {
      "type": "integer",
      "description": "Status code indicating the result of the API call. Typically 0 for success."
    },
    "msg": {
      "type": "string",
      "description": "Message describing the result, e.g., 'success'."
    },
    "processed_time": {
      "type": "number",
      "description": "Time taken to process the request in seconds."
    },
    "data": {
      "type": "object",
      "properties": {
        "user_list": {
          "type": "array",
          "description": "List of user objects matching the search criteria.",
          "items": {
            "type": "object",
            "properties": {
              "user": {
                "type": "object",
                "description": "Detailed user profile information.",
                "properties": {
                  "id": {
                    "type": "string",
                    "description": "Unique identifier for the user."
                  },
                  "region": {
                    "type": "string",
                    "description": "User's region or country code."
                  },
                  "uniqueId": {
                    "type": "string",
                    "description": "Username or unique handle."
                  },
                  "nickname": {
                    "type": "string",
                    "description": "Display name of the user."
                  },
                  "avatarThumb": {
                    "type": "string",
                    "description": "URL to the user's small thumbnail avatar."
                  },
                  "avatarMedium": {
                    "type": "string",
                    "description": "URL to the user's medium-sized avatar."
                  },
                  "avatarLarger": {
                    "type": "string",
                    "description": "URL to the user's large avatar."
                  },
                  "signature": {
                    "type": "string",
                    "description": "User's bio or description."
                  },
                  "verified": {
                    "type": "boolean",
                    "description": "Indicates if the user account is verified."
                  },
                  "secUid": {
                    "type": "string",
                    "description": "Secure user ID."
                  },
                  "secret": {
                    "type": "boolean",
                    "description": "Indicates if the account is secret."
                  },
                  "ftc": {
                    "type": "boolean",
                    "description": "Flag for FTC-related status."
                  },
                  "relation": {
                    "type": "integer",
                    "description": "Relationship status with the requesting user."
                  },
                  "openFavorite": {
                    "type": ["null", "boolean"],
                    "description": "Indicates if favorites are open, can be null."
                  },
                  "commentSetting": {
                    "type": "integer",
                    "description": "User's comment setting (e.g., 0 for open)."
                  },
                  "duetSetting": {
                    "type": "integer",
                    "description": "User's duet setting (e.g., 0 for disabled, 1 for enabled)."
                  },
                  "stitchSetting": {
                    "type": "integer",
                    "description": "User's stitch setting (e.g., 0 for disabled, 1 for enabled)."
                  },
                  "privateAccount": {
                    "type": "boolean",
                    "description": "Indicates if the account is private."
                  },
                  "isADVirtual": {
                    "type": "boolean",
                    "description": "Indicates if the account is an ad virtual account."
                  },
                  "isUnderAge18": {
                    "type": "boolean",
                    "description": "Indicates if the user is under 18 years old."
                  },
                  "ins_id": {
                    "type": "string",
                    "description": "Instagram ID associated with the user."
                  },
                  "twitter_id": {
                    "type": "string",
                    "description": "Twitter ID associated with the user."
                  },
                  "youtube_channel_title": {
                    "type": "string",
                    "description": "Title of the associated YouTube channel."
                  },
                  "youtube_channel_id": {
                    "type": "string",
                    "description": "ID of the associated YouTube channel."
                  }
                },
                "required": ["id", "region", "uniqueId", "nickname", "avatarThumb", "avatarMedium", "avatarLarger", "signature", "verified", "secUid", "secret", "ftc", "relation", "openFavorite", "commentSetting", "duetSetting", "stitchSetting", "privateAccount", "isADVirtual", "isUnderAge18", "ins_id", "twitter_id", "youtube_channel_title", "youtube_channel_id"]
              },
              "stats": {
                "type": "object",
                "description": "User's engagement and activity statistics.",
                "properties": {
                  "followingCount": {
                    "type": "integer",
                    "description": "Number of users this user is following."
                  },
                  "followerCount": {
                    "type": "integer",
                    "description": "Number of followers."
                  },
                  "heartCount": {
                    "type": "integer",
                    "description": "Total number of hearts/likes received."
                  },
                  "videoCount": {
                    "type": "integer",
                    "description": "Number of videos posted."
                  },
                  "diggCount": {
                    "type": "integer",
                    "description": "Number of diggs (likes given)."
                  },
                  "heart": {
                    "type": "integer",
                    "description": "Alternative field for heart count, often duplicates heartCount."
                  }
                },
                "required": ["followingCount", "followerCount", "heartCount", "videoCount", "diggCount", "heart"]
              }
            },
            "required": ["user", "stats"]
          }
        },
        "cursor": {
          "type": "integer",
          "description": "Pagination cursor for fetching the next set of results."
        },
        "hasMore": {
          "type": "boolean",
          "description": "Indicates if more results are available beyond the current cursor."
        }
      },
      "required": ["user_list", "cursor", "hasMore"]
    }
  },
  "required": ["code", "msg", "processed_time", "data"]
}
```
    """
    url = "https://tiktok-scraper7.p.rapidapi.com/user/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"keywords": keywords, "count": count}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "tiktok-scraper7.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


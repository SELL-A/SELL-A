import os
import requests

def v1_posts(url: str, filter: str):
    """
    :API_description: Retrieve hot, new, or top posts from a specified subreddit URL, providing detailed metadata and engagement metrics for each post.
    :param url: The URL of the subreddit to fetch posts from(e.g. https://www.reddit.com/r/wallstreetbets).
    :param filter: The filter to apply to the posts (e.g., 'hot', 'new', etc.).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "meta": {
      "type": "object",
      "properties": {
        "version": {
          "type": "string"
        },
        "status": {
          "type": "integer"
        },
        "copywrite": {
          "type": "string"
        },
        "total": {
          "type": "integer"
        }
      },
      "required": ["version", "status", "copywrite", "total"]
    },
    "body": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "approved_at_utc": {
            "type": ["null", "integer"]
          },
          "subreddit": {
            "type": "string"
          },
          "selftext": {
            "type": "string"
          },
          "author_fullname": {
            "type": "string"
          },
          "saved": {
            "type": "boolean"
          },
          "mod_reason_title": {
            "type": ["null", "string"]
          },
          "gilded": {
            "type": "integer"
          },
          "clicked": {
            "type": "boolean"
          },
          "title": {
            "type": "string"
          },
          "link_flair_richtext": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "e": {
                  "type": "string"
                },
                "t": {
                  "type": "string"
                }
              },
              "required": ["e", "t"]
            }
          },
          "subreddit_name_prefixed": {
            "type": "string"
          },
          "hidden": {
            "type": "boolean"
          },
          "pwls": {
            "type": "integer"
          },
          "link_flair_css_class": {
            "type": "string"
          },
          "downs": {
            "type": "integer"
          },
          "thumbnail_height": {
            "type": ["null", "integer"]
          },
          "top_awarded_type": {
            "type": ["null", "string"]
          },
          "hide_score": {
            "type": "boolean"
          },
          "name": {
            "type": "string"
          },
          "quarantine": {
            "type": "boolean"
          },
          "link_flair_text_color": {
            "type": "string"
          },
          "upvote_ratio": {
            "type": "number"
          },
          "author_flair_background_color": {
            "type": ["null", "string"]
          },
          "subreddit_type": {
            "type": "string"
          },
          "ups": {
            "type": "integer"
          },
          "total_awards_received": {
            "type": "integer"
          },
          "media_embed": {
            "type": "array",
            "items": {}
          },
          "thumbnail_width": {
            "type": ["null", "integer"]
          },
          "author_flair_template_id": {
            "type": ["null", "string"]
          },
          "is_original_content": {
            "type": "boolean"
          },
          "user_reports": {
            "type": "array",
            "items": {}
          },
          "secure_media": {
            "type": ["null", "object"]
          },
          "is_reddit_media_domain": {
            "type": "boolean"
          },
          "is_meta": {
            "type": "boolean"
          },
          "category": {
            "type": ["null", "string"]
          },
          "secure_media_embed": {
            "type": "array",
            "items": {}
          },
          "link_flair_text": {
            "type": "string"
          },
          "can_mod_post": {
            "type": "boolean"
          },
          "score": {
            "type": "integer"
          },
          "approved_by": {
            "type": ["null", "string"]
          },
          "is_created_from_ads_ui": {
            "type": "boolean"
          },
          "author_premium": {
            "type": "boolean"
          },
          "thumbnail": {
            "type": "string"
          },
          "edited": {
            "type": "boolean"
          },
          "author_flair_css_class": {
            "type": ["null", "string"]
          },
          "author_flair_richtext": {
            "type": "array",
            "items": {}
          },
          "gildings": {
            "type": "object"
          },
          "content_categories": {
            "type": ["null", "array"]
          },
          "is_self": {
            "type": "boolean"
          },
          "mod_note": {
            "type": ["null", "string"]
          },
          "created": {
            "type": "integer"
          },
          "link_flair_type": {
            "type": "string"
          },
          "wls": {
            "type": "integer"
          },
          "removed_by_category": {
            "type": ["null", "string"]
          },
          "banned_by": {
            "type": ["null", "string"]
          },
          "author_flair_type": {
            "type": "string"
          },
          "domain": {
            "type": "string"
          },
          "allow_live_comments": {
            "type": "boolean"
          },
          "selftext_html": {
            "type": ["null", "string"]
          },
          "likes": {
            "type": ["null", "boolean"]
          },
          "suggested_sort": {
            "type": ["null", "string"]
          },
          "banned_at_utc": {
            "type": ["null", "integer"]
          },
          "view_count": {
            "type": ["null", "integer"]
          },
          "archived": {
            "type": "boolean"
          },
          "no_follow": {
            "type": "boolean"
          },
          "is_crosspostable": {
            "type": "boolean"
          },
          "pinned": {
            "type": "boolean"
          },
          "over_18": {
            "type": "boolean"
          },
          "all_awardings": {
            "type": "array",
            "items": {}
          },
          "awarders": {
            "type": "array",
            "items": {}
          },
          "media_only": {
            "type": "boolean"
          },
          "can_gild": {
            "type": "boolean"
          },
          "spoiler": {
            "type": "boolean"
          },
          "locked": {
            "type": "boolean"
          },
          "author_flair_text": {
            "type": ["null", "string"]
          },
          "treatment_tags": {
            "type": "array",
            "items": {}
          },
          "visited": {
            "type": "boolean"
          },
          "removed_by": {
            "type": ["null", "string"]
          },
          "num_reports": {
            "type": ["null", "integer"]
          },
          "distinguished": {
            "type": ["null", "string"]
          },
          "subreddit_id": {
            "type": "string"
          },
          "author_is_blocked": {
            "type": "boolean"
          },
          "mod_reason_by": {
            "type": ["null", "string"]
          },
          "removal_reason": {
            "type": ["null", "string"]
          },
          "link_flair_background_color": {
            "type": "string"
          },
          "id": {
            "type": "string"
          },
          "is_robot_indexable": {
            "type": "boolean"
          },
          "report_reasons": {
            "type": ["null", "array"]
          },
          "author": {
            "type": "string"
          },
          "discussion_type": {
            "type": ["null", "string"]
          },
          "num_comments": {
            "type": "integer"
          },
          "send_replies": {
            "type": "boolean"
          },
          "contest_mode": {
            "type": "boolean"
          },
          "mod_reports": {
            "type": "array",
            "items": {}
          },
          "author_patreon_flair": {
            "type": "boolean"
          },
          "author_flair_text_color": {
            "type": ["null", "string"]
          },
          "permalink": {
            "type": "string"
          },
          "stickied": {
            "type": "boolean"
          },
          "url": {
            "type": "string"
          },
          "subreddit_subscribers": {
            "type": "integer"
          },
          "created_utc": {
            "type": "integer"
          },
          "num_crossposts": {
            "type": "integer"
          },
          "media": {
            "type": ["null", "object"]
          },
          "is_video": {
            "type": "boolean"
          }
        },
        "required": [
          "approved_at_utc", "subreddit", "selftext", "author_fullname", "saved", "mod_reason_title", "gilded", "clicked", "title", "link_flair_richtext", "subreddit_name_prefixed", "hidden", "pwls", "link_flair_css_class", "downs", "thumbnail_height", "top_awarded_type", "hide_score", "name", "quarantine", "link_flair_text_color", "upvote_ratio", "author_flair_background_color", "subreddit_type", "ups", "total_awards_received", "media_embed", "thumbnail_width", "author_flair_template_id", "is_original_content", "user_reports", "secure_media", "is_reddit_media_domain", "is_meta", "category", "secure_media_embed", "link_flair_text", "can_mod_post", "score", "approved_by", "is_created_from_ads_ui", "author_premium", "thumbnail", "edited", "author_flair_css_class", "author_flair_richtext", "gildings", "content_categories", "is_self", "mod_note", "created", "link_flair_type", "wls", "removed_by_category", "banned_by", "author_flair_type", "domain", "allow_live_comments", "selftext_html", "likes", "suggested_sort", "banned_at_utc", "view_count", "archived", "no_follow", "is_crosspostable", "pinned", "over_18", "all_awardings", "awarders", "media_only", "can_gild", "spoiler", "locked", "author_flair_text", "treatment_tags", "visited", "removed_by", "num_reports", "distinguished", "subreddit_id", "author_is_blocked", "mod_reason_by", "removal_reason", "link_flair_background_color", "id", "is_robot_indexable", "report_reasons", "author", "discussion_type", "num_comments", "send_replies", "contest_mode", "mod_reports", "author_patreon_flair", "author_flair_text_color", "permalink", "stickied", "url", "subreddit_subscribers", "created_utc", "num_crossposts", "media", "is_video"
        ]
      }
    }
  },
  "required": ["meta", "body"]
}
    ```
    """
    api_url = "https://reddit3.p.rapidapi.com/v1/reddit/posts"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"url": url, "filter": filter}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "reddit3.p.rapidapi.com"
    }

    response = requests.get(api_url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
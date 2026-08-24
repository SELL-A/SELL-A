import os
import requests

def v1_user_data(username, filter="comments", sortType="new"):
    """
    :API_description: Retrieve posts and comments from a specified user, with options to filter and sort the results.
    :param username: The Reddit username whose data is to be retrieved(e.g. spez).
    :param filter: The type of data to filter, e.g., 'comments' or 'posts'. Default is 'comments'.
    :param sortType: The sorting criteria, e.g., 'new', 'top', etc. Default is 'new'.
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
        "username": {
          "type": "string"
        },
        "filter": {
          "type": "string"
        },
        "sortType": {
          "type": "string"
        }
      },
      "required": ["version", "status", "copywrite", "username", "filter", "sortType"]
    },
    "body": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "subreddit_id": {
            "type": "string"
          },
          "approved_at_utc": {
            "type": ["null", "integer"]
          },
          "author_is_blocked": {
            "type": "boolean"
          },
          "comment_type": {
            "type": ["null", "string"]
          },
          "link_title": {
            "type": "string"
          },
          "mod_reason_by": {
            "type": ["null", "string"]
          },
          "banned_by": {
            "type": ["null", "string"]
          },
          "ups": {
            "type": "integer"
          },
          "num_reports": {
            "type": ["null", "integer"]
          },
          "author_flair_type": {
            "type": "string"
          },
          "total_awards_received": {
            "type": "integer"
          },
          "subreddit": {
            "type": "string"
          },
          "link_author": {
            "type": "string"
          },
          "likes": {
            "type": ["null", "boolean"]
          },
          "replies": {
            "type": "string"
          },
          "user_reports": {
            "type": "array",
            "items": {}
          },
          "saved": {
            "type": "boolean"
          },
          "id": {
            "type": "string"
          },
          "banned_at_utc": {
            "type": ["null", "integer"]
          },
          "mod_reason_title": {
            "type": ["null", "string"]
          },
          "gilded": {
            "type": "integer"
          },
          "archived": {
            "type": "boolean"
          },
          "collapsed_reason_code": {
            "type": ["null", "string"]
          },
          "no_follow": {
            "type": "boolean"
          },
          "author": {
            "type": "string"
          },
          "num_comments": {
            "type": "integer"
          },
          "can_mod_post": {
            "type": "boolean"
          },
          "send_replies": {
            "type": "boolean"
          },
          "parent_id": {
            "type": "string"
          },
          "score": {
            "type": "integer"
          },
          "author_fullname": {
            "type": "string"
          },
          "over_18": {
            "type": "boolean"
          },
          "report_reasons": {
            "type": ["null", "string"]
          },
          "removal_reason": {
            "type": ["null", "string"]
          },
          "approved_by": {
            "type": ["null", "string"]
          },
          "controversiality": {
            "type": "integer"
          },
          "body": {
            "type": "string"
          },
          "edited": {
            "type": "boolean"
          },
          "top_awarded_type": {
            "type": ["null", "string"]
          },
          "downs": {
            "type": "integer"
          },
          "author_flair_css_class": {
            "type": ["null", "string"]
          },
          "is_submitter": {
            "type": "boolean"
          },
          "collapsed": {
            "type": "boolean"
          },
          "author_flair_richtext": {
            "type": "array",
            "items": {}
          },
          "author_patreon_flair": {
            "type": "boolean"
          },
          "body_html": {
            "type": "string"
          },
          "gildings": {
            "type": "array",
            "items": {}
          },
          "collapsed_reason": {
            "type": ["null", "string"]
          },
          "distinguished": {
            "type": ["null", "string"]
          },
          "associated_award": {
            "type": ["null", "string"]
          },
          "stickied": {
            "type": "boolean"
          },
          "author_premium": {
            "type": "boolean"
          },
          "can_gild": {
            "type": "boolean"
          },
          "link_id": {
            "type": "string"
          },
          "unrepliable_reason": {
            "type": ["null", "string"]
          },
          "author_flair_text_color": {
            "type": ["null", "string"]
          },
          "score_hidden": {
            "type": "boolean"
          },
          "permalink": {
            "type": "string"
          },
          "subreddit_type": {
            "type": "string"
          },
          "link_permalink": {
            "type": "string"
          },
          "name": {
            "type": "string"
          },
          "author_flair_template_id": {
            "type": ["null", "string"]
          },
          "subreddit_name_prefixed": {
            "type": "string"
          },
          "author_flair_text": {
            "type": ["null", "string"]
          },
          "treatment_tags": {
            "type": "array",
            "items": {}
          },
          "created": {
            "type": "integer"
          },
          "created_utc": {
            "type": "integer"
          },
          "awarders": {
            "type": "array",
            "items": {}
          },
          "all_awardings": {
            "type": "array",
            "items": {}
          },
          "locked": {
            "type": "boolean"
          },
          "author_flair_background_color": {
            "type": ["null", "string"]
          },
          "collapsed_because_crowd_control": {
            "type": ["null", "string"]
          },
          "mod_reports": {
            "type": "array",
            "items": {}
          },
          "quarantine": {
            "type": "boolean"
          },
          "mod_note": {
            "type": ["null", "string"]
          },
          "link_url": {
            "type": "string"
          }
        },
        "required": [
          "subreddit_id",
          "approved_at_utc",
          "author_is_blocked",
          "comment_type",
          "link_title",
          "mod_reason_by",
          "banned_by",
          "ups",
          "num_reports",
          "author_flair_type",
          "total_awards_received",
          "subreddit",
          "link_author",
          "likes",
          "replies",
          "user_reports",
          "saved",
          "id",
          "banned_at_utc",
          "mod_reason_title",
          "gilded",
          "archived",
          "collapsed_reason_code",
          "no_follow",
          "author",
          "num_comments",
          "can_mod_post",
          "send_replies",
          "parent_id",
          "score",
          "author_fullname",
          "over_18",
          "report_reasons",
          "removal_reason",
          "approved_by",
          "controversiality",
          "body",
          "edited",
          "top_awarded_type",
          "downs",
          "author_flair_css_class",
          "is_submitter",
          "collapsed",
          "author_flair_richtext",
          "author_patreon_flair",
          "body_html",
          "gildings",
          "collapsed_reason",
          "distinguished",
          "associated_award",
          "stickied",
          "author_premium",
          "can_gild",
          "link_id",
          "unrepliable_reason",
          "author_flair_text_color",
          "score_hidden",
          "permalink",
          "subreddit_type",
          "link_permalink",
          "name",
          "author_flair_template_id",
          "subreddit_name_prefixed",
          "author_flair_text",
          "treatment_tags",
          "created",
          "created_utc",
          "awarders",
          "all_awardings",
          "locked",
          "author_flair_background_color",
          "collapsed_because_crowd_control",
          "mod_reports",
          "quarantine",
          "mod_note",
          "link_url"
        ]
      }
    }
  },
  "required": ["meta", "body"]
}
    ```
    """
    url = "https://reddit3.p.rapidapi.com/v1/reddit/user-data"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"username": username, "filter": filter, "sortType": sortType}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "reddit3.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
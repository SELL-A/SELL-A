import os
import requests

def v1_post_details(url: str):
    """
    :API_description: Retrieve detailed metadata and content of a Reddit post, including title, author, engagement metrics, and a comparative analysis of hedge funds versus the S&P 500.
    :param url: The URL of the Reddit post to retrieve information for(e.g. https://www.reddit.com/r/wallstreetbets/comments/p0esdp/do_hedge_funds_beat_the_market_i_analyzed_the).
    :response_schema: 
    ```json
{
  "meta": {
    "version": "v1.0",
    "status": 200,
    "copywrite": "https://devAPI.ai",
    "totalComments": 7
  },
  "body": {
    "post": {
      "approved_at_utc": null,
      "subreddit": "wallstreetbets",
      "selftext": "...",
      "author_fullname": "t2_q15pxyy",
      "saved": false,
      "mod_reason_title": null,
      "gilded": 1,
      "clicked": false,
      "title": "Do Hedge Funds beat the market? - I analyzed the performance of 5000+ Hedge Funds over the past 24 years and benchmarked it against SP500. Here are the results!",
      "link_flair_richtext": [
        {
          "e": "text",
          "t": "DD"
        }
      ],
      "subreddit_name_prefixed": "r/wallstreetbets",
      "hidden": false,
      "pwls": 7,
      "link_flair_css_class": "dd",
      "downs": 0,
      "thumbnail_height": 37,
      "top_awarded_type": null,
      "hide_score": false,
      "name": "t3_p0esdp",
      "quarantine": false,
      "link_flair_text_color": "light",
      "upvote_ratio": 0.96,
      "author_flair_background_color": "#000000",
      "subreddit_type": "public",
      "ups": 951,
      "total_awards_received": 0,
      "media_embed": [],
      "thumbnail_width": 140,
      "author_flair_template_id": "28fbe25a-7c59-11ea-965e-0e0a65cd3f97",
      "is_original_content": true,
      "user_reports": [],
      "secure_media": null,
      "is_reddit_media_domain": false,
      "is_meta": false,
      "category": null,
      "secure_media_embed": [],
      "link_flair_text": "DD",
      "can_mod_post": false,
      "score": 951,
      "approved_by": null,
      "is_created_from_ads_ui": false,
      "author_premium": true,
      "thumbnail": "https://a.thumbs.redditmedia.com/dM77I9_0EljbAwXEDgnYHVXteh7c7aGtSVxV2L6iN00.jpg",
      "edited": false,
      "author_flair_css_class": null,
      "author_flair_richtext": [
        {
          "e": "text",
          "t": "Anal(yst)"
        }
      ],
      "gildings": [],
      "content_categories": null,
      "is_self": true,
      "mod_note": null,
      "created": 1628429859,
      "link_flair_type": "richtext",
      "wls": 7,
      "removed_by_category": null,
      "banned_by": null,
      "author_flair_type": "richtext",
      "domain": "self.wallstreetbets",
      "allow_live_comments": true,
      "selftext_html": "...",
      "likes": null,
      "suggested_sort": "confidence",
      "banned_at_utc": null,
      "view_count": null,
      "archived": false,
      "no_follow": false,
      "is_crosspostable": false,
      "pinned": false,
      "over_18": false,
      "all_awardings": [],
      "awarders": [],
      "media_only": false,
      "link_flair_template_id": "5692ce02-b860-11e5-b542-0edc7016bbd3",
      "can_gild": false,
      "spoiler": false,
      "locked": false,
      "author_flair_text": "Anal(yst)",
      "treatment_tags": [],
      "visited": false,
      "removed_by": null,
      "num_reports": null,
      "distinguished": null,
      "subreddit_id": "t5_2th52",
      "author_is_blocked": false,
      "mod_reason_by": null,
      "removal_reason": null,
      "link_flair_background_color": "#365b8c",
      "id": "p0esdp",
      "is_robot_indexable": true,
      "num_duplicates": 1,
      "report_reasons": null,
      "author": "nobjos",
      "discussion_type": null,
      "num_comments": 207,
      "send_replies": true,
      "whitelist_status": "some_ads",
      "contest_mode": false,
      "mod_reports": [],
      "author_patreon_flair": false,
      "author_flair_text_color": "light",
      "permalink": "/r/wallstreetbets/comments/p0esdp/do_hedge_funds_beat_the_market_i_analyzed_the/",
      "parent_whitelist_status": "some_ads",
      "stickied": false,
      "url": "https://www.reddit.com/r/wallstreetbets/comments/p0esdp/do_hedge_funds_beat_the_market_i_analyzed_the/",
      "subreddit_subscribers": 14410674,
      "created_utc": 1628429859,
      "num_crossposts": 1,
      "media": null,
      "is_video": false
    },
    "post_comments": [
      {
        "id": "h86287t",
        "author": "VisualMod",
        "up_votes": 1,
        "score": 1,
        "likes": "",
        "created_utc": 1628429951,
        "content": "..."
      },
      {
        "id": "h866eio",
        "author": "Original-Ad-4642",
        "up_votes": 480,
        "score": 480,
        "likes": "",
        "created_utc": 1628432189,
        "content": "..."
      },
      {
        "id": "h863fjs",
        "author": "nobjos",
        "up_votes": 178,
        "score": 178,
        "likes": "",
        "created_utc": 1628430610,
        "content": "..."
      }
    ]
  }
}
```
    """
    api_url = "https://reddit3.p.rapidapi.com/v1/reddit/post"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"url": url}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "reddit3.p.rapidapi.com"
    }

    response = requests.get(api_url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


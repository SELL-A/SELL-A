import os
import requests

def v1_search(search, filter, timeFilter, sortType):
    """
    :API_description: Search and filter Reddit posts, comments, users, and communities based on specific topics and time frames.
    :param search: The term to search for in Reddit posts(The search term. Example: investing or (stock market AND (interest rates OR inflation))).
    :param filter: The type of content to filter (e.g., posts, comments The type of content to filter (posts, comments, media, users, or communities). Users and communities are available sitewide only.).
    :param timeFilter: The time frame to filter the search results (e.g., day, week, month, year) The time period to filter by (all, year, month, week, day, or hour). 
    :param sortType: The sorting method for the search results (e.g., relevance, new) The sorting type (relevance, hot, top, new, or comments). Default: relevance.
    :response_schema: 
    ```json
{
  "meta": {
    "version": "v1.0",
    "status": 200,
    "copywrite": "https://devAPI.ai",
    "search": "investing",
    "subreddit": "wallstreetbets",
    "filter": "posts",
    "timeFilter": "all",
    "sortType": "relevance",
    "total": 25
  },
  "body": [
    {
      "approved_at_utc": null,
      "subreddit": "stocks",
      "selftext": "After reading many books, watching hundreds of videos, and even joining things like skillshare, I still am not sold that investing long term is the way to go. \n\nI am 18 and make $27 an hour, everything I watched and learned from told me to save $10,000 and invest it into an ETF like the S&amp;P500 for 22 years until I'm 40. Use compound interest from that 10k (about 8%-10% is the common return of the S&amp;P) until it reaches 1.7M and then I can retire at 40.\n\nBut that all seems too easy, what's the catch. I know things like COVID-19 crashed the market but wouldn't you just sell and buy back at the lowest and continue?",
      "author_fullname": "t2_5gw4zam8",
      "saved": false,
      "mod_reason_title": null,
      "gilded": 0,
      "clicked": false,
      "title": "Does Investing Actually Work?",
      "link_flair_richtext": [],
      "subreddit_name_prefixed": "r/stocks",
      "hidden": false,
      "pwls": 6,
      "link_flair_css_class": "advice",
      "downs": 0,
      "thumbnail_height": null,
      "top_awarded_type": null,
      "hide_score": false,
      "name": "t3_1694h71",
      "quarantine": false,
      "link_flair_text_color": "light",
      "upvote_ratio": 0.59,
      "author_flair_background_color": null,
      "subreddit_type": "public",
      "ups": 41,
      "total_awards_received": 0,
      "media_embed": [],
      "thumbnail_width": null,
      "author_flair_template_id": null,
      "is_original_content": false,
      "user_reports": [],
      "secure_media": null,
      "is_reddit_media_domain": false,
      "is_meta": false,
      "category": null,
      "secure_media_embed": [],
      "link_flair_text": "Advice",
      "can_mod_post": false,
      "score": 41,
      "approved_by": null,
      "is_created_from_ads_ui": false,
      "author_premium": false,
      "thumbnail": "self",
      "edited": false,
      "author_flair_css_class": null,
      "author_flair_richtext": [],
      "gildings": [],
      "content_categories": null,
      "is_self": true,
      "mod_note": null,
      "created": 1693766009,
      "link_flair_type": "text",
      "wls": 6,
      "removed_by_category": null,
      "banned_by": null,
      "author_flair_type": "text",
      "domain": "self.stocks",
      "allow_live_comments": false,
      "selftext_html": "&lt;!-- SC_OFF --&gt;&lt;div class=\"md\"&gt;&lt;p&gt;After reading many books, watching hundreds of videos, and even joining things like skillshare, I still am not sold that investing long term is the way to go. &lt;/p&gt;\n\n&lt;p&gt;I am 18 and make $27 an hour, everything I watched and learned from told me to save $10,000 and invest it into an ETF like the S&amp;amp;P500 for 22 years until I&amp;#39;m 40. Use compound interest from that 10k (about 8%-10% is the common return of the S&amp;amp;P) until it reaches 1.7M and then I can retire at 40.&lt;/p&gt;\n\n&lt;p&gt;But that all seems too easy, what&amp;#39;s the catch. I know things like COVID-19 crashed the market but wouldn&amp;#39;t you just sell and buy back at the lowest and continue?&lt;/p&gt;\n&lt;/div&gt;&lt;!-- SC_ON --&gt;",
      "likes": null,
      "suggested_sort": "confidence",
      "banned_at_utc": null,
      "view_count": null,
      "archived": false,
      "no_follow": false,
      "is_crosspostable": true,
      "pinned": false,
      "over_18": false,
      "all_awardings": [],
      "awarders": [],
      "media_only": false,
      "link_flair_template_id": "823be0a6-65e6-11e5-9784-125ee764bc01",
      "can_gild": false,
      "spoiler": false,
      "locked": false,
      "author_flair_text": null,
      "treatment_tags": [],
      "visited": false,
      "removed_by": null,
      "num_reports": null,
      "distinguished": null,
      "subreddit_id": "t5_2qjfk",
      "author_is_blocked": false,
      "mod_reason_by": null,
      "removal_reason": null,
      "link_flair_background_color": "#646d73",
      "id": "1694h71",
      "is_robot_indexable": true,
      "report_reasons": null,
      "author": "Low_Entry5644",
      "discussion_type": null,
      "num_comments": 277,
      "send_replies": true,
      "whitelist_status": "all_ads",
      "contest_mode": false,
      "mod_reports": [],
      "author_patreon_flair": false,
      "author_flair_text_color": null,
      "permalink": "/r/stocks/comments/1694h71/does_investing_actually_work/",
      "parent_whitelist_status": "all_ads",
      "stickied": false,
      "url": "https://www.reddit.com/r/stocks/comments/1694h71/does_investing_actually_work/",
      "subreddit_subscribers": 6888353,
      "created_utc": 1693766009,
      "num_crossposts": 0,
      "media": null,
      "is_video": false
    },
    {
      "approved_at_utc": null,
      "subreddit": "dataisbeautiful",
      "selftext": "",
      "author_fullname": "t2_7vc8bvxk",
      "saved": false,
      "mod_reason_title": null,
      "gilded": 1,
      "clicked": false,
      "title": "[OC] Why you should start investing early in life",
      "link_flair_richtext": [],
      "subreddit_name_prefixed": "r/dataisbeautiful",
      "hidden": false,
      "pwls": 6,
      "link_flair_css_class": "oc",
      "downs": 0,
      "thumbnail_height": 140,
      "top_awarded_type": null,
      "hide_score": false,
      "name": "t3_wo6fpu",
      "quarantine": false,
      "link_flair_text_color": null,
      "upvote_ratio": 0.75,
      "author_flair_background_color": null,
      "subreddit_type": "public",
      "ups": 19617,
      "total_awards_received": 0,
      "media_embed": [],
      "thumbnail_width": 140,
      "author_flair_template_id": "1c7d62a6-099d-11e7-9b3c-0ee50bfd7a4c",
      "is_original_content": false,
      "user_reports": [],
      "secure_media": {
        "reddit_video": {
          "bitrate_kbps": 4800,
          "fallback_url": "https://v.redd.it/r3bpj2n6loh91/DASH_1080.mp4?source=fallback",
          "height": 1080,
          "width": 864,
          "scrubber_media_url": "https://v.redd.it/r3bpj2n6loh91/DASH_96.mp4",
          "dash_url": "https://v.redd.it/r3bpj2n6loh91/DASHPlaylist.mpd?a=1717560956%2CNGIyYTk3YWRhOWU4NWI5ODRkM2IxMWVmZmU1NmFiNTg3YmE0OGNjNDc0N2Q5M2MwMWU5NGIyYzFhMzM3MDBiYg%3D%3D&amp;v=1&amp;f=sd",
          "duration": 33,
          "hls_url": "https://v.redd.it/r3bpj2n6loh91/HLSPlaylist.m3u8?a=1717560956%2CMmY4YTc3ZGRhODQ5YTcxYTAwMGU5ZGI5ZGI1NmY0NGQ4NTE4OGE0ZTQ2YTdjYjY2Y2IwMGFjZDAwYzM0MjhkMQ%3D%3D&amp;v=1&amp;f=sd",
          "is_gif": false,
          "transcoding_status": "completed"
        }
      },
      "is_reddit_media_domain": true,
      "is_meta": false,
      "category": null,
      "secure_media_embed": [],
      "link_flair_text": "OC",
      "can_mod_post": false,
      "score": 19617,
      "approved_by": null,
      "is_created_from_ads_ui": false,
      "author_premium": false,
      "thumbnail": "https://b.thumbs.redditmedia.com/L8gQTBQsWCN-4EQCKx9pP_FXsDSYEUfJfZCAsSoVzMU.jpg",
      "edited": false,
      "author_flair_css_class": "ocmaker",
      "author_flair_richtext": [],
      "gildings": [],
      "post_hint": "hosted:video",
      "content_categories": null,
      "is_self": false,
      "mod_note": null,
      "created": 1660483764,
      "link_flair_type": "text",
      "wls": 6,
      "removed_by_category": null,
      "banned_by": null,
      "author_flair_type": "text",
      "domain": "v.redd.it",
      "allow_live_comments": true,
      "selftext_html": null,
      "likes": null,
      "suggested_sort": null,
      "banned_at_utc": null,
      "url_overridden_by_dest": "https://v.redd.it/r3bpj2n6loh91",
      "view_count": null,
      "archived": true,
      "no_follow": false,
      "is_crosspostable": true,
      "pinned": false,
      "over_18": false,
      "preview": {
        "images": [
          {
            "source": {
              "url": "https://external-preview.redd.it/nrq5J7SjH-CvI8OTIW_vnNxxgbu83Ewn98te7EE1UBc.png?format=pjpg&amp;auto=webp&amp;s=937ae3e08043053cd571671111a9851af399016d",
              "width": 1080,
              "height": 1350
            },
            "resolutions": [
              {
                "url": "https://external-preview.redd.it/nrq5J7SjH-CvI8OTIW_vnNxxgbu83Ewn98te7EE1UBc.png?width=108&amp;crop=smart&amp;format=pjpg&amp;auto=webp&amp;s=d1c22659490e61ca7d373f446a17448a9c029687",
                "width": 108,
                "height": 135
              },
              {
                "url": "https://external-preview.redd.it/nrq5J7SjH-CvI8OTIW_vnNxxgbu83Ewn98te7EE1UBc.png?width=216&amp;crop=smart&amp;format=pjpg&amp;auto=webp&amp;s=105e965d178890ad3790e8be2e1bac9713d62ae8",
                "width": 216,
                "height": 270
              },
              {
                "url": "https://external-preview.redd.it/nrq5J7SjH-CvI8OTIW_vnNxxgbu83Ewn98te7EE1UBc.png?width=320&amp;crop=smart&amp;format=pjpg&amp;auto=webp&amp;s=1d5d1b689a5c61790535d8251b3b68a8823038d6",
                "width": 320,
                "height": 400
              }
            ],
            "variants": [],
            "id": "-h7WvabrrmgK2Oc63bHzKcbLX1qokJhS6LU0dwy6y2Q"
          }
        ],
        "enabled": false
      },
      "all_awardings": [],
      "awarders": [],
      "media_only": false,
      "can_gild": false,
      "spoiler": false,
      "locked": false,
      "author_flair_text": "OC: 95",
      "treatment_tags": [],
      "visited": false,
      "removed_by": null,
      "num_reports": null,
      "distinguished": null,
      "subreddit_id": "t5_2tk95",
      "author_is_blocked": false,
      "mod_reason_by": null,
      "removal_reason": null,
      "link_flair_background_color": null,
      "id": "wo6fpu",
      "is_robot_indexable": true,
      "report_reasons": null,
      "author": "PieChartPirate",
      "discussion_type": null,
      "num_comments": 3187,
      "send_replies": true,
      "whitelist_status": "all_ads",
      "contest_mode": false,
      "mod_reports": [],
      "author_patreon_flair": false,
      "author_flair_text_color": "dark",
      "permalink": "/r/dataisbeautiful/comments/wo6fpu/oc_why_you_should_start_investing_early_in_life/",
      "parent_whitelist_status": "all_ads",
      "stickied": false,
      "url": "https://v.redd.it/r3bpj2n6loh91",
      "subreddit_subscribers": 20722217,
      "created_utc": 1660483764,
      "num_crossposts": 11,
      "media": {
        "reddit_video": {
          "bitrate_kbps": 4800,
          "fallback_url": "https://v.redd.it/r3bpj2n6loh91/DASH_1080.mp4?source=fallback",
          "height": 1080,
          "width": 864,
          "scrubber_media_url": "https://v.redd.it/r3bpj2n6loh91/DASH_96.mp4",
          "dash_url": "https://v.redd.it/r3bpj2n6loh91/DASHPlaylist.mpd?a=1717560956%2CNGIyYTk3YWRhOWU4NWI5ODRkM2IxMWVmZmU1NmFiNTg3YmE0OGNjNDc0N2Q5M2MwMWU5NGIyYzFhMzM3MDBiYg%3D%3D&amp;v=1&amp;f=sd",
          "duration": 33,
          "hls_url": "https://v.redd.it/r3bpj2n6loh91/HLSPlaylist.m3u8?a=1717560956%2CMmY4YTc3ZGRhODQ5YTcxYTAwMGU5ZGI5ZGI1NmY0NGQ4NTE4OGE0ZTQ2YTdjYjY2Y2IwMGFjZDAwYzM0MjhkMQ%3D%3D&amp;v=1&amp;f=sd",
          "is_gif": false,
          "transcoding_status": "completed"
        }
      },
      "is_video": true
    }
  ]
}
    ```
    """
    url = "https://reddit3.p.rapidapi.com/v1/reddit/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "search": search,
        "filter": filter,
        "timeFilter": timeFilter,
        "sortType": sortType
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "reddit3.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
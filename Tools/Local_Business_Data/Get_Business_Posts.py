import os
import requests

def Get_Business_Posts(business_id):
    """
    :API_description: Get all / paginate Business Owner Posts ("From the owner" section on Google Maps) by Business Id, sorted chronologically. Supports for limit + cursor based pagination / scrolling.
    :param business_id: The unique identifier of the business.
    :response_schema: 
    ```json
{
  "status": "OK",
  "request_id": "07af6ffe-13c1-4a4d-9394-68a1e0177448",
  "parameters": {
    "business_id": "0x880fd393d427a591:0x8cba02d713a995ed",
    "language": "en",
    "region": "us",
    "cursor": null
  },
  "data": {
    "posts": [
      {
        "post_id": "CIHM0ogKEIGt9-DK_vKrbQ",
        "post_link": "...",
        "post_datetime_utc": "2026-06-03T16:14:13.000Z",
        "post_timestamp": 1780503253,
        "post_text": "...",
        "post_links": null,
        "post_photos": [
          "..."
        ]
      },
      {
        "post_id": "CIHM0ogKENPRstGc8qnj_wE",
        "post_link": "...",
        "post_datetime_utc": "2026-06-03T14:48:15.000Z",
        "post_timestamp": 1780498095,
        "post_text": "...",
        "post_links": [
          {
            "url": "https://www.myrescueplumbing.com/plumbing-services/drain-cleaning-chicago/",
            "caption": "Learn more"
          }
        ],
        "post_photos": [
          "https://lh3.googleusercontent.com/geougc/AF1QipORCIpXsWGUXxyA4N38wy_2-4C2MMx_I3jwZcoV=h400-no"
        ]
      },
      {
        "post_id": "CIHM0ogKELWt1f6Ei5mNwwE",
        "post_link": "...",
        "post_datetime_utc": "2026-06-03T14:47:23.000Z",
        "post_timestamp": 1780498043,
        "post_text": "...",
        "post_links": [
          {
            "url": "...",
            "caption": "Learn more"
          }
        ],
        "post_photos": [
          "https://lh3.googleusercontent.com/geougc/AF1QipPmAO-iv5_9pYGpJDVE8YV7qQslkyd3dINlxiBa=h400-no"
        ]
      }
    ],
    "cursor": "..."
  }
}
```
    """
    url = "https://api.openwebninja.com/local-business-data/business-posts"
    querystring = {
        "business_id": business_id
    }
    headers = {
        "X-API-Key": "ak_2a42z3zdrr3rnxcapzcpfplyqqohqtgk8n0rsxjtvftpre3"
        }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
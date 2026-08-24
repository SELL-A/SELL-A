import os
import requests

def Get_Business_Photos(business_id):
    """
    :API_description: Get business photos by Business Id with support for limit + cursor based pagination / scrolling.
    :param business_id: The unique identifier of the business.
    :response_schema: 

    '''json
    {
  "status": "OK",
  "request_id": "4f489210-f61d-431a-9958-588b25b49c74",
  "parameters": {
    "business_id": "0x89c259b5a9bd152b:0x31453e62a3be9f76",
    "language": "en",
    "region": "us",
    "limit": 20,
    "is_video": false
  },
  "data": [
    {
      "photo_id": "AF1QipOSDUfeln6UIJbDk9H91kw25tCC_DjWQOn_FHlM",
      "photo_url": "...",
      "photo_url_large": null,
      "video_thumbnail_url": "...",
      "latitude": 40.752668568450744,
      "longitude": -73.99356477987595,
      "type": "video",
      "photo_datetime_utc": "2022-05-13T00:00:00.000Z",
      "photo_timestamp": 1652400000
    },
    {
      "photo_id": "AF1QipO6t7byRQC6yQ9xFgoMCUDCOSVrzyGZA2WV6mSl",
      "photo_url": "....",
      "photo_url_large": "....",
      "video_thumbnail_url": null,
      "latitude": 40.752502299999996,
      "longitude": -73.99320519999999,
      "type": "photo",
      "photo_datetime_utc": "2025-04-25T00:00:00.000Z",
      "photo_timestamp": 1745539200
    }
  ],
  "cursor": "EvgDKYQi49-NlUMIDwAAAAEAAAMAAAAA..."
}
    '''
    """
    url = "https://api.openwebninja.com/local-business-data/business-photos"
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
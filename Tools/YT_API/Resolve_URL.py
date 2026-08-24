import os
import requests

def Resolve_URL(youtube_url):
    """
    :API_description: Retrieves metadata about a YouTube channel, including its type, vanity URL status, and unique identifier.
    :param youtube_url: The URL of the YouTube channel or video to be resolved(e.g., https://www.youtube.com/@TED).
    :response_schema: 
    ```json
{
  "webPageType": "WEB_PAGE_TYPE_CHANNEL",
  "isVanityUrl": true,
  "browseId": "UCAuUUnT6oDeKwE6v1NGQxug",
  "params": "EgC4AQCSAwDyBgQKAjIA"
}
    ```
    """
    url = "https://yt-api.p.rapidapi.com/resolve"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"url": youtube_url}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yt-api.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
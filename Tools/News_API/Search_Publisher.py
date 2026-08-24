import os
import requests

def Search_Publisher(query):
    """
    :API_description: This endpoint allows you to search for publishers based on specific criteria such as language, country, or category
    :param query: The search query string(Just type what you're looking for.).
    :response_schema: 
    ```json{
  "success": true,
  "data": [
    {
      "title": "Basketball Forever | News. Highlights. Analysis. Trade Rumours and more.",
      "name": "Basketball Forever",
      "url": "https://basketballforever.com",
      "language": "en",
      "category": "Sports",
      "description": "Get the latest basketball news straight to the palm of your hand. Covering the NBA, NBL, NCAA, Streetball and more every day. For the love of the game.",
      "logo": "...",
      "favicon": "...",
      "links": [
        {
          "url": "...",
          "type": "facebook",
          "username": "basketballforever"
        },
        {
          "url": "...",
          "type": "twitter",
          "username": "Bballforeverfb"
        },
        {
          "url": "...",
          "type": "instagram",
          "username": "basketballforever"
        },
        {
          "url": "...",
          "type": "youtube",
          "username": "UCqhmKxk-r1URUcHLAc0b5BA"
        }
      ]
    }
  ]
}```
    """
    url = "https://news-api14.p.rapidapi.com/v2/search/publishers"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"query": query}
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "news-api14.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


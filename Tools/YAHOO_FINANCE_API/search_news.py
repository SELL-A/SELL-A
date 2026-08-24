import os
import requests

def search_news(query):
    """
    :API_description: Retrieves a list of news stories related to a specified query.
    :param query: The search query string (e.g., "AA").
    :response_schema: the news maybe is empty, the quotes maybe is empty too.
    ```json
{
  "explains": [],
  "count": 16,
  "quotes": [
    {
      "exchange": "NYQ",
      "shortname": "Alcoa Corporation",
      "quoteType": "EQUITY",
      "symbol": "AA",
      "index": "quotes",
      "score": 10010500,
      "typeDisp": "equity",
      "longname": "Alcoa Corporation",
      "exchDisp": "NYSE",
      "sector": "Basic Materials",
      "sectorDisp": "Basic Materials",
      "industry": "Aluminum",
      "industryDisp": "Aluminum",
      "dispSecIndFlag": true,
      "isYahooFinance": true
    }
  ],
  "news": [
    {
      "uuid": "f03c53d4-3cb1-37c5-827f-2912d601c767",
      "title": "Alcoa vs. Ryerson: Which Aluminum Stock Boasts Better Prospects?",
      "publisher": "Zacks",
      "link": "https://finance.yahoo.com/markets/stocks/articles/alcoa-vs-ryerson-aluminum-stock-151600663.html",
      "providerPublishTime": 1779722160,
      "type": "STORY",
      "thumbnail": {
        "resolutions": [
          {
            "url": "https://s.yimg.com/uu/api/res/1.2/GcbW5m7qBxvZwEKmAlGG8w--~B/aD00MDA7dz02MzU7YXBwaWQ9eXRhY2h5b24-/https://media.zenfs.com/en/zacks.com/947c6e6074bb9c6e577530e5110e031e",
            "width": 635,
            "height": 400,
            "tag": "original"
          },
          {
            "url": "https://s.yimg.com/uu/api/res/1.2/Y6HMdFNPxpxTyGDmuRxSGA--~B/Zmk9ZmlsbDtoPTE0MDtweW9mZj0wO3c9MTQwO2FwcGlkPXl0YWNoeW9u/https://media.zenfs.com/en/zacks.com/947c6e6074bb9c6e577530e5110e031e",
            "width": 140,
            "height": 140,
            "tag": "140x140"
          }
        ]
      },
      "relatedTickers": [
        "ALI=F",
        "AA",
        "RYZ"
      ]
    }
  ],
  "nav": [
    {
      "navName": "Aarthi Swaminathan",
      "navUrl": "https://www.yahoo.com/author/aarthi-swaminathan/"
    }
  ],
  "lists": [],
  "researchReports": [],
  "screenerFieldResults": [],
  "totalTime": 72,
  "timeTakenForQuotes": 451,
  "timeTakenForNews": 600,
  "timeTakenForAlgowatchlist": 400,
  "timeTakenForPredefinedScreener": 400,
  "timeTakenForCrunchbase": 0,
  "timeTakenForNav": 400,
  "timeTakenForResearchReports": 0,
  "timeTakenForScreenerField": 0,
  "timeTakenForCulturalAssets": 0,
  "timeTakenForSearchLists": 0
}
```
    """
    url = "https://yh-finance166.p.rapidapi.com/api/autocomplete"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"query": query}
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yahoo-finance166.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")

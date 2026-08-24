import os
import requests

def Sources():
    """
    :API_description: Retrieves a list of available news sources, excluding proprietary blocks like Twitter or Stock Tickers.
    :param None
    :response_schema: 
    ```json
[
  {
    "id": "tfswallst",
    "title": "24/7 Wall Street",
    "web": "https://247wallst.com/"
  },
  {
    "id": "abc",
    "title": "ABC News",
    "web": "https://abcnews.go.com"
  },
  {
    "id": "apnews",
    "title": "AP News",
    "web": "https://apnews.com/business"
  },
  {
    "id": "abnormalreturns",
    "title": "Abnormal Returns",
    "web": "https://abnormalreturns.com/"
  },
  {
    "id": "asiafinancial",
    "title": "Asia Financial",
    "web": "https://www.asiafinancial.com"
  },
  {
    "id": "blockworks",
    "title": "Asian Banking",
    "web": "https://asianbankingandfinance.net/"
  },
  {
    "id": "axios",
    "title": "Axios",
    "web": "https://www.axios.com"
  },
  {
    "id": "bbc",
    "title": "BBC",
    "web": "https://www.bbc.com"
  },
  {
    "id": "marketbeat",
    "title": "Baha Breaking News",
    "web": "https://breakingthenews.net/"
  },
  {
    "id": "barchart",
    "title": "Barchart",
    "web": "https://www.barchart.com/"
  },
  {
    "id": "barrons",
    "title": "Barrons",
    "web": "https://www.barrons.com"
  },
  {
    "id": "ritholtz",
    "title": "Barry Ritholtz",
    "web": "https://ritholtz.com/"
  },
  {
    "id": "benzinga",
    "title": "Benzinga",
    "web": "https://www.benzinga.com/"
  },
  {
    "id": "bloomberg",
    "title": "Bloomberg",
    "web": "https://www.bloomberg.com/"
  },
  {
    "id": "quicktake",
    "title": "Bloomberg Quicktake",
    "web": "https://www.youtube.com/channel/UChirEOpgFCupRAk5etXqPaA"
  },
  {
    "id": "bizjournals",
    "title": "Business Journals",
    "web": "https://www.bizjournals.com/"
  },
  {
    "id": "cbc",
    "title": "CBC",
    "web": "https://www.cbc.ca/s"
  },
  {
    "id": "cbs",
    "title": "CBS",
    "web": "https://www.cbsnews.com"
  },
  {
    "id": "cnbc",
    "title": "CNBC",
    "web": "https://www.cnbc.com/"
  },
  {
    "id": "cnn",
    "title": "CNN",
    "web": "https://edition.cnn.com/business"
  },
  {
    "id": "coindesk",
    "title": "Coindesk",
    "web": "https://www.coindesk.com"
  },
  {
    "id": "dw",
    "title": "DW",
    "web": "https://www.dw.com/en/business/s-1431"
  },
  {
    "id": "dailyupside",
    "title": "Daily Upside",
    "web": "https://www.thedailyupside.com/"
  },
  {
    "id": "seattle",
    "title": "Digiday",
    "web": "https://digiday.com/"
  },
  {
    "id": "entrepreneur",
    "title": "Entrepreneur",
    "web": "https://www.entrepreneur.com/"
  },
  {
    "id": "stocktwits",
    "title": "EurActiv",
    "web": "https://www.euractiv.com/"
  },
  {
    "id": "euronews",
    "title": "Euronews",
    "web": "https://www.euronews.com/"
  },
  {
    "id": "fastcompany",
    "title": "FastCompany",
    "web": "https://www.fastcompany.com"
  },
  {
    "id": "instinv",
    "title": "Financial News London",
    "web": "https://www.fnlondon.com"
  },
  {
    "id": "finpost",
    "title": "Financial Post",
    "web": "https://financialpost.com/"
  },
  {
    "id": "ft",
    "title": "Financial Times",
    "web": "https://www.ft.com"
  },
  {
    "id": "forbes",
    "title": "Forbes",
    "web": "https://www.forbes.com"
  },
  {
    "id": "fortune",
    "title": "Fortune",
    "web": "https://fortune.com/"
  },
  {
    "id": "fox",
    "title": "Fox Business",
    "web": "https://www.foxbusiness.com"
  },
  {
    "id": "globeandmail",
    "title": "Globe And Mail",
    "web": "https://www.theglobeandmail.com"
  },
  {
    "id": "google_business",
    "title": "Google Business",
    "web": "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pWVXlnQVAB?hl=en-US&gl=US&ceid=US%3Aen"
  },
  {
    "id": "googletrends",
    "title": "Google Trends",
    "web": "https://trends.google.com/trends/?geo=US"
  },
  {
    "id": "inc",
    "title": "Inc.",
    "web": "https://www.inc.com"
  }
]
```
    """
    url = "https://biztoc.p.rapidapi.com/sources"
    rapid_api_key = os.getenv('RAPID_API_KEY')

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "biztoc.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
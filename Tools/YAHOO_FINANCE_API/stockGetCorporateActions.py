import os
import requests

def stockGetCorporateActions(region, symbol):
    """
    :API_description: Retrieve YAHOO FINANCE stock CorporateActions
    :param region: The market region to query(e.g., AR, AU, BR, CA, CN, FR, DE, HK, IN, IT, MX, NZ, SG, KR, ES, TW, GB, US).
    :param symbol: The stock symbol to query(e.g., AAPL).
    :response_schema: 
    ```json
   {
  "quoteSummary": {
    "result": [
      {
        "secFilings": {
          "filings": [
            {
              "date": "2026-05-28",
              "epochDate": 1779926400,
              "type": "SD",
              "title": "Specialized Disclosure Report filed pursuant to Section 1502 of the Dodd-Frank Wall Street Reform and Consumer Protection Act relating to the use of conflict minerals (Rule 13p-1)",
              "edgarUrl": "https://finance.yahoo.com/sec-filing/AAPL/0001140361-26-023149_320193",
              "exhibits": [
                {
                  "type": "SD",
                  "url": "https://cdn.yahoofinance.com/prod/sec-filings/0000320193/000114036126023149/ef20073373_sd.htm"
                }
              ],
              "maxAge": 1
            },
            {
              "date": "2026-05-01",
              "epochDate": 1777593600,
              "type": "10-Q",
              "title": "Periodic Financial Reports",
              "edgarUrl": "https://finance.yahoo.com/sec-filing/AAPL/0000320193-26-000013_320193",
              "exhibits": [
                {
                  "type": "10-Q",
                  "url": "https://cdn.yahoofinance.com/prod/sec-filings/0000320193/000032019326000013/aapl-20260328.htm"
                },
                {
                  "type": "EX-31.1",
                  "url": "https://cdn.yahoofinance.com/prod/sec-filings/0000320193/000032019326000013/a10-qexhibit31103282026.htm"
                },
                {
                  "type": "EX-31.2",
                  "url": "https://cdn.yahoofinance.com/prod/sec-filings/0000320193/000032019326000013/a10-qexhibit31203282026.htm"
                },
                {
                  "type": "EX-32.1",
                  "url": "https://cdn.yahoofinance.com/prod/sec-filings/0000320193/000032019326000013/a10-qexhibit32103282026.htm"
                }
              ],
              "maxAge": 1
            },
            {
              "date": "2026-04-30",
              "epochDate": 1777507200,
              "type": "8-K",
              "title": "Corporate Changes & Voting Matters",
              "edgarUrl": "https://finance.yahoo.com/sec-filing/AAPL/0000320193-26-000011_320193",
              "exhibits": [
                {
                  "type": "EX-99.1",
                  "url": "https://cdn.yahoofinance.com/prod/sec-filings/0000320193/000032019326000011/a8-kex991q2202603282026.htm"
                },
                {
                  "type": "8-K",
                  "url": "https://cdn.yahoofinance.com/prod/sec-filings/0000320193/000032019326000011/aapl-20260430.htm"
                }
              ],
              "maxAge": 1
            },
            {
              "date": "2026-04-20",
              "epochDate": 1776643200,
              "type": "8-K",
              "title": "Corporate Changes & Voting Matters",
              "edgarUrl": "https://finance.yahoo.com/sec-filing/AAPL/0001140361-26-015711_320193",
              "exhibits": [
                {
                  "type": "8-K",
                  "url": "https://cdn.yahoofinance.com/prod/sec-filings/0000320193/000114036126015711/ef20071035_8k.htm"
                }
              ],
              "maxAge": 1
            }
          ],
          "maxAge": 86400
        }
      }
    ],
    "error": null
  }
}
    ```
    """
    url = "https://yahoo-finance166.p.rapidapi.com/api/stock/get-sec-filings"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"region": region, "symbol": symbol}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yahoo-finance166.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
import os
import requests

def stockGetStatistics(region, symbol):
    """
    :API_description: Retrieve YAHOO FINANCE  stock Statistics
    :param region: The market region to query(e.g., AR, AU, BR, CA, CN, FR, DE, HK, IN, IT, MX, NZ, SG, KR, ES, TW, GB, US).
    :param symbol: The stock symbol to query(e.g., AAPL).
    :response_schema: 
    ```json
{
  "quoteSummary": {
    "result": [
      {
        "defaultKeyStatistics": {
          "maxAge": 1,
          "priceHint": {
            "raw": 2,
            "fmt": "2",
            "longFmt": "2"
          },
          "enterpriseValue": {
            "raw": 4292134043648,
            "fmt": "4.29T",
            "longFmt": "4,292,134,043,648"
          },
          "forwardPE": {
            "raw": 30.341877,
            "fmt": "30.34"
          },
          "profitMargins": {
            "raw": 0.27152002,
            "fmt": "27.15%"
          },
          "floatShares": {
            "raw": 14662534368,
            "fmt": "14.66B",
            "longFmt": "14,662,534,368"
          },
          "sharesOutstanding": {
            "raw": 14687356000,
            "fmt": "14.69B",
            "longFmt": "14,687,356,000"
          },
          "sharesShort": {
            "raw": 155886024,
            "fmt": "155.89M",
            "longFmt": "155,886,024"
          },
          "sharesShortPriorMonth": {
            "raw": 134675274,
            "fmt": "134.68M",
            "longFmt": "134,675,274"
          },
          "sharesShortPreviousMonthDate": {
            "raw": 1777507200,
            "fmt": "2026-04-30"
          },
          "dateShortInterest": {
            "raw": 1780012800,
            "fmt": "2026-05-29"
          },
          "sharesPercentSharesOut": {
            "raw": 0.0106,
            "fmt": "1.06%"
          },
          "heldPercentInsiders": {
            "raw": 0.01632,
            "fmt": "1.63%"
          },
          "heldPercentInstitutions": {
            "raw": 0.65829,
            "fmt": "65.83%"
          },
          "shortRatio": {
            "raw": 3.12,
            "fmt": "3.12"
          },
          "shortPercentOfFloat": {
            "raw": 0.0106,
            "fmt": "1.06%"
          },
          "beta": {
            "raw": 1.086,
            "fmt": "1.09"
          },
          "impliedSharesOutstanding": {
            "raw": 14687356000,
            "fmt": "14.69B",
            "longFmt": "14,687,356,000"
          },
          "morningStarOverallRating": {},
          "morningStarRiskRating": {},
          "category": null,
          "bookValue": {
            "raw": 7.26,
            "fmt": "7.26"
          },
          "priceToBook": {
            "raw": 40.10055,
            "fmt": "40.10"
          },
          "annualReportExpenseRatio": {},
          "ytdReturn": {},
          "qtdReturn": {},
          "beta3Year": {},
          "totalAssets": {},
          "yield": {},
          "fundFamily": null,
          "fundInceptionDate": {},
          "legalType": null,
          "threeYearAverageReturn": {},
          "fiveYearAverageReturn": {},
          "priceToSalesTrailing12Months": {},
          "lastFiscalYearEnd": {
            "raw": 1758931200,
            "fmt": "2025-09-27"
          },
          "nextFiscalYearEnd": {
            "raw": 1790467200,
            "fmt": "2026-09-27"
          },
          "mostRecentQuarter": {
            "raw": 1774656000,
            "fmt": "2026-03-28"
          },
          "earningsQuarterlyGrowth": {
            "raw": 0.194,
            "fmt": "19.40%"
          },
          "revenueQuarterlyGrowth": {},
          "netIncomeToCommon": {
            "raw": 122575003648,
            "fmt": "122.58B",
            "longFmt": "122,575,003,648"
          },
          "trailingEps": {
            "raw": 8.27,
            "fmt": "8.27"
          },
          "forwardEps": {
            "raw": 9.59499,
            "fmt": "9.59"
          },
          "pegRatio": {
            "raw": 2.35,
            "fmt": "2.35"
          },
          "lastSplitFactor": "4:1",
          "lastSplitDate": {
            "raw": 1598832000,
            "fmt": "2020-08-31"
          },
          "enterpriseToRevenue": {
            "raw": 9.508,
            "fmt": "9.51"
          },
          "enterpriseToEbitda": {
            "raw": 26.83,
            "fmt": "26.83"
          },
          "52WeekChange": {
            "raw": 0.46724117,
            "fmt": "46.72%"
          },
          "SandP52WeekChange": {
            "raw": 0.23177934,
            "fmt": "23.18%"
          },
          "lastDividendValue": {
            "raw": 0.27,
            "fmt": "0.27"
          },
          "lastDividendDate": {
            "raw": 1778457600,
            "fmt": "2026-05-11"
          },
          "lastCapGain": {},
          "annualHoldingsTurnover": {},
          "latestFundingDate": {},
          "latestAmountRaised": {},
          "latestImpliedValuation": {},
          "latestShareClass": null,
          "leadInvestor": null,
          "fundingToDate": {},
          "totalFundingRounds": {}
        }
      }
    ],
    "error": null
  }
}
```
    """
    url = "https://yahoo-finance166.p.rapidapi.com/api/stock/get-statistics"
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
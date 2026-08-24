import os
import requests

def agents_list(location, search_type):
    """
    :API_description: Retrieve detailed information about real estate agents in the Oxford area, including names, addresses, contact numbers, and listing statistics.
    :param location: The location to search for estate agents. The value of geoIdentifier field returned in .../v2/auto-complete endpoint with listings as search_type.(e.g., "Oxford")
    :param search_type: The type of search, e.g., 'estate-agents'. One of the followings : estate-agents|letting-agents|commercial-agents
    :response_schema: 
    ```json
{
  "pageProps": {
    "type": "success",
    "data": {
      "agents": {
        "__typename": "AgentsSearchConnection",
        "results": [
          {
            "__typename": "Agent",
            "displayName": "Alistair Redhouse Estate Agents Ltd",
            "description": "Problem:In 2020, the world changes and the traditional departmentalised model of estate agencies was proving to be impersonal and inefficient for our clients. We recognised the need for a more personalised approach that would provide sellers with a single point of contact throughout the entire property transaction process.Solution:Introducing our innovative Property Partner model, where we assign a dedicated, highly qualified expert to be your sole contact from the initial meeting until the day you hand over the keys and beyond. At AR Property Partners, we've revamped our approach to prioritise your experience, making it seamless, personal, and tailored to your specific needs.Outcome:Since transitioning to our new model in 2020, AR Property Partners has redefined the real estate experience for our clients. Our Property Partners ensure that you receive a bespoke service, with a free valuation and market appraisal from a trained professional, a carefully considered market valuation, and a customised marketing plan aligned with your unique circumstances.Your property will be showcased on major platforms, and our membership with The Guild of Property Professionals guarantees national exposure, including our prestigious Park Lane office in London. Our trained Property Partners will accompany viewings, providing detailed and prompt feedback whilst they guide you through your journey. We are committed to achieving the best possible outcome for your property and ensuring a smooth legal process once a sale is agreed.Our services extend beyond the transaction - we can guide you in the right direction for conveyancing, surveying, and mortgage services. At AR, we are not just another faceless estate agent; we are guided by our principle \"Care More\".A modern, client-focused approach to real estate that has garnered a reputation we are truly proud of. Visit ARPropertyPartners.co.uk to book your personalised appointment with your dedicated Property Partner today.",
            "id": 55447,
            "name": "Alistair Redhouse Estate Agents Ltd",
            "uriName": "alistair-redhouse-estate-agents-ltd-kidlington-55447",
            "displayAddress": "65 High Street, Kidlington, OX5 2DN",
            "featured": true,
            "listingsStatistics": {
              "residential": {
                "forSale": {
                  "avgAskingPrice": 432424,
                  "avgWeeksOnMarket": 17,
                  "availableListings": 74
                },
                "toRent": {
                  "avgAskingPrice": 437,
                  "avgWeeksOnMarket": 3,
                  "availableListings": 16
                }
              },
              "commercial": null
            },
            "logo": {
              "height": "70",
              "width": "140",
              "uri": "https://st.zoocdn.com/zoopla_static_agent_logo_(754506).png"
            },
            "contactNumber": "01865 366225"
          }
        ],
        "pagination": {
          "pageNumber": 1,
          "pageTotal": 2
        },
        "locationDisplayName": "Oxford",
        "total": 44
      },
      "breadcrumbs": [
        {
          "ariaLabel": "Zoopla",
          "text": "Zoopla",
          "href": "/",
          "id": "home"
        }
      ],
      "isLoggedIn": false
    },
    "companyName": null,
    "searchType": "estate-agents",
    "initialLocation": "/find-agents/estate-agents/oxford?search_source=find-agents&agents_sort=a_z&radius=0",
    "taxonomy": {
      "page": "/find-agents/estate-agents/results/",
      "section": "find-agents",
      "brand": "zoopla",
      "activity": "agent_developer_directory",
      "search_term_agent": "",
      "search_term_location": null,
      "search_result_count": 44
    },
    "ecommerce": {
      "impressions": [
        {
          "id": 55447,
          "variant": "Featured",
          "position": 0
        },
        {
          "id": 17513,
          "variant": "Featured",
          "position": 1
        }
      ]
    }
  },
  "__N_SSP": true
}
```
    """
    url = "https://zoopla.p.rapidapi.com/agents/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"location": location, "search_type": search_type}
    
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "zoopla.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
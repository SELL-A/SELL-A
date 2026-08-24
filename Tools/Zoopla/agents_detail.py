import os
import requests

def agents_detail(branchId):
    """
    :API_description: Retrieve comprehensive details about a real estate branch, including identification, contact information, memberships, location, statistics, and property listings.
    :param branchId: The unique identifier for the real estate branch.(e.g., "68584") come from agents_list api.
    :response_schema: 
    ```json
{
  "data": {
    "agentBranch": {
      "address": "14 High Street, Wendover",
      "branchDetailsUri": "/find-agents/branch/fine-and-country-vale-and-chilterns-wendover-68584/",
      "branchDisplayName": "Fine & Country - Vale & Chilterns",
      "logoUrl": "https://st.zoocdn.com/zoopla_static_agent_logo_(773626).png",
      "postcode": "HP22 6EA"
    },
    "agentAdditional": {
      "memberships": [
        {
          "memberOf": "prs",
          "url": "https://www.zoopla.co.uk/tips/agent-affiliation-prs/"
        }
      ]
    }
  },
  "extensions": {
    "requestId": "07490cce-3ae3-410b-87ba-0794afcdc944"
  }
}
}
    ```
    """
    url = "https://zoopla.p.rapidapi.com/agents/v2/detail"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"branchId": branchId}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "zoopla.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
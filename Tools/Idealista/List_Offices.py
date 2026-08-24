import os
import requests

def List_Offices(order, operation, locationId, location, locale):
    """
    :API_description: Retrieve detailed listings of offices for sale in Madrid, Spain, including property details, multimedia content, and contact information.
    :param order: The order of the results, e.g., "relevance" Order by one of the followings: relevance|lowestprice|highestprice|mostrecent|leastrecent|highestpricereduction|lowestpricem2|highestpricem2|biggest|smallest|highestfloors|lowestfloors.
    :param operation: The type of operation, e.g., "sale","rent".
    :param locationId: The ID of the location, e.g., "0-EU-ES-28-07-001-079".
    :param location: The country code, ("One of the following values: es|pt|it").
    :param locale: The locale for the results, e.g., "es".
    :response_schema: 
    ```json

    ```
    """
    url = "https://idealista7.p.rapidapi.com/listoffices"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "order": order,
        "operation": operation,
        "locationId": locationId,
        "maxItems": 30,
        "numPage": 1,
        "location": location,
        "locale": locale
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "idealista7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
  
if __name__ == "__main__":
    print(List_Offices("relevance", "sale", "0-EU-ES-28-07-001-079", "es", "es"))
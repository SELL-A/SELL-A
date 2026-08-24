import os
import requests

def Verify_GSTIN_Status(gstin):
    """
    :API_description: This API checks the status of a GSTIN, indicating whether it is active or not.
    :param gstin: The GSTIN number for which the status is to be retrieved(e.g. 18AAACR5055K1Z6).
    :response_schema: 
    ```json
{
    "type": "object",
    "properties": {
        "data": {
            "type": "object",
            "properties": {
                "gstin": {
                    "type": "string",
                    "description": "Unique identifier for GST (Goods and Services Tax) registration"
                },
                "status": {
                    "type": "string",
                    "description": "Current status of the GST registration"
                },
                "is_active": {
                    "type": "boolean",
                    "description": "Indicates whether the GST registration is active"
                }
            },
            "required": ["gstin", "status", "is_active"]
        }
    },
    "required": ["data"]
}
    ```
    """
    url = f"https://powerful-gstin-tool.p.rapidapi.com/v1/gstin/{gstin}/status"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "powerful-gstin-tool.p.rapidapi.com"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
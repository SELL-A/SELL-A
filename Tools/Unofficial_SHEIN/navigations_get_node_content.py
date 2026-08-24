import os
import requests

def navigations_get_node_content(language, country, currency, cat_id, id):
    """
    :API_description: Retrieve detailed product categories and their associated thumbnails for dynamic product listings or recommendations.
    :param language: The language code for the content (e.g., 'en' for English).
    :param country: The country code (e.g., 'US' for the United States).
    :param currency: The currency code (e.g., 'USD' for US Dollar).
    :param cat_id: The category ID for the node(The value of 'cat_id' field returned in .../navigations/get-tabs endpoint).
    :param id: The specific ID of the node content to retrieve(The value of 'id' field returned in .../navigations/get-root endpoint).
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "code": {
      "type": "string"
    },
    "msg": {
      "type": "string"
    },
    "info": {
      "type": "object",
      "properties": {
        "content": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "level": {
                "type": "string"
              },
              "id": {
                "type": "string"
              },
              "type": {
                "type": "string"
              },
              "hrefType2": {
                "type": "string"
              },
              "color": {
                "type": "string"
              },
              "relativeUrl": {
                "type": "string"
              },
              "name": {
                "type": "string"
              },
              "hrefTarget": {
                "type": "string"
              },
              "hrefType": {
                "type": "string"
              },
              "style": {
                "type": "object",
                "properties": {
                  "remark": {
                    "type": "string"
                  },
                  "type": {
                    "type": "string"
                  },
                  "sampleImg": {
                    "type": "string"
                  },
                  "isNeedAda": {
                    "type": "boolean"
                  }
                },
                "required": ["remark", "type", "sampleImg", "isNeedAda"]
              },
              "navNodeId": {
                "type": "string"
              },
              "cateTreeNodeId": {
                "type": "string"
              },
              "isAutoRec": {
                "type": "boolean"
              },
              "trackHrefType": {
                "type": "string"
              },
              "trackHrefTarget": {
                "type": "string"
              },
              "isRecommendation": {
                "type": "boolean"
              },
              "parentName": {
                "type": "string"
              },
              "thumb": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "relativeUrl": {
                      "type": "string"
                    },
                    "target": {
                      "type": "string"
                    },
                    "width": {
                      "type": "integer"
                    },
                    "hrefTarget": {
                      "type": "string"
                    },
                    "hrefType": {
                      "type": "string"
                    },
                    "height": {
                      "type": "integer"
                    },
                    "alt": {
                      "type": "string"
                    },
                    "navNodeId": {
                      "type": "string"
                    },
                    "cateTreeNodeId": {
                      "type": "string"
                    },
                    "goodsId": {
                      "type": "string"
                    },
                    "isAuto": {
                      "type": "boolean"
                    },
                    "tagId": {
                      "type": "string"
                    },
                    "trackHrefType": {
                      "type": "string"
                    },
                    "trackHrefTarget": {
                      "type": "string"
                    },
                    "rec_mark": {
                      "type": "string"
                    },
                    "is_rec_img": {
                      "type": "string"
                    },
                    "clickUrl": {
                      "type": "string"
                    }
                  },
                  "required": ["relativeUrl", "target", "width", "hrefTarget", "hrefType", "height", "alt", "navNodeId", "cateTreeNodeId", "goodsId", "isAuto", "tagId", "trackHrefType", "trackHrefTarget", "rec_mark", "is_rec_img", "clickUrl"]
                }
              }
            },
            "required": ["level", "id", "type", "hrefType2", "color", "relativeUrl", "name", "hrefTarget", "hrefType", "style", "navNodeId", "cateTreeNodeId", "isAutoRec", "trackHrefType", "trackHrefTarget", "isRecommendation"]
          }
        }
      },
      "required": ["content"]
    }
  },
  "required": ["code", "msg", "info"]
}
    ```
    """
    url = "https://unofficial-shein.p.rapidapi.com/navigations/get-node-content"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"language": language, "country": country, "currency": currency, "cat_id": cat_id, "id": id}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "unofficial-shein.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
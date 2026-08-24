import os
import requests

def navigations_get_root(language, country, channelType, currency):
    """
    :API_description: Retrieve the root categories for product recommendations and navigation within an e-commerce platform, based on the specified channel type.
    :param language: The language code for the response (e.g., 'en' for English).
    :param country: The country code for the response (e.g., 'US' for the United States).
    :param channelType: The type of channel (e.g., '2' for a specific channel type).
    :param currency: The currency code for the response (e.g., 'USD' for US Dollar).
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
        "abtBranch": {
          "type": "string"
        },
        "autoMap": {
          "type": "string"
        },
        "autoSort": {
          "type": "string"
        },
        "cateTreeId": {
          "type": "string"
        },
        "content": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string"
              },
              "id": {
                "type": "string"
              },
              "type": {
                "type": "string"
              },
              "navNodeId": {
                "type": "string"
              },
              "enName": {
                "type": "string"
              },
              "is_recommend": {
                "type": "string"
              },
              "hrefType": {
                "type": "string"
              },
              "child": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "enName": {
                      "type": "string"
                    },
                    "hrefType": {
                      "type": "string"
                    },
                    "navNodeId": {
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
                          "target": {
                            "type": "string"
                          },
                          "hrefTarget": {
                            "type": "string"
                          },
                          "hrefType": {
                            "type": "string"
                          },
                          "alt": {
                            "type": "string"
                          },
                          "navNodeId": {
                            "type": "string"
                          },
                          "goodsId": {
                            "type": "string"
                          },
                          "isAuto": {
                            "type": "boolean"
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
                          "enName": {
                            "type": "string"
                          }
                        },
                        "required": [
                          "target",
                          "hrefTarget",
                          "hrefType",
                          "alt",
                          "navNodeId",
                          "goodsId",
                          "isAuto",
                          "trackHrefType",
                          "trackHrefTarget",
                          "rec_mark",
                          "is_rec_img",
                          "enName"
                        ]
                      }
                    },
                    "isAutoRec": {
                      "type": "boolean"
                    },
                    "trackHrefTarget": {
                      "type": "string"
                    },
                    "isRecommendation": {
                      "type": "boolean"
                    }
                  },
                  "required": [
                    "type",
                    "name",
                    "enName",
                    "hrefType",
                    "navNodeId",
                    "isAutoRec",
                    "trackHrefType",
                    "trackHrefTarget",
                    "isRecommendation"
                  ]
                }
              }
            },
            "required": [
              "name",
              "id",
              "type",
              "navNodeId",
              "enName",
              "is_recommend",
              "hrefType",
              "child"
            ]
          }
        }
      },
      "required": [
        "abtBranch",
        "autoMap",
        "autoSort",
        "cateTreeId",
        "content"
      ]
    }
  },
  "required": [
    "code",
    "msg",
    "info"
  ]
}
    ```
    """
    url = "https://unofficial-shein.p.rapidapi.com/navigations/get-root"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"language": language, "country": country, "channelType": channelType, "currency": currency}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "unofficial-shein.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
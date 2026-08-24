import os
import requests

def news_detail(uuid):
    """
    :API_description: Retrieves comprehensive metadata and content for a specific financial news article or editorial package using its unique identifier. The response includes article details, authorship, financial metadata, advertising tags, and engagement metrics.
    :param uuid: The unique identifier of the news article (required).
    :response_schema:
    ```json
    {
      "$schema": "http://json-schema.org/draft-07/schema#",
      "type": "object",
      "properties": {
        "data": {
          "type": "object",
          "description": "Container for the main content data",
          "properties": {
            "contents": {
              "type": "array",
              "description": "Array of content items",
              "items": {
                "type": "object",
                "properties": {
                  "content": {
                    "type": "object",
                    "description": "Detailed content information object",
                    "properties": {
                      "id": {
                        "type": "string",
                        "format": "uuid",
                        "description": "Unique identifier for the content"
                      },
                      "contentType": {
                        "type": "string",
                        "description": "Type of content (e.g., EDITORIAL-PACKAGE)"
                      },
                      "title": {
                        "type": ["string", "null"],
                        "description": "Content title"
                      },
                      "description": {
                        "type": "string",
                        "description": "Content description"
                      },
                      "pubDate": {
                        "type": ["string", "null"],
                        "format": "date-time",
                        "description": "Publication date"
                      },
                      "lastModifiedTime": {
                        "type": ["string", "null"],
                        "format": "date-time",
                        "description": "Last modification time"
                      },
                      "isHosted": {
                        "type": ["boolean", "null"],
                        "description": "Indicates if content is hosted"
                      },
                      "canonicalUrl": {
                        "type": ["string", "null"],
                        "format": "uri",
                        "description": "Canonical URL for the content"
                      },
                      "clickThroughUrl": {
                        "type": ["string", "null"],
                        "format": "uri",
                        "description": "Click-through URL"
                      },
                      "structuredSummary": {
                        "type": ["string", "null"],
                        "description": "Structured summary of content"
                      },
                      "author": {
                        "type": ["string", "null"],
                        "description": "Primary author"
                      },
                      "authors": {
                        "type": ["array", "null"],
                        "description": "Array of authors"
                      },
                      "coverImage": {
                        "type": ["string", "null"],
                        "description": "Cover image URL"
                      },
                      "provider": {
                        "type": ["string", "null"],
                        "description": "Content provider"
                      },
                      "providerBrand": {
                        "type": ["string", "null"],
                        "description": "Provider brand information"
                      },
                      "providerContentUrl": {
                        "type": ["string", "null"],
                        "format": "uri",
                        "description": "Provider content URL"
                      },
                      "readingMeta": {
                        "type": ["string", "null"],
                        "description": "Reading metadata"
                      },
                      "thumbnail": {
                        "type": ["string", "null"],
                        "description": "Thumbnail image URL"
                      },
                      "canvass": {
                        "type": "object",
                        "description": "Engagement/canvassing metrics",
                        "properties": {
                          "contextId": {
                            "type": "string",
                            "format": "uuid",
                            "description": "Context identifier"
                          },
                          "count": {
                            "type": "integer",
                            "description": "Count metric"
                          }
                        },
                        "required": ["contextId", "count"]
                      },
                      "readMoreList": {
                        "type": ["array", "null"],
                        "description": "List of related content"
                      },
                      "modifiedTime": {
                        "type": ["string", "null"],
                        "format": "date-time",
                        "description": "Modification time"
                      },
                      "displayTime": {
                        "type": ["string", "null"],
                        "format": "date-time",
                        "description": "Display time"
                      },
                      "isCreatorContent": {
                        "type": ["boolean", "null"],
                        "description": "Indicates if content is creator-generated"
                      },
                      "subheadline": {
                        "type": ["string", "null"],
                        "description": "Subheadline text"
                      },
                      "isOpinion": {
                        "type": ["boolean", "null"],
                        "description": "Indicates if content is opinion piece"
                      },
                      "presentation": {
                        "type": ["string", "null"],
                        "description": "Presentation format"
                      },
                      "heroModule": {
                        "type": ["string", "null"],
                        "description": "Hero module information"
                      },
                      "summary": {
                        "type": "string",
                        "description": "Content summary"
                      },
                      "commentsAllowed": {
                        "type": ["boolean", "null"],
                        "description": "Comments allowed flag"
                      },
                      "storyBody": {
                        "type": ["string", "null"],
                        "description": "Full story body content"
                      },
                      "finance": {
                        "type": "object",
                        "description": "Financial content metadata",
                        "properties": {
                          "stockTickers": {
                            "type": ["array", "null"],
                            "description": "Array of stock tickers"
                          },
                          "premiumFinance": {
                            "type": "object",
                            "description": "Premium finance information",
                            "properties": {
                              "isPremiumNews": {
                                "type": "boolean",
                                "description": "Premium news flag"
                              },
                              "isPremiumFreeNews": {
                                "type": "boolean",
                                "description": "Premium free news flag"
                              }
                            },
                            "required": ["isPremiumNews", "isPremiumFreeNews"]
                          }
                        },
                        "required": ["stockTickers", "premiumFinance"]
                      },
                      "previewUrl": {
                        "type": ["string", "null"],
                        "format": "uri",
                        "description": "Preview URL"
                      },
                      "adMeta": {
                        "type": "object",
                        "description": "Advertising metadata",
                        "properties": {
                          "hashtag": {
                            "type": "string",
                            "description": "Hashtags for categorization"
                          },
                          "rs": {
                            "type": "string",
                            "description": "Tracking/reference string"
                          },
                          "site": {
                            "type": ["string", "null"],
                            "description": "Site information"
                          },
                          "siteAttribute": {
                            "type": "string",
                            "description": "Site attributes"
                          }
                        },
                        "required": ["hashtag", "rs", "site", "siteAttribute"]
                      },
                      "commerceAffiliateStat": {
                        "type": "object",
                        "description": "Commerce affiliate statistics",
                        "properties": {
                          "yahooLinkCount": {
                            "type": "integer",
                            "description": "Yahoo link count"
                          }
                        },
                        "required": ["yahooLinkCount"]
                      }
                    },
                    "required": ["id", "contentType", "description", "summary", "canvass", "finance", "adMeta", "commerceAffiliateStat"]
                  }
                },
                "required": ["content"]
              }
            }
          },
          "required": ["contents"]
        },
        "status": {
          "type": "string",
          "description": "API response status",
          "enum": ["OK", "ERROR"]
        }
      },
      "required": ["data", "status"]
    }
    ```
    """
    url = "https://yh-finance.p.rapidapi.com/news/v2/get-details"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"uuid": uuid}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "yh-finance.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
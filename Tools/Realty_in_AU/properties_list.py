from ast import If
import os
import requests

def properties_list(page, pageSize, sortType, channel, searchLocation, searchLocationSubtext, type):
    """
    :API_description: Retrieve a list of properties based on various filters and options, including location, property type, and price range.
    :param page: The page number of the results to retrieve(default: 1).
    :param pageSize: The number of results per page(default: 30).
    :param sortType: The type of sorting to apply to the results(One of the following relevance|new-asc|new-desc|price-asc|price-desc|sold-relevance|sold-date-desc|sold-price-desc|sold-price-asc).
    :param channel: The channel through which the properties are listed One of the following : buy|rent|sold.
    :param searchLocation: The main location to search for properties(e.g. Melbourne City - Greater Region, VIC).
    :param searchLocationSubtext: Additional location details or subtext(e.g. Region).
    :param type: The type of location (e.g., region).
   
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "prettyUrl": {
      "type": "string"
    },
    "totalResultsCount": {
      "type": "integer"
    },
    "resolvedLocalities": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "display": {
            "type": "string"
          },
          "precision": {
            "type": "string"
          },
          "atlasId": {
            "type": "string"
          },
          "state": {
            "type": "string"
          }
        },
        "required": ["display", "precision", "atlasId", "state"]
      }
    },
    "resolvedQuery": {
      "type": "object",
      "properties": {
        "localities": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "locality": {
                "type": "string"
              },
              "subdivision": {
                "type": "string"
              },
              "searchLocation": {
                "type": "string"
              }
            },
            "required": ["locality", "subdivision", "searchLocation"]
          }
        },
        "channel": {
          "type": "string"
        },
        "pageSize": {
          "type": "string"
        },
        "page": {
          "type": "string"
        },
        "filters": {
          "type": "object",
          "properties": {
            "surroundingSuburbs": {
              "type": "boolean"
            }
          },
          "required": ["surroundingSuburbs"]
        }
      },
      "required": ["localities", "channel", "pageSize", "page", "filters"]
    },
    "tieredResults": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "tier": {
            "type": "integer"
          },
          "count": {
            "type": "integer"
          },
          "results": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "prettyUrl": {
                  "type": "string"
                },
                "standard": {
                  "type": "boolean"
                },
                "midtier": {
                  "type": "boolean"
                },
                "lister": {
                  "type": "object",
                  "properties": {
                    "mobilePhoneNumber": {
                      "type": "string"
                    },
                    "website": {
                      "type": "string"
                    },
                    "agentId": {
                      "type": "string"
                    },
                    "phoneNumber": {
                      "type": "string"
                    },
                    "powerProfile": {
                      "type": "boolean"
                    },
                    "name": {
                      "type": "string"
                    },
                    "mainPhoto": {
                      "type": "object",
                      "properties": {
                        "server": {
                          "type": "string"
                        },
                        "name": {
                          "type": "string"
                        },
                        "uri": {
                          "type": "string"
                        }
                      },
                      "required": ["server", "name", "uri"]
                    },
                    "id": {
                      "type": "string"
                    },
                    "email": {
                      "type": "string"
                    }
                  },
                  "required": ["mobilePhoneNumber", "website", "agentId", "phoneNumber", "powerProfile", "name", "mainPhoto", "id", "email"]
                },
                "featured": {
                  "type": "boolean"
                },
                "signature": {
                  "type": "boolean"
                },
                "constructionStatus": {
                  "type": "string"
                },
                "channel": {
                  "type": "string"
                },
                "description": {
                  "type": "string"
                },
                "advertising": {
                  "type": "object",
                  "properties": {
                    "region": {
                      "type": "string"
                    },
                    "priceRange": {
                      "type": "string"
                    }
                  },
                  "required": ["region", "priceRange"]
                },
                "showAgencyLogo": {
                  "type": "boolean"
                },
                "title": {
                  "type": "string"
                },
                "isLinkedExternalChildListing": {
                  "type": "boolean"
                },
                "listers": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "mobilePhoneNumber": {
                        "type": "string"
                      },
                      "website": {
                        "type": "string"
                      },
                      "agentId": {
                        "type": "string"
                      },
                      "phoneNumber": {
                        "type": "string"
                      },
                      "powerProfile": {
                        "type": "boolean"
                      },
                      "name": {
                        "type": "string"
                      },
                      "mainPhoto": {
                        "type": "object",
                        "properties": {
                          "server": {
                            "type": "string"
                          },
                          "name": {
                            "type": "string"
                          },
                          "uri": {
                            "type": "string"
                          }
                        },
                        "required": ["server", "name", "uri"]
                      },
                      "id": {
                        "type": "string"
                      },
                      "email": {
                        "type": "string"
                      }
                    },
                    "required": ["mobilePhoneNumber", "website", "agentId", "phoneNumber", "powerProfile", "name", "mainPhoto", "id", "email"]
                  }
                },
                "features": {
                  "type": "object",
                  "properties": {
                    "general": {
                      "type": "object",
                      "properties": {
                        "bedrooms": {
                          "type": "integer"
                        },
                        "bathrooms": {
                          "type": "integer"
                        },
                        "parkingSpaces": {
                          "type": "integer"
                        }
                      },
                      "required": ["bedrooms", "bathrooms", "parkingSpaces"]
                    }
                  },
                  "required": ["general"]
                },
                "price": {
                  "type": "object",
                  "properties": {
                    "display": {
                      "type": "string"
                    }
                  },
                  "required": ["display"]
                },
                "propertyType": {
                  "type": "string"
                },
                "isExternalChildListing": {
                  "type": "boolean"
                },
                "productDepth": {
                  "type": "string"
                },
                "calculator": {
                  "type": "object",
                  "properties": {
                    "brandingColors": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "string"
                        },
                        "primary": {
                          "type": "string"
                        }
                      },
                      "required": ["text", "primary"]
                    },
                    "subtitle": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    }
                  },
                  "required": ["brandingColors", "subtitle", "title"]
                },
                "images": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "server": {
                        "type": "string"
                      },
                      "name": {
                        "type": "string"
                      },
                      "uri": {
                        "type": "string"
                      },
                      "resize": {
                        "type": "boolean"
                      }
                    },
                    "required": ["server", "name", "uri"]
                  }
                },
                "address": {
                  "type": "object",
                  "properties": {
                    "streetAddress": {
                      "type": "string"
                    },
                    "locality": {
                      "type": "string"
                    },
                    "postcode": {
                      "type": "string"
                    },
                    "suburb": {
                      "type": "string"
                    },
                    "postCode": {
                      "type": "string"
                    },
                    "location": {
                      "type": "object",
                      "properties": {
                        "latitude": {
                          "type": "number"
                        },
                        "longitude": {
                          "type": "number"
                        }
                      },
                      "required": ["latitude", "longitude"]
                    },
                    "subdivisionCode": {
                      "type": "string"
                    },
                    "state": {
                      "type": "string"
                    },
                    "showAddress": {
                      "type": "boolean"
                    }
                  },
                  "required": ["streetAddress", "locality", "postcode", "suburb", "postCode", "location", "subdivisionCode", "state", "showAddress"]
                },
                "classicProject": {
                  "type": "boolean"
                },
                "agency": {
                  "type": "object",
                  "properties": {
                    "website": {
                      "type": "string"
                    },
                    "address": {
                      "type": "object",
                      "properties": {
                        "streetAddress": {
                          "type": "string"
                        },
                        "postcode": {
                          "type": "string"
                        },
                        "suburb": {
                          "type": "string"
                        },
                        "state": {
                          "type": "string"
                        }
                      },
                      "required": ["streetAddress", "postcode", "suburb", "state"]
                    },
                    "phoneNumber": {
                      "type": "string"
                    },
                    "branded": {
                      "type": "boolean"
                    },
                    "brandingColors": {
                      "type": "object",
                      "properties": {
                        "text": {
                          "type": "string"
                        },
                        "primary": {
                          "type": "string"
                        }
                      },
                      "required": ["text", "primary"]
                    },
                    "name": {
                      "type": "string"
                    },
                    "logo": {
                      "type": "object",
                      "properties": {
                        "images": {
                          "type": "array",
                          "items": {
                            "type": "object",
                            "properties": {
                              "server": {
                                "type": "string"
                              },
                              "name": {
                                "type": "string"
                              },
                              "uri": {
                                "type": "string"
                              }
                            },
                            "required": ["server", "name", "uri"]
                          }
                        },
                        "links": {
                          "type": "object",
                          "properties": {
                            "small": {
                              "type": "string"
                            },
                            "hero image": {
                              "type": "string"
                            },
                            "default": {
                              "type": "string"
                            },
                            "large": {
                              "type": "string"
                            }
                          },
                          "required": ["small", "hero image", "default", "large"]
                        }
                      },
                      "required": ["images", "links"]
                    },
                    "agencyId": {
                      "type": "string"
                    },
                    "email": {
                      "type": "string"
                    }
                  },
                  "required": ["website", "address", "phoneNumber", "branded", "brandingColors", "name", "logo", "agencyId", "email"]
                },
                "isSoldChannel": {
                  "type": "boolean"
                },
                "isBuyChannel": {
                  "type": "boolean"
                },
                "signatureProject": {
                  "type": "boolean"
                },
                "agencyListingId": {
                  "type": "string"
                },
                "propertyFeatures": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "features": {
                        "type": "array",
                        "items": {
                          "type": "string"
                        }
                      },
                      "section": {
                        "type": "string"
                      },
                      "label": {
                        "type": "string"
                      }
                    },
                    "required": ["features", "section", "label"]
                  }
                },
                "listingId": {
                  "type": "string"
                },
                "isInternalChildListing": {
                  "type": "boolean"
                },
                "mainImage": {
                  "type": "object",
                  "properties": {
                    "server": {
                      "type": "string"
                    },
                    "name": {
                      "type": "string"
                    },
                    "uri": {
                      "type": "string"
                    }
                  },
                  "required": ["server", "name", "uri"]
                },
                "statementOfInformation": {
                  "type": "object",
                  "properties": {
                    "href": {
                      "type": "string"
                    },
                    "title": {
                      "type": "string"
                    },
                    "statementSummary": {
                      "type": "string"
                    }
                  },
                  "required": ["href", "title", "statementSummary"]
                },
                "modifiedDate": {
                  "type": "object",
                  "properties": {
                    "value": {
                      "type": "string"
                    }
                  },
                  "required": ["value"]
                },
                "inspectionsAndAuctions": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "dateDisplay": {
                        "type": "string"
                      },
                      "startTimeDisplay": {
                        "type": "string"
                      },
                      "endTimeDisplay": {
                        "type": "string"
                      },
                      "startTime": {
                        "type": "string"
                      },
                      "endTime": {
                        "type": "string"
                      },
                      "auction": {
                        "type": "boolean"
                      }
                    },
                    "required": ["dateDisplay", "startTimeDisplay", "endTimeDisplay", "startTime", "endTime", "auction"]
                  }
                },
                "generalFeatures": {
                  "type": "object",
                  "properties": {
                    "bedrooms": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string"
                        },
                        "value": {
                          "type": "integer"
                        }
                      },
                      "required": ["label", "type", "value"]
                    },
                    "bathrooms": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string"
                        },
                        "value": {
                          "type": "integer"
                        }
                      },
                      "required": ["label", "type", "value"]
                    },
                    "parkingSpaces": {
                      "type": "object",
                      "properties": {
                        "label": {
                          "type": "string"
                        },
                        "type": {
                          "type": "string"
                        },
                        "value": {
                          "type": "integer"
                        }
                      },
                      "required": ["label", "type", "value"]
                    }
                  },
                  "required": ["bedrooms", "bathrooms", "parkingSpaces"]
                },
                "isRentChannel": {
                  "type": "boolean"
                }
              },
              "required": [
                "prettyUrl",
                "standard",
                "midtier",
                "lister",
                "featured",
                "signature",
                "constructionStatus",
                "channel",
                "description",
                "advertising",
                "showAgencyLogo",
                "title",
                "isLinkedExternalChildListing",
                "listers",
                "features",
                "price",
                "propertyType",
                "isExternalChildListing",
                "productDepth",
                "calculator",
                "images",
                "address",
                "classicProject",
                "agency",
                "isSoldChannel",
                "isBuyChannel",
                "signatureProject",
                "agencyListingId",
                "propertyFeatures",
                "listingId",
                "isInternalChildListing",
                "mainImage",
                "statementOfInformation",
                "modifiedDate",
                "inspectionsAndAuctions",
    ```
    """
    url = "https://realty-in-au.p.rapidapi.com/properties/list"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "page": page,
        "pageSize": pageSize,
        "sortType": sortType,
        "channel": channel,
        "searchLocation": searchLocation,
        "searchLocationSubtext": searchLocationSubtext,
        "type": type
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "realty-in-au.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


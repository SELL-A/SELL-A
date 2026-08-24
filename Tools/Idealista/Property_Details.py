import os
import requests

def Property_Details(propertyId, location, language):
    """
    :API_description: Retrieve detailed information about a specific property, including its unique identifier, type, location, and contact details.
    :param propertyId: The unique identifier of the property(e.g., "110620813").
    :param location: The location code, ("One of the following values: es|pt|it").
    :param language: The language code for the response, e.g., 'en' for English.
    :response_schema: 
    ```json
{
  "type": "object",
  "properties": {
    "message": {
      "type": "string",
      "description": "A message indicating the status or result of the API call."
    },
    "httpStatus": {
      "type": "integer",
      "description": "The HTTP status code returned by the API."
    },
    "ad": {
      "type": "object",
      "properties": {
        "adid": {
          "type": "integer",
          "description": "Unique identifier for the ad."
        },
        "operation": {
          "type": "string",
          "description": "Type of operation (e.g., sale, rent)."
        },
        "propertyType": {
          "type": "string",
          "description": "Type of property (e.g., homes, apartments)."
        },
        "locationId": {
          "type": "string",
          "description": "Identifier for the location of the property."
        },
        "lastDeactivationDate": {
          "type": "integer",
          "description": "Timestamp of the last deactivation of the ad."
        },
        "deactivationReason": {
          "type": "string",
          "description": "Reason for the deactivation of the ad."
        },
        "isAuction": {
          "type": "boolean",
          "description": "Indicates if the ad is for an auction."
        },
        "tracking": {
          "type": "object",
          "properties": {
            "unsubscriptionId": {
              "type": "integer",
              "description": "Unique identifier for the subscription."
            },
            "isSuitableForRecommended": {
              "type": "boolean",
              "description": "Indicates if the ad is suitable for recommended listings."
            },
            "stateCode": {
              "type": "string",
              "description": "State code for the ad."
            },
            "commercialDataId": {
              "type": "integer",
              "description": "Identifier for commercial data associated with the ad."
            }
          }
        },
        "allowsRecommendation": {
          "type": "boolean",
          "description": "Indicates if the ad allows recommendations."
        },
        "contactInfo": {
          "type": "object",
          "properties": {
            "commercialName": {
              "type": "string",
              "description": "Commercial name of the contact."
            },
            "phone1": {
              "type": "object",
              "properties": {
                "phoneNumber": {
                  "type": "string",
                  "description": "Phone number of the contact."
                },
                "formattedPhone": {
                  "type": "string",
                  "description": "Formatted phone number for display."
                },
                "prefix": {
                  "type": "string",
                  "description": "Phone number prefix."
                },
                "phoneNumberForMobileDialing": {
                  "type": "string",
                  "description": "Phone number formatted for mobile dialing."
                },
                "nationalNumber": {
                  "type": "boolean",
                  "description": "Indicates if the phone number is a national number."
                },
                "formattedPhoneWithPrefix": {
                  "type": "string",
                  "description": "Formatted phone number with prefix."
                }
              }
            },
            "contactName": {
              "type": "string",
              "description": "Name of the contact."
            },
            "externalReference": {
              "type": "string",
              "description": "External reference identifier."
            },
            "userType": {
              "type": "string",
              "description": "Type of user (e.g., professional, individual)."
            },
            "agencyLogo": {
              "type": "string",
              "description": "URL of the agency's logo."
            },
            "contactMethod": {
              "type": "string",
              "description": "Preferred contact method."
            },
            "micrositeShortName": {
              "type": "string",
              "description": "Short name of the microsite."
            },
            "address": {
              "type": "object",
              "properties": {
                "streetName": {
                  "type": "string",
                  "description": "Name of the street."
                },
                "streetNumber": {
                  "type": "integer",
                  "description": "Street number."
                },
                "locationName": {
                  "type": "string",
                  "description": "Name of the location."
                },
                "postalCode": {
                  "type": "string",
                  "description": "Postal code of the location."
                }
              }
            },
            "agentInfo": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string",
                  "description": "Name of the agent."
                },
                "picture": {
                  "type": "string",
                  "description": "URL of the agent's picture."
                },
                "proAgent": {
                  "type": "boolean",
                  "description": "Indicates if the agent is a professional."
                }
              }
            },
            "inVirtualMicrosite": {
              "type": "boolean",
              "description": "Indicates if the contact is in a virtual microsite."
            },
            "profilePicture": {
              "type": "string",
              "description": "URL of the profile picture."
            },
            "corporateVideo": {
              "type": "object",
              "properties": {
                "thumbnail": {
                  "type": "string",
                  "description": "URL of the video thumbnail."
                },
                "url": {
                  "type": "string",
                  "description": "URL of the corporate video."
                }
              }
            },
            "corporatePhrase": {
              "type": "object",
              "properties": {
                "text": {
                  "type": "string",
                  "description": "Corporate phrase or slogan."
                },
                "autoTranslated": {
                  "type": "boolean",
                  "description": "Indicates if the phrase is auto-translated."
                }
              }
            },
            "totalAds": {
              "type": "integer",
              "description": "Total number of ads associated with the contact."
            },
            "professional": {
              "type": "boolean",
              "description": "Indicates if the contact is a professional."
            }
          }
        }
      }
    }
  }
}
    ```
    """
    url = "https://idealista7.p.rapidapi.com/propertydetails"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {"propertyId": propertyId, "location": location, "language": language}

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "idealista7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
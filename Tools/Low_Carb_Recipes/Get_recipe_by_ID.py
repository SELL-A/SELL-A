import os
import requests

def Get_recipe_by_ID(recipe_id):
    """
    :API_description: Retrieve detailed information about a specific recipe, including its name, ingredients, and preparation steps.
    :param recipe_id: The unique identifier for the recipe e.g., "2807982c-986a-4def-9e3a-153a3066af7a".
    :response_schema: 
    ```json
    {
      "type": "object",
      "properties": {
        "id": {
          "type": "string",
          "description": "Unique identifier for the recipe."
        },
        "name": {
          "type": "string",
          "description": "Name of the recipe."
        },
        "tags": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "List of tags associated with the recipe."
        },
        "description": {
          "type": "string",
          "description": "Detailed description of the recipe, including additional tips and variations."
        },
        "prepareTime": {
          "type": "integer",
          "description": "Time required to prepare the recipe in minutes."
        },
        "cookTime": {
          "type": "integer",
          "description": "Time required to cook the recipe in minutes."
        },
        "ingredients": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "name": {
                "type": "string",
                "description": "Name of the ingredient."
              },
              "servingSize": {
                "type": "object",
                "properties": {
                  "units": {
                    "type": "string",
                    "description": "Units in which the serving size is measured."
                  },
                  "desc": {
                    "type": "string",
                    "description": "Description of the serving size."
                  },
                  "qty": {
                    "type": "number",
                    "description": "Quantity of the ingredient."
                  },
                  "grams": {
                    "type": "number",
                    "description": "Weight of the ingredient in grams."
                  },
                  "scale": {
                    "type": "number",
                    "description": "Scaling factor for the ingredient."
                  }
                },
                "required": ["units", "desc", "qty", "scale"]
              }
            },
            "required": ["name", "servingSize"]
          },
          "description": "List of ingredients required for the recipe."
        },
        "steps": {
          "type": "array",
          "items": {
            "type": "string"
          },
          "description": "Step-by-step instructions to prepare the recipe."
        },
        "servings": {
          "type": "integer",
          "description": "Number of servings the recipe yields."
        },
        "servingSizes": {
          "type": "array",
          "items": {
            "type": "object",
            "properties": {
              "scale": {
                "type": "number",
                "description": "Scaling factor for the serving size."
              },
              "qty": {
                "type": "number",
                "description": "Quantity of the serving."
              },
              "grams": {
                "type": "number",
                "description": "Weight of the serving in grams."
              },
              "units": {
                "type": "string",
                "description": "Units in which the serving size is measured."
              },
              "originalWeight": {
                "type": "number",
                "description": "Original weight of the serving."
              },
              "originalWeightUnits": {
                "type": "string",
                "description": "Original units in which the serving size was measured."
              }
            },
            "required": ["scale", "qty", "grams", "units", "originalWeight", "originalWeightUnits"]
          },
          "description": "List of serving sizes for the recipe."
        },
        "nutrients": {
          "type": "object",
          "properties": {
            "caloriesKCal": {
              "type": "number",
              "description": "Calories in kilocalories."
            },
            "caloriesKJ": {
              "type": "number",
              "description": "Calories in kilojoules."
            },
            "totalCarbs": {
              "type": "number",
              "description": "Total carbohydrates in grams."
            },
            "diabetesCarbsADA": {
              "type": "number",
              "description": "Carbohydrates for diabetes management according to ADA guidelines in grams."
            },
            "netCarbs": {
              "type": "number",
              "description": "Net carbohydrates in grams."
            },
            "diabetesCarbs": {
              "type": "number",
              "description": "Carbohydrates for diabetes management in grams."
            },
            "fiber": {
              "type": "number",
              "description": "Fiber content in grams."
            },
            "starch": {
              "type": "number",
              "description": "Starch content in grams."
            },
            "sugar": {
              "type": "number",
              "description": "Sugar content in grams."
            },
            "addedSugar": {
              "type": "number",
              "description": "Added sugar content in grams."
            },
            "sugarAlcohols": {
              "type": "number",
              "description": "Sugar alcohols content in grams."
            },
            "protein": {
              "type": "number",
              "description": "Protein content in grams."
            },
            "fat": {
              "type": "number",
              "description": "Total fat content in grams."
            },
            "transFat": {
              "type": "number",
              "description": "Trans fat content in grams."
            },
            "monousatFat": {
              "type": "number",
              "description": "Monounsaturated fat content in grams."
            },
            "polyunsatFat": {
              "type": "number",
              "description": "Polyunsaturated fat content in grams."
            },
            "omega3Fat": {
              "type": "number",
              "description": "Omega-3 fatty acids content in grams."
            },
            "omega6Fat": {
              "type": "number",
              "description": "Omega-6 fatty acids content in grams."
            },
            "saturatedFat": {
              "type": "number",
              "description": "Saturated fat content in grams."
            },
            "cholesterol": {
              "type": "number",
              "description": "Cholesterol content in milligrams."
            },
            "vitaminA": {
              "type": "number",
              "description": "Vitamin A content in micrograms."
            },
            "vitaminC": {
              "type": "number",
              "description": "Vitamin C content in milligrams."
            },
            "vitaminD": {
              "type": "number",
              "description": "Vitamin D content in micrograms."
            },
            "vitaminE": {
              "type": "number",
              "description": "Vitamin E content in milligrams."
            },
            "vitaminK": {
              "type": "number",
              "description": "Vitamin K content in micrograms."
            },
            "vitaminB1": {
              "type": "number",
              "description": "Vitamin B1 (Thiamine) content in milligrams."
            },
            "vitaminB2": {
              "type": "number",
              "description": "Vitamin B2 (Riboflavin) content in milligrams."
            },
            "vitaminB3": {
              "type": "number",
              "description": "Vitamin B3 (Niacin) content in milligrams."
            },
            "vitaminB5": {
              "type": "number",
              "description": "Vitamin B5 (Pantothenic Acid) content in milligrams."
            },
            "vitaminB6": {
              "type": "number",
              "description": "Vitamin B6 content in milligrams."
            },
            "vitaminB12": {
              "type": "number",
              "description": "Vitamin B12 content in micrograms."
            },
            "potassium": {
              "type": "number",
              "description": "Potassium content in milligrams."
            },
            "magnesium": {
              "type": "number",
              "description": "Magnesium content in milligrams."
            },
            "calcium": {
              "type": "number",
              "description": "Calcium content in milligrams."
            },
            "iron": {
              "type": "number",
              "description": "Iron content in milligrams."
            },
            "zinc": {
              "type": "number",
              "description": "Zinc content in milligrams."
            },
            "copper": {
              "type": "number",
              "description": "Copper content in milligrams."
            },
            "phosphorus": {
              "type": "number",
              "description": "Phosphorus content in milligrams."
            },
            "sodium": {
              "type": "number",
              "description": "Sodium content in milligrams."
            },
            "selenium": {
              "type": "number",
              "description": "Selenium content in micrograms."
            },
            "folate": {
              "type": "number",
              "description": "Folate content in micrograms."
            },
            "choline": {
              "type": "number",
              "description": "Choline content in milligrams."
            },
            "alcohol": {
              "type": "number",
              "description": "Alcohol content in grams."
            },
            "caffeine": {
              "type": "number",
              "description": "Caffeine content in milligrams."
            },
            "gluten": {
              "type": "number",
              "description": "Gluten content in grams."
            },
            "manganese": {
              "type": "number",
              "description": "Manganese content in milligrams."
            },
            "conjugatedLinoleicAcid": {
              "type": "number",
              "description": "Conjugated Linoleic Acid content in grams."
            },
            "phyticAcid": {
              "type": "number",
              "description": "Phytic Acid content in milligrams."
            },
            "xylitol": {
              "type": "number",
              "description": "Xylitol content in grams."
            },
            "isomalt": {
              "type": "number",
              "description": "Isomalt content in grams."
            },
            "sorbitol": {
              "type": "number",
              "description": "Sorbitol content in grams."
            },
            "maltitol": {
              "type": "number",
              "description": "Maltitol content in grams."
            },
            "lactitol": {
              "type": "number",
              "description": "Lactitol content in grams."
            },
            "erythritol": {
              "type": "number",
              "description": "Erythritol content in grams."
            },
            "pinitol": {
              "type": "number",
              "description": "Pinitol content in grams."
            },
            "inositol": {
              "type": "number",
              "description": "Inositol content in grams."
            },
            "mannitol": {
              "type": "number",
              "description": "Mannitol content in grams."
            }
          },
          "description": "Nutritional information for the recipe."
        },
        "image": {
          "type": "string",
          "description": "URL to the image of the recipe."
        }
      },
      "required": ["id", "name", "tags", "description", "prepareTime", "cookTime", "ingredients", "steps", "servings", "servingSizes", "nutrients", "image"]
    }
    ```
    """
    url = f"https://low-carb-recipes.p.rapidapi.com/recipes/{recipe_id}"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "low-carb-recipes.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
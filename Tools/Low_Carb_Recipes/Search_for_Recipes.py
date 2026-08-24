import os
import requests

def Search_for_Recipes(name, tags, includeIngredients, excludeIngredients, maxPrepareTime, maxCookTime, maxCalories, maxNetCarbs, maxSugar, maxAddedSugar, limit):
    """
    :API_description: Search for recipes based on various criteria such as name, tags, ingredients, and nutritional values.
    :param name: The name of the recipe to search for, Search terms to be appeared in the recipe name.
    :param tags: Tags to filter the recipes, the allowed value must be 15-minute-meals,3-ingredient-meals,30-minute-meals,5-ingredient-meals,air-fryer,alcoholic-beverages,american,appetizer,batch-cook,bbq,beef,beef-free,beverages,blender,brazilian,breakfast,budget-friendly,carnivore,celery,chicken,chicken-free,chinese,coffee,corn,crock-pot,crustaceans,dairy,dairy-free,desserts,dutch-oven,egg-free,eggs,english,family-friendly,fasting-friendly,fish,fish-free,food-processer,freezer-friendly,french,fructose,gluten,gluten-free,good-for-leftovers,grains,high-protein,indian,instant-pot,italian,japanese,juicer,keto,keto-beginners,kid-friendly,korean,lchf,low-carb,low-fodmap,low-histamine,lunch,lupin,main-dishes,meal-plan-ok,meal-prep,mediterranean,mexican,microwave,middle-eastern,mixer,moderate-carb,molluscs,msg,mug-recipes,mushrooms,mustard,nightshade-vegetables,no-cooking-required,nuts,one-pot-meals,paleo,pantry-recipes,peanut-free,peanuts,pescatarian,philippino,pork,pork-free,quick-easy,relevant-meal--breakfast,relevant-meal--desserts,relevant-meal--lunch,relevant-meal--main-dishes,relevant-meal--sides,relevant-meal--snacks,salads,sesame,sheet-pan-dinners,shellfish,shellfish-free,sides,skillet,slow-cooker,snacks,soy,soy-free,spanish,spiralizer,sulphites,sweeteners,thai,tree-nut-free,treenuts,vegan,vegetarian,vietnamese,wheat,wheat-free,whole-30,whole-foods.
    :param includeIngredients: Ingredients that must be included in the recipe e.g., egg. Semicolon separated terms to be included in ingredients
    :param excludeIngredients: Ingredients that must be excluded from the recipe e.g., cinnamon.
    :param maxPrepareTime: Maximum preparation time in minutes Default: 10.
    :param maxCookTime: Maximum cooking time in minutes Default: 20.
    :param maxCalories: Maximum calories per serving Default: 500.
    :param maxNetCarbs: Maximum net carbs per serving Default: 5.
    :param maxSugar: Maximum sugar content per serving Default: 3.
    :param maxAddedSugar: Maximum added sugar content per serving Default: 0.
    :param limit: The maximum number of recipes to return Default: 10.
    :response_schema: 
    ```json
  [
  {
    "id": "2807982c-986a-4def-9e3a-153a3066af7a",
    "name": "Ultimate Keto Blueberry Sponge Cake In A Mug",
    "tags": [
      "american",
      "beef-free",
      "breakfast",
      "chicken-free",
      "dairy",
      "desserts",
      "eggs",
      "fish-free",
      "gluten-free",
      "keto",
      "keto-beginners",
      "kid-friendly",
      "microwave",
      "nuts",
      "peanut-free",
      "pescatarian",
      "pork-free",
      "quick-easy",
      "shellfish-free",
      "snacks",
      "soy-free",
      "sweeteners",
      "treenuts",
      "vegetarian",
      "wheat-free"
    ],
    "description": "...",
    "prepareTime": 3,
    "cookTime": 2,
    "ingredients": [
      {
        "name": "Butter",
        "servingSize": {
          "units": "tablespoon",
          "desc": "1 tablespoon",
          "qty": 1,
          "grams": 14,
          "scale": 1
        }
      },
      {
        "name": "Cream Cheese",
        "servingSize": {
          "units": "tablespoon",
          "desc": "2 tablespoon",
          "qty": 2,
          "grams": 29,
          "scale": 2
        }
      },
      {
        "name": "Coconut Flour",
        "servingSize": {
          "units": "tablespoon",
          "desc": "2 tablespoon",
          "qty": 2,
          "grams": 14,
          "scale": 0.125
        }
      },
      {
        "name": "The Ultimate Sugar Replacement Granular by Swerve",
        "servingSize": {
          "units": "tablespoon",
          "desc": "1 tablespoon",
          "qty": 1,
          "grams": null,
          "scale": 3
        }
      },
      {
        "name": "Vanilla Extract",
        "servingSize": {
          "units": "teaspoon",
          "desc": "1 teaspoon",
          "qty": 1,
          "grams": 4,
          "scale": 1
        }
      },
      {
        "name": "Baking Powder",
        "servingSize": {
          "units": "teaspoon",
          "desc": "¼ teaspoon",
          "qty": 0.25,
          "grams": null,
          "scale": 0.25
        }
      },
      {
        "name": "Raw Egg",
        "servingSize": {
          "units": "large",
          "desc": "1 large",
          "qty": 1,
          "grams": 50,
          "scale": 1
        }
      },
      {
        "name": "Blueberries, Frozen, Unsweetened",
        "servingSize": {
          "units": "tablespoon",
          "desc": "1-½ tablespoon",
          "qty": 1.5,
          "grams": 22,
          "scale": 0.094
        }
      }
    ],
    "steps": [
      "Combine the butter and cream cheese together in a heat-safe container. Microwave the ingredients on high heat for 20 seconds until they’re melted. Stir the butter and cream cheese together into one mixture.",
      "Combine the butter and cream cheese mixture with coconut flour, brown sugar substitute, and vanilla extract in the heat-safe dish. You may also wish to add a small pinch of salt. If necessary, you can mix the ingredients in a separate mixing bowl before adding it to your heat-safe dish or mug."
    ],
    "servings": 2,
    "servingSizes": [
      {
        "scale": 1,
        "qty": 1,
        "grams": 100,
        "units": "servings",
        "originalWeight": 100,
        "originalWeightUnits": "g"
      }
    ],
    "nutrients": {
      "caloriesKCal": 185.437,
      "caloriesKJ": 763.317,
      "totalCarbs": 12.83,
      "diabetesCarbsADA": 9.83,
      "netCarbs": 4.032,
      "diabetesCarbs": 4.035,
      "fiber": 2.792,
      "starch": 1.213,
      "sugar": 2.514,
      "addedSugar": 0,
      "sugarAlcohols": 6.006,
      "protein": 5.145,
      "fat": 14.471,
      "transFat": 0.403,
      "monousatFat": 3.811,
      "polyunsatFat": 0.815,
      "omega3Fat": 0.075,
      "omega6Fat": 0.74,
      "saturatedFat": 8.398,
      "cholesterol": 123.147,
      "vitaminA": 130.784,
      "vitaminC": 0.27,
      "vitaminD": 0.562,
      "vitaminE": 0.605,
      "vitaminK": 2.651,
      "vitaminB1": 0.028,
      "vitaminB2": 0.177,
      "vitaminB3": 0.137,
      "vitaminB5": 0.498,
      "vitaminB6": 0.064,
      "vitaminB12": 0.322,
      "potassium": 96.907,
      "magnesium": 10.781,
      "calcium": 63.155,
      "iron": 0.49,
      "zinc": 0.482,
      "copper": 0.064,
      "phosphorus": 87.572,
      "sodium": 198.378,
      "selenium": 10.234,
      "folate": 13.833,
      "choline": 80.661,
      "alcohol": 0.746,
      "caffeine": 0,
      "gluten": 0,
      "manganese": 0.207,
      "conjugatedLinoleicAcid": 0.038,
      "phyticAcid": 74.205,
      "xylitol": 0,
      "isomalt": 0,
      "sorbitol": 0,
      "maltitol": 0,
      "lactitol": 0,
      "erythritol": 0,
      "pinitol": 0,
      "inositol": 0.006,
      "mannitol": 0
    },
    "image": "https://images.low-carb-recipes.com/2807982c-986a-4def-9e3a-153a3066af7a.png"
  }
]
    ```
    """
    url = "https://low-carb-recipes.p.rapidapi.com/search"
    rapid_api_key = os.getenv('RAPID_API_KEY')
    querystring = {
        "name": name,
        "tags": tags,
        "includeIngredients": includeIngredients,
        "excludeIngredients": excludeIngredients,
        "maxPrepareTime": maxPrepareTime,
        "maxCookTime": maxCookTime,
        "maxCalories": maxCalories,
        "maxNetCarbs": maxNetCarbs,
        "maxSugar": maxSugar,
        "maxAddedSugar": maxAddedSugar,
        "limit": limit
    }

    headers = {
        "x-rapidapi-key": rapid_api_key,
        "x-rapidapi-host": "low-carb-recipes.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API request failed with status code {response.status_code}: {response.text}")
import requests

API_KEY = "YOUR_API_KEY_HERE"

def search_food(query):
    url = "https://api.spoonacular.com/recipes/complexSearch"

    params = {
        "query": query,
        "number": 1,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    return response.json()


def get_nutrition(recipe_id):
    url = f"https://api.spoonacular.com/recipes/{recipe_id}/information"

    params = {
        "includeNutrition": True,
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    nutrients = data["nutrition"]["nutrients"]

    nutrition_data = {}

    for n in nutrients:
        if n["name"] in ["Calories", "Fat", "Carbohydrates", "Protein"]:
            nutrition_data[n["name"]] = f"{n['amount']} {n['unit']}"

    return nutrition_data

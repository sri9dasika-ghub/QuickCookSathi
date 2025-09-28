from flask import Flask, request
import re


app = Flask(__name__)


# 🧠 Sample vegetarian recipe database
RECIPE_DB = [
    {
        "name": "Carrot Tomato Moong Dal Curry",
        "ingredients": ["carrot", "tomato", "moong dal"],
        "time": "25 min",
        "nutrition": "Protein + Vitamin A + Antioxidants",
        "method": "Pressure cook moong dal with chopped carrots and tomatoes, turmeric, and cumin. Temper with garlic and mustard seeds."
    },
    {
        "name": "Cabbage Carrot Stir Fry",
        "ingredients": ["cabbage", "carrot"],
        "time": "15 min",
        "nutrition": "Fiber + Antioxidants",
        "method": "Stir fry cabbage and carrot with mustard seeds, curry leaves, and green chilies."
    },
    {
        "name": "Tomato Upma",
        "ingredients": ["rava", "tomato", "onion"],
        "time": "20 min",
        "nutrition": "Quick carbs + Vitamin C",
        "method": "Roast rava, sauté tomato and onion, then cook together with water and spices."
    }
]


# 🧠 Extract ingredients from user message
def extract_ingredients(message):
    message = message.lower()
    items = re.split(r',|and|with|have|got', message)
    ingredients = [item.strip() for item in items if item.strip()]
    return ingredients


# 🧠 Match recipe based on ingredients
def match_recipe(user_ingredients):
    for recipe in RECIPE_DB:
        if all(item in recipe["ingredients"] for item in user_ingredients):
            return recipe
    for recipe in RECIPE_DB:
        if any(item in recipe["ingredients"] for item in user_ingredients):
            return recipe
    return None


# 🧠 Generate response
def generate_response(message):
    user_ingredients = extract_ingredients(message)
    recipe = match_recipe(user_ingredients)
    if recipe:
        return f"🥘 Try '{recipe['name']}'\n{recipe['method']}\n✅ {recipe['nutrition']} | ⏱️ {recipe['time']}"
    else:
        return "Sorry, I couldn't find a recipe with those ingredients. Try adding more common veggies or pulses."


# 🛎️ WhatsApp webhook endpoint
@app.route('/whatsapp', methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.form.get('Body')
    reply = generate_response(incoming_msg)
    return f"<Response><Message>{reply}</Message></Response>", 200


if __name__ == '__main__':
    app.run()
from flask import Flask, request
import re


app = Flask(__name__)


def extract_ingredients(message): 
    message = message.lower() 
    items = re.split(r',|and|with|have|got', message) 
    return [item.strip() for item in items if item.strip()]
 
def searchrecipes_online(ingredients): 
    query = "+".join(ingredients) 
    search_url = f"https://www.forksoverknives.com/?s={query}" 
    return search_url

def generate_response(message): 
    ingredients = extract_ingredients(message) 
    recipelink = searchrecipes_online(ingredients) 
    return f"🔍\nBased on your ingredients, here's a recipe search:\n" \
           f"{recipelink}\nTry exploring the top results!"

@app.route('/whatsapp', methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.form.get('Body')
    reply = generate_response(incoming_msg)
    return f"<Response><Message>{reply}</Message></Response>", 200


if __name__ == '__main__':
    app.run()






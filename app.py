from flask import Flask, request
import re


app = Flask(__app.py__)


# 🧠 Extract ingredients from user message
python 
def extract_ingredients(message): 
    message = message.lower() 
    items = re.split(r',|and|with|have|got', message) 
    return [item.strip() for item in items if item.strip()]


# 2⃣ Perform Web Search 
Use a Python library like requests or httpx to query recipe websites or APIs. Example using 
Forks Over Knives: 
 
`python 
import requests 
 
def searchrecipesonline(ingredients): 
    query = "+".join(ingredients) 
     search_url = f"https://www.forksoverknives.com/?s={query}" 
    return search_url  # You can scrape or return this link


# 🧠 Generate response -3⃣ Format the Reply 
`python 
def generate_response(message): 
    ingredients = extract_ingredients(message) 
recipelink = searchrecipes_online(ingredients) 
return f"
 🔍
 Based on your ingredients, here's a recipe search:\n{recipe_link}\nTry 
exploring the top results!" 


# 🛎️ WhatsApp webhook endpoint
@app.route('/whatsapp', methods=['POST'])
def whatsapp_bot():
    incoming_msg = request.form.get('Body')
    reply = generate_response(incoming_msg)
    return f"<Response><Message>{reply}</Message></Response>", 200


if __name__ == '__main__':
    app.run()


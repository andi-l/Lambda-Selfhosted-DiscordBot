import os
from flask import Flask, jsonify, request
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi
from discord_interactions import verify_key_decorator
from pymongo import MongoClient
from bson.objectid import ObjectId

DISCORD_PUBLIC_KEY = os.environ.get("DISCORD_PUBLIC_KEY")
MONGODB_URI = os.environ.get("MONGODB_URI")

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)
handler = Mangum(asgi_app)

# Initialize MongoDB client at global scope
client = MongoClient(MONGODB_URI)
db = client.your_database_name
items_collection = db.items


@app.route("/", methods=["POST"])
def interactions():
    try:
        print(f"👉 Request: {request.json}")
        raw_request = request.json
        return interact(raw_request)
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return jsonify({"type": 4, "data": {"content": "An error occurred while processing your request."}})



@verify_key_decorator(DISCORD_PUBLIC_KEY)
def interact(raw_request):
    try:
        if raw_request["type"] == 1:
            return {"type": 1}

        data = raw_request["data"]
        command_name = data["name"]

        if command_name == "hello":
            return create_message_response("Hello there!")
        elif command_name == "echo":
            original_message = data["options"][0]["value"]
            return create_message_response(f"Echoing: {original_message}")
        elif command_name == "info":
            return create_message_response("This bot was created by <@637803920340549633>")
        elif command_name == "spreadsheet":
            return create_message_response("Spreadsheet <https://tinyurl.com/repparadise>")
        elif command_name == "register":
            return create_message_response("Register here <https://www.cssbuy.com/paradise>")
        elif command_name == "search":
            category = next(option for option in data["options"] if option["name"] == "category")["value"]
            keywords = next(option for option in data["options"] if option["name"] == "keywords")["value"]
            return search_item(category, keywords)
        else:
            return create_message_response("Command not recognized.")
    except Exception as e:
        print(f"Error in interact function: {str(e)}")
        return create_message_response("An error occurred while processing your command.")


def search_item(category, keywords):
    try:
        query = {
            "category": category,
            "$text": {"$search": keywords}
        }
        results = list(items_collection.find(query).limit(5))

        if not results:
            return create_message_response(f"No results found for '{keywords}' in the '{category}' category.")

        embed = {
            "type": "rich",
            "title": f"Search Results for '{keywords}' in '{category}'",
            "description": f"Here are the top results for your search:",
            "color": 0xffffff,
            "fields": []
        }

        for item in results:
            embed["fields"].append({
                "name": item['name'],
                "value": f"[View Item]({item['link']})",
                "inline": False
            })

        return {
            "type": 4,
            "data": {
                "embeds": [embed]
            }
        }
    except Exception as e:
        print(f"Error in search_item function: {str(e)}")
        return create_message_response("An error occurred while searching for items.")


def create_message_response(content):
    return {
        "type": 4,
        "data": {
            "content": content
        }
    }


def add_item(name, category, link):
    try:
        item = {
            "name": name,
            "category": category,
            "link": link
        }
        result = items_collection.insert_one(item)
        return str(result.inserted_id)
    except Exception as e:
        print(f"Error in add_item function: {str(e)}")
        return None


# Lambda handler
def lambda_handler(event, context):
    return handler(event, context)


if __name__ == "__main__":
    app.run(debug=True)
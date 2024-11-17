import os
from flask import Flask, jsonify, request
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi
from discord_interactions import verify_key_decorator

DISCORD_PUBLIC_KEY = os.environ.get("DISCORD_PUBLIC_KEY")
BLACKLISTED_WORDS = {"link", "W2C"}
SPECIFIC_CHANNEL_ID = 1100493828718329867

app = Flask(__name__)
asgi_app = WsgiToAsgi(app)
handler = Mangum(asgi_app)

@app.route("/", methods=["POST"])
async def interactions():
    print(f"👉 Request: {request.json}")
    raw_request = request.json
    return interact(raw_request)

@verify_key_decorator(DISCORD_PUBLIC_KEY)
def interact(raw_request):
    if raw_request["type"] == 1:  # PING
        response_data = {"type": 1}  # PONG
    else:
        data = raw_request["data"]
        command_name = data["name"]

        # Check if this is a message in the specific channel
        if raw_request["type"] == 2 and raw_request.get("channel_id") == str(SPECIFIC_CHANNEL_ID):
            message_content = data.get("content", "").lower()
            if BLACKLISTED_WORDS in message_content:
                return jsonify({
                    "type": 4,
                    "data": {
                        "content": "Please send this in <#1100491526724923434>.",
                        "flags": 64  # This makes the response ephemeral (only visible to the sender)
                    }
                })

        # Existing command handling
        if command_name == "info":
            message_content = "This bot was created by <@637803920340549633>"
        elif command_name == "spreadsheet":
            message_content = "Spreadsheet <https://tinyurl.com/repparadise>"
        elif command_name == "register":
            message_content = "Register here <https://www.cssbuy.com/paradise>"
        else:
            message_content = "Command not recognized."

        response_data = {
            "type": 4,
            "data": {"content": message_content},
        }

    return jsonify(response_data)

if __name__ == "__main__":
    app.run(debug=True)

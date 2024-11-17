import os
from flask import Flask, jsonify, request
from mangum import Mangum
from asgiref.wsgi import WsgiToAsgi
from discord_interactions import verify_key_decorator

DISCORD_PUBLIC_KEY = os.environ.get("DISCORD_PUBLIC_KEY")

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

        if command_name == "hello":
            message_content = "Hello there!"
        elif command_name == "echo":
            original_message = data["options"][0]["value"]
            message_content = f"Echoing: {original_message}"
        elif command_name == "info":
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

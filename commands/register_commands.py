import requests
import yaml


TOKEN = "MTE4NzczNTUyNTY4ODM0NDU3Ng.GhzIRT.IMOu64KhEF-00v2dQVpzSgooiwtKJxoOZTxJ6c"
APPLICATION_ID = "1187735525688344576"
URL = f"https://discord.com/api/v9/applications/{APPLICATION_ID}/commands"


with open("discord_commands.yaml", "r") as file:
    yaml_content = file.read()

commands = yaml.safe_load(yaml_content)
headers = {"Authorization": f"Bot {TOKEN}", "Content-Type": "application/json"}

# Send the POST request for each command
for command in commands:
    response = requests.post(URL, json=command, headers=headers)
    command_name = command["name"]
    print(f"Command {command_name} created: {response.status_code}")

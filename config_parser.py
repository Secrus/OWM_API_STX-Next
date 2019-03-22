import json


class ConfigParser():
    def __init__(self):
        try:
            with open("config.json", "r") as config_file:
                try:
                    self.config = json.loads(config_file.read())
                except json.JSONDecodeError:
                    print("Error while parsing config file")
        except FileNotFoundError:
            print("Error loading config file")

    def get_api_key(self):
        return str(self.config["API_KEY"])

    def get_api_address(self):
        return str(self.config["API_address"])

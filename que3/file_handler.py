import json
import os

FILE = "application.json"


def load_application():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            try:
                return json.load(file)

            except json.JSONDecodeError:
                return []
    return []


def save_application(applications):
    with open(FILE, "w") as file:
        json.dump(applications, file, indent=4)

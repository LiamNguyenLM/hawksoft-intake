from dotenv import load_dotenv
load_dotenv()

import os

username = os.environ.get("HAWKSOFT_USERNAME", "NOT SET")
password = os.environ.get("HAWKSOFT_PASSWORD", "NOT SET")

print("Username:", username)
print("Password set:", bool(password) and password != "NOT SET")

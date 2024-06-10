import requests
import json
from datetime import datetime


url = "http://127.0.0.1:8000/contacts"

response = requests.get(url)

print(response.json())

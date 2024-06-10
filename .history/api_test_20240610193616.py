import requests
import json
from datetime import datetime


def main():
    url = "http://127.0.0.1:8000/contacts"
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)


if __name__ == "__main__":
    main()

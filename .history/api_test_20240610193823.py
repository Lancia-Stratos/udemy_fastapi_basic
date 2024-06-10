import requests
import json
from datetime import datetime


def main():
    url = "http://localhost:8000/contacts"
    body = {
        "id": 1,
        "name": "山田さん",
        "email": "test1@test.com",
        "url": "https://example.com",
        "gender": 2,
        "birthday": "2024-01-01",
    }


if __name__ == "__main__":
    main()

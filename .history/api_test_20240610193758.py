import requests
import json
from datetime import datetime


def main():
    url = "http://localhost:8000/contacts"
    body = {
        "id": 1,
        "name": "山田さん",
        "email": "test1@test.com",
        "phone": "1234567890",
        "gender": 1,
        "birthday": "2024-01-01",
    }


if __name__ == "__main__":
    main()

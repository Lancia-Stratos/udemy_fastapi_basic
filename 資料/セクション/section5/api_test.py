import requests

url = "https://dog.ceo/api/breeds/image/random"

res = requests.get(url)
print(res.status_code)

print(res.json())
print(res.json()["message"])
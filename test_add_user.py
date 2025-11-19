import requests

data = {
    "id": 1,
    "name": "Apsana",
    "email": "apsana@example.com"
}

response = requests.post("http://127.0.0.1:5000/users", json=data)
print(response.json())

import requests

endpoint = "http://localhost:8000/api/products/"

data = {
    "title": "Product 1",
}

response = requests.post(endpoint, json=data)
print(response.json())
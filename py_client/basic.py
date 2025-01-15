import requests

endpoint = "https://httpbin.org/anything"

response = requests.get(endpoint, json={"query": "Hello World"}) #Emulate HTTP get request
print(response.json()) #Print the response
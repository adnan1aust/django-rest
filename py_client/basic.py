import requests

endpoint = "http://localhost:8080/api/"

response = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello World"}) #Emulate HTTP get request
print(response.json()) #Print the response
#print(response.status_code)
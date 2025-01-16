import requests

endpoint = "http://localhost:8000/api/"

response = requests.get(endpoint, json={"query": "Hello World"}) #Emulate HTTP get request
print(response.json()) #Print the response
#print(response.status_code)
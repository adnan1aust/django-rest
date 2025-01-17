import requests

endpoint = "http://localhost:8000/api/"

response = requests.post(endpoint, json={"test": "Rosemary"}) #Emulate HTTP get request
print(response.json()) #Print the response
#print(response.status_code)
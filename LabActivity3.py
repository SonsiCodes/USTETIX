import requests

response = requests.get("http://ip-api.com/json/24.48.0.1")
print(response.content)
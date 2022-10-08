import requests
import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)

print(IPAddr)

response = requests.get("http://ip-api.com/json").json()
print(response)



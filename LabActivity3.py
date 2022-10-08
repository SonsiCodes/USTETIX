import requests

# api call 
response = requests.get("http://ip-api.com/json").json()

# getting ipv4 address
ipv4 = response["query"]
print("Your ipv4 address is: " + ipv4)

#getting ISP
isp = response["isp"]
print("Your internet service provider is: " + isp)

# getting ASN
asn = response["as"]
print("with the Autonomous System Number: " + asn)

# getting location info 
country = response["country"]
countryCode = response["countryCode"]
region = response["region"]
city = response["city"]
zipcode = response["zip"]

#concatenating location info
geolocation = ("The IP address in located in: " + country + "\n with the country code: " + countryCode 
+ "\n in region: " + region + "\n in the city of: " + city + "\n with the zip code: " + zipcode)
print(geolocation)





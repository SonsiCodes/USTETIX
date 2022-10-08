import requests
import ipaddress

# api call 
response = requests.get("http://ip-api.com/json").json()

# getting ipv4 address
ipv4 = response["query"]
print("Your ipv4 address is: " + ipv4)

#function to convert ipv4 to ipv6
def convertusingipaddress(ipv4address):
    print('Your ipv6 address is: ', ipaddress.IPv6Address('2002::' + ipv4address).compressed)

#displaying ipv6 address
convertusingipaddress(ipv4)

#getting ISP
isp = response["isp"]
print("Your internet service provider is: " + isp)

# getting ASN
asn = response["as"]
print("with the Autonomous System Number: " + asn[0:6])

# getting location info 
country = response["country"]
lat = str(response["lat"])
lon = str(response["lon"])
GeoLocation = " The latitude is " + lat + " and longitude " + lon
countryCode = response["countryCode"]
region = response["region"]
city = response["city"]
zipcode = response["zip"]

#concatenating location info
CompleteLoc = ("The IP address in located in: " + country + "\n with the country code: " + countryCode 
+ "\n in region: " + region + "\n in the city of: " + city + "\n with the zip code: " + zipcode + "\n Geolocation:"+ GeoLocation)
print(CompleteLoc)







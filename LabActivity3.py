import requests
import ipaddress
import pandas as pd


response = requests.get("http://ip-api.com/json").json()
responsetxt = requests.get("http://ip-api.com/json")




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



#function to save response to a text file
def savefile(responsetxt):
    with open("response.txt", "w") as f:
        f.write(CompleteLoc)
        f.close()


#function to get response using manual ip address
def getManualIP(manIp):
    manReq = requests.get("http://ip-api.com/json/"+manIp).json()
    manReqtxt = requests.get("http://ip-api.com/json/"+manIp)

    ipv4 = manIp
    print("Your ipv4 address is: " + ipv4)

    def convertusingipaddress(ipv4address):
        print('Your ipv6 address is: ', ipaddress.IPv6Address('2002::' + ipv4address).compressed)

    convertusingipaddress(ipv4)

    isp = manReq["isp"]
    print("Your internet service provider is: " + isp)

    asn = manReq["as"]
    print("with the Autonomous System Number: " + asn[0:6])

    country = manReq["country"]
    countryCode = manReq["countryCode"]
    region = manReq["region"]
    city = manReq["city"]
    zipcode = manReq["zip"]
    CompleteLoc = ("The IP address in located in: " + country + "\n with the country code: " + countryCode 
    + "\n in region: " + region + "\n in the city of: " + city + "\n with the zip code: " + zipcode)
    print(CompleteLoc)

    print("\n Additional Features: Type the corresponding letter for each choice \n Manually Input desired IP address = m \n Save Previous Response to a text file = s ")
    choice = input()

    if choice == "m":
        manIp = input("Type your desired IP address: ")
        getManualIP(manIp)

    if choice == "s":
        with open("response2.txt", "w") as f:
            f.write(CompleteLoc)
            print("response succesfully saved!")      

    else:
        print("thank you for using our service")
  


# additional features      

print("Additional Features: Type the corresponding letter for each choice \n Manually Input desired IP address = m \n Save Previous Response to a text file = s ")
choice = input()

if choice == "m":
    manIp = input("Type your desired IP address: ")
    getManualIP(manIp)

if choice == "s":
    savefile(CompleteLoc)
    print("response succesfully saved!")  

else:
    print("thank you for using our service")












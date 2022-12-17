import requests
import xml.dom.minidom
import requests
from ncclient import manager

#onnects to Cisco-IOS-XE-native
m = manager.connect(
 host="136.158.16.20",
 port=10000,
 username="devasc",
 password="cisco123!",
 hostkey_verify=False
 )

changes = ''
previousconfig= ''
newconfig = ''

access_token = 'NmFmYTlhYjAtMDcwMC00ZWJhLTlhZjYtNjRlMTcyNDhkMjg3NjI2Y2I0YzUtNDg5_P0A1_782d819d-6cea-4125-8e28-7c1c7843971f'  
L1rm = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vOTBiMGZlZDAtN2QxNC0xMWVkLTgxYmMtOWI5Y2U5YzVkN2Fh'
L2rm = 'Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vOWMyZDM2MjAtN2QxNC0xMWVkLWFlN2QtNjNhOWU3MzY5ODg2'
def message_room(roomid, text, access_token):
    url = 'https://webexapis.com/v1/messages'
    headers = {
        'Authorization': 'Bearer {}'.format(access_token),
        'Content-Type': 'application/json'
    }
    params={
        "roomId": roomid,
        "text": text
    }
    res = requests.post(url, headers=headers, json=params)
    print(res.json())


def viewrunningconfig():
        netconf_reply = m.get_config(source="running")
        res = xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()
        netconf_filter = """
        <filter>
         <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native"/>
        </filter>
        """
        print('')
        return res



def editdevicename(hostname):
    netconf_input_hostname = """
    <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <hostname>"""+ hostname +"""</hostname>
    </native>
    </config>
    """
    changes+= str('\n The hostname has been modified to: '+ hostname +'.')
    netconf_reply = m.edit_config(target="running", config=netconf_input_hostname)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()) 
    message = 'The hostname has been modified to: '+ hostname +'.'
    message_room(L1rm, message, access_token)
    message_room(L2rm, message, access_token)
    print('')      



def editdevicedesc(description):
    netconf_input_description = """
    <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <interface>
    <GigabitEthernet>
    <name>1</name>
    <description>"""+ description +"""</description>
    </GigabitEthernet>
    </interface>
    </native>
    </config>
    """
    changes+= str('\n GigabitEthernet 1\'s description has been modified to: '+ description +'.')
    netconf_reply = m.edit_config(target="running", config=netconf_input_description)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml()) 
    message = 'GigabitEthernet 1\'s description has been modified to: '+ description +'.'
    message_room(L1rm, message, access_token)
    message_room(L2rm, message, access_token)
    print('')  

def editdevicebanner(banner):
 
    netconf_input_banner = """
    <config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <banner>
    <motd>
    <banner>#"""+ banner +"""#</banner>
    </motd>
    </banner>
    </native>
    </config>
    """
    changes+=  str('\n The banner has been modified to: '+ banner +'.')
    netconf_reply = m.edit_config(target="running", config=netconf_input_banner)
    print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
    message = 'The banner has been modified to: '+ banner +'.'
    message_room(L1rm, message, access_token)
    message_room(L2rm, message, access_token)
    print('')


def makechanges():
    editdevicedesc('lorem ipsum')
    editdevicename('new hostname')
    editdevicebanner('good day to you all')






previousconfig = viewrunningconfig()
print(previousconfig)
makechanges()
print(changes)
newconfig = viewrunningconfig()
print(newconfig)


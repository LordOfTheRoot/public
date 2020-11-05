#!/usr/bin/python3
'''This is just some simple code to get info about your NordVPN connection on GNU/Linux.'''
import os
import requests

def main():
    NORDVPN = True
    if NORDVPN == True:
        try:
            OUTPUT = os.popen("nordvpn status").read()
        except:
            NORDVPN = False
    try:
        R = requests.get("https://ifconfig.io/ip")
        IP = "IP: "+R.text.split("\n")[0]
    except:
        exit("Offline")

    if NORDVPN == True:
        VPN_STATUS = "VPN status: "+OUTPUT.split("Status: ")[1].split("\n")[0]
        VPN_SERVER = "VPN server: "+OUTPUT.split("Current server: ")[1].split("\n")[0]
        VPN_COUNTRY = "VPN country: "+OUTPUT.split("Country: ")[1].split("\n")[0]
        VPN_CITY = "VPN city: "+OUTPUT.split("City: ")[1].split("\n")[0]
        
        print(IP)
        print(VPN_STATUS)
        print(VPN_SERVER)
        print(VPN_COUNTRY)
        print(VPN_CITY)

    if NORDVPN == False:
        print(IP)

if __name__ == "__main__":
    main()

#! /usr/bin/python
import os
import requests
import json

listIpv4 = []
uniqueIpv4 = [];
numOfRow = 0

def main():
    print ("Check IP Origin for HTTPD Access Log V0.1")
    os.system('cls')

    getIp()
    readURL(uniqueIpv4)

    print ("\nEnd of Program. Bye!")

def getIp():
    f=open("access_log", "r")
    if f.mode== "r":
        contents = f.readlines()
        print("Number of line is: " + str(len(contents)))
        for x in contents:
            rowData = x.split(" ");
            getIpV4(rowData[0])

def getIpV4(ip):
    if(len(ip) > 7 and len(ip) < 15):
##      remove duplicate IP
        if ip not in uniqueIpv4:
            uniqueIpv4.append(ip)
            listIpv4.append(ip)

def getIpV6():
    print("Getting IPV6 only: ")

def filterDuplicateIp(list1):
    for x in list1: 
        if x not in uniqueIpv4: 
            uniqueIpv4.append(x)

def getBothVer():
    print("Getting IPV4 and IPV6: ")

def readURL(ip):
    i = 0;
    for x in ip:
##    print("https://api.ipgeolocation.io/ipgeo?apiKey=[API_KEY]&ip="+ip[i]+"")
        link = "https://api.ipgeolocation.io/ipgeo?apiKey=[API_KEY]&ip="+ip[i]+""
        response = requests.get(link)
        json_data = json.loads(response.text)
        print(ip[i]+" - "+json_data['city']+", "+json_data['country_name'])
        i += 1

def printUniqueIp():
    print(uniqueIpv4)

if __name__ == "__main__":
    main()

#! /usr/bin/python3
import os
import requests
import json

listIpv4 = []
uniqueIpv4 = [];
numOfRow = 0

def main():
    print ("Check IP Origin for HTTPD Access Log V0.1", end="\n")
    os.system('cls')

    getIp()
    readURL(listIpv4)
##    getIp()
##    unique(listIpv4)
##    printUniqueIp()
##    print("")
    print ("\nEnd of Program. Bye!")

def getIp():
    f=open("access_log", "r")
    if f.mode== "r":
        contents = f.readlines()
        print("Number of line is: " + str(len(contents)))
        for x in contents:
            rowData = x.split(" ");
            getIpV4(rowData[0])
##        print(str(len(listIpv4)))
##        print(listIpv4[3])

def getIpV4(ip):
##    print("Getting IPV4 only: ")
    if(len(ip) > 7 and len(ip) < 15):
##        print(ip)
        listIpv4.append(ip)

def getIpV6():
    print("Getting IPV6 only: ")

def getBothVer():
    print("Getting IPV4 and IPV6: ")

def filterDuplicate():
##    print("Remove Duplicate IP")
    ip = ["127.0.0.1", "127.0.0.1", "127.0.0.2"]

    print(unique(ip))
##    for x in range(0, len(ip)):
##        print("how many time(s)"+ str(x))
    
def unique(list1):
    for x in list1: 
        if x not in uniqueIpv4: 
            uniqueIpv4.append(x) 

def readURL(ip):
    i = 0;
##    print(ip)
    for x in ip:
##      print("https://api.ipgeolocation.io/ipgeo?apiKey=1646fff566d646bdabe1bb1362612fcb&ip="+ip[i]+"")
        link = "https://api.ipgeolocation.io/ipgeo?apiKey=1646fff566d646bdabe1bb1362612fcb&ip="+ip[i]+""
        response = requests.get(link)
        json_data = json.loads(response.text)
        print(ip[i]+" - "+json_data['city']+", "+json_data['country_name'])
        i += 1

def printUniqueIp():
    print(uniqueIpv4, end="\n")

if __name__ == "__main__":
    main()

# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 07:41:45 2021

@author: david
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
#orig=quito
#dest="Guayaquil
key= "LG6GuA87w8MGANG8Dt9yCAYMxpJYQT7k"
while True:
    orig=input("starting location: ")
    if orig == "quit" or orig =="q":
        break
    
    
    dest=input("destination:  ")
    if dest== "quit" or dest=="q":
        break
    
    
    url= main_api + urllib.parse.urlencode({"key":key,"from":orig,"to":dest})
    print ("URL: "+(url))
    
    json_data= requests.get(url).json()
    json_status = json_data["info"]["status code"]
    
    if json_status == 0:
        print("API Status: " + str(json_status)+ " = A succesfull route call .\n")
        print("directions from "+ (orig) + "to " + (dest))
        print("trip duration:  "+(json_data ["route"]["formated Time"]))
        print("Kilometers:    "+ str ("{:. 2f}" .format ((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): "+ str("{:. 2f}".format ((json_data["route"]["fuel used"])*3.78)))
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " ("+ str("{:.2f}".format((each["distance"])*1.61)+ " km) "))
        print("=====================================\n")
    elif json_status == 402:
        print("\n****************************************************************")
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
        print("****************************************************************\n")
    else:
        print("\n************************************************************************")
        print("Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")
        
    
        







#!/usr/bin/python

#import libraries
import json
import requests 
import os
import sys
import pandas as pd

#declare parameters
key=sys.argv[1]
bus_ref=sys.argv[2]
filename=sys.argv[3]

url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+key+"&VehicleMonitoringDetailLevel=calls&LineRef="+bus_ref
js_file=requests.get(url).json()
buses=js_file['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
num_buses=len(buses)
#create dataframe
columns = ['Latitude','Longitude','Stop Name','Stop Status']
dataframe = pd.DataFrame(columns=columns)
for x in range(num_buses):
#for x in range(2):
    long=buses[x]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    lat=buses[x]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    if len(buses[x]['MonitoredVehicleJourney']['OnwardCalls'])==0:
        stop_nm="N/A"
        stop_sta="N/A"
    else:
        stop_nm=buses[x]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName']
        stop_sta=buses[x]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance']
    for_ap = pd.DataFrame([[lat,long,stop_nm,stop_sta]], columns=['Latitude','Longitude','Stop Name','Stop Status'])
    dataframe=dataframe.append([for_ap])
dataframe.to_csv(filename,header=True, index=False, encoding='utf-8')

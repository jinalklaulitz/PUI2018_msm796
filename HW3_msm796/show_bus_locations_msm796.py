#!/usr/bin/python

#import libraries
import json
import requests 
import os
import sys

#declare parameters
key=sys.argv[1]
bus_ref=sys.argv[2]

url="http://bustime.mta.info/api/siri/vehicle-monitoring.json?key="+key+"&VehicleMonitoringDetailLevel=calls&LineRef="+bus_ref
js_file=requests.get(url).json()
buses=js_file['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
num_buses=len(buses)
print("Bus Line : "+bus_ref)
print("Number of active buses: "+str(num_buses))
for x in range(num_buses):
    long=buses[x]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
    lat=buses[x]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
    print("bus "+str(x)+" is at latitude "+str(lat)+" and longitude "+str(long))

from netmiko import ConnectHandler
from operator import itemgetter
from getpass import getpass
import json
import csv
import os

ControllerIP = input('IP of WLC: ')
username = input('Enter your username: ')
password = getpass()

filename = 'H:/WLC/' + ControllerIP +'.csv'
write_header = not os.path.exists(filename)


WLC = {
    'ip':   ControllerIP,
    'username': username,
    'password': password,
    'device_type': 'cisco_wlc_ssh',


    }

net_connect = ConnectHandler(**WLC)
output = net_connect.send_command('show ap summary', use_textfsm=True)

l = len(output)
for a in range(0,l):

    Name = output[a]['ap_name']
    Model = output[a]['ap_model']
    MAC = output[a]['mac']
    IP = output[a]['ip']
    Location = output[a]['location']

    with open(filename, 'a') as csvfile:
        writer = csv.writer(csvfile)
        csvdata = (Name,Model,MAC,IP,Location)
        writer.writerow(csvdata)
#print (json.dumps(output, indent=2))

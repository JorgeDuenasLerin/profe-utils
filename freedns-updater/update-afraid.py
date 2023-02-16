#!/bin/env python3

import json
import os
import urllib3

from requests import get

IP_FILE='ip.txt'
CREDENTIAL_FILE='credentials.real.json'

if not os.path.isfile(CREDENTIAL_FILE):
    print("Crea el fichero de credenciales real.")
    exit()

if not os.path.isfile(IP_FILE):
    print("Primera ejecución")
    with open(IP_FILE, 'w') as ipfile:
        ip=get('https://api.ipify.org').text
        ipfile.write(ip)

last_ip=None
with open(IP_FILE, 'r') as ipfile:
    last_ip=ipfile.read()

current_ip=get('https://api.ipify.org').text
         
if current_ip != last_ip:
    print("Actualizando!")
    f = open(CREDENTIAL_FILE)
    credential = json.load(f)
    http = urllib3.PoolManager()
    headerAuth = urllib3.util.make_headers(basic_auth=f"{credential['username']}:{credential['password']}")
    req = http.request(
        'GET',
        "http://sync.afraid.org/u/",
        headers=headerAuth,
        fields={
            'u': credential['username'],
            'p': credential['password'],
            'h': credential['hostname'],
            'ip': current_ip
        }
    )
    print(req.data)
    print("Actualizando última ip")
    with open(IP_FILE, 'w') as ipfile:
        ipfile.write(current_ip)

else:
    print("Sin cambio...")

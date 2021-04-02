# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:05:58 2016
Written by Diego Zuñiga
Adapted by Jostin Kitmang
mail: jkitmang@gmail.com

Proposito:
    - Descargar latitud y longitud de cada dispensario.

Input:
    - Dispensaries_pw1.txt  CANNABIS WEB
    - Dispensaries_pw2.txt  WEEDMAPS
    - Dispensaries_pw3.txt  LEAFLY
    - Dispensaries_pw4.txt  MARIJUANA DOCTORS

Output:
    - Dispensaries_gis.txt

"""

# for Marijuana Dispensaries directions

import requests
import re

#Directorios
cd = "C:/Users/jkitmang/Dropbox/Research/1. Researchers/Marijuana and health/00_Data/MarijuanaDispensaries/txtfiles/"
cd_gis = cd + "output/Dispensaries_gis.txt"

f = open(cd_gis, 'r')
f.close()


# A = Listado de dispensarios descargados en "scrapping_MarijuanaDispensaries.py"

direc = []
for i in range(1, 5):
    temp_dis = cd + "temp/Dispensaries_pw" + str(i) + ".txt"
    f = open(temp_dis, 'r')
    addresses = f.readlines()
    for address in addresses[0:len(addresses) - 1]:
        direc.append(address[0:len(address) - 1])
    direc.append(addresses[-1])
    f.close()

print(len(direc))

# B = Listado de dispensarios que ya se han georeferenciado
f = open(cd_gis, 'r')
info = f.readlines()
place  = []
for x in info:
    place.append(x.split('\t')[0])
f.close()

# A - B = Listado de dispensarios que faltan georeferenciar
direc = set(direc).difference(place)
direc = set(direc)
print(len(direc))

#GoogleMapsAPI
lat = []
lon = []
formatted_address = []
place_id = []
for direccion in direc:
    address2 = ""
    for i, char in enumerate(direccion):

        if char == " ":
            address2 += "+"
        else:
            address2 += char
    key = 'here put your key'
    url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address2 + key
    response = requests.get(url)
    resp_json_payload = response.json()

    #Crear elementos
    if resp_json_payload['status'] == "OK":
        a = resp_json_payload['results'][0]['geometry']['location']
        lat = a["lat"]
        lon = a["lng"]

        b = resp_json_payload['results'][0]
        formatted_address = b['formatted_address']
        place_id = b["place_id"]

    else:
        lat = 999
        lon = 999
        formatted_address = "999"
        place_id = "999"

    print('Direcciones calculadas: {}' + direccion)

    # Guardar elementos
    f = open(cd_gis, 'a', encoding='utf-8')
    direccion = direccion.replace("\n", " ")
    towrite = direccion + "\t" + str(lat) + "\t" + str(lon) + "\t" + str(formatted_address) + "\t" + str(place_id) + "\t" + "\n"
    f.write(towrite)
    f.close()

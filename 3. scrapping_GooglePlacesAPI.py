# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:05:58 2016
Written by Jostin Kitmang
mail: jostin.kitmang@gmail.com

Proposito:
    - Validar la información descargada.

Input:
    - Dispensaries_gis.txt (Columna 4: Clave_ID)
Output:
    - Dispensaries_closed.txt
"""

# for Marijuana Dispensaries

import requests
import re

cd = "C:/Users/jkitmang/Dropbox/Research/1. Researchers/Marijuana and health/00_Data/MarijuanaDispensaries/txtfiles/output/"
cd_gis = cd + "Dispensaries_gis.txt"
cd_clo = cd + "Dispensaries_closed.txt"

# A = Listado de ID Dispensario
f = open(cd_gis, 'r')
info = f.readlines()
place_id = []
for x in info:
    place_id.append(x.split('\t')[4])
f.close()

# B = Listado descargado de situación (Cerrado permanentemente?) y telefono de cada Dispensario
f = open(cd_clo, 'r')
info = f.readlines()
place  = []
for x in info:
    place.append(x.split('\t')[0])
f.close()

# A - B
place_id = set(place_id).difference(place)
print(len(place_id))

# GooglePlaceAPI
closed = []
number = []
for direccion in place_id:
    clave = '&key=XXXX'
    url = 'https://maps.googleapis.com/maps/api/place/details/json?placeid=' + direccion + clave
    response = requests.get(url)

    resp_json_payload = response.json()

    # Descargar elementos
    if resp_json_payload['status'] == "OK":
        a = resp_json_payload['result']
        name = a["name"]
        try:
            number = a["international_phone_number"]
        except:
            number = "9999"

        try:
            closed = a['permanently_closed']
        except:
            closed = "FALSE"
    else:
        closed = "NO OK"
        number = "NO OK"
        name = "NO OK"
    print('Empresa:' + str(direccion))

    #Guardar elementos
    f = open(cd_clo, 'a', encoding='utf-8')
    direccion = direccion.replace("\n", " ")
    towrite = direccion + "\t" + str(closed) + "\t" + str(number) + "\n"
    f.write(towrite)
    f.close()

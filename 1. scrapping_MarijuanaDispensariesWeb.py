# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 10:05:58 2016
Written by Jostin Kitmang
mail: jostin.kitmang@gmail.com

DESCRIPCION:
    1) Descargar nombres y direcciones de todos los dispensarios de marihuana en USA de las siguientes paginas:
        - https://cannabis.net/find/dispensary
        - https://weedmaps.com/dispensaries/in/united-states
        - https://www.leafly.com/finder
        - https://www.marijuanadoctors.com/medical-marijuana-dispensaries/

INPUTS:
    search_1.txt >> Estados
    search_3.txt >>
    search_4.txt >>

OUTPUT:
    - Dispensaries_pw1.txt  CANNABIS WEB
    - Dispensaries_pw2.txt  WEEDMAPS
    - Dispensaries_pw3.txt  LEAFLY
    - Dispensaries_pw4.txt  MARIJUANA DOCTORS

"""

import os
from selenium import webdriver
import time

# Driver de chrome
chromedriver = "C:/Users/jkitmang/Dropbox/Sotfware/Python/Installers/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/jkitmang/AppData/Local/Google/Chrome/User Data/Default")
b = webdriver.Chrome(chromedriver, chrome_options=options)

#Crear txtfiles
cd = "C:/Users/jkitmang/Dropbox/Research/1. Researchers/Marijuana and health/00_Data/MarijuanaDispensaries/txtfiles/"

out_dis1 = cd + "temp/Dispensaries_pw1.txt"
out_dis2 = cd + "temp/Dispensaries_pw2.txt"
out_dis3 = cd + "temp/Dispensaries_pw3.txt"
out_dis4 = cd + "temp/Dispensaries_pw4.txt"

search_1 = cd + "input/item_1.txt"
search_3 = cd + "input/item_3.txt"
search_4 = cd + "input/item_4.txt"

#Abrir la pagina 1
f = open(out_dis1, 'w')
f.close()

b.get("https://cannabis.net/find/dispensary")

cerrar = b.find_element_by_xpath('//*[@id="noresults_map"]/span/p/a')
cerrar.click()

# Poner lista de estados para buscar
f = open(search_1, 'r')
addresses = f.readlines()
direc = []
for address in addresses[0:len(addresses) - 1]:
    direc.append(address[0:len(address) - 1])
direc.append(addresses[-1])
f.close()

for state in direc:
    print(state)

    cuadro = b.find_element_by_xpath("//*[@id='search-input']")
    cuadro.clear()
    cuadro.send_keys(state)

    search = b.find_element_by_xpath('//*[@id="search-btn"]/span')
    search.click()

    time.sleep(5)

    count = len(b.find_elements_by_xpath('//*[@id="search-result-items"]/div'))
    count = count + 1

    for ll in range(1, count):
        print(ll)

        filas = len(b.find_elements_by_xpath('//*[@id="search-result-items"]/div['+str(ll)+']/div/div'))
        filas = filas - 1

        local = b.find_element_by_xpath('//*[@id="search-result-items"]/div['+str(ll)+']/div/div['+str(filas)+']/div[1]/a/h4').text
        f = open(out_dis1, 'a')
        towrite = str(local) + ", " + str(state) + "\n"
        f.write(towrite)
        f.close()

#Abrir la pagina 2: WEEDMAPS
f = open(out_dis2, 'w')s
f.close()
b.get("https://weedmaps.com/dispensaries/in/united-states")

count = len(b.find_elements_by_xpath('/html/body/ion-nav-view/ion-nav-view/ion-view/wm-listings-map/div/wm-multi-map-overlay/div/div[1]/ion-content/div/wm-listing-peek')) + 1

for i in range(1, count):
    name = b.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/ion-view/wm-listings-map/div/wm-multi-map-overlay/div/div[1]/ion-content/div/wm-listing-peek['+str(i)+']/div/div/a/wm-map-peek/div/div/div[2]/h2').text
    place = b.find_element_by_xpath('/html/body/ion-nav-view/ion-nav-view/ion-view/wm-listings-map/div/wm-multi-map-overlay/div/div[1]/ion-content/div/wm-listing-peek['+str(i)+']/div/div/a/wm-map-peek/div/div/div[3]/span').text

    f = open(out_dis2, 'a')
    towrite = str(name) + ", " + str(place) + "\n"
    f.write(towrite)
    f.close()

#Abrir la pagina 3: LEAFLY
#ESTA PAGINA DESCARGA DEL ESTADO BUSCADO Y DE LOS ALEDAÑOS
f = open(out_dis3, 'w')
f.close()
f = open(search_3, 'r')
info = f.readlines()
search = []
for x in info:
    search.append(x.split('\t')[0])
f.close()
search = set(search)

b.get("https://www.leafly.com/finder")
try:
    close = b.find_element_by_xpath('/html/body/div[5]/div/div/div/div[1]/button/i')
    close.click()
except:
    print("NO")
edad = b.find_element_by_xpath('/html/body/div[4]/div/div/div/form/div[1]/div[1]/fieldset/label')
edad.click()
cont = b.find_element_by_xpath('/html/body/div[4]/div/div/div/form/div[2]/button')
cont.click()


for x in search:
    cuadro = b.find_element_by_xpath("//*[@id='finder']/div/h1/location-changer/form/input")
    cuadro.clear()
    cuadro.send_keys(x)

    loc = b.find_element_by_xpath('//*[@id="finder"]/div/h1/location-changer/form/i')
    loc.click()
    time.sleep(4)
    count = len(b.find_elements_by_xpath('//*[@id="finder"]/finder-container/div/ul/li')) + 1
    for i in range(2, count):
        local = b.find_element_by_xpath('//*[@id="finder"]/finder-container/div/ul/li[' + str(i) + ']/a/div/div[1]/div[1]').text
        f = open(out_dis3, 'a')
        towrite = str(local) + ", " + str(x) + "\n"
        f.write(towrite)
        f.close()



#Abrir la pagina 4: https://www.marijuanadoctors.com/medical-marijuana-dispensaries/


f = open(out_dis4, 'w')
f.close()

f = open(search_4, 'r')
info = f.readlines()
search = []
for x in info:
    search.append(x.split('\n')[0])
f.close()

for x in search:
    #x = "ak"
    b.get("https://www.marijuanadoctors.com/medical-marijuana-dispensaries/" + x)
    count = len(b.find_elements_by_xpath('//*[@id="top"]/section[1]/div[1]/div/div[1]/div[2]/div')) + 1
    if count < 2:
        print(x + "NO HAY")
    else:
        state = b.find_element_by_xpath('//*[@id="top"]/section[1]/div[1]/div/div[1]/div[2]/h2').text
        state = state.split(' ')[2]
        for i in range(2, count):
            #i = 2
            local = b.find_element_by_xpath('//*[@id="top"]/section[1]/div[1]/div/div[1]/div[2]/div[' + str(i) + ']/div/div[1]/a[2]/h1').text
            f = open(out_dis4, 'a')
            towrite = str(local) + ", " + str(state) + "\n"
            f.write(towrite)
            f.close()


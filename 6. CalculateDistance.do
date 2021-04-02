*************************************************************************
* Distance between marijuana dispensaries and the center of the county in USA
* @Author: Jostin Kitmang 
* Last updated: Febrary 6, 2018
*************************************************************************

clear all
set more off, perm

global out "C:\Users\jkitmang\Dropbox\Research\1. Researchers\Marijuana and health\00_Data\MarijuanaDispensaries\txtfiles\output\"

***Dispensaries_closed 
import delimited "$out\Dispensaries_closed.txt", clear
ren (v1 v2 v3) (place_id closed_perm number)
replace closed_perm = "False" if closed_perm != "True" 
tempfile closed
save `closed'

***Dispensaries_gis
import delimited "$out\Dispensaries_gis.txt", clear
drop v6
g founded = (v2!=999)
foreach var in v4 v5{
replace `var' = "" 	if `var' == "999"
}
foreach var in v2 v3{
replace `var' = . 	if `var' ==  999
}

ren	(v1 v2 v3 v4 v5) (search lat lon address place_id)
merge m:1 place_id using `closed', keep(1 3)

*clean up some observations
g 		coming_soon = 0
replace coming_soon = regexm(search, "Soon") | regexm(search, "soon") | regexm(search, "Open")
drop if coming_soon == 1
drop _merge coming_soon

keep address place_id closed_perm number
drop if address==""
duplicates drop

tempfile data_gis
save `data_gis'

***Dispensary county
import delimited "$out\Dispensaries_county.txt", clear 
duplicates drop place_id, force

merge 1:1 place_id using `data_gis', keep(3) nogen

drop fid join_count target_fid xcoord ycoord geoid
lab var place_id 	"ID unico del local en Google Maps"
lab var lat 		"Latitud del dispensario"
ren lat place_lat
lab var lon			"Longitud del dispensario"
ren lon place_lon
ren name county_name 
lab var county_name "Nombre del condado"
ren statefp state_id
lab var state_id "ID del estado"
ren countyfp county_id
lab var county_id "ID del condado"
ren intptlat county_lat
lab var county_lat ""
ren intptlon county_lon	
lab var county_lon ""

replace county_lat=. if county_lat==0
replace county_lon=. if county_lat==0
ren address place_address
lab var place_address "Direccion del dispensario"
lab var closed_perm   "Indicador de cerrado permanente"
lab var number 		"Numero del dispensario"
ren number place_number

*calculate distance
geodist place_lat place_lon county_lat county_lon, g(distance)
lab var distance "Distancia al centro del condado (en millas)"

global dta "C:\Users\jkitmang\Dropbox\Research\1. Researchers\Marijuana and health\00_Data\MarijuanaDispensaries\dtafiles"
save "$dta\Dispensaries_distance.dta", replace

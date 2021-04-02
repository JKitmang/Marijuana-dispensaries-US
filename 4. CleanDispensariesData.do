*************************************************************************
* Clean georeferenced data from marijuana dispensaries
* @Author: Jostin Kitmang 
* Last updated: Febrary 6, 2018
*************************************************************************

clear all
set more off, perm

global out "C:\Users\jkitmang\Dropbox\Research\1. Researchers\Marijuana and health\00_Data\MarijuanaDispensaries\txtfiles\output\"

*Dispensaries closed
import delimited "$out\Dispensaries_closed.txt", clear
ren (v1 v2 v3) (place_id closed_perm number)
tempfile closed
save `closed'

*Dispensaries GIS
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

duplicates drop
*missing download 442 places
drop if lat==.

keep place_id lat lon
order place_id lat lon
duplicates drop
export delimited place_id lat lon using "$out\Dispensaries_gis_cleaned.txt", replace



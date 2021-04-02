# -*- coding: utf-8 -*-
# ---------------------------------------------------------------------------
# Created on Wed Oct  5 10:05:58 2016
# Written by Jostin Kitmang
# mail: jostin.kitmang@gmail.com
# Description: 
# Create "Dispensary_county.txt"
# ---------------------------------------------------------------------------

############################## Preamble #################################

### Read the ArcGIS object ###
print "Launching ArcGIS 10"
import arcpy

### Set environment ###
print "Setting the environment"

# Local variables:
tl_2016_us_county_shp__2_ = "C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\input\\tl_2016_us_county.shp"
Dispensaries_gis_cleaned_txt__2_ = "C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\MarijuanaDispensaries\\txtfiles\\output\\Dispensaries_gis_cleaned.txt"
cb_2016_us_county_500k_shp = "C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\input\\cb_2016_us_county_500k.shp"
Dispensaries_gis_shp = "C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\MarijuanaDispensaries\\shpfiles\\Dispensaries_gis.shp"
cb_2016_us_county_500k_wcenter_shp = "C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\output\\cb_2016_us_county_500k_wcenter.shp"
Dispensaries_county_shp = "C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\MarijuanaDispensaries\\shpfiles\\Dispensaries_county.shp"
Dispensaries_county_txt = "C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\MarijuanaDispensaries\\txtfiles\\output\\Dispensaries_county.txt"
tl_2016_us_county_txt = "C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\txtfiles\\tl_2016_us_county.txt"
Dispensaries_gis = "Dispensaries_gis"
tl_2016_us_county_Layer = "tl_2016_us_county_Layer"
cb_2016_us_county_500k_center_shp = "C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\output\\cb_2016_us_county_500k_center.shp"

# Process: Make XY Event Layer (2)
arcpy.MakeXYEventLayer_management(Dispensaries_gis_cleaned_txt__2_, "lon", "lat", Dispensaries_gis, "", "")

# Process: Copy Features
arcpy.CopyFeatures_management(Dispensaries_gis, Dispensaries_gis_shp, "", "0", "0", "0")

# Process: Export Feature Attribute to ASCII (2)
arcpy.ExportXYv_stats(tl_2016_us_county_shp__2_, "FID;INTPTLAT;INTPTLON", "COMMA", tl_2016_us_county_txt, "ADD_FIELD_NAMES")

# Process: Make XY Event Layer
arcpy.MakeXYEventLayer_management(tl_2016_us_county_txt, "INTPTLON", "INTPTLAT", tl_2016_us_county_Layer, "", "")

# Process: Copy Features (2)
arcpy.CopyFeatures_management(tl_2016_us_county_Layer, cb_2016_us_county_500k_center_shp, "", "0", "0", "0")

# Process: Spatial Join (2)
arcpy.SpatialJoin_analysis(cb_2016_us_county_500k_shp, cb_2016_us_county_500k_center_shp, cb_2016_us_county_500k_wcenter_shp, "JOIN_ONE_TO_ONE", "KEEP_ALL", "STATEFP \"STATEFP\" true true false 2 Text 0 0 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\input\\cb_2016_us_county_500k.shp,STATEFP,-1,-1;COUNTYFP \"COUNTYFP\" true true false 3 Text 0 0 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\input\\cb_2016_us_county_500k.shp,COUNTYFP,-1,-1;COUNTYNS \"COUNTYNS\" true true false 8 Text 0 0 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\input\\cb_2016_us_county_500k.shp,COUNTYNS,-1,-1;AFFGEOID \"AFFGEOID\" true true false 14 Text 0 0 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\input\\cb_2016_us_county_500k.shp,AFFGEOID,-1,-1;GEOID \"GEOID\" true true false 5 Text 0 0 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\input\\cb_2016_us_county_500k.shp,GEOID,-1,-1;NAME \"NAME\" true true false 100 Text 0 0 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\input\\cb_2016_us_county_500k.shp,NAME,-1,-1;LSAD \"LSAD\" true true false 2 Text 0 0 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\input\\cb_2016_us_county_500k.shp,LSAD,-1,-1;ALAND \"ALAND\" true true false 14 Double 0 14 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\input\\cb_2016_us_county_500k.shp,ALAND,-1,-1;AWATER \"AWATER\" true true false 14 Double 0 14 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\input\\cb_2016_us_county_500k.shp,AWATER,-1,-1;XCoord \"XCoord\" true true false 8 Double 0 0 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\output\\cb_2016_us_county_500k_center.shp,XCoord,-1,-1;YCoord \"YCoord\" true true false 8 Double 0 0 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\output\\cb_2016_us_county_500k_center.shp,YCoord,-1,-1;FID_ \"FID_\" true true false 4 Long 0 0 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\output\\cb_2016_us_county_500k_center.shp,FID,-1,-1;INTPTLAT \"INTPTLAT\" true true false 8 Double 0 0 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\output\\cb_2016_us_county_500k_center.shp,INTPTLAT,-1,-1;INTPTLON \"INTPTLON\" true true false 8 Double 0 0 ,First,#,C:\\Users\\jkitmang\\Dropbox\\Research\\1. Researchers\\Marijuana and health\\00_Data\\CensusBureau\\shpfiles\\output\\cb_2016_us_county_500k_center.shp,INTPTLON,-1,-1", "INTERSECT", "", "")

# Process: Spatial Join
arcpy.SpatialJoin_analysis(Dispensaries_gis_shp, cb_2016_us_county_500k_wcenter_shp, Dispensaries_county_shp, "JOIN_ONE_TO_ONE", "KEEP_ALL", "", "INTERSECT", "", "")

# Process: Export Feature Attribute to ASCII
arcpy.ExportXYv_stats(Dispensaries_county_shp, "FID;Join_Count;TARGET_FID;place_id;lat;lon;STATEFP;COUNTYFP;GEOID;NAME;INTPTLAT;INTPTLON", "COMMA", Dispensaries_county_txt, "ADD_FIELD_NAMES")


import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_7/Exercise07"
sql1 = " \"FEATURE\" = 'Airport'"
sql2 = " \"FEATURE\" = 'Seaplane Base'"
arcpy.Select_analysis ("airports.shp", "Results/airports_final.shp",sql1)
arcpy.Select_analysis ("airports.shp", "Results/seaports.shp", sql2)
arcpy.Buffer_analysis("Results/airports_final.shp", "Results/aiports_buffers.shp", "15000 METERS")
arcpy.Buffer_analysis("Results/seaports.shp", "Results/seaports_buffers.shp", "7500 METERS")

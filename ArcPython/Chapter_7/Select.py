import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_7/Exercise07"
infc = "airports.shp"
outfc = "Results/airports_anchorage.shp"
delimitedfield = arcpy.AddFieldDelimiters(infc, "COUNTY")
arcpy.Select_analysis(infc, outfc, delimitedfield + " ='Anchorage Borough'")

import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_7/Exercise07"
fc = "airports.shp"
unique_name = arcpy.CreateUniqueName("Results/buffer.shp")
arcpy.Buffer_analysis(fc, unique_name, "5000 METERS")

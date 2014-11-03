import arcpy
from arcpy import env
env.overwriteOutput = True
env.workspace = "P:/py3200k/Homework/Exercise_6/Exercise06"
fieldlist = arcpy.ListFields("cities.shp")
for field in fieldlist:
    print field.name + " " + field.type

import arcpy
from arcpy import env
arcpy.env.workspace = "P:/py3200k/Homework/Exercise_5/Exercise05"
arcpy.AddXY_management("hospitals.shp")

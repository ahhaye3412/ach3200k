import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_7/Exercise07"
fc = "Results/airports.shp"
cursor = arcpy.da.InsertCursor(fc, "NAME")
cursor.insertRow(["New Airport"])
del cursor

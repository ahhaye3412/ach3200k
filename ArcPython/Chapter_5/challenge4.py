import arcpy
from arcpy import env
arcpy.env.workspace = "P:/py3200k/Homework/Exercise_5/Exercise05"
arcpy.CheckExtension("3D") == "Available"
arcpy.CheckExtension("Network") == "Available"
arcpy.CheckExtension("Spatial") == "Available"
print "The extensions are available"

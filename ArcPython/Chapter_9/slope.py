import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "P:/py3200k/Homework/Exercise_9/Exercise09"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    outraster = arcpy.sa.Slope("elevation", "PERCENT_RISE")
    outraster.save("slope_per")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."

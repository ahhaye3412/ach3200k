import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "P:/py3200k/Homework/Exercise_9/Exercise09"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    mynbr = NbrCircle(3, "CELL")
    outraster = FocalStatistics("landcover.tif", mynbr, "MAJORITY")
    outraster.save("lc_nbr")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."

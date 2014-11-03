import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise05/Exercise05"
if arcpy.CheckExtension("spatial") == "Available":
    arcpy.CheckOutExtension("spatial")
    out_distance = arcpy.sa.EucDistance("bike_routes.shp", cell_size = 100)
    out_distance.save("P:/py3200k/Homework/Exercise05/Exercise05/Results/bike_dist")
    arcpy.CheckInExtension("spatial")
else:
    print "Spatial Analyst license is not available."

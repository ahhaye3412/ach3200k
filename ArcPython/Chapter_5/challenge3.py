import arcpy
from arcpy import env
arcpy.env.workspace = "P:/py3200k/Homework/Exercise_5/Exercise05"
arcpy.Dissolve_management("parks.shp", "parks_dissolved.shp", "PARK_Type", "", "FALSE")

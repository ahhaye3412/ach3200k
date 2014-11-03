import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_8/Exercise08"
fc = "dams.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@XY"])
for row in cursor:
    x, y = row[0]
    print("{0}, {1}".format(x, y))

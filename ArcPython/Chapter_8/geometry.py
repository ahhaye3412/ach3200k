import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_8/Exercise08"
fc = "rivers.shp"
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"])
length = 0
for row in cursor:
    length = length + row[0]
units = arcpy.Describe(fc).spatialReference.linearUnitName
print str(length) + " " + units

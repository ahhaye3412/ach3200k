import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_7/Exercise07"
fc = "airports.shp"
delimitedField = arcpy.AddFieldDelimiters(fc, "COUNTY")
cursor = arcpy.da.SearchCursor(fc, ["NAME"], delimitedField + " ='Anchorage Borough'")
for row in cursor:
    print row[0]
del row
del cursor

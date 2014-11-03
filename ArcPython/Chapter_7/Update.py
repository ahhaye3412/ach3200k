import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_7/Exercise07"
fc = "Results/airports.shp"
delimfield = arcpy.AddFieldDelimiters(fc, "STATE")
cursor = arcpy.da.UpdateCursor(fc, ["STATE"], delimfield + " <> 'AK'")
for row in cursor:
    row[0] = "AK"
    cursor.updateRow(row)
del row
del cursor

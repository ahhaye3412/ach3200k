import arcpy
import list
arcpy.env.workspace = "P:/py3200k/Homework/Exercise_12/Exercise12"
fields = list.listfieldnames("streets.shp")
print fields

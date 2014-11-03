import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_6/Exercise06"
fclist = arcpy.ListFeatureClasses()
for fc in fclist:
    fcdescribe = arcpy.Describe(fc)
    print "Name: " + fcdescribe.name
    print "Data type: " + fcdescribe.dataType





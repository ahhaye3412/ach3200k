import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_6/Exercise06"
fc_list = arcpy.ListFeatureClasses()
for fc in fc_list:
    desc = arcpy.Describe(fc)
    print "{0} is a {1} feature class".format(desc.basename,desc.shapeType)

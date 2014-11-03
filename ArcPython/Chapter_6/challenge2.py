import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_6/Exercise06/study.mdb"
fc_list = arcpy.ListFeatureClasses()
arcpy.CreateFileGDB_management("P:/py3200k/Homework/Exercise_6/Exercise06", "newstudy.gdb")
for feature_class in fc_list:
    desc = arcpy.Describe(feature_class)
    type = desc.shapeType
    if type == "Polygon":
        arcpy.Copy_management (feature_class, "P:/py3200k/Homework/Exercise_6/Exercise06/newstudy.gdb/" + feature_class)

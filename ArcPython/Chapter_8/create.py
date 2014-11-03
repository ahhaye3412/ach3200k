import arcpy
import fileinput
import string
import os
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_8/Exercise08"
env.overwriteOutput = True
outpath = "P:/py3200k/Homework/Exercise_8/Exercise08"
newfc = "Results/newpolyline.shp"
arcpy.CreateFeatureclass_management(outpath, newfc, "Polyline")
infile = "P:/py3200k/Homework/Exercise_8/Exercise08/coordinates.txt"
cursor = arcpy.da.InsertCursor(newfc, ["SHAPE@"])
array = arcpy.Array()
for line in fileinput.input(infile):
    ID, X, Y = string.split(line," ")
    array.add(arcpy.Point(X, Y))
cursor.insertRow([arcpy.Polyline(array)])
fileinput.close()
del cursor

import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_8/Exercise08"
fc = "newpoly2.shp"
arcpy.CreateFeatureclass_management("P:/py3200k/Homework/Exercise_8/Exercise08", fc, "Polygon")
cursor = arcpy.da.InsertCursor(fc, ["SHAPE@"])
array = arcpy.Array()
coordlist =[[0, 0], [0, 1000], [1000, 1000], [1000, 0]]
for x, y in coordlist:
    point = arcpy.Point(x,y)
    array.append(point)
polygon = arcpy.Polygon(array)
cursor.insertRow([polygon])
del cursor

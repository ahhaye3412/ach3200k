import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_9/Exercise09"
rasterlist = arcpy.ListRasters()
for raster in rasterlist:
    print raster

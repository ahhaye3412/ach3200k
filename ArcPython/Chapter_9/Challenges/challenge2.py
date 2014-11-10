import arcpy
from arcpy import env
file_path = "P:/py3200k/Homework/Exercise_9/Exercise09"
env.workspace = file_path
rasterlist = arcpy.ListRasters()
arcpy.CreatePersonalGDB_management(file_path + "/Results", "newrastersfile.gdb")
for rasters in rasterlist:
    desc = arcpy.Describe(rasters)
    rname = desc.baseName
    outraster = file_path + "/Results/newrastersfile.gdb/" + rname
    

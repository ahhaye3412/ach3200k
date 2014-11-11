import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_10/Exercise10"
mxd = arcpy.mapping.MapDocument("P:/py3200k/Homework/Exercise_10/Exercise10/Austin_TX.mxd")
df = arcpy.mapping.ListDataFrames(mxd, "Parks")[0]
lyr = arcpy.mapping.ListLayers(mxd, "parks", df)[0]
dflist = arcpy.mapping.ListDataFrames(mxd)
for dframe in dflist:
    if dframe.name <> "Parks":
        arcpy.mapping.AddLayer(dframe, lyr)
mxd.save()
del mxd

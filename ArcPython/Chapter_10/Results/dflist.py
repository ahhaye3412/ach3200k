import arcpy
mxd = "P:/py3200k/Homework/Exercise_10/Exercise10/Austin_TX.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
listdf = arcpy.mapping.ListDataFrames(mapdoc)
for df in listdf:
    print df.name
del mapdoc
del listdf

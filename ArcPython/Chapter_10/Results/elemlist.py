import arcpy
mxd = "P:/py3200k/Homework/Exercise_10/Exercise10/Georgia.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
for elem in elemlist:
    print elem.name + " " + elem.type
del mapdoc

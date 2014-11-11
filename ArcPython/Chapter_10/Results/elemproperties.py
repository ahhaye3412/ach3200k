import arcpy
mxd = "P:/py3200k/Homework/Exercise_10/Exercise10/Georgia.mxd"
mapdoc = arcpy.mapping.MapDocument(mxd)
elemlist = arcpy.mapping.ListLayoutElements(mapdoc)
title = elemlist[0]
title.text = "Housing Vacancy for Georgia Counties (2000)"
mapdoc.save()
del mapdoc

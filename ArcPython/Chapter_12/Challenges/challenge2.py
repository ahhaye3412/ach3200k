import arcpy
import parcelclass
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise_12/Exercise12"
fc = "parcels.shp"
cursor = arcpy.da.SearchCursor(fc, ["FID", "Landuse", "Value"])
for row in cursor:
    myparcel = parcelclass.Parcel(row[1], row[2])
    mytax = myparcel.assessment()
    print "{0}: {1}".format(row[0], mytax)

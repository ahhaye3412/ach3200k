import arcpy
from arcpy import env
env.workspace = "P:/py3200k/Homework/Exercise05/Exercise05"
in_features = "parks.shp"
out_featureclass = "Results/parks_centroid.shp"
if arcpy.ProductInfo() == "ArcInfo":
    arcpy.FeatureToPoint_management(in_features, out_featureclass)
else:
    print "An ArcInfo license is not available."

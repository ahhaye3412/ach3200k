import arcpy
from arcpy import env
from arcpy.sa import *
env.workspace = "P:/py3200k/Homework/Exercise_9/Exercise09"
if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")
elev = arcpy.Raster("elevation")
lc = arcpy.Raster("landcover.tif")
slope = Slope(elev)
aspect = Aspect(elev)
mod_slope = ((slope > 5) & (slope < 20))
south_aspect = ((aspect > 150) & (aspect < 270))
forest = ((lc == 41) | (lc == 42) | (lc ==43))
outraster = (mod_slope & south_aspect & forest)
outraster.save("P:/py3200k/Homework/Exercise_9/Exercise09/Results/final")
arcpy.CheckInExtension("Spatial")

import arcpy
import os
def countstringfields(table):
    fields = arcpy.ListFields(table)
    x = 0
    for field in fields:
        if field.type == "String":
            x += 1
    return x

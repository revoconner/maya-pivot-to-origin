import maya.cmds as cmds
import maya.mel as mm

# Get the current selection
selection = cmds.ls(selection=True)

mm.eval("FreezeTransformations;")

# Iterate over the selection
for s in selection:
    # Move the pivot to the origin
    cmds.xform(s, pivots=(0, 0, 0))

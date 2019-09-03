import bpy
from bpy.props import *

class PandasNodeTree(bpy.types.NodeTree):
    bl_idname = "pn_PandasNodeTree"
    bl_label = "Pandas Nodes"
    bl_icon = "CON_SAMEVOL"

register_class = [PandasNodeTree]
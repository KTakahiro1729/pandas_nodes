import bpy
from bpy.props import *
from .node_template import TemplateNode

class AddNode(TemplateNode):
    bl_idname = "pn_AddNode"
    bl_label = "Add"
    menu_text = "Add"
    input_nodes = [("NodeSocketFloat", "x"), ("NodeSocketFloat", "y")] 
    output_nodes = [("NodeSocketFloat", "x + y")]
    def code_template(self):
        return "{inp[0]}+{inp[1]},"


register_class = [AddNode]
import bpy
from bpy.props import *
from .node_template import TemplateNode
from .. utils import node_utils as nu

class AddNode(TemplateNode):
    bl_idname = "pn_AddNode"
    bl_label = "Add"
    menu_text = "Add"
    input_nodes = [("NodeSocketFloat", "in1"), ("NodeSocketFloat", "in2")] 
    output_nodes = [("NodeSocketFloat", "in1 + in2")]
    input_count : nu.input_count(2)
    add_input_nodes = True
    def code_template(self):
        return "{inp[0]}+{inp[1]},"


register_class = [AddNode]
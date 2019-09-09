import bpy
from bpy.props import *
from .node_template import TemplateNode
from .. utils import node_utils as nu

class GetAttrNode(TemplateNode):
    bl_idname = "pn_GetAttrNode"
    bl_label = "Get Attribute"
    menu_text = "Get Attribute"
    input_nodes = [("NodeSocketInt", "list"), ("NodeSocketString", "name")] 
    output_nodes = [("NodeSocketInt", "attr")]
    def code_template(self):
        return nu.code_left + "getattr({inp[0]},{inp[1]}),"

register_class = [GetAttrNode]
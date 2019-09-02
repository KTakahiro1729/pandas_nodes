import bpy
from bpy.props import *
from .node_template import TemplateNode

class PrintNode(TemplateNode):
    bl_idname = "pn_PrintNode"
    bl_label = "Print"
    menu_text = "Print"
    input_nodes = [("NodeSocketFloat", "x")]
    def code_template(self):
        return "print({inp[0]}),"


register_class = [PrintNode]
output_nodes = [PrintNode]

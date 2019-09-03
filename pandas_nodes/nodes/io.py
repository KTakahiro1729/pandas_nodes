import bpy
from bpy.props import *
from .node_template import TemplateNode
from .. utils import node_utils as nu


class PrintNode(TemplateNode):
    bl_idname = "pn_PrintNode"
    bl_label = "Print"
    menu_text = "Print"
    input_nodes = [("NodeSocketFloat", "in1")]
    input_count : nu.input_count(1)
    add_input_nodes = True
    def code_template(self):
        return "print({inp[0]}),"


register_class = [PrintNode]
display_nodes = [node.bl_idname for node in [PrintNode]]

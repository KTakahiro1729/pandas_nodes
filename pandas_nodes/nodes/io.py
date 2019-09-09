import bpy
from bpy.props import *
from .node_template import TemplateNode, DynamicInputsTemplateNode
from .. utils import node_utils as nu


class PrintNode(DynamicInputsTemplateNode):
    bl_idname = "pn_PrintNode"
    bl_label = "Print"
    menu_text = "Print"
    input_nodes = [("NodeSocketFloat", "in0")]
    input_count : nu.input_count(1)
    def code_template(self):
        return "print("+nu.starexpr_list_template(len(self.inputs))+"),"

class ImportModuleNode(TemplateNode):
    bl_idname = "pn_ImportModuleNode"
    bl_label = "Import Module"
    menu_text = "Import Module"
    module : StringProperty(default = "pandas")
    output_nodes = [("NodeSocketInt", "module")]
    def run_first(self):
        return [f"import {self.module}"]
    def code_template(self):
        if nu.any_output(self):
            return nu.code_left + f"__import__('{self.module}'),"
        return []
    def draw_buttons(self, context, layout):
        layout.prop(self, "module", text = "module")

register_class = [PrintNode, ImportModuleNode]
display_nodes = [node.bl_idname for node in [PrintNode]]
run_fist_class = [node.bl_idname for node in [ImportModuleNode]]

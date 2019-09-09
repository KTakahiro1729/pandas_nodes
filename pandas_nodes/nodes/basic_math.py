import bpy
from bpy.props import *
from .node_template import TemplateNode, DynamicInputsTemplateNode
from .. utils import node_utils as nu

class AddNode(DynamicInputsTemplateNode):
    bl_idname = "pn_AddNode"
    bl_label = "Add"
    menu_text = "Add"
    input_nodes = [("NodeSocketFloat", "in1"), ("NodeSocketFloat", "in2")] 
    output_nodes = [("NodeSocketFloat", "in1+in2+...")]
    input_count : nu.input_count(2)
    def code_template(self):
        return nu.code_left + " + ".join(nu.unpack_list_template(len(self.inputs))) + ","


class ExpressionNode(DynamicInputsTemplateNode):
    bl_idname = "pn_ExpressionNode"
    bl_label = "Expression"
    menu_text = "Expression"
    input_nodes = [("NodeSocketFloat", "in0"), ("NodeSocketFloat", "in1")] 
    output_nodes = [("NodeSocketFloat", "result")]
    input_count : nu.input_count(2)
    expression : StringProperty(default="in0+in1")
    def code_template(self):
        result = self.equation
        for i, inp in enumerate(self.inputs):
            result = result.replace(inp.name, "{inp["+str(i)+"]}")
        return nu.code_left + result + ","
    def draw_buttons(self, context, layout):
        super().draw_buttons(context, layout)
        layout.prop(self, "expression", text="result")

register_class = [AddNode, ExpressionNode]
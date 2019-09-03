import bpy
from bpy.props import *
from .node_template import TemplateNode
from .. utils import node_utils as nu

class ValueInputTemplateNode(TemplateNode):
    input_count = nu.input_count(1)
    def code_template(self):
        return self.cast_type + "({inp[0]}),"

class IntegerInputNode(ValueInputTemplateNode):
    bl_idname = "pn_IntInputNode"
    bl_label = "Integer"
    menu_text = "Integer"
    input_nodes = [("NodeSocketInt", "value")] 
    output_nodes = [("NodeSocketInt", "int")]
    cast_type = "int"


class FloatInputNode(ValueInputTemplateNode):
    bl_idname = "pn_FloatInputNode"
    bl_label = "Float"
    menu_text = "Float"
    input_nodes = [("NodeSocketFloat", "value")] 
    output_nodes = [("NodeSocketFloat", "float")]
    cast_type = "float"

class StringInputNode(ValueInputTemplateNode):
    bl_idname = "pn_StringInputNode"
    bl_label = "String"
    menu_text = "String"
    input_nodes = [("NodeSocketString", "value")] 
    output_nodes = [("NodeSocketString", "str")]
    cast_type = "str"


register_class = [IntegerInputNode, FloatInputNode, StringInputNode]
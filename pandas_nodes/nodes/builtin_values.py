import bpy
from bpy.props import *
from .node_template import TemplateNode, DynamicInputsTemplateNode
from .. utils import node_utils as nu
# from .. utils.ops_utils import var_name_from_child_tuple as v_from_ct

class ValueInputTemplateNode(TemplateNode):
    def code_template(self):
        return nu.code_left + self.cast_type + "({inp[0]}),"

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

class ListInputNode(DynamicInputsTemplateNode):
    bl_idname = "pn_ListInputNode"
    bl_label = "List"
    menu_text = "List"
    input_count : nu.input_count(2, name_template= "list[{count}]")
    input_nodes = [("NodeSocketFloat", "list[0]"),("NodeSocketFloat", "list[1]")] 
    output_nodes = [("NodeSocketList", "list")]
    def draw_buttons(self, context, layout):
        layout.prop(self, "input_count", text = "len")
    def code_template(self):
        return nu.code_left + "["+nu.starexpr_list_template(len(self.inputs))+"],"

class DictInputNode(DynamicInputsTemplateNode):
    bl_idname = "pn_DictInputNode"
    bl_label = "Dict"
    menu_text = "Dict"
    input_count : nu.input_count(2, sock_type = "NodeSocketDictElementd", name_template = "in{count}")
    input_nodes = [("NodeSocketDictElement", "dict[0]"),("NodeSocketDictElement", "dict[1]")] 
    output_nodes = [("NodeSocketDict", "dict")]
    def draw_buttons(self, context, layout):
        layout.prop(self, "input_count", text = "len")
    def code_template(self):
        result = "{{"
        for i, inp in enumerate(self.inputs):
            if inp.is_linked:
                result += "{" + f"inp[{i}]" + "}[0] : {" + f"inp[{i}]" + "}[1], "
            else:
                result += "{" + f"inp[{i}][0]" + "} : {" + f"inp[{i}][1]" + "}, "
        return nu.code_left + result + "}},"

class ListIndexNode(TemplateNode):
    bl_idname = "pn_ListIndexNode"
    bl_label = "List Index"
    menu_text = "List Index"
    input_nodes = [("NodeSocketList", "list"), ("NodeSocketInt", "index")] 
    output_nodes = [("NodeSocketInt", "value")]
    def code_template(self):
        return nu.code_left + "{inp[0]}[{inp[1]}],"

class DictIndexNode(TemplateNode):
    bl_idname = "pn_DictIndexNode"
    bl_label = "Dict Index"
    menu_text = "Dict Index"
    input_nodes = [("NodeSocketDict", "dict"), ("NodeSocketString", "key")] 
    output_nodes = [("NodeSocketInt", "value")]
    def code_template(self):
        return nu.code_left + "{inp[0]}[{inp[1]}],"

class ToListNode(ValueInputTemplateNode):
    bl_idname = "pn_ToListNode"
    bl_label = "To List"
    menu_text = "To List"
    input_nodes = [("NodeSocketList", "value")] 
    output_nodes = [("NodeSocketList", "list")]
    cast_type = "list"

class ToDictNode(ValueInputTemplateNode):
    bl_idname = "pn_ToDictNode"
    bl_label = "To Dict"
    menu_text = "To Dict"
    input_nodes = [("NodeSocketDict", "value")] 
    output_nodes = [("NodeSocketDict", "dict")]
    cast_type = "dict"

register_class = [
    IntegerInputNode, FloatInputNode, StringInputNode, 
    ListInputNode, DictInputNode,
    ListIndexNode, DictIndexNode,
    ToListNode, ToDictNode,
    ]
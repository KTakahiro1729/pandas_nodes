import bpy
from bpy.props import *
from .. utils import node_utils as nu

class TemplateNode(bpy.types.Node):
    bl_idname : str
    bl_label : str
    menu_text : str

    # [(SocketType : str , SocketName : str), ...]
    input_nodes = [] 
    output_nodes = []
    def init(self, context):
        for s_type, s_name in self.input_nodes:
            self.inputs.new(s_type, s_name)
        for s_type, s_name in self.output_nodes:
            self.outputs.new(s_type, s_name)
    def code_template(self):
        raise NotImplemented(f"Code Generation for {type(self)} is not implemented. Contact developer")

class DynamicInputsTemplateNode(TemplateNode):
    input_count = nu.input_count(0)
    def draw_buttons(self, context, layout):
        layout.prop(self, "input_count", text = "input size")
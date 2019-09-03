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
    add_input_nodes = False
    input_count = nu.input_count(0)
    def init(self, context):
        for s_type, s_name in self.input_nodes:
            self.inputs.new(s_type, s_name)
        for s_type, s_name in self.output_nodes:
            self.outputs.new(s_type, s_name)
    def draw_buttons(self, context, layout):
        if self.add_input_nodes:
            layout.prop(self, "input_count")
    def code_template(self):
        raise NotImplemented(f"Code Generation for {type(self)} is not implemented. Contact developer")

    
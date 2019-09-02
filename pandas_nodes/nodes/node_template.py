import bpy
from bpy.props import *
from .. utils import ops_utils

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
        raise NotImplementedError(f"Code Generation for {type(self)} is not implemented. Contact developer")
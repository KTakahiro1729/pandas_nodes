import bpy
from bpy.props import *
from bpy.types import NodeTree, Node, NodeSocket


class ListSocket(NodeSocket):
    bl_idname = 'NodeSocketList'
    bl_label = "List"

    eval : StringProperty(default="[0,1]")

    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "eval", text="list")
    def draw_color(self, context, node):
        return (0.1, 0.1, 0.2, 1)

class DictSocket(NodeSocket):
    bl_idname = 'NodeSocketDict'
    bl_label = "Dict"

    eval : StringProperty(default="{'key' : 'value'}")

    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "eval", text="dict")
    def draw_color(self, context, node):
        return (0.1, 0.1, 0.2, 1)

class NamedFloatSocket(NodeSocket):
    bl_idname = 'NamedFloatSocket'
    bl_label = "Named Float"

    name : StringProperty(default="in0")
    value : FloatProperty(default=0)
    default_props = ["name", "value"]

    def draw(self, context, layout, node, text):
        if self.is_output:
            layout.label(text=text)
        if self.is_linked:
            layout.label(text=text)
            layout.prop(self, "name", text = "name")
        else:
            layout.prop(self, "name", text = "name")
            layout.prop(self, "value", text="value")
    def draw_color(self, context, node):
        return (0.1, 0.1, 0.2, 1)

# def change_default_dict(self, context):
#     self.default_value = f"{self.key} : {self.value}"

class DictElementSocket(NodeSocket):
    bl_idname = 'NodeSocketDictElement'
    bl_label = "Dict Element"

    key : StringProperty(default="'key'")#, update=change_default_dict)
    value : StringProperty(default="'value'")#, update=change_default_dict)
    default_props = ["key", "value"]
    
    # default_value : StringProperty(default="'key' : 'value'")
    # default_is_raw : BoolProperty(default=True)
    def draw(self, context, layout, node, text):
        if self.is_output or self.is_linked:
            layout.label(text=text)
        else:
            layout.prop(self, "key", text="")
            layout.prop(self, "value", text=" ")
    def draw_color(self, context, node):
        return (0.1, 0.1, 0.25, 1)


register_class = [ListSocket, DictSocket, NamedFloatSocket, DictElementSocket, ]
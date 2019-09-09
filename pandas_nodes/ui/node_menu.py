import bpy
from bpy.props import *
from .. import nodes

def drawMenu(self, context):
    if context.space_data.tree_type != "pn_PandasNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    # layout.operator("pn.node_search", text = "Search", icon = "VIEWZOOM")
    layout.separator()
    for menu in inner_menues:
        layout.menu(menu.bl_idname, text = menu.text, icon = menu.icon)

def insertNode(layout, id_name, text, settings = {}, icon = "NONE"):
    operator = layout.operator("node.add_node", text = text, icon = icon)
    operator.type = id_name
    operator.use_transform = True
    for name, value in settings.items():
        item = operator.settings.add()
        item.name = name
        item.value = value
    return operator

class MenuTemplate(bpy.types.Menu):
    bl_idname : str
    bl_label : str
    text : str
    icon = "NONE"
    register_nodes : list

    def draw(self, context):
        layout = self.layout
        for reg_node in self.register_nodes:
            insertNode(layout, reg_node.bl_idname, reg_node.menu_text)

class PN_MT_builtin_values_menu(MenuTemplate):
    bl_idname = "PN_MT_builtin_values_menu"
    bl_label = "Builtin Values Menu"
    text = "Builtin Values"
    icon = "LINENUMBERS_ON"
    register_nodes = nodes.builtin_values.register_class

class PN_MT_basic_math_menu(MenuTemplate):
    bl_idname = "PN_MT_basic_math_menu"
    bl_label = "Basic Maths Menu"
    text = "Basic Maths"
    icon = "LINENUMBERS_ON"
    register_nodes = nodes.basic_math.register_class

class PN_MT_io_menu(MenuTemplate):
    bl_idname = "PN_MT_io_menu"
    bl_label = "Input/Output Menu"
    text = "Input/Output"
    icon = "LINENUMBERS_ON"
    register_nodes = nodes.io.register_class

class PN_MT_builtin_func_menu(MenuTemplate):
    bl_idname = "PN_MT_builtin_func_menu"
    bl_label = "Builtin Functions Menu"
    text = "Builtin Functions"
    icon = "LINENUMBERS_ON"
    register_nodes = nodes.buitlin_func.register_class

inner_menues = [PN_MT_builtin_values_menu, PN_MT_basic_math_menu, PN_MT_io_menu, PN_MT_builtin_func_menu]
register_class = inner_menues

def register():
    bpy.types.NODE_MT_add.append(drawMenu)

def unregister():
    bpy.types.NODE_MT_add.remove(drawMenu)
import bpy

from . import node_tree, node_menu, n_panel
from .. utils import register_utils

modules = [node_tree, node_menu, n_panel]

register_class = register_utils.join_register_class(modules)

def register():
    # bpy.types.NODE_MT_add.append(node_menu.drawMenu)
    node_menu.register()

def unregister():
    # bpy.types.NODE_MT_add.remove(node_menu.drawMenu)
    node_menu.unregister()
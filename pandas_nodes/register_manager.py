from . import ui, nodes, operator, sockets
modules = [ui, nodes, operator, sockets]


import bpy
def register_all():
    for module in modules:
        for cls in module.register_class:
            bpy.utils.register_class(cls)
        if hasattr(module, "register"):
            module.register()
    

def unregister_all():
    for module in modules:
        for cls in module.register_class:
            bpy.utils.unregister_class(cls)
        if hasattr(module, "unregister"):
            module.unregister()






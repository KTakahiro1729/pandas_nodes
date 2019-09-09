bl_info = {
    "name":        "Pandas Nodes",
    "description": "Node based data analysis module based on pandas.",
    "author":      "Allosteric",
    "version":     (0, 1, 0),
    "blender":     (2, 80, 0),
    # "location":    "Animation Nodes Editor",
    "category":    "Node",
    # "warning":     "This version is still in dZevelopment."
}



from . import register_manager

def register():
    register_manager.register_all()

def unregister():
    register_manager.unregister_all()
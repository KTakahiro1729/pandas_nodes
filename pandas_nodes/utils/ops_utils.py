import bpy
from .. import nodes as nodes_mod

def get_tree():
    return bpy.context.space_data.edit_tree



    print(self.inputs.new("NodeSocketFloat", "x"))
# get nodes that display outputs
def get_display_nodes(tree):
    return [node for node in tree.nodes if node.bl_idname in nodes_mod.display_nodes]

# add text
def add_text_datablock(name, text, overwrite = True):
    if overwrite and name in bpy.data.texts:
        datablock = bpy.data.texts[name]
    else:
        datablock = bpy.data.texts.new(name)
    datablock.from_string(text)
    return datablock



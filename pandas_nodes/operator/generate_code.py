import bpy
from .. utils import ops_utils as ou

class GenerateCodeFromPandasNodeTree(bpy.types.Operator):
    bl_idname = "pandas_nodes.code_from_pntree"
    bl_label = "Generate code from Pandas Node Tree"
    bl_description = "Generate code from Pandas Node Tree"
    def execute(self, context):
        tree = ou.get_tree()
        run_first_class = ou.get_run_first_class(tree)
        parent_nodes = ou.get_display_nodes(tree)
        code = "\n".join(ou.node_tree_to_code(run_first_class, parent_nodes))
        ou.add_text_datablock(tree.name, code)
        return {'FINISHED'}

register_class = [GenerateCodeFromPandasNodeTree]
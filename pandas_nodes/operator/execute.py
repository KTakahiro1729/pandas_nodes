import bpy
from .. utils import ops_utils

class ExecutePandasNodeTree(bpy.types.Operator):
    bl_idname = "pandas_nodes.execute_pntree"
    bl_label = "Execute Pandas Node Tree"
    bl_description = "Execute Pandas Node Tree"
    def execute(self, context):
        tree = ops_utils.getTree()
        print(tree)
        print(dir(tree))
        return {'FINISHED'}

register_class = [ExecutePandasNodeTree]
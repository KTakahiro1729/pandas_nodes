import bpy
from .. utils import ops_utils

class PN_PT_develpment(bpy.types.Panel):
    bl_idname = "PN_PT_develpment"
    bl_label = "Development Panel"
    bl_space_type = "NODE_EDITOR"
    bl_region_type = "UI"
    bl_category = "Display"

    @classmethod
    def poll(cls, context):
        tree = ops_utils.get_tree()
        if tree is None: return False
        return tree.bl_idname == "pn_PandasNodeTree"
    def draw(self, context):
        layout = self.layout
        col = layout.column(align=True)
        col.operator("pandas_nodes.execute_pntree", text="Execute Node Tree")
register_class = [PN_PT_develpment]

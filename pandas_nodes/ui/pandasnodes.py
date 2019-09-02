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

import bpy

class PandasNodeTree(bpy.types.NodeTree):
    bl_idname = "pn_PandasNodeTree"
    bl_label = "Pandas Nodes"
    bl_icon = "ONIONSKIN_ON"

def drawMenu(self, context):
    if context.space_data.tree_type != "an_AnimationNodeTree": return

    layout = self.layout
    layout.operator_context = "INVOKE_DEFAULT"

    if drawNodeTreeChooser(layout, context):
        return

    layout.operator("an.node_search", text = "Search", icon = "VIEWZOOM")
    layout.separator()
    layout.menu("AN_MT_number_menu", text = "Number", icon = "LINENUMBERS_ON")
    layout.menu("AN_MT_vector_menu", text = "Vector", icon = "EXPORT")
    layout.menu("AN_MT_rotation_menu", text = "Rotation", icon = "FILE_REFRESH")
    layout.menu("AN_MT_matrix_menu", text = "Matrix", icon = "GRID")
    layout.menu("AN_MT_text_menu", text = "Text", icon = "SORTALPHA")
    layout.menu("AN_MT_boolean_menu", text = "Boolean", icon = "CHECKBOX_HLT")
    layout.menu("AN_MT_color_menu", text = "Color", icon = "COLOR")
    layout.menu("AN_MT_list_menu", text = "List", icon = "WORDWRAP_ON")
    layout.separator()
    layout.menu("AN_MT_object_menu", text = "Object", icon = "OBJECT_DATAMODE")
    layout.menu("AN_MT_mesh_menu", text = "Mesh", icon = "MESH_DATA")
    layout.menu("AN_MT_spline_menu", text = "Spline", icon = "CURVE_DATA")
    layout.menu("AN_MT_particle_system_menu", text = "Particle System", icon = "PARTICLE_DATA")
    layout.separator()
    layout.menu("AN_MT_animation_menu", text = "Animation", icon = "RENDER_ANIMATION")
    layout.menu("AN_MT_interpolation_menu", text = "Interpolation", icon = "IPO_BEZIER")
    layout.menu("AN_MT_falloff_menu", text = "Falloff", icon = "SMOOTHCURVE")
    layout.menu("AN_MT_action_menu", text = "Action", icon = "ANIM_DATA")
    layout.menu("AN_MT_fcurve_menu", text = "FCurves", icon = "FCURVE")
    layout.menu("AN_MT_material_menu", text = "Material", icon = "NODE_MATERIAL")
    layout.menu("AN_MT_sound_menu", text = "Sound", icon = "SPEAKER")
    layout.menu("AN_MT_sequence_menu", text = "Sequence", icon = "SEQUENCE")
    layout.separator()
    layout.menu("AN_MT_geometry_menu", text = "Geometry", icon = "ORIENTATION_NORMAL")
    layout.menu("AN_MT_kdtree_bvhtree_menu", text = "KD & BVH Tree", icon = "STICKY_UVS_LOC")
    layout.separator()
    layout.menu("AN_MT_viewer_menu", text = "Viewer", icon = "INFO")
    layout.menu("AN_MT_subprograms_menu", text = "Subprograms", icon = "FILE_SCRIPT")
    layout.menu("AN_MT_layout_menu", text = "Layout", icon = "IMGDISPLAY")

def drawNodeTreeChooser(layout, context):
    if len(getAnimationNodeTrees()) == 0:
        col = layout.column()
        col.scale_y = 1.6
        col.operator("an.create_node_tree", text = "New Node Tree", icon = "PLUS")
        return True
    return False



def register():
    bpy.utils.register_class(PandasNodeTree)


def unregister():
    bpy.utils.unregister_class(PandasNodeTree)
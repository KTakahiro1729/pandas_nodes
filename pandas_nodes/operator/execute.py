import bpy
from .. utils import ops_utils as ou

class ExecutePandasNodeTree(bpy.types.Operator):
    bl_idname = "pandas_nodes.execute_pntree"
    bl_label = "Execute Pandas Node Tree"
    bl_description = "Execute Pandas Node Tree"
    def execute(self, context):
        tree = ou.get_tree()
        parent_nodes = ou.get_display_nodes(tree)
        code = "\n".join(node_tree_to_code(parent_nodes))
        ou.add_text_datablock(tree.name, code)
        return {'FINISHED'}

# generating code from nodetree
def node_tree_to_code(parent_nodes):
    result = ["ns = dict([])"]
    for node_tuple in walk_input_trees(parent_nodes, True):
        result.append(node_to_code(node_tuple))
    return result

## walk nodetree from the given nodes
def walk_input_trees(parent_nodes, rev_pol = False):
    def _walk_input_tree(parent_node, rev_pol = False):
        cur_node = parent_node
        child_nodes = get_input_nodes(cur_node)
        if not rev_pol:
            walked_node.add(cur_node.name)
            yield cur_node, child_nodes
        for child_socket, val_type in child_nodes:
            if val_type == "Value":
                continue
            if child_socket.node.name in walked_node:
                continue
            for result in _walk_input_tree(child_socket.node, rev_pol):
                yield result
        if rev_pol:
            walked_node.add(cur_node.name) 
            yield cur_node, child_nodes
    walked_node = set()
    for parent_node in parent_nodes:
        for node_tuple in _walk_input_tree(parent_node, rev_pol):
            yield node_tuple

def get_input_nodes(node):
    result = []
    for in_soc in node.inputs:
        links = in_soc.links
        if in_soc.links and links[0].is_valid:
            val = (links[0].from_socket, "Node")
        else:
            val = (in_soc.default_value, "Value")
        result.append(val)
    return result

## generate code from node and its inputs
def node_to_code(node_tuple):
    cur_node, child_nodes = node_tuple
    code_template = cur_node.code_template()
    inp = list(map(var_name_from_child_tuple, child_nodes))
    left = f"ns['{cur_node.name}']"
    right =  code_template.format(inp=inp)
    return f"{left} = {right}"

def var_name_from_child_tuple(child_tuple):
    sock_object, node_type = child_tuple
    if node_type == "Node":
        name = sock_object.node.name
        sock_idx = get_socket_idx(sock_object)
        return f"ns['{name}'][{sock_idx}]" 
    elif node_type == "Value":
        if type(sock_object) == int:
            return f"{sock_object}"
        if type(sock_object) == float:
            return f"{sock_object:.10e}"
        if type(sock_object) == str:
            return f"'{sock_object}'"

def get_socket_idx(socket):
    return int(repr(socket)[:-1].split("[")[-1])

register_class = [ExecutePandasNodeTree]
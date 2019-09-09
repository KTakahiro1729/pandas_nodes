import bpy
from .. import nodes as nodes_mod
from collections import namedtuple

ParsedNode = namedtuple("ParsedNode", ["value", "val_type"])

def get_tree():
    return bpy.context.space_data.edit_tree

# generating code from nodetree
def node_tree_to_code(run_first_class, parent_nodes):
    result = []
    for cls in run_first_class:
        code = cls.run_first()
        result += list([c for c in code if c not in result])
    result.append("ns = dict([])")
    for node_tuple in walk_input_trees(parent_nodes, True):
        code = node_to_code(node_tuple)
        if type(code) == str:
            result.append(code)
        elif type(cod) == list:
            result += code
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
            if val_type in ["Value", "Raw"]:
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
        elif hasattr(in_soc,"default_value"):
            val = (in_soc.default_value, "Value")
        else:
            val = ([getattr(in_soc,prop) for prop in in_soc.default_props], "Raw")
        result.append(val)
    return result

## generate code from node and its inputs
def node_to_code(node_tuple):
    cur_node, child_nodes = node_tuple
    code_template = cur_node.code_template()
    inp = list(map(var_name_from_child_tuple, child_nodes))
    var = f"ns['{cur_node.name}']"
    result =  code_template.format(var=var, inp=inp)
    return result

def var_name_from_child_tuple(child_tuple):
    sock_object, node_type = child_tuple
    if node_type == "Node":
        name = sock_object.node.name
        sock_idx = get_socket_idx(sock_object)
        return f"ns['{name}'][{sock_idx}]"
    elif node_type == "Raw":
        return sock_object
    elif node_type == "Value":
        if type(sock_object) == int:
            return f"{sock_object}"
        if type(sock_object) == float:
            return f"{sock_object:.10e}"
        if type(sock_object) == str:
            return f"'{sock_object}'"



def get_socket_idx(socket):
    return int(repr(socket)[:-1].split("[")[-1])

# get nodes that display outputs
def get_display_nodes(tree):
    return [node for node in tree.nodes if node.bl_idname in nodes_mod.display_nodes]


# get classes that needs to run run_first method
def get_run_first_class(tree):
    return [node for node in tree.nodes if node.bl_idname in nodes_mod.run_first_class]

# add text
def add_text_datablock(name, text, overwrite = True):
    if overwrite and name in bpy.data.texts:
        datablock = bpy.data.texts[name]
    else:
        datablock = bpy.data.texts.new(name)
    datablock.from_string(text)
    return datablock



import bpy

# increase and decrease inputs so that len(self.inputs) == self.input_count
def change_input_count(self, context, sock_type, name_template):
    old_count = len(self.inputs)
    new_count = self.input_count
    if old_count == new_count:
        return
    if old_count < new_count:
        for count in range(old_count, new_count):
            self.inputs.new(sock_type, name_template.format(count=count))
    if new_count < old_count:
        for _ in range(new_count, old_count):
            last_sock = list(self.inputs)[-1]
            self.inputs.remove(last_sock)
def input_count(default, sock_type = "NodeSocketFloat", name_template = "in{count}",**kwargs):
    return bpy.props.IntProperty(
        default = default,
        update = lambda s,c: change_input_count(s,c,sock_type, name_template),**kwargs)

def unpack_list_template(size):
    return ["{inp["+str(i)+"]}" for i in range(size)]
def starexpr_list_template(size):
    return ", ".join(unpack_list_template(size))
def any_output(node):
    for out in node.outputs:
        if out.is_linked:
            return True
    return False


code_left = "{var} = "
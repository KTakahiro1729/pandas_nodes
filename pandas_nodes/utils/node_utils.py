import bpy

# increase and decrease inputs so that len(self.inputs) == self.input_count
def change_input_count(self, context, sock_type, name_template):
    old_count = len(self.inputs)
    new_count = self.input_count
    if old_count == new_count:
        return
    if old_count < new_count:
        for count in range(old_count+1, new_count+1):
            self.inputs.new(sock_type, name_template.format(count=count))
    if new_count < old_count:
        for _ in range(new_count, old_count):
            last_sock = list(self.inputs)[-1]
            self.inputs.remove(last_sock)
def input_count(default, sock_type = "NodeSocketFloat", name_template = "in{count}"):
    return bpy.props.IntProperty(
        default = default, 
        update = lambda s,c: change_input_count(s,c,sock_type, name_template))
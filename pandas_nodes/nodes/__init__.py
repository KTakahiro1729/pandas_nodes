from . import builtin_values, basic_math, io, buitlin_func
from .. utils import register_utils

modules = [builtin_values, basic_math, io, buitlin_func]

register_class = register_utils.join_register_class(modules)
display_nodes = io.display_nodes
run_first_class = io.run_fist_class
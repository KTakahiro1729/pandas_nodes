from . import builtin_values, basic_math, io
from .. utils import register_utils

modules = [builtin_values, basic_math, io]

register_class = register_utils.join_register_class(modules)
display_nodes = io.display_nodes
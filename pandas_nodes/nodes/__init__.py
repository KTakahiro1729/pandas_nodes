from . import builtin_values, basic_math, io
from .. utils import register_utils

modules = [builtin_values, basic_math, io]

register_class = register_utils.join_register_class(modules)
output_nodes = io.output_nodes
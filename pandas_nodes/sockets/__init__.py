from . import buitlin_types
from .. utils import register_utils

modules = [buitlin_types]

register_class = register_utils.join_register_class(modules)
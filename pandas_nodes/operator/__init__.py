import bpy

from . import execute
from .. utils import register_utils

modules = [execute]

register_class = register_utils.join_register_class(modules)

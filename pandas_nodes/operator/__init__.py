import bpy

from . import generate_code
from .. utils import register_utils

modules = [generate_code]

register_class = register_utils.join_register_class(modules)

def join_register_class(modules):
    return sum([module.register_class for module in modules], [])
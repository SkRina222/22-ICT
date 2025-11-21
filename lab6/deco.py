_readonly_funcs = {}

def readonly(func):
    name = func.__name__
    if name not in _readonly_funcs:
        _readonly_funcs[name] = func
    return _readonly_funcs[name]

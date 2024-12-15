import inspect


def introspection_info(obj):
    info = {
        'attributes': dir(obj),
        'type': type(obj),
        'methods': [met for met in dir(obj) if callable(getattr(obj, met))],
        'module': obj.__module__ if hasattr(obj, '__module__') else None
    }

    return info

def sum_(x, y):
    return x+y


number_info = introspection_info(sum_)
print(number_info)

def curry(function):
    arity = len(function)

    def _curry(*args):
        if len(args) < arity:
            return _curry(args)
        
        return function(*args)

def add(x):
    add_other = lambda y: x + y
    return add_other

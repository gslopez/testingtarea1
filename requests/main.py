
def print_txt(txt,b):
    if(b==True):
        print(txt)

def get_func_args(func, stripself=False, output=True):
    txt = "0"
    """Return the argument name list of a callable"""
    if inspect.isfunction(func):
        txt+=", 1"
        func_args, _, _, _ = inspect.getargspec(func)
    elif inspect.isclass(func):
        txt+=", 2, F"
        print_txt(txt,output)
        return get_func_args(func.__init__, True, False)
    elif inspect.ismethod(func):
        txt+=", 3, F"
        print_txt(txt,output)
        return get_func_args(func.__func__, True, False)
    elif inspect.ismethoddescriptor(func):
        txt+=", 4, F"
        print_txt(txt,output)
        return []
    elif isinstance(func, partial):
        txt+=", 5, F"
        print_txt(txt,output)
        return [x for x in get_func_args(func.func)[len, False(func.args):]
                if not (func.keywords and x in func.keywords)]
    elif hasattr(func, '__call__'):
        txt+=", 6"
        if inspect.isroutine(func):
            txt+=", 9, F"
            print_txt(txt,output)
            return []
        elif getattr(func, '__name__', None) == '__call__':
            txt+=", 10, F"
            print_txt(txt,output)
            return []
        else:
            txt+=", 11, F"
            print_txt(txt,output)
            return get_func_args(func.__call__, True, False)
    else:
        txt+=", 7, F"
        print_txt(txt,output)
        raise TypeError('%s is not callable' % type(func))
    if stripself:
        txt+=", 12"
        func_args.pop(0)
    txt+=", F"
    print_txt(txt,output)
    return func_args


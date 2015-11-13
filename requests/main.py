import functools
import inspect
import unittest
import six
import operator

def print_txt(txt,b):
    if(b==True):
        print(txt+"\n")

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
    elif isinstance(func, functools.partial):
        txt+=", 5, F"
        print_txt(txt,output)
        return [x for x in get_func_args(func.func,False,False)[len(func.args):]
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
    txt+=", 8"
    if stripself:
        txt+=", 12"
        func_args.pop(0)
    txt+=", F"
    print_txt(txt,output)
    return func_args

class TestStringMethods(unittest.TestCase):
    def test_get_func_args(self):
        def f1(a, b, c):
            pass

        def f2(a, b=None, c=None):
            pass

        class A(object):
            def __init__(self, a, b, c):
                pass

            def method(self, a, b, c):
                pass

        class Callable(object):
            def __call__(self, a, b, c):
                pass

        class CallableWithName(object):
            def __init__(self):
                self.__name__="__call__"
            def __call__(self, a, b, c):
                pass

        class Nebil:
            def __init__(self):
                pass
            def __get__(self):
                return None

        class FTools():
            def __init__(self):
                pass
            def __get__(self):
                return None

        a = A(1, 2, 3)
        cal = Callable()
        cal_with_name = CallableWithName()
        partial_f1 = functools.partial(f1, None)
        partial_f2 = functools.partial(f1, b=None)
        partial_f3 = functools.partial(partial_f2, None)
        n = Nebil()

        print "Caso 1:"
        try:
            self.assertEqual(get_func_args(None), None)
        except:
            pass

        print "Caso 2:"
        self.assertEqual(get_func_args(f2, True), ['b', 'c'])
        print "Caso 3:"
        self.assertEqual(get_func_args(f1), ['a', 'b', 'c'])
        print "Caso 4:"
        self.assertEqual(get_func_args(A), ['a', 'b', 'c'])
        print "Caso 5:"
        self.assertEqual(get_func_args(a.method), ['a', 'b', 'c'])
        print "Caso 6:"
        self.assertEqual(get_func_args(n), [])#4
        print "Caso 7:"
        self.assertEqual(get_func_args(partial_f1), ['b', 'c'])#5
        print "Caso 8:"
        self.assertEqual(get_func_args(" ".join), [])
        print "Caso 9:"
        self.assertEqual(get_func_args(cal_with_name), [])

        print "Caso 10:"
        self.assertEqual(get_func_args(operator.itemgetter(2)), [])
        # print "Caso 10:"
        # self.assertEqual(get_func_args(partial_f3), ['c'])
        # print "Caso 11:"
        # self.assertEqual(get_func_args(object), [])
        # print "Caso 12:"
        # self.assertEqual(get_func_args(cal), ['a', 'b', 'c'])
        # print "Caso 13:"
        # self.assertEqual(get_func_args(six.text_type.split), [])
        # print "Caso 14:"
        # self.assertEqual(get_func_args(operator.itemgetter(2)), [])
unittest.main()
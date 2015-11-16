import functools
import inspect
import unittest
import six
import operator

class Func(object):

    def print_txt(self,txt,b):
        if(b==True):
            print(txt+"\n")

    def get_func_args(self,func, stripself=False, output=True):
        txt = "0"
        """Return the argument name list of a callable"""
        if inspect.isfunction(func):
            txt+=", 1"
            func_args, _, _, _ = inspect.getargspec(func)
        elif inspect.isclass(func):
            txt+=", 2, F"
            self.print_txt(txt,output)
            return self.get_func_args(func.__init__, True, False)
        elif inspect.ismethod(func):
            txt+=", 3, F"
            self.print_txt(txt,output)
            return self.get_func_args(func.__func__, True, False)
        elif inspect.ismethoddescriptor(func):
            txt+=", 4, F"
            self.print_txt(txt,output)
            return []
        elif isinstance(func, functools.partial):
            txt+=", 5, F"
            self.print_txt(txt,output)
            return [x for x in self.get_func_args(func.func,False,False)[len(func.args):]
                    if not (func.keywords and x in func.keywords)]
        elif hasattr(func, '__call__'):
            txt+=", 6"
            if inspect.isroutine(func):
                txt+=", 9, F"
                self.print_txt(txt,output)
                return []
            elif getattr(func, '__name__', None) == '__call__':
                txt+=", 10, F"
                self.print_txt(txt,output)
                return []
            else:
                txt+=", 11, F"
                self.print_txt(txt,output)
                return self.get_func_args(func.__call__, True, False)
        else:
            txt+=", 7, F"
            self.print_txt(txt,output)
            raise TypeError('%s is not callable' % type(func))
        txt+=", 8"
        if stripself:
            txt+=", 12"
            func_args.pop(0)
        txt+=", F"
        self.print_txt(txt,output)
        return func_args

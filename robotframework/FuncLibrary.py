from scrapy.utils.python import get_func_args
import functools
import inspect
import six
import operator


class FuncLibrary(object):
    """Test library for testing *Calculator* business logic.

    Interacts with the calculator directly using its ``push`` method.
    """

    def __init__(self):
        self._result = None

        #ORDENAR ESTO
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

        self.a = A(1, 2, 3)
        self.A = A

        self.cal = Callable()
        self.cal_with_name = CallableWithName()
        self.partial_f1 = functools.partial(f1, None)
        self.partial_f2 = functools.partial(f1, b=None)
        self.partial_f3 = functools.partial(self.partial_f2, None)
        self.n = Nebil()

        self.f2=f2
        self.f1=f1

    def get_arguments(self, func, stripself):
        self._result = get_func_args(func, stripself)


    def result_should_be(self, expected):
        """Verifies that the current result is ``expected``.

        Example:
        | Push Buttons     | 1 + 2 = |
        | Result Should Be | 3       |
        """
        if self._result != expected:
            raise AssertionError('%s != %s' % (self._result, expected))

    def should_cause_error(self, func, stripself):
        """Verifies that calculating the given ``expression`` causes an error.

        The error message is returned and can be verified using, for example,
        `Should Be Equal` or other keywords in `BuiltIn` library.

        Examples:
        | Should Cause Error | invalid            |                   |
        | ${error} =         | Should Cause Error | 1 / 0             |
        | Should Be Equal    | ${error}           | Division by zero. |
        """
        try:
            self.get_arguments(func,stripself)
        except TypeError, err:
            return str(err)
        else:
            raise AssertionError("'%s' should have caused an error."
                                 % expression)

    def get_partial(self, num):
        if num == "1":
            return self.partial_f1
        elif num == "2":

            return self.partial_f2
        elif num == "3":
            return self.partial_f3
        else:
            return None

    def get_function(self, num):
        if num == "1":
            return self.f1
        elif num == "2":
            return self.f2
        else:
            return None

    def get_standard_class(self):
        return self.A

    def get_class_method(self):
        return self.a.method

    def get_enumerable_class(self):
        return self.n

    def get_string_method(self):
        return " ".join

    def get_method_descriptor(self):
        return self.n

    def get_item_getter(self):
        return operator.itemgetter(2)



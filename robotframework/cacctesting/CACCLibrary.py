from scrapy.utils.spider import iter_spider_classes
import log1, log2, log3, log4

class CACCLibrary(object):
    """Test library for testing *CACC* in method *iter_spider_classes*
    from *scrapy.utils.spider*.
    """

    def __init__(self):
        self._result = None

    def get_module_1(self):        
        return log1

    def get_module_2(self):        
        return log2

    def get_module_3(self):        
        return log3

    def get_module_4(self):        
        return log4

    def get_spider_1(self):
        return log1.MySpider1

    def all_true_case(self, module1):
        self._result = list(iter_spider_classes(module1))

    def b_false_others_true_case(self, module2):
        self._result = list(iter_spider_classes(module2))

    def c_false_others_true_case(self, module3):
        self._result = list(iter_spider_classes(module3))

    def d_false_others_true_case(self, module4):
        self._result = list(iter_spider_classes(module4))

    def result_should_be(self, expected):
        """Verifies that the current result is ``expected``.

        Example:
        | Push Buttons     | 1 + 2 = |
        | Result Should Be | 3       |
        """
        if self._result != expected:
            raise AssertionError('%s != %s' % (self._result, expected))
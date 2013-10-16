import types
import inspect

from . import styles

import matplotlib.pyplot as plt


def is_style_function(x):
    return isinstance(x, types.FunctionType) and x.__name__.startswith('style_')


STYLE_FUNCTIONS = dict((name[6:], func) for name, func in inspect.getmembers(styles, predicate=is_style_function))


class style(object):
    def __enter__(self):
        pass
    def __exit__(self, ext, exv, trb):
        for parameter, setting in self.previous.iteritems():
            plt.rcParams[parameter] = setting
    def __init__(self, name):
        self.name = name
        self.previous = {}
        for parameter, setting in STYLE_FUNCTIONS[self.name]().iteritems():
            self.previous[parameter] = plt.rcParams[parameter]
            plt.rcParams[parameter] = setting

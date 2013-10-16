import sys
import types
import inspect

from . import styles

from matplotlib import rc_context, rcParams
import matplotlib.pyplot as plt


def is_style_function(x):
    return isinstance(x, types.FunctionType) and x.__name__.startswith('style_')


STYLE_FUNCTIONS = dict((name[6:], func) for name, func in inspect.getmembers(styles, predicate=is_style_function))


def style(name):
    context = rc_context()
    try:
        rcParams.update(STYLE_FUNCTIONS[name]())
    except:
        context.__exit__(*sys.exc_info())
        raise
    return context

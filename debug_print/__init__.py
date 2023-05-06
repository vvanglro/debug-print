import inspect
import builtins

__version__ = "0.1.1"

original_print = builtins.print


def print_hook(*args, **kwargs):
    frame = inspect.currentframe().f_back
    file_name = frame.f_code.co_filename
    line_num = frame.f_lineno
    new_args = ("[{}:{}]".format(file_name, line_num),) + args
    original_print(*new_args, **kwargs)


builtins.print = print_hook

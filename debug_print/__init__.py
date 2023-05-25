import inspect
import builtins

__version__ = "0.1.2"


def patch():
    original_print = builtins.print
    green = "\033[1;32m"
    reset = "\033[0m"

    def print_hook(*args, **kwargs):
        frame = inspect.currentframe().f_back
        file_name = frame.f_code.co_filename
        line_num = frame.f_lineno
        new_args = (green + "[{}:{}]".format(file_name, line_num) + reset,) + args
        original_print(*new_args, **kwargs)

    builtins.print = print_hook

# debug-print
Capture the print function and add some output information to it for easy debugging

## why？
Is there such a situation？  
That you need to temporarily use `print` debugging in third-party packages or source code, 
but you may forget where to add `print` when thinking or jumping back and forth. 
Now you only need to install and import `debug_print` to let print output the file name and line number, 
which is more convenient for debugging.

## Install：
```shell
pip install debug-print2
```

## Usage:
Just run the file import at the very beginning.
```python
import debug_print
```

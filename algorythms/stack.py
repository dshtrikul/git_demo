import traceback
import sys

def foo(name):
    sys.stderr.write(("Hello {} ...\n".format(name)))
    traceback.print_stack()

traceback.print_stack()
foo('bar')
sys.stderr.write('!!! After foo() call ...\n')
traceback.print_stack()
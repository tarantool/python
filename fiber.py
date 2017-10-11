#!/usr/bin/env python

from dofile_python_bridge import ffi, lib

def testcancel():
    if lib.fiber_is_cancelled():
        raise RuntimeError("Fiber is canceled")

def sleep(s=0):
    lib.fiber_sleep(s)
    testcancel()

@ffi.def_extern()
def python_fiber_run(function, args):
    function = ffi.from_handle(function)
    args = ffi.from_handle(args)

    try:
        function(*args)
    finally:
        return 0

def create(function, *args):
    function = ffi.new_handle(function)
    args = ffi.new_handle(args)

    lib.python_fiber_create(lib.python_fiber_run, function, args)

#print(lib.fiber_run_f)

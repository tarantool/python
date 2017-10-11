#!/usr/bin/env pypy

import cffi
ffibuilder = cffi.FFI()

ffibuilder.embedding_api("""
void dofile_python(const char*);
""")

fiber = open("fiber.h").read()

ffibuilder.set_source("dofile_python_bridge", """
#include <stdbool.h>
#include <stdarg.h>
#include "module.h"

typedef int (*python_fiber_run_f)(void*, void*);
extern int python_fiber_create(python_fiber_run_f cb, void* function, void* args);

""")

ffibuilder.cdef(fiber)

ffibuilder.embedding_init_code("""
    from dofile_python_bridge import ffi, lib
    import imp
    import os
    imp.load_source('fiber', "fiber.py")

    @ffi.def_extern()
    def dofile_python(filename):
        filename = ffi.string(filename)
        imp.load_source('__main__', filename)
""")


#ffibuilder.compile(target="libdofile_python_bridge.*", verbose=True)
ffibuilder.emit_c_code("dofile_python_bridge.c")

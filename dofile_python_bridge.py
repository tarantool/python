#!/usr/bin/env pypy

import cffi
ffibuilder = cffi.FFI()

ffibuilder.embedding_api("""
void dofile_python(const char*);
""")

ffibuilder.set_source("dofile_python_bridge", """
""")

ffibuilder.embedding_init_code("""
    from dofile_python_bridge import ffi
    import imp
    import os

    @ffi.def_extern()
    def dofile_python(filename):
        filename = ffi.string(filename)

        imp.load_source('__main__', filename)
""")


#ffibuilder.compile(target="libdofile_python_bridge.*", verbose=True)
ffibuilder.emit_c_code("dofile_python_bridge.c")

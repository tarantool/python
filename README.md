# Python support for Tarantool

This is an experimental module to add support for Python as a
scripting language to Tarantool along with Lua.

# Installation

You'll need:
- PyPy
- CFFI

For development you can do:

```sh
cmake .
make
```

Then run `test.lua` which calls `test.py`

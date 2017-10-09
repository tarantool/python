#!/usr/bin/env python

import sys
import distutils.sysconfig

if sys.argv[1] == "inc":
    print(distutils.sysconfig.get_python_inc())
elif sys.argv[1] == "lib":
    print(distutils.sysconfig.get_config_vars()['LIBDIR'])
else:
    raise RuntimeError("Unknown option: %s" % sys.argv[1])

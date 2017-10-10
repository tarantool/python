find_program(PYPY_BIN pypy pypy3 pypy2)

execute_process(COMMAND ${PYPY_BIN} ${PROJECT_SOURCE_DIR}/python_paths.py inc
  OUTPUT_VARIABLE PYPY_INCLUDE_DIR)

execute_process(COMMAND ${PYPY_BIN} ${PROJECT_SOURCE_DIR}/python_paths.py lib
  OUTPUT_VARIABLE PYPY_LIBRARY_HINT)

find_library(PYPY_LIBRARY NAMES pypy-c HINTS "${PYPY_LIBRARY_HINT}")

include(FindPackageHandleStandardArgs)

find_package_handle_standard_args(PyPy
    REQUIRED_VARS PYPY_INCLUDE_DIR PYPY_LIBRARY)
set(PYPY_INCLUDE_DIRS ${PYPY_INCLUDE_DIR})
set(PYPY_LIBRARIES ${PYPY_LIBRARY})
mark_as_advanced(PYPY_INCLUDE_DIR PYPY_INCLUDE_DIRS
                 PYPY_LIBRARY PYPY_LIBRARIES)

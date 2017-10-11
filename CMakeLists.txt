cmake_minimum_required(VERSION 2.8 FATAL_ERROR)

project(python C)

if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Debug)
endif()
set(CMAKE_MODULE_PATH "${CMAKE_CURRENT_SOURCE_DIR}" ${CMAKE_MODULE_PATH})

# Find Tarantool and Lua dependecies
set(TARANTOOL_FIND_REQUIRED ON)
find_package(Tarantool)
include_directories(${TARANTOOL_INCLUDE_DIRS})

# Find MsgPuck llibrary
set(MsgPuck_FIND_REQUIRED ON)
find_package(MsgPuck)
include_directories(${MSGPUCK_INCLUDE_DIRS})

# Find MsgPuck llibrary
set(PyPy_FIND_REQUIRED ON)
find_package(PyPy)
include_directories(${PYPY_INCLUDE_DIRS})


# Find other dependecies

# Set CFLAGS
# set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS}")
set(CMAKE_C_FLAGS_DEBUG "${CMAKE_C_FLAGS_DEBUG} -Wall -Wextra")
# Set CXXFLAGS
# set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS}")
set(CMAKE_CXX_FLAGS_DEBUG "${CMAKE_CXX_FLAGS_DEBUG} -Wall -Wextra")

link_directories(${PROJECT_SOURCE_DIR})

# Build module
if (APPLE)
    set(CMAKE_SHARED_LINKER_FLAGS "${CMAKE_SHARED_LINKER_FLAGS} -undefined suppress -flat_namespace")
endif(APPLE)

#add_custom_command(OUTPUT dofile_python_bridge PRE_BUILD MAIN_DEPENDENCY dofile_python_bridge.py COMMAND pypy dofile_python_bridge.py)

message("SOURCE DIR: " ${PROJECT_SOURCE_DIR})

add_custom_command(OUTPUT dofile_python_bridge.c
  COMMAND pypy ${PROJECT_SOURCE_DIR}/dofile_python_bridge.py
  MAIN_DEPENDENCY ${PROJECT_SOURCE_DIR}/dofile_python_bridge.py
  DEPENDS fiber.h fiber.py)


# Add C library
add_library(python SHARED python.c dofile_python_bridge.c fiber.c)
target_link_libraries(python ${MSGPUCK_LIBRARIES})
target_link_libraries(python ${PYPY_LIBRARIES})
set_target_properties(python PROPERTIES PREFIX "" OUTPUT_NAME "python")

# Install module
install(TARGETS python LIBRARY DESTINATION ${TARANTOOL_INSTALL_LIBDIR}/${PROJECT_NAME}/)

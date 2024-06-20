#
# Copyright (c) 2018 Nordic Semiconductor
#
# SPDX-License-Identifier: LicenseRef-Nordic-5-Clause
#

# Point to NCS root directory.
set(NRF_DIR ${CMAKE_CURRENT_LIST_DIR} CACHE PATH "NCS root directory")

# Set expected variable for imported CMake scripts
set(ZEPHYR_NRF_MODULE_DIR ${NRF_DIR})

zephyr_include_directories(include)

add_subdirectory(drivers)
add_subdirectory(lib)
add_subdirectory(modules)
add_subdirectory(subsys)

# ncs_version.h generation
file(STRINGS ${NRF_DIR}/VERSION NCS_VERSION LIMIT_COUNT 1 LENGTH_MINIMUM 5)
string(REGEX MATCH "([^\.]*)\.([^\.]*)\.([^-]*)[-]?(.*)" OUT_VAR ${NCS_VERSION})

set(NCS_VERSION_MAJOR ${CMAKE_MATCH_1})
set(NCS_VERSION_MINOR ${CMAKE_MATCH_2})
set(NCS_VERSION_PATCH ${CMAKE_MATCH_3})
set(NCS_VERSION_EXTRA ${CMAKE_MATCH_4})

include(cmake/version.cmake)

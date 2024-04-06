#
# Copyright (c) 2018 Nordic Semiconductor
#
# SPDX-License-Identifier: LicenseRef-Nordic-5-Clause
#

# Point to NCS root directory.
set(NRF_DIR ${CMAKE_CURRENT_LIST_DIR} CACHE PATH "NCS root directory")

# Set expected variable for imported CMake scripts
set(ZEPHYR_NRF_MODULE_DIR ${NRF_DIR})

add_subdirectory(drivers)

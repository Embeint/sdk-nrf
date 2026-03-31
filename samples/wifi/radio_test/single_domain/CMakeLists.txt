#
# Copyright (c) 2024 Nordic Semiconductor ASA
#
# SPDX-License-Identifier: LicenseRef-Nordic-5-Clause
#

cmake_minimum_required(VERSION 3.20.0)

find_package(Zephyr REQUIRED HINTS $ENV{ZEPHYR_BASE})
project(wifi_radio_test)

target_include_directories(app PRIVATE inc)

# NORDIC SDK APP START
target_sources(app PRIVATE
  ./src/main.c
  ./src/nrf_wifi_radio_test_shell.c
  ./src/nrf_wifi_radio_ficr_shell.c
  ./src/ficr_prog.c
)
# NORDIC SDK APP END

target_link_libraries(app PRIVATE nrf-wifi-osal)

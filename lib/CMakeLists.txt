#
# Copyright (c) 2018 Nordic Semiconductor ASA
#
# SPDX-License-Identifier: LicenseRef-Nordic-5-Clause
#

add_subdirectory_ifdef(CONFIG_AT_MONITOR at_monitor)
add_subdirectory_ifdef(CONFIG_AT_HOST_LIBRARY at_host)
add_subdirectory_ifdef(CONFIG_AT_PARSER at_parser)
add_subdirectory_ifdef(CONFIG_LTE_LINK_CONTROL lte_link_control)
add_subdirectory_ifdef(CONFIG_MULTITHREADING_LOCK multithreading_lock)
add_subdirectory_ifdef(CONFIG_NRF_MODEM_LIB nrf_modem_lib)
add_subdirectory_ifdef(CONFIG_PDN pdn)

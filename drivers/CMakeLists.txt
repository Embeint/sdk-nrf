#
# Copyright (c) 2018-2020 Nordic Semiconductor ASA
#
# SPDX-License-Identifier: LicenseRef-Nordic-5-Clause
#

add_subdirectory(entropy)
add_subdirectory(hw_cc3xx)

add_subdirectory_ifdef(CONFIG_WIFI wifi)

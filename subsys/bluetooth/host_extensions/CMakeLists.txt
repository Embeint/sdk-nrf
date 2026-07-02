#
# Copyright (c) 2023 Nordic Semiconductor
#
# SPDX-License-Identifier: LicenseRef-Nordic-5-Clause
#

if(CONFIG_BT)
  zephyr_library_named(bt_host_extensions)

  zephyr_library_sources(host_extensions.c)
  zephyr_library_sources_ifdef(CONFIG_BT_RADIO_NOTIFICATION_CONN_CB radio_notification_conn_cb.c)
  zephyr_library_sources_ifdef(CONFIG_BT_NRF_CONN_SET_LTK custom_ltk.c)
endif()

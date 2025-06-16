/*
 * Copyright (c) 2025 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: LicenseRef-Nordic-5-Clause
 */

#include "hci_internal_wrappers.h"
#include <zephyr/sys/util.h>
#include <zephyr/bluetooth/buf.h>

#if defined(CONFIG_BT_HCI_ACL_FLOW_CONTROL)
int sdc_hci_cmd_cb_host_buffer_size_wrapper(const sdc_hci_cmd_cb_host_buffer_size_t *cmd_params)
{
	sdc_hci_cmd_cb_host_buffer_size_t ctrl_cmd_params = *cmd_params;

	return sdc_hci_cmd_cb_host_buffer_size(&ctrl_cmd_params);
}
#endif /* CONFIG_BT_HCI_ACL_FLOW_CONTROL */

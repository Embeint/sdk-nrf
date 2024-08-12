/**
 * @file
 * @copyright 2024 Embeint Inc
 * @author Jordan Yates <jordan@embeint.com>
 *
 * SPDX-License-Identifier: LicenseRef-Embeint
 */

#include <zephyr/devicetree.h>
#include <zephyr/toolchain.h>

#define SRAM_MODEM DT_NODELABEL(sram0_ns_modem)

#define PM_NRF_MODEM_LIB_SRAM_ADDRESS  DT_REG_ADDR(SRAM_MODEM)
#define PM_NRF_MODEM_LIB_SRAM_SIZE_MAX DT_REG_SIZE(SRAM_MODEM)

#define PM_NRF_MODEM_LIB_CTRL_ADDRESS (PM_NRF_MODEM_LIB_SRAM_ADDRESS)
#define PM_NRF_MODEM_LIB_TX_ADDRESS                                                                \
	(PM_NRF_MODEM_LIB_CTRL_ADDRESS + CONFIG_NRF_MODEM_LIB_SHMEM_CTRL_SIZE)
#define PM_NRF_MODEM_LIB_RX_ADDRESS                                                                \
	(PM_NRF_MODEM_LIB_TX_ADDRESS + CONFIG_NRF_MODEM_LIB_SHMEM_TX_SIZE)
#define PM_NRF_MODEM_LIB_TRACE_ADDRESS                                                             \
	(PM_NRF_MODEM_LIB_RX_ADDRESS + CONFIG_NRF_MODEM_LIB_SHMEM_RX_SIZE)
#define PM_NRF_MODEM_LIB_SRAM_SIZE                                                                 \
	(CONFIG_NRF_MODEM_LIB_SHMEM_CTRL_SIZE + CONFIG_NRF_MODEM_LIB_SHMEM_TX_SIZE +               \
	 CONFIG_NRF_MODEM_LIB_SHMEM_RX_SIZE + CONFIG_NRF_MODEM_LIB_SHMEM_TRACE_SIZE)

BUILD_ASSERT(PM_NRF_MODEM_LIB_SRAM_SIZE <= PM_NRF_MODEM_LIB_SRAM_SIZE_MAX, "Modem SRAM overflow");

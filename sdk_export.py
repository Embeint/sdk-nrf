#!/usr/bin/env python3

import argparse
import re
import shutil
import pathlib


def tree_replace(upstream: pathlib.Path, output: pathlib.Path, path):
    shutil.rmtree(output.joinpath(*path), ignore_errors=True)
    shutil.copytree(upstream.joinpath(*path), output.joinpath(*path))


def tree_delete(output: pathlib.Path, path):
    shutil.rmtree(output.joinpath(*path), ignore_errors=True)


def file_replace(upstream: pathlib.Path, output: pathlib.Path, path):
    output_file = output.joinpath(*path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(upstream.joinpath(*path), output_file)


def file_copy(upstream: pathlib.Path, upstream_path, output: pathlib.Path, output_path):
    output_file = output.joinpath(*output_path)
    output_file.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(upstream.joinpath(*upstream_path), output_file)


def file_delete(output: pathlib.Path, path):
    output_file = output.joinpath(*path)
    output_file.unlink()


def sample_tests_delete(output: pathlib.Path, path, tests):
    sample_file = output.joinpath(*path)
    contents = sample_file.read_text()
    for test in tests:
        pattern = rf"^  {re.escape(test)}:\n(?:^(?:    .*)?\n)*"
        contents, count = re.subn(pattern, "", contents, flags=re.MULTILINE)
        if count != 1:
            raise RuntimeError(f"Test '{test}' not found in {sample_file}")
    sample_file.write_text(contents)


def export(upstream: pathlib.Path, output: pathlib.Path):
    tree_replace(upstream, output, ["drivers", "bluetooth"])
    tree_replace(upstream, output, ["drivers", "entropy"])
    tree_replace(upstream, output, ["drivers", "mpsl"])
    tree_replace(upstream, output, ["drivers", "mspi"])
    tree_replace(upstream, output, ["drivers", "serial"])
    tree_replace(upstream, output, ["dts", "bindings", "radio_coex"])
    tree_replace(upstream, output, ["dts", "bindings", "mspi"])
    tree_replace(upstream, output, ["include", "bluetooth"])
    tree_replace(upstream, output, ["include", "fem_al"])
    tree_replace(upstream, output, ["include", "modem"])
    tree_replace(upstream, output, ["include", "mpsl"])
    tree_replace(upstream, output, ["lib", "at_parser"])
    tree_replace(upstream, output, ["lib", "at_host"])
    tree_replace(upstream, output, ["lib", "at_monitor"])
    tree_replace(upstream, output, ["lib", "dtm_twowire"])
    tree_replace(upstream, output, ["lib", "fem_al"])
    tree_replace(upstream, output, ["lib", "lte_link_control"])
    tree_replace(upstream, output, ["lib", "modem_antenna"])
    tree_replace(upstream, output, ["lib", "modem_key_mgmt"])
    tree_replace(upstream, output, ["lib", "multithreading_lock"])
    tree_replace(upstream, output, ["lib", "nrf_modem_lib"])
    tree_replace(upstream, output, ["samples", "bluetooth", "direct_test_mode"])
    tree_replace(upstream, output, ["samples", "peripheral", "radio_test"])
    tree_replace(upstream, output, ["samples", "wifi", "radio_test", "single_domain"])
    file_replace(upstream, output, ["samples", "wifi", "Kconfig.sysbuild.nrf70"])
    tree_replace(upstream, output, ["snippets", "nrf70-wifi"])
    tree_replace(upstream, output, ["subsys", "bluetooth", "controller"])
    tree_replace(upstream, output, ["subsys", "bluetooth", "host_extensions"])
    tree_replace(upstream, output, ["subsys", "mpsl"])
    file_replace(upstream, output, ["cmake", "version.cmake"])
    file_replace(upstream, output, ["VERSION"])

    # Files we do not want
    file_delete(output, ["include", "bluetooth", "adv_prov.h"])
    file_delete(output, ["include", "bluetooth", "bt_rpc.h"])
    tree_delete(output, ["include", "bluetooth", "services"])
    tree_delete(output, ["include", "bluetooth", "fast_pair"])
    file_delete(output, ["drivers", "serial", "uart_ipc.c"])
    file_delete(output, ["drivers", "serial", "Kconfig.ipc"])
    tree_delete(output, ["samples", "bluetooth", "direct_test_mode", "boards"])
    tree_delete(output, ["samples", "bluetooth", "direct_test_mode", "remote_hci"])
    file_delete(output, ["samples", "bluetooth", "direct_test_mode", "Kconfig.sysbuild"])
    # Only the sources and Kconfig are used, by the Wi-Fi radio test
    file_delete(output, ["samples", "peripheral", "radio_test", "sample.yaml"])
    # Require the nRF7002 EB interposer shield and nRF71 Wi-Fi support, not exported
    sample_tests_delete(
        output,
        ["samples", "wifi", "radio_test", "single_domain", "sample.yaml"],
        ["sample.nrf70.wifi_ble_radio_test_sd", "sample.nrf7120.wifi_ble_radio_test_sd"],
    )

    # Files Nordic placed in Zephyr fork instead of ncs
    upstream_zephyr = upstream / ".." / "zephyr"
    file_replace(upstream_zephyr, output, ["include", "zephyr", "net", "socket_ncs.h"])
    file_copy(
        upstream_zephyr,
        ["modules", "hal_nordic", "nrfx", "nrfx_reserved_resources_ncs.h"],
        output,
        ["include", "nrfx_config_reserved_resources_ncs.h"],
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser("sdk-nrf exporter")
    parser.add_argument(
        "--upstream", type=str, required=True, help="Upstream repository"
    )
    args = parser.parse_args()

    export(pathlib.Path(args.upstream), pathlib.Path(__file__).parent)

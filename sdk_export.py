#!/usr/bin/env python3

import argparse
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


def file_delete(output: pathlib.Path, path):
    output_file = output.joinpath(*path)
    output_file.unlink()


def export(upstream: pathlib.Path, output: pathlib.Path):
    tree_replace(upstream, output, ["drivers", "bluetooth"])
    tree_replace(upstream, output, ["drivers", "entropy"])
    tree_replace(upstream, output, ["drivers", "mpsl"])
    tree_replace(upstream, output, ["drivers", "serial"])
    tree_replace(upstream, output, ["dts", "bindings", "radio_coex"])
    tree_replace(upstream, output, ["include", "bluetooth"])
    tree_replace(upstream, output, ["include", "modem"])
    tree_replace(upstream, output, ["include", "mpsl"])
    tree_replace(upstream, output, ["lib", "at_parser"])
    tree_replace(upstream, output, ["lib", "at_host"])
    tree_replace(upstream, output, ["lib", "at_monitor"])
    tree_replace(upstream, output, ["lib", "fem_al"])
    tree_replace(upstream, output, ["lib", "lte_link_control"])
    tree_replace(upstream, output, ["lib", "modem_antenna"])
    tree_replace(upstream, output, ["lib", "modem_key_mgmt"])
    tree_replace(upstream, output, ["lib", "multithreading_lock"])
    tree_replace(upstream, output, ["lib", "nrf_modem_lib"])
    tree_replace(upstream, output, ["lib", "pdn"])
    tree_replace(upstream, output, ["modules", "nrfxlib"])
    tree_replace(upstream, output, ["subsys", "bluetooth", "controller"])
    tree_replace(upstream, output, ["subsys", "bluetooth", "host_extensions"])
    tree_replace(upstream, output, ["subsys", "mpsl"])
    file_replace(upstream, output, ["cmake", "version.cmake"])
    file_replace(upstream, output, ["VERSION"])

    # Files we do not want
    file_delete(output, ["include", "bluetooth", "adv_prov.h"])
    file_delete(output, ["include", "bluetooth", "bt_rpc.h"])
    tree_delete(output, ["include", "bluetooth", "services"])

    # Files Nordic placed in Zephyr fork instead of ncs
    upstream_zephyr = upstream / ".." / "zephyr"
    file_replace(upstream_zephyr, output, ["include", "zephyr", "net", "socket_ncs.h"])


if __name__ == "__main__":
    parser = argparse.ArgumentParser("sdk-nrf exporter")
    parser.add_argument(
        "--upstream", type=str, required=True, help="Upstream repository"
    )
    args = parser.parse_args()

    export(pathlib.Path(args.upstream), pathlib.Path(__file__).parent)

    print("Manually validate NRFX_RESERVED_RESOURCES_HEADER!")

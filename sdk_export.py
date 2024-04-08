#!/usr/bin/env python3

import argparse
import shutil
import pathlib

def tree_replace(upstream: pathlib.Path, output: pathlib.Path, path):
    shutil.rmtree(output.joinpath(*path), ignore_errors=True)
    shutil.copytree(upstream.joinpath(*path), output.joinpath(*path))

def export(upstream: pathlib.Path, output: pathlib.Path):
    tree_replace(upstream, output, ['drivers', 'entropy'])
    tree_replace(upstream, output, ['ext', 'oberon'])
    tree_replace(upstream, output, ['modules', 'nrfxlib'])

if __name__ == '__main__':
    parser = argparse.ArgumentParser('sdk-nrf exporter')
    parser.add_argument('--upstream', type=str, required=True, help='Upstream repository')
    args = parser.parse_args()

    export(pathlib.Path(args.upstream), pathlib.Path(__file__).parent)

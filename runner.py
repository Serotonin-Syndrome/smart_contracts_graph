#!/usr/bin/env python3
import testnet
import importlib.util
import generators
import sys


def import_by_path(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main():
    if len(sys.argv) != 3:
        sys.stderr.write('USAGE: runner.py <contract file> <tests file>\n')
        exit(2)
    mod_contract = import_by_path('contract', sys.argv[1])
    mod_tests = import_by_path('tests', sys.argv[2])
    mod_tests.run_tests(generators, testnet.TestNet, mod_contract.MyContract)


if __name__ == '__main__':
    main()

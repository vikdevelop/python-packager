#!/usr/bin/env python
import os
import argparse
import sys
import json
def pkg_path(path):
    if os.path.isdir(path):
        return path
    else:
        raise argparse.ArgumentTypeError(f"dir {path} is not exists. Try entering a different path.")

parser = argparse.ArgumentParser()
parser.add_argument("-V", "--version", help="displays version of Python Packager and Python", action="store_true")
parser.add_argument("-I", "--install", help="Install Python Package to your OS", type=pkg_path)
parser.add_argument("-C", "--create", help="Create Python Package from manifest file python-package.json", type=pkg_path)
parser.add_argument("-R", "--remove", help="Remove Python Package from your OS.", action="store_true")

args = parser.parse_args()

if args.version:
    print("Version of Python Packager: 1.1")
    print("Version of Python:")
    os.system('python3 --version')

if args.install:
    sys.path.append('/app/src')
    os.chdir(args.install + '/package')
    import installer

if args.create:
    sys.path.append('/app/src')
    os.chdir(args.create)
    import pythonpackager

if args.remove:
    sys.path.append('/app/src')
    import uninstall

#!/usr/bin/env python3.11

import sys
import os
import shlex
import subprocess

def main():
    newtag = os.environ["NEW_TAG"]
    cmd = f"gh release  view {newtag} --jq '.assets[].url' --json assets"
    try:
        output = subprocess.run(shlex.split(cmd), capture_output=True, check=True, text=True).stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(e.stderr, file=sys.stderr)
        print(e.stdout, file=sys.stderr)
        sys.exit(1)

    print("<html>")
    for o in output:
        print("<a>")
        print(o)
        print("</a>")
    print("</html>")

if __name__ == '__main__':
    main()

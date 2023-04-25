#!/usr/bin/env python3

import os
import shlex
import subprocess

def main():
    newtag = os.environ["NEW_TAG"]
    cmd = f"gh release  view {newtag} --jq '.assets[].url' --json assets"
    output = subprocess.run(shlex.split(cmd), capture_output=True, check=True, text=True).stdout.splitlines()

    print("<html>")
    for o in output:
        print("<a>")
        print(o)
        print("</a>")
    print("</html>")

if __name__ == '__main__':
    main()

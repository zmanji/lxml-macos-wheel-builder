#!/usr/bin/env python3.11

from pathlib import Path
import sys
import os
import shlex
import subprocess

def main():
    newtag = os.environ["NEW_TAG"]
    repo = os.environ["REPO"]
    cmd = f"gh release  view {newtag} --jq '.assets[].url' --json assets"
    try:
        output = subprocess.run(shlex.split(cmd), capture_output=True, check=True, text=True).stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(e.stderr, file=sys.stderr)
        print(e.stdout, file=sys.stderr)
        sys.exit(1)

    index = ""
    index += "<html>\n"
    for o in output:
        index += "<a>\n"
        index += o
        index += "\n"
        index += "</a>"
    index += "</html>\n"

    
    Path("./index.html").write_text(index)

     
    cmd = f"gh release upload {newtag} index.html -R {repo}"
    try:
        output = subprocess.run(shlex.split(cmd), capture_output=True, check=True, text=True).stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(e.stderr, file=sys.stderr)
        print(e.stdout, file=sys.stderr)
        sys.exit(1)
    print(output)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3.11

from pprint import pprint
import json
from urllib.parse import urlparse
from pathlib import Path
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

    index = ""
    index += "<html>\n"
    for o in output:
        index += "<a>\n"
        index += o
        index += "\n"
        index += "</a>"
    index += "</html>\n"

    
    Path("./index.html").write_text(index)

    cmd = f"gh release view {newtag} --json uploadUrl --jq '.uploadUrl'"
    try:
        url = subprocess.run(shlex.split(cmd), capture_output=True, check=True, text=True).stdout
    except subprocess.CalledProcessError as e:
        print(e.stderr, file=sys.stderr)
        print(e.stdout, file=sys.stderr)
        sys.exit(1)

    url = urlparse(url)

    cmd = f"""
gh api \
  --method POST \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  -H "Content-Type: text/html" \
  {url.scheme}://{url.hostname}{url.path[:-1]}?name=index.html \
  --input index.html
    """

    cmd = shlex.split(cmd)
    try:
        output = subprocess.run(cmd, capture_output=True, check=True, text=True).stdout
    except subprocess.CalledProcessError as e:
        print(e.stderr, file=sys.stderr)
        print(e.stdout, file=sys.stderr)
        sys.exit(1)
    pprint(json.loads(output))

if __name__ == '__main__':
    main()

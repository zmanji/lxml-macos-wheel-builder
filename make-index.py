#!/usr/bin/env python3.11

from pathlib import Path
import sys
import os
import shlex
import subprocess

def main():
    newtag = os.environ["NEW_TAG"]
    repo = os.environ["REPO"]
    token = os.environ["GH_TOKEN"]

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

    url.rsplit('{', maxsplit=1)[0]

    cmd = f"""
    curl -L \
  -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer {token}"\
  -H "X-GitHub-Api-Version: 2022-11-28" \
  -H "Content-Type: text/html" \
  {url}?name=index.html \
  --data-binary "@index.html"
    """

    try:
        output = subprocess.run(shlex.split(cmd), capture_output=True, check=True, text=True).stdout.splitlines()
    except subprocess.CalledProcessError as e:
        print(e.stderr, file=sys.stderr)
        print(e.stdout, file=sys.stderr)
        sys.exit(1)
    print(output)

if __name__ == '__main__':
    main()

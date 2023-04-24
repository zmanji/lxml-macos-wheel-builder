#!/bin/bash

set -euox pipefail

sudo xcode-select -s /Applications/Xcode_14.3.app/Contents/Developer

xcrun --sdk macosx --show-sdk-path
xcrun --sdk macosx --show-sdk-platform-path
xcrun --sdk macosx --show-sdk-version
xcrun --sdk macosx --show-sdk-build-version
sw_vers
arch

wget https://github.com/zmanji/reproducible-wheel-builder/releases/download/v0.0.1/main.pex
chmod +x main.pex


wget https://files.pythonhosted.org/packages/06/5a/e11cad7b79f2cf3dd2ff8f81fa8ca667e7591d3d8451768589996b65dec1/lxml-4.9.2.tar.gz
tar xvzf lxml-4.9.2.tar.gz

PEX_PYTHON=$(which python3.9) CFLAGS='-mmacosx-version-min=11' SOURCE_DATE_EPOCH=0 \
  ./main.pex --lock setuptools.lock --src ./lxml-4.9.2 --out ./out --dist wheel

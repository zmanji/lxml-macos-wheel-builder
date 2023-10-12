#!/bin/bash

set -euox pipefail

sudo xcode-select -s /Applications/Xcode_14.3.app/Contents/Developer

xcrun --sdk macosx --show-sdk-path
xcrun --sdk macosx --show-sdk-platform-path
xcrun --sdk macosx --show-sdk-version
xcrun --sdk macosx --show-sdk-build-version
sw_vers
arch

wget https://github.com/zmanji/reproducible-wheel-builder/releases/download/v0.0.3/main.pex
chmod +x main.pex


wget https://files.pythonhosted.org/packages/30/39/7305428d1c4f28282a4f5bdbef24e0f905d351f34cf351ceb131f5cddf78/lxml-4.9.3.tar.gz
tar xvzf lxml-4.9.3.tar.gz

for py in python3.10 python3.11 python3.12
do
  MACOSX_DEPLOYMENT_TARGET=11.0 PEX_PYTHON=$(which $py) SOURCE_DATE_EPOCH=0 \
    ./main.pex --lock setuptools.lock --src ./lxml-4.9.3 --out ./out --dist wheel
done



#!/bin/bash

set -euox pipefail

python3.9 --help

python3.10 --help

python3.11 --help

python3.12 --help

sudo xcode-select -s /Applications/Xcode_14.3.app/Contents/Developer

xcrun --sdk macosx --show-sdk-path
xcrun --sdk macosx --show-sdk-platform-path
xcrun --sdk macosx --show-sdk-version
xcrun --sdk macosx --show-sdk-build-version

exit 1

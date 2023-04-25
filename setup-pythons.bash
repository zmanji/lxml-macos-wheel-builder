#!/bin/bash

set -euox pipefail

wget https://www.python.org/ftp/python/3.11.3/python-3.11.3-macos11.pkg
sudo installer -dumplog -pkg *.pkg -target /
rm *.pkg

wget https://www.python.org/ftp/python/3.10.11/python-3.10.11-macos11.pkg
sudo installer -dumplog -pkg *.pkg -target /
rm *.pkg

wget https://www.python.org/ftp/python/3.9.13/python-3.9.13-macos11.pkg
sudo installer -dumplog -pkg *.pkg -target /
rm *.pkg

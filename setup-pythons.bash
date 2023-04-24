#!/bin/bash

set -euox pipefail

wget https://www.python.org/ftp/python/3.12.0/python-3.12.0a7-macos11.pkg
sudo installer -pkg python-3.12.0a7-macos11 -target /
rm *.pkg

wget https://www.python.org/ftp/python/3.11.3/python-3.11.3-macos11.pkg
sudo installer -pkg python-3.11.3-macos11.pkg -target /
rm *.pkg

wget https://www.python.org/ftp/python/3.10.11/python-3.10.11-macos11.pkg
sudo installer -pkg ./python3.10.11.macos11.pkg -target /
rm *.pkg

wget https://www.python.org/ftp/python/3.9.13/python-3.9.13-macos11.pkg
sudo installer -pkg python-3.9.13-macos11.pkg -target /
rm *.pkg

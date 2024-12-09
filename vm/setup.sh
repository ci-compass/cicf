#!/bin/bash

#
# Commands to set up a Debian 12 virtual machine.
#
# Intended use: clone this repository or copy this file to the target VM. Then
# run this script. There may be prompts for sudo access.
# 
#     ./setup.sh
#
# It expects the default user to be cicf.

sudo apt update
sudo apt upgrade
sudo apt install ubuntu-desktop
sudo reboot



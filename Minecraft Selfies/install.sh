#!/usr/bin/env bash

sudo ap-get update && apt-get upgrade && apt-get install -y python3-skimage

pip install mcpi

sudo apt-get install python-dev && sudo pip install Pillow

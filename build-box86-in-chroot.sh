#!/bin/bash
cd /
apt update
apt install sudo dpkg-dev git make aria2 fakeroot -y
mkdir box
cd box
aria2c -x 16 -s 16 $1
tar -xvf *
cd box*/
apt build-dep . -y
dpkg-buildpackage -b
#cp *.deb ..
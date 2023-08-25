#!/bin/bash
cpu=$(cat /proc/cpuinfo | grep processor | wc -l)
cd /
apt update
apt install sudo dpkg-dev git make python3 aria2 fakeroot cmake -y
mkdir box
cd box
aria2c -x 16 -s 16 $1
tar -xvf *
cd box*/
apt build-dep . -y
#dpkg-buildpackage -b
cmake .
make -j$cpu
cp *.deb ..
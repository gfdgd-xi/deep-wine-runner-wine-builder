#!/bin/bash
cpu=$(cat /proc/cpuinfo | grep processor | wc -l)
cd /
apt update
apt install sudo dpkg-dev git make python3 wget fakeroot cmake -y
mkdir box
cd box
wget $1
tar -xvf *
cd box*/
apt build-dep . -y
#dpkg-buildpackage -b
cmake .
make -j$cpu
cp *.deb ..
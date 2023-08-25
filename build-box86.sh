#!/bin/bash
url=`cat /tmp/url.txt`
version=`cat /tmp/version.txt`
sudo apt update
sudo apt install qemu-user-static binfmt-support deboostrap aria2 -y
mkdir result
sudo aria2c -d /usr/bin -o pardus-chroot https://github.com/gfdgd-xi/deep-wine-runner/raw/main/pardus-chroot
sudo chmod 777 /usr/bin/pardus-chroot
sudo deboostrap --arch=amd64 buster debian10-amd64
sudo pardus-chroot debian10-amd64
sudo aria2c -d debian10-amd64 -o build.sh https://github.com/gfdgd-xi/auto-building-wine/raw/main/build-box86-in-chroot.sh
sudo chroot debian10-amd64 bash /build.sh
cp debian10-amd64/box/*.deb result -rv
sudo deboostrap --arch=arm64 buster debian10-arm64
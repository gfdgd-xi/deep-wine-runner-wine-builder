#!/bin/bash
url=`cat /tmp/url.txt`
version=`cat /tmp/version.txt`
sudo apt update
sudo apt install qemu-user-static binfmt-support debootstrap aria2 -y
mkdir result
sudo aria2c -d /usr/bin -o pardus-chroot https://github.com/gfdgd-xi/deep-wine-runner/raw/main/pardus-chroot
sudo chmod 777 /usr/bin/pardus-chroot
sudo debootstrap --arch=amd64 focal debian10-amd64
sudo pardus-chroot debian10-amd64
sudo aria2c -d debian10-amd64 -o build.sh https://github.com/gfdgd-xi/auto-building-wine/raw/main/build-box86-in-chroot.sh
sudo chroot debian10-amd64 bash /build.sh https://github.com/ptitSeb/box86/archive/refs/tags/v0.3.2.tar.gz
cp debian10-amd64/box/*.deb result -rv
#sudo debootstrap --arch=arm64 focal debian10-arm64
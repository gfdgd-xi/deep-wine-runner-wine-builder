#!/bin/bash
url=`cat url.txt`
version=`cat version.txt`
sudo apt update
sudo apt install qemu-user-static binfmt-support debootstrap aria2 -y
mkdir /tmp/result
sudo aria2c -d /usr/bin -o pardus-chroot https://github.com/gfdgd-xi/deep-wine-runner/raw/main/pardus-chroot
sudo chmod 777 /usr/bin/pardus-chroot
sudo debootstrap --arch=armhf buster debian10-amd64
sudo pardus-chroot debian10-amd64
sudo aria2c -d debian10-amd64 -o build.sh https://github.com/gfdgd-xi/auto-building-wine/raw/main/build-box86-in-chroot.sh
sudo chroot debian10-amd64 bash /build.sh $url
cp debian10-amd64/box/*.deb /tmp/result/box86_${version}_armhf.deb -rv
cp debian10-amd64/box/*.deb /tmp/result/box86_armhf.deb -rv

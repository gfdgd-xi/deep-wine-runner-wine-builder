#!/bin/bash
box86url=`cat url.txt`
box64url=`cat urlbox64.txt`
box86version=`cat version.txt`
box64version=`cat versionbox64.txt`
sudo apt update
sudo apt install qemu-user-static binfmt-support debootstrap aria2 -y
mkdir /tmp/result
sudo aria2c -d /usr/bin -o pardus-chroot https://github.com/gfdgd-xi/deep-wine-runner/raw/main/pardus-chroot
sudo chmod 777 /usr/bin/pardus-chroot
sudo debootstrap --arch=amd64 buster debian10-amd64
sudo debootstrap --arch=armhf buster debian10-armhf
sudo debootstrap --arch=arm64 buster debian10-arm64
sudo debootstrap --arch=riscv64 focal ubuntu20.04-riscv64
sudo pardus-chroot debian10-amd64
sudo pardus-chroot debian10-armhf
sudo pardus-chroot debian10-arm64
sudo pardus-chroot ubuntu20.04-riscv64
sudo aria2c -d debian10-amd64 -o build.sh https://github.com/gfdgd-xi/auto-building-wine/raw/main/build-box86-in-chroot.sh
sudo aria2c -d debian10-armhf -o build.sh https://github.com/gfdgd-xi/auto-building-wine/raw/main/build-box86-in-chroot.sh
sudo aria2c -d debian10-arm64 -o build.sh https://github.com/gfdgd-xi/auto-building-wine/raw/main/build-box86-in-chroot.sh
sudo aria2c -d ubuntu20.04-riscv64 -o build.sh https://github.com/gfdgd-xi/auto-building-wine/raw/main/build-box86-in-chroot.sh
sudo chroot debian10-amd64 bash /build.sh $box64url
sudo chroot debian10-armhf bash /build.sh $box86url
sudo chroot debian10-arm64 bash /build.sh $box64url
sudo chroot ubuntu20.04-riscv64 bash /build.sh $box64url
cp debian10-armhf/box/*.deb /tmp/result/box86_${box86version}_armhf.deb -rv
cp debian10-armhf/box/*.deb /tmp/result/box86_armhf.deb -rv
cp debian10-amd64/box/*.deb /tmp/result/box64_${box64version}_amd64.deb -rv
cp debian10-amd64/box/*.deb /tmp/result/box64_amd64.deb -rv
cp debian10-arm64/box/*.deb /tmp/result/box64_${box64version}_arm64.deb -rv
cp debian10-arm64/box/*.deb /tmp/result/box64_arm64.deb -rv
cp ubuntu20.04-riscv64/box/*.deb /tmp/result/box64_${box64version}_riscv64.deb -rv
cp ubuntu20.04-riscv64/box/*.deb /tmp/result/box64_riscv64.deb -rv

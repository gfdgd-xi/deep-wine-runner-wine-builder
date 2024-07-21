#!/bin/bash
system=$1
sudo apt install deboostrap -y
sudo deboostrap $1 system
chrootRun="sudo chroot system"
sudo aria2c -d /usr/bin -o pardus-chroot https://github.com/gfdgd-xi/deep-wine-runner/raw/main/pardus-chroot
sudo chmod 777 /usr/bin/pardus-chroot
sudo pardus-chroot $systemPath
$chrootRun bash -c "echo deb http://deb.debian.org/debian bookworm main"
$chrootRun apt update
$chrootRun apt source virtualbox
$chrootRun 
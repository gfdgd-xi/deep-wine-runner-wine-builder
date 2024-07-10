#!/bin/bash
CURRENT_DIR=$(cd $(dirname $0); pwd)
if [[ ! -f /etc/box64.box64rc ]]; then
    pkexec cp -rv $CURRENT_DIR/box64/box64.box64rc /etc/box64.box64rc
fi
export LD_LIBRARY_PATH=$CURRENT_DIR/box64/x86_64-linux-gnu/:$LD_LIBRARY_PATH
$CURRENT_DIR/box64/box64 $CURRENT_DIR/bin/wine-i386 $*
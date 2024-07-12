#!/bin/bash
CURRENT_DIR=$(cd $(dirname $0); pwd)
if [[ ! -f ~/.box64rc ]]; then
    cp -rv $CURRENT_DIR/box64/box64.box64rc ~/.box64rc
fi
export LD_LIBRARY_PATH=$CURRENT_DIR/box64/x86_64-linux-gnu/:$LD_LIBRARY_PATH
$CURRENT_DIR/box64/box64 $CURRENT_DIR/bin/wine-i386 $*
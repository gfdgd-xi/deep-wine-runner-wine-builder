#!/bin/bash
CURRENT_DIR=$(cd $(dirname $0); pwd)
cp -r $CURRENT_DIR/box64/box64.box64rc ~/.box64rc
export LD_LIBRARY_PATH=$CURRENT_DIR/box64/x86_64-linux-gnu/:$LD_LIBRARY_PATH
$CURRENT_DIR/box64/box64 $CURRENT_DIR/wine/bin/wine $*
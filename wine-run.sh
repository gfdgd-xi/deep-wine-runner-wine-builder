#!/bin/bash
echo Power by Wine Runner
echo 由 Wine 运行器提供支持
CURRENT_DIR=$(cd $(dirname $0); pwd)
cp -r $CURRENT_DIR/box64/box64.box64rc ~/.box64rc
export LD_LIBRARY_PATH=$CURRENT_DIR/box64/box64-x86_64-linux-gnu/:$LD_LIBRARY_PATH
if [[ `uname -m` == "loongarch64" ]]; then
    if [[ `getconf PAGESIZE` != "4096" ]]; then
        echo 不支持当前内核，Pagesize 应该为 4096 而非 `getconf PAGESIZE`
        echo 可以在 GXDE 内核管理器获取使用 4k Pagesize 的龙芯新世界内核
        exit 1
    fi
fi
$CURRENT_DIR/box64/box64 $CURRENT_DIR/wine/bin/wine "$*"

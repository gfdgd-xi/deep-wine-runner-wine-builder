#!/bin/bash
CURRENT_DIR=$(cd $(dirname $0); pwd)
bash $CURRENT_DIR/../run.sh "$*"

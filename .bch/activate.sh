#!/usr/bin/env bash

r=$(dirname $(dirname $BASH_SOURCE))
export BCH_ZJOT__root=${r}

source $(dirname $BASH_SOURCE)/init/fn.sh
::lbin:: $(dirname $BASH_SOURCE)/lbin

bch.zjot.uv-sync
source ~/.config/bch-zjot/activate.sh

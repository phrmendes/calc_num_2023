#!/usr/bin/env bash

export MAMBA_ROOT_PREFIX=$PWD/.mamba

eval "$(micromamba shell hook --shell=posix)"

if [ ! -d "$MAMBA_ROOT_PREFIX" ]; then
  micromamba create -f env.yaml --yes
fi

if ! git diff --quiet -- env.yaml; then
  micromamba update -f env.yaml --yes
fi

micromamba activate calc_num

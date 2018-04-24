#!/bin/bash

python train.py \
    --dataroot ~/data/space-juno \
    --checkpoints_dir ~/data/checkpoints \
    --name juno_combo_cyclegan \
    --model cycle_gan \
    --pool_size 50 \
    --no_dropout

#!/bin/bash

python test.py \
    --dataroot ~/data/space-juno \
    --checkpoints_dir ~/data/checkpoints \
    --name juno_combo_cyclegan \
    --model cycle_gan \
    --phase test \
    --results_dir ~/data/space-juno/results
    --no_dropout

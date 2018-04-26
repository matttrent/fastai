#!/bin/bash

python test.py \
    --dataroot ~/data/space-juno \
    --name juno_combo_pix \
    --model pix2pix \
    --which_model_netG unet_256 \
    --which_direction BtoA \
    --dataset_mode aligned \
    --results_dir ~/data/space-juno/results
    --norm batch

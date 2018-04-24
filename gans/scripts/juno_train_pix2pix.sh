#!/bin/bash

python train.py \
    --dataroot ~/data/space-juno \
    --name juno_combo_pix \
    --model pix2pix \
    --which_model_netG unet_256 \
    --which_direction BtoA \
    --lambda_A 100 \
    --dataset_mode aligned \
    --no_lsgan \
    --norm batch \
    --pool_size 0 \
    --no_flip

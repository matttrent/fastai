#!/bin/bash

name=moto_pix2pix_batch1
subdirs='00k 10k 20k 30k'
epochs='20'

for epoch in $epochs
do

for subdir in $subdirs
do

python feedback.py \
    --dataroot ~/data/moto-gopro --name $name --model pix2pix \
    --which_model_netG unet_256 --which_direction AtoB --dataset_mode feedback \
    --norm batch --how_many 500 --subdir $subdir --which_epoch $epoch

ffmpeg -y -r 30 -f image2 -i ~/data/moto-gopro/feedback/$subdir/%04d.png \
    -vcodec libx264 -crf 25 -pix_fmt yuv420p \
    ~/data/moto-gopro/videos/${name}_${subdir}_epoch_${epoch}.mp4

done
done

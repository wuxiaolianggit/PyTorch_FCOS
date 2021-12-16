python train.py \
        --cuda \
        --root /home/jxk/object-detection/dataset/ \
        -d coco \
        -v fcos_rt_r50_fpn_4x \
        --lr 0.01 \
        --batch_size 8 \
        --train_min_size 512 \
        --train_max_size 900 \
        --val_min_size 512 \
        --val_max_size 736 \
        --wp_iter 500 \
        --multi_scale \
        --accumulate 2

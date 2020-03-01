#!/bin/bash

read foo
echo $foo
IFS=';' read -ra ADDR <<< $foo
# echo ${ADDR[0]}
echo ${ADDR[1]}

# performance_rnn_generate \
# --config=multiconditioned_performance_with_dynamics \
# --bundle_file=./models/multiconditioned_performance_with_dynamics.mag \
# --output_dir=./out/piano \
# --num_outputs=10 \
# --num_steps=3000 \
# --pitch_class_histogram="$1" \
# --temperature=$2
#!/bin/bash
read foo
IFS=';' read -ra ADDR <<< $foo

performance_rnn_generate \
--config=multiconditioned_performance_with_dynamics \
--bundle_file=./models/multiconditioned_performance_with_dynamics.mag \
--output_dir=./out/piano \
--num_outputs=10 \
--num_steps=3000 \
--pitch_class_histogram="${ADDR[0]}" \
--temperature=${ADDR[1]}
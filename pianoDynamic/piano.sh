#!/bin/bash
# read foo
IFS=';' read -ra ADDR < ./params

# echo ${ADDR[0]} pitch hist
# echo ${ADDR[1]} notes_per_second
# echo ${ADDR[2]}


performance_rnn_generate \
--config=multiconditioned_performance_with_dynamics \
--bundle_file=./models/multiconditioned_performance_with_dynamics.mag \
--output_dir=./out/piano \
--num_outputs=1 \
--num_steps=3000 \
--pitch_class_histogram="${ADDR[0]}" \
--temperature=${ADDR[1]} \
--primer_melody="[60,62,64,65,67,69,71,72]"
--temperature=1.0 \
--beam_width=2 \
--primer_pitches="[60,67]" \
--notes_per_second=20 \
--branch_factor=1
# --notes_per_second=${ADDR[1]} \


# --branch_factor=0.5 \

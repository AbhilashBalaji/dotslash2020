cwd=$(pwd) 
python3 ./drums/drums_rnn_generate.py \
--config=drum_kit \
--bundle_file=./models/drum_kit_rnn.mag \
--hparams="batch_size=64,rnn_layer_sizes=[64,64]" \
--output_dir=./out/drums \
--num_outputs=6 \
--num_steps=64 \
--primer_drums="[(36,)]"
import os
from bokeh.io import show
from magenta.models.performance_rnn import performance_sequence_generator
from magenta.music.protobuf import generator_pb2
from magenta.music.protobuf import music_pb2

import magenta.music as mm

from magenta.models.shared import sequence_generator_bundle


'''
   Args:
      num_steps: The integer length in steps of the final track, after
          generation. Includes the primer.
      primer_sequence: The primer sequence, a Performance object.
      temperature: A float specifying how much to divide the logits by
         before computing the softmax. Greater than 1.0 makes tracks more
         random, less than 1.0 makes tracks less random.
      beam_size: An integer, beam size to use when generating tracks via
          beam search.
      branch_factor: An integer, beam search branch factor to use.
      steps_per_iteration: An integer, number of steps to take per beam search
          iteration.
      control_signal_fns: A list of functions that map time step to desired
          control value, or None if not using control signals.
      disable_conditioning_fn: A function that maps time step to whether or not
          conditioning should be disabled, or None if there is no conditioning
          or conditioning is not optional.

'''


def switch(sentiment):
    hist = []
    n_sec = 1
    if sentiment['Sadness'] < 0.5:
        hist = [2, 0, 1, 1, 0, 1, 0, 2, 0, 1, 1, 0]

    elif sentiment['Sadness'] < 0.6:
        n_sec = 5
        hist = [2, 1, 1, 1, 0, 1, 0, 2, 1, 0, 1, 0]
    else:
        n_sec = 5
        hist = [2, 1, 1, 1, 0, 1, 0, 2, 1, 0, 1, 0]

    if sentiment['Joy'] < 0.5:

        hist = [2, 0, 1, 0, 3, 1, 0, 1, 0, 1, 0, 1]
    elif sentiment['Joy'] < 0.6:
        hist = [2, 0, 0, 0, 1, 1, 0, 2, 0, 1, 0, 1]
    elif sentiment['Joy'] < 0.7:
        hist = [2, 0, 0, 0, 1, 0, 0, 2, 0, 1, 0, 0]
    else:
        hist = [2, 0, 0, 0, 1, 1, 0, 4, 0, 1, 0, 0]
    pass
    return (hist, n_sec)


def _generate(generator, options, n_outputs):
    for i in range(n_outputs):
        sequence = generator.generate(music_pb2.NoteSequence(), options)
        mid_path = os.getcwd()+"/out/midis/test"+str(i)+".mid"
        mm.sequence_proto_to_midi_file(sequence, mid_path)
    print("Genereated to "+os.getcwd()+"/out/midis/test")


def generate(sentiment, n_sec, n_op):
    BUNDLE_DIR = os.getcwd()+'/models/'
    MODEL_NAME = 'multiconditioned_performance_with_dynamics'
    BUNDLE_NAME = MODEL_NAME + '.mag'

    bundle = sequence_generator_bundle.read_bundle_file(
        os.path.join(BUNDLE_DIR, BUNDLE_NAME))
    generator_map = performance_sequence_generator.get_generator_map()
    generator = generator_map[MODEL_NAME](checkpoint=None, bundle=bundle)
    generator.initialize()
    generator_options = generator_pb2.GeneratorOptions()

    generator_options.args['temperature'].float_value = 2.0

    # generator_options.args['pitch_class_histogram'].string_value = switch()
    generator_options.args['pitch_class_histogram'].string_value = "[2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]"

    # Cannot append
    generate_section = generator_options.generate_sections.add(
        start_time=0, end_time=n_sec)

    _generate(generator, generator_options, n_op)


generate({}, 4, 4)

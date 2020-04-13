import os

from os import environ, path

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from pocketsphinx import LiveSpeech, get_model_path

model_path = get_model_path()
print(model_path)

# Here is the configuration for Spanish
config = Decoder.default_config()
config.set_string('-hmm', model_path + '/es-es')
config.set_string('-lm', model_path + '/es-20k.lm.bin')
config.set_string('-dict', model_path + '/es.dict')
decoder = Decoder(config)

# Decode streaming data.
speech = LiveSpeech(
    verbose=False,
    sampling_rate=16000,
    buffer_size=2048,
    no_search=False,
    full_utt=False,
    hmm= os.path.join(model_path, 'es-es'),
    lm= os.path.join(model_path, 'es-20k.lm.bin'),
    dict= os.path.join(model_path, 'es.dict'),
)

for phrase in speech:
    print(phrase)

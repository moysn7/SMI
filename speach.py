#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import environ, path
import pyaudio

from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *
from pocketsphinx import get_model_path


model_path = get_model_path()


#dirección del diccionario español 
'''
config = Decoder.default_config()
config.set_string('-hmm', path.join(model_path + '/es-es'))
config.set_string('-lm', path.join(model_path + '/es-20K.lm.bin'))
config.set_string('-dict', path.join(model_path + '/es.dict'))
decoder = Decoder(config)
'''
#diccionario inglés
config = Decoder.default_config()
config.set_string('-hmm', path.join(model_path + '/en-us'))
config.set_string('-lm', path.join(model_path + '/en-us.lm.bin'))
config.set_string('-dict', path.join(model_path + '/cmudict-en-us.dict'))
decoder = Decoder(config)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=1024)
stream.start_stream() 

in_speech_bf = False
decoder.start_utt()

while True:
    buf = stream.read(1024)
    if buf:
        decoder.process_raw(buf, False, False)
        if decoder.get_in_speech() != in_speech_bf:
            in_speech_bf = decoder.get_in_speech()
            if not in_speech_bf:
                decoder.end_utt()
                print 'Result:', decoder.hyp().hypstr
                if decoder.hyp().hypstr == 'uno':
                    print 'Hasta luego Lucas'
                    break
                decoder.start_utt()

    else:
        break
decoder.end_utt()
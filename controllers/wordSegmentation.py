# Word segmentation
import json
import math
import os

import librosa
import numpy
import pandas as pd
import vosk


def extract_words(res):
    jres = json.loads(res)
    if not 'result' in jres:
        return []
    words = jres['result']
    return words


def transcribe_words(recognizer, bytes):
    results = []

    chunk_size = 4000
    for chunk_no in range(math.ceil(len(bytes) / chunk_size)):
        start = chunk_no * chunk_size
        end = min(len(bytes), (chunk_no + 1) * chunk_size)
        data = bytes[start:end]

        if recognizer.AcceptWaveform(data) and recognizer.SetWords(1):
            words = extract_words(recognizer.Result())
            results += words
    results += extract_words(recognizer.FinalResult())

    return results


def word_segmentation(file):
    vosk.SetLogLevel(-1)

    model_path = 'C:/Users/ravin/Desktop/Research Local/VOSK/vosk-model-en-us-daanzu-20200905'
    sample_rate = 16000

    audio, sr = librosa.load(file, sr=16000)
    # convert to 16bit signed PCM, as expected by VOSK
    int16 = numpy.int16(audio * 32768).tobytes()

    # XXX: Model must be downloaded from https://alphacephei.com/vosk/models
    # https://alphacephei.com/vosk/models/vosk-model-small-de-0.15.zip
    if not os.path.exists(model_path):
        raise ValueError(f'Could not find VOSK model at {model_path}')

    model = vosk.Model(model_path)
    recognizer = vosk.KaldiRecognizer(model, sample_rate)
    recognizer.SetWords(1)

    res = transcribe_words(recognizer, int16)
    df = pd.DataFrame.from_records(res)
    df = df.sort_values('start')

    df.to_json(r'./preparedAudio/word_transcript.json')
    return res

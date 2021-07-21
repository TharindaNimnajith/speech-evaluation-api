from fastapi import FastAPI
import controllers
import algorithms

app = FastAPI()

@app.post("/convertAudio")
def convert_audio(path):
    controllers.audio_convert(path) #'./samples/googleFemale.wav'
    return "processed"

@app.post("/getTextTranscript")
def word_segmentation(path):
    return controllers.word_segmentation(path) #'./preparedAudio/selectedWord-extract.wav'

@app.post("/selectWord")
def audio_segmentation(start, end):
    return controllers.audio_segmentation(float(start), float(end)) #1.92, 2.28

@app.post("/getFormantFrequencyRange")
def get_formants_frequency_range(path):
    return controllers.get_frequency_range(path) #'./preparedAudio/selectedWord-extract.wav'

@app.post("/phonemeExtraction")
def phoneme_extraction(path, word):
    return controllers.phoneme_extraction_test(path, word) #'./preparedAudio/selectedWord-extract.wav', "IY"

@app.post("/findRhymings")
def rhyme_find(word):
    return controllers.find_rhyming_words(word) #'Some Word'
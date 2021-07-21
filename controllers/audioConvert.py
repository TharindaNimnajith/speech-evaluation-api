from pydub import AudioSegment

def audio_convert(file):
    sound = AudioSegment.from_mp3(file)
    sound = sound.set_channels(1)
    sound = sound.set_frame_rate(16000)
    sound.export("./preparedAudio/convertedAudio.wav", format="wav")
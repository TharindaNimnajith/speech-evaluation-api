#audio segment by word
from pydub import AudioSegment

def audio_segmentation(start, end):
    file_name = 'selectedWord'

    #time ms
    startTime = start * 1000
    endTime = end * 1000

    # Opening file and extracting segment
    song = AudioSegment.from_mp3( './preparedAudio/convertedAudio.wav' )
    extract = song[startTime:endTime]

    # Saving
    extract.export( './preparedAudio/'+file_name+'-extract.wav', format="wav")
    return "word Selected"
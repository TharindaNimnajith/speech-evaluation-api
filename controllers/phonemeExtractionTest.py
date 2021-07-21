import controllers
import pandas as pd
import pronouncing
import algorithms

def phoneme_extraction_test(audio_input, word):

    df = pd.DataFrame(algorithms.measureFormants(audio_input))#Frequency range[0] -> 0 means the first word. In the audio, there are three words.
    transformedTable = df.T

    # Load data into pandas DataFrame       
    dataFrame = pd.DataFrame(transformedTable, columns=['f1','f2'])
    pronunced_vowel = []

    # f1 = [558, 420, 238, 728, 689, 460, 400, 304, 513, 292, 641]
    # f2 = [819, 1376, 2547, 1181,1744, 1870, 2400, 937, 1555, 2278, 1257]
    # n = ["AO", "UH", "IY", "AA", "AE", "EH", "EI", "UW", "ER", "IH", "AH"]

    vowel_categories = {'A':{'AA', 'AH', 'AE', 'ER'}, 'E':{'EH'}, 'I':{'IY', 'IH'}, 'O':{'AO'}, 'U':{'UH', 'UW'}}

    vowels = {
        0:{'phone':'IY', 'f1_low':138, 'f1_high':338, 'f2_low':2047, 'f2_high':2647, 'color': "pink"},
        1:{'phone':'AO', 'f1_low':458, 'f1_high':658, 'f2_low':719, 'f2_high':919, 'color': "red"},
        2:{'phone':'AA', 'f1_low':628, 'f1_high':828, 'f2_low':1081, 'f2_high':1281, 'color': "yellow"},
        3:{'phone':'UH', 'f1_low':320, 'f1_high':520, 'f2_low':1206, 'f2_high':1476, 'color': "black"},
        4:{'phone':'UW', 'f1_low':204, 'f1_high':404, 'f2_low':837, 'f2_high':1037, 'color': "blue"},
        5:{'phone':'AE', 'f1_low':589, 'f1_high':789, 'f2_low':1644, 'f2_high':1854, 'color': "orange"},
        6:{'phone':'EH', 'f1_low':360, 'f1_high':600, 'f2_low':1770, 'f2_high':1970, 'color': "gray"},
        7:{'phone':'ER', 'f1_low':413, 'f1_high':613, 'f2_low':1455, 'f2_high':1655, 'color': "gold"},
        8:{'phone':'IH', 'f1_low':192, 'f1_high':392, 'f2_low':2178, 'f2_high':2378, 'color': "white"},
        9:{'phone':'AH', 'f1_low':541, 'f1_high':741, 'f2_low':1157, 'f2_high':1357, 'color': "cyan"}
    }

    for i in range(len(dataFrame)):
        for x in range(len(vowels)):
            if dataFrame['f1'][i + 1] > vowels[x]['f1_low'] and dataFrame['f1'][i + 1] < vowels[x]['f1_high'] and dataFrame['f2'][i + 1] > vowels[x]['f2_low'] and dataFrame['f2'][i + 1] < vowels[x]['f2_high']:
                pronunced_vowel.append(vowels[x]['phone'])
    
    vowel_count = {}
    for ws in pronunced_vowel:
        if ws not in vowel_count:
            vowel_count[ws] = 1
        else:
            vowel_count[ws] += 1

    for x in vowel_count:
        percentage = (vowel_count[x] / len(pronunced_vowel)) * 100
        vowel_count[x] = {percentage}
       
    return vowel_count
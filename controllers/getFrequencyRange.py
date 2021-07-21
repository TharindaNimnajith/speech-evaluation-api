import json

import algorithms


def get_frequency_range(audio_input):
    # Word segmentation
    f = open('./preparedAudio/word_transcript.json', )
    segmented_words = json.load(f)

    # Extract formants
    formants_frequencies = algorithms.measureFormants(audio_input)

    # Create time array
    time_array = []
    for i in range(len(formants_frequencies)):
        value = formants_frequencies[i + 1]['time']
        time_array.append(value)

    # Identify frequency within time frame
    frequency_range = {}
    count = 0

    for x in range(len(segmented_words['word'])):
        segments = {}
        end = segmented_words['end'][str(x)]
        start = segmented_words['start'][str(x)]
        sum_f1 = 0
        sum_f2 = 0

        for i in range(len(time_array)):

            if end >= time_array[i] >= start:
                segments[count] = {'index': i, 'time': time_array[i], 'f1': formants_frequencies[i + 1]['f1'],
                                   'f2': formants_frequencies[i + 1]['f2'],
                                   'distance': formants_frequencies[i + 1]['f2'] - formants_frequencies[i + 1]['f1']}
                sum_f1 = sum_f1 + formants_frequencies[i + 1]['f1']
                sum_f2 = sum_f2 + formants_frequencies[i + 1]['f2']
                count += 1

    frequency_range[x] = segments
    print('Calculated frequency range')

    return frequency_range

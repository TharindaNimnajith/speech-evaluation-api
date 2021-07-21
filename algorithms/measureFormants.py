#!/usr/bin/env python3
import parselmouth 
from parselmouth.praat import call

# This function measures formants using Formant Position formula
def measureFormants(sound):
    f0min = 75
    f0max = 300
    sound = parselmouth.Sound(sound) # read the sound
    pointProcess = call(sound, "To PointProcess (periodic, cc)", f0min, f0max)
    #print(pitch)
    formants = call(sound, "To Formant (burg)", 0.0025, 5, 5000, 0.025, 50)
    numPoints = call(pointProcess, "Get number of points")

    formant_list = {}

    # Measure formants only at glottal pulses
    for point in range(0, numPoints):
        point += 1
        t = call(pointProcess, "Get time from index", point)
        f1 = call(formants, "Get value at time", 1, t, 'Hertz', 'Linear')
        f2 = call(formants, "Get value at time", 2, t, 'Hertz', 'Linear')
  
        formant_list[point] = {'time':t, 'f1': f1, 'f2':f2}
        
    print("mesured formants frequencies")
    return formant_list
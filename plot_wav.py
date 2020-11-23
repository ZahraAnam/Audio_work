import glob
import os
import sys
import sox
import numpy as np 
import pandas as pd
from scipy.io import wavfile
from matplotlib import pyplot as plt 

inp_files =glob.iglob('/home/anam/Desktop/Trimmed_Audio_Data/AgeGroup_003/258640/Audio/*.wav')
for file in inp_files:
    fs,data = wavfile.read(file)
    print(file)
    print(data)
    times = np.arange(len(data))/float(fs)

import os
import sys
import sox
import numpy as np 
import wave
from scipy.io import wavfile
import scipy.signal as sps

def sammpler(inp_aud,oup_file,new_rate):
    fs,data = wavfile.read(inp_aud)
    num_samples = round(len(data)*float(new_rate)/fs)
    data = sps.resample(data,num_samples)
    wavfile.write(out_file,new_rate,data)
    return
def wav_sampler(inp_aud,oup_file,new_rate):
    spf = wave.open(inp_aud,'rb')
    fs = spf.getframerate()
    signal = spf.readframes(-1)
    ch = spf.getnchannels()
    #wd = spf.getsampwidth()
    wf = wave.open('oup_file','wb')
    wf.setnchannels(ch)
    wf.setsampwidth(1)
    wf.setframerate(new_rate)
    wf.writeframesraw(signal)
    wf.close()
    return
def sox_sampler(inp_aud,out_file,new_rate):
    fs,data = wavfile.read(inp_aud)
    tfm=sox.Transformer()
    tfm.set_output_format(rate=new_rate)
    tfm.build(input_array=data,sample_rate_in=fs,output_filepath=out_file)
    return



inp_base = '/home/anam/Desktop/Leipzig'
oup_base = '/home/anam/Desktop/Resampled_Audios'
for dirpath, subdirs, files in os.walk(inp_base):
    for x in files:
        if x.endswith(".wav"):
            aud_file = os.path.join(dirpath,x)
            out_direc = dirpath.replace(inp_base,oup_base)
            out_file = os.path.join(out_direc,x)
            if not os.path.exists(out_direc):
                os.makedirs(out_direc)
            sox_sampler(aud_file,out_file,16000)
        
print('Done')
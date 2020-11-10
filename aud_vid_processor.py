import glob
import os
import sys
import numpy as np
from pydub import AudioSegment
import speech_recognition as sr
import moviepy.editor as mp
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
#import waterfall_chart

def extractor(p_in,p_out):
    print('In Extractor')
    clip =  mp.VideoFileClip(p_in)
    print(p_out)
    clip.audio.write_audiofile(p_out)
    return

def converter(p_in,p_out):
    sound = AudioSegment.from_mp3(p_in)
    sound.export(p_out, format="wav")
    return

def Comparator(base_dir,n,*argv):
    # This is the function to draw the several graphs for comparison in one figure
    # Pass in the arguments the folder names that contain the "all.rttm" file for each case
    # Give the base directory
    # Output path for storing the figure
    # Number of files you want to comapre
    
    fig,axs = plt.subplots(int(n))
    fig.suptitle("Comparison of Given Audio Analysis")
    nx=0
    for arg in argv:
        file_name = os.path.join(base_dir,arg)
        file_name = os.path.join(file_name,"all.rttm")
        In_file = np.genfromtxt(file_name,dtype=None,delimiter="\n",encoding=None).reshape(-1,1)
        in_proc = np.empty([1,3])
        labels=[]
        A = 'SPEAKER ' + arg
        for i in range(len(In_file)):
            #X = {In_file[i,0].repalce(A,"").replace('<NA> <NA>',"")}
            #X = "".join()
            #X = X.split()
            X = str(In_file[i])
            X = {X.replace(A,"").replace('<NA> <NA>',"")}
            X ="".join(X)
            X = X.split()
            n1 = float(X[1])
            n2 = float(X[2])
            n3 = float(X[3])
            labels = np.append(labels,X[4])
            num = [n1,n2,n3]
            #num = np.asarray([n1,n2,n3],X[4]).reshape(-1,4)
            in_proc = np.vstack((in_proc,num))
        print(type(labels))
        colorMap = {'SPEECH': 'g',
            'CHI': 'r',
            'KCHI': 'b',
            'FEM': 'c',
            'MAL': 'y'}
        colors = [ colorMap[label] for label in labels]
        in_proc = in_proc[1:,:]
        axs[nx].scatter(in_proc[:,1],labels,color=colors,marker='s')
        axs[nx].title.set_text('Speech Analysis')
        nx=nx+1
    plt.show()
    return
"""
src_files = glob.iglob("/home/anam/Desktop/mpi_testing/video/252447/*.mp4")

for src in src_files:

    filename,ext = os.path.splitext (src)
    out_file = filename + ".wav"
    extractor(src,out_file)

    


audio_files = glob.glob("/home/anam/Desktop/mpi_testing/audio/252447/*.mp3")
print(audio_files)
for aud_file in audio_files:
    filename,ext = os.path.splitext (aud_file)
    out_file = filename + ".wav"
    converter(aud_file,out_file)

base_dir = "/home/anam/Desktop/mpi_testing/Comparator"
Comparator(base_dir,2,"MPILab_0001_252447_01_S_Audio","MPILab_0001_252447_02_P_Video")
"""
src_file = '/home/anam/Desktop/OutdoorSamplesMPI/00000_00000020201016142243_0001A.mp4'
filename,ext = os.path.splitext(src_file)
out_file = filename + ".wav"
extractor(src_file,out_file)
src = '/home/anam/Desktop/OutdoorSamplesMPI/191016_1319.mp3'
file_name,ext = os.path.splitext(src)
out_file = file_name + ".wav"
converter(src,out_file)
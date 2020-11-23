import os
import sys
import sox
import numpy as np 
import pandas as pd
from scipy.io import wavfile

def rttm_data_extractor(rttm_file):
    rttm_data = pd.read_csv(rttm_file,
                        delimiter=' ',
                        names = ['Speaker','Audio_ID','Number','Onset','Duration','NA','NA-','Gender','Na','Na-'])
    #names = ['Speaker','Audio ID','Number','Onset','Duration','NA','NA-','Gender','Na','Na-']
    #Data = pd.DataFrame(rttm_data,columns=names)
    rttm_data.drop(['Speaker','Number','NA','NA-','Na','Na-'],axis=1,inplace=True)
    rttm_numpi = rttm_data.to_numpy()
    locs = np.where(rttm_numpi[:,3]=='CHI') 
    new_rttm_data = rttm_numpi[locs]
    time_stamps = new_rttm_data[:,1:3]
    rttm_data_frame = pd.DataFrame(data=new_rttm_data,columns=['Audio_ID','Onset','Duration','Gender'])
    return rttm_data_frame
def audio_trimmer(rttm_frame,aud_file,output_direc):
    
    for ind,row in rttm_frame.iterrows():
        tfm = sox.Transformer()
        aud_file_name , ext = os.path.splitext(aud_file)
        direc,aud_file_name = os.path.split(aud_file_name)
        start_t = row['Onset']
        dur = row['Duration']
        aud_file_name = aud_file_name + '_'+ str(start_t) + '.wav'
        op_path = os.path.join(output_direc,aud_file_name)
        end_t = start_t + dur
        tfm.trim(start_t,end_t)
        tfm.build(aud_file,op_path)

    return



######################################################################################################
rttm_base = '/home/anam/Codes/Audio_work/Data/Rttm_Data'
inp_base = '/home/anam/Desktop/Leipzig'
oup_base = '/home/anam/Desktop/Trimmed_Audio_Data'
for dirpath, subdirs, files in os.walk(inp_base):
    for x in files:
        if x.endswith(".wav"):
            aud_file = os.path.join(dirpath,x)
            out_direc = dirpath.replace(inp_base,oup_base)
            if not os.path.exists(out_direc):
                os.makedirs(out_direc)
            rttm_direc = dirpath.replace(inp_base,rttm_base)
            rttm_folder,ext = os.path.splitext(x)
            rttm_file = os.path.join(rttm_direc,rttm_folder)
            rttm_file = os.path.join(rttm_file,'all.rttm')
            rttm_frame = rttm_data_extractor(rttm_file)
            audio_trimmer(rttm_frame,aud_file,out_direc)




            
#######################################################################################################
"""
rttm_file = '/home/anam/Codes/Audio_work/test_data/all.rttm'
rttm_frame = rttm_data_extractor(rttm_file)
aud_file = '/home/anam/Desktop/Leipzig/AgeGroup_003/258640/Audio/MPILab_0001_258640_01_S_Audio.wav'
output_direc = '/home/anam/Codes/Audio_work/Data/Trimmed_Audio_Data/AgeGroup003/258640'
audio_trimmer(rttm_frame,aud_file,output_direc)

fs,data = wavfile.read('/home/anam/Desktop/Leipzig/AgeGroup_003/258640/Audio/MPILab_0001_258640_01_S_Audio.wav')
print (fs)
print (data)
print(len(data))
del_t = 1/fs
print(del_t)
print("\n")

sample_rate = sox.file_info.sample_rate('/home/anam/Desktop/Leipzig/AgeGroup_003/258640/Audio/MPILab_0001_258640_01_S_Audio.wav')
print(sample_rate)
n_samples = sox.file_info.num_samples('/home/anam/Desktop/Leipzig/AgeGroup_003/258640/Audio/MPILab_0001_258640_01_S_Audio.wav')
print(n_samples)
print("\n")
print(rttm_frame)
print("\n")
"""

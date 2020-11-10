import os
import matplotlib.pyplot as plt
import plotly.offline
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objs as go
import numpy as np
import pandas as pd

def Comparator(base_dir,n,*argv):
    nx=0
    for arg in argv:
        file_name = os.path.join(base_dir,arg)
        file_name = os.path.join(file_name,"all.rttm")
        print(file_name)
        In_file = np.genfromtxt(file_name,dtype=None,delimiter="\n",encoding=None).reshape(-1,1)
        in_proc = np.empty([1,4])
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
            n4 = n2+n3
            labels = np.append(labels,X[4])
            num = [n1,n2,n3,n4]
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
        df = pd.DataFrame(in_proc, columns = ['Num','Start','Duration','End'])
        df.insert(4,'Person',labels)
        df.insert(5,'Color',colors)
        fig = go.Figure(
            layout = {
                'barmode': 'stack',
                'xaxis': {'automargin':True},
                'yaxis': {'automargin':True}
            }
        )
        for character,character_df in df.groupby('Person'):
            fig.add_bar(x=character_df.Duration,
                        y=character_df.Person,
                        base = character_df.Start,
                        orientation = 'h',
                        showlegend = False,
                        name = character)

        fig.show()
        nx=nx+1
    
    return


base_dir = "/home/anam/Desktop/mpi_testing/Comparator"
Comparator(base_dir,2,"MPILab_0001_252447_01_S_Audio","MPILab_0001_252447_02_P_Video")
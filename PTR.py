# -*- coding: utf-8 -*-
"""
@author: Andrew Calhoun
         University of Illinois at Urbana-Champaign
Created on Sat Dec 8 2018
Last edited on Sat Jan 12 2019
"""

###This file is meant as a test realm for experimental ideas and tinkering
###that is not yet ready to be worked on in the main project files


import numpy as np
import pandas as pd
from tqdm import tqdm
from scipy.io import wavfile
import matplotlib.pyplot as plt

#from numba import jit
from definitions import ROOT_DIR,import_fnames


if __name__ == '__main__':

    fs,data = wavfile.read('C:/Users/Andrew/Desktop/Balcony_Mic_Recordings/kDA73#08.wav')

    print(data)
    print(len(data))

    amp = []
    for i in range(0,len(data)-1):
        diff = abs( data[i+1]-data[i] )
        amp.append(diff)

    #plt.plot( np.linspace(0,800000-500000-1,800000-500000) , abs(data[500000:800000]) )
    plt.plot( np.linspace(0,800000-500000-1,800000-500000) , abs(data[500000:800000]) )
    plt.show()

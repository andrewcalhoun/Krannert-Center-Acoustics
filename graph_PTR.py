# -*- coding: utf-8 -*-
"""
@author: Andrew Calhoun
         University of Illinois at Urbana-Champaign
Created on Jan 17 2019
Last edited on Jan 21 2019

This program is used to create graphs of pickled FFT sound data.
I recommend running this from the console, then you can resize the plot in the console
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

from Sound_Decay import import_pickle,import_fnames #no need to rewirte these functions here


def ask_freq():
    #asks the user for the desired frequency and returns the DataFrame index value associated with that frequency

    print('What Frequency?')
    freq_input = int(input()) #ask for the desired frequency

    if freq_input%20 == 0:
        freq = freq_input / 20 #take the frequency input and convert it into an equivalent DataFrame index value
    else:
        print('You must choose a frequency that is some integer multiple of 20')
        print('Freq automatically set to 440Hz')
        freq = 22 #automatically set the frequency if the users inputs a frequency not covered in the FFT program

    return freq


if __name__ == '__main__':

    pnames = import_fnames() # get a list of the filenames in the data folder

    freq = ask_freq() #ask for the desired frequency
    print('What file(numerical integer)?')
    fnum = int(input()) #ask for the file to graph (its number in alphabetical order)
    print(pnames[fnum])
    print('Dot or line (d/l)')
    gtype = input() #ask for the graph type

    if gtype == 'd':
        gtype = '.'
    elif gtype == 'l':
        gtype = ''

    df = import_pickle(pnames[fnum]) #import the pickled DataFrame from the desired file
    df = df[freq].T #get a nx1 table of just the desired frequency and transpose it to be 1xn

    ampf = df[0:4500] #cut the DataFrame down to just the time specified
    fname = pnames[fnum][0:-8]

    plt.plot(np.linspace(0,4501,4500),ampf,gtype) #plot the FFT amp data
    plt.title(str(fname) + ': ' + str(freq*20)[0:-2] + 'Hz')
    plt.show()

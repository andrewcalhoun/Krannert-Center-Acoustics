# -*- coding: utf-8 -*-
"""
@author: Andrew Calhoun
         University of Illinois at Urbana-Champaign
Created on Sat Jan 12 2019
Last edited on Sat Jan 12 2019
"""

###This file is used to calculate the rate of sound decay in recordings made in the Krannert Center Great Hall


import numpy as np
import pandas as pd
import sys
import os

from definitions import ROOT_DIR


def import_fnames():
    """This reads the data directory and creates a list of the file names"""

    dataDirectory = ROOT_DIR + "/Data"
    if len(sys.argv) > 1:
        dataDirectory = sys.argv[1]
    ### find all kDQ pickled files by recursively walking the data directory
    print("dataDirectory: "+dataDirectory)
    print("ROOT_DIR: "+ROOT_DIR)
    fnames = []
    for subdir, dirs, files in os.walk(dataDirectory):
        for filen in files:
            continue

    fnames = files
    print("fnames: "+fnames)

    return fnames


def import_pickle(pname):
    """Easy to call function to import pickled Pandas DataFrames"""

    data_master = pd.read_pickle(pname)
    return data_master


if __name__ == '__main__':

    pnames = import_fnames() #return all names of the kDQ FFT data directory

# -*- coding: utf-8 -*-
"""
@author: Andrew Calhoun
         University of Illinois at Urbana-Champaign
Created on Jan 12 2019
Last edited on Jan 17 2019
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

    return files


def import_pickle(pname):
    """Easy to call function to import pickled Pandas DataFrames"""

    pname = 'Data/'+pname #add the path into the filename
    data_master = pd.read_pickle(pname)
    data_master = data_master.T.reset_index(drop=True).T #reset the column index so we have integer indices

    return data_master


def main(fnum):
    """This takes the number assigned to the desired file and runs the analysis on it"""

    pnames = import_fnames() #return all names of the kDQ FFT data directory
    print(pnames)

    test = import_pickle(pnames[fnum])
    print(test)


if __name__ == '__main__':
    """"This runs the whole code for one file"""
    """This is broken up so Run.py can call main() across many files"""

    main()

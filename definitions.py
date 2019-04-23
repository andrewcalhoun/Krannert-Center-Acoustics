# -*- coding: utf-8 -*-
"""
@author: Andrew Calhoun
         University of Illinois at Urbana-Champaign
Created on Sat Jan 12 2019
Last edited on Sun Apr 21 2019
"""

###This file is to contain any important information that must be shared
###across multiple files in the Krannert-Center-Acoustics repository.


import os
import sys


ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) #Project root


def import_fnames(dataDirectory):
    """This reads a file directory and creates a list of the file names"""

    if len(sys.argv) > 1:
        dataDirectory = sys.argv[1]
    ### find all kDQ pickled files by recursively walking the data directory
    #print("dataDirectory: "+dataDirectory)
    #print("ROOT_DIR: "+ROOT_DIR)
    for subdir, dirs, files in os.walk(dataDirectory):
        for filen in files:
            continue

    return files

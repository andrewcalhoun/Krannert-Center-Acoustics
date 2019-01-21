# -*- coding: utf-8 -*-
"""
@author: Andrew Calhoun
         University of Illinois at Urbana-Champaign
Created on Jan 16 2019
Last edited on Jan 21 2019
"""


import Sound_Decay as sd
from tqdm import tqdm


if __name__ == '__main__':

    fnames = sd.import_fnames()
    print(fnames)

    for pname in tqdm(fnames):

        sd.main(fnames,0)

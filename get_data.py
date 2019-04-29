# -*- coding: utf-8 -*-
"""
@author: Andrew Calhoun
         University of Illinois at Urbana-Champaign
Created on Apr 28 2019
Last edited on Apr 28 2019
Much coding thanks to https://janakiev.com/blog/csv-in-python/
"""
import numpy as np
import csv
from definitions import ROOT_DIR

def get_data(seat_num,freq):
    """Takes a seat number and frequency value and returns the crms data for that frequency and seat"""


    data_path = ROOT_DIR+'/Data/crms/kDA'+seat_num[0:2]+'#'+seat_num[3:6]+'.csv'

    with open(data_path,'r') as f:
        reader = csv.reader(f, delimiter=',') #this code is taken from the website credited at the top
        headers = next(reader)
        data = list(reader)
        data = np.array(data).astype(float) #/end their code

        if freq == 220:
            i = [0,1,2]
        elif freq == 440:
            i = [3,4,5]
        elif freq == 880:
            i = [6,7,8]
        elif freq == 1760:
            i = [9,10,11]
        elif freq == 3520:
            i = [12,13,14]
        else:
            print('There was a frequency error in get_data')

        camp1 = data[i[0],1]
        camp2 = data[i[1],1]
        camp3 = data[i[2],1]

    return [camp1,camp2,camp3]

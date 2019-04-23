# -*- coding: utf-8 -*-
"""
@author: Andrew Calhoun
         University of Illinois at Urbana-Champaign
Created on Apr 21 2019
Last edited on Apr 23 2019
Much coding thanks to https://janakiev.com/blog/csv-in-python/
We have a directory of csv files(Data/crms) and we want to average the 220Hz rms and the 440Hz, etc.
And I want to create a text file that I can copy-paste into my interference code and tunr into a pandas DataFrame
"""

import numpy as np
import csv
from definitions import ROOT_DIR
from definitions import import_fnames

dir = ROOT_DIR+'/Data/crms'
fnames = import_fnames(dir)

print(dir)
endfile = [] #init a list that we can append all our averaged values to

for i in range(0,len(fnames)):
    data_path = dir+'/'+fnames[i] #get the path of the file we are averaging

    with open(data_path,'r') as f:
        reader = csv.reader(f, delimiter=',') #this code is taken from the website credited at the top
        headers = next(reader)
        data = list(reader)
        data = np.array(data).astype(float) #/end their code

        l220 = (data[0,1]+data[1,1]+data[2,1])/3 #average all 220 rms tone numbers
        l440 = (data[3,1]+data[4,1]+data[5,1])/3 #average all 440 rms tone numbers
        l880 = (data[6,1]+data[7,1]+data[8,1])/3 #average all 880 rms tone numbers
        l1760 = (data[9,1]+data[10,1]+data[11,1])/3 #etc
        l3520 = (data[12,1]+data[13,1]+data[14,1])/3

        line = [fnames[i][3:5]+','+fnames[i][6:8],l220,l440,l880,l1760,l3520] #create a list of all the info i want for each file; position,220,440,etc
                                                                                #eg. ['71,06',1.3,5.6,7.89,24.56,69,04]
        endfile.append(line) #append our data from one file to the overall list

text_file = open("averaged_crms.txt", "w") #create/open a text file
text_file.write(str(endfile)) #write our total data to the file
text_file.close() #safely close the file

print(endfile)

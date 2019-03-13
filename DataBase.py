# -*- coding: utf-8 -*-
"""
@author: Andrew Calhoun
         University of Illinois at Urbana-Champaign
Created on Mar 4 2019
Last edited on Mar 10 2019
"""


import pandas as pd


from definitions import ROOT_DIR,import_fnames


def kcoord(coord):

    rowdict = {'0':'AA','1':'A','4':'C','5':'D','7':'F','10':'J','13':'M',
            '15':'O','16':'P','19':'S','22':'V','25':'WW','28':'Y','30':'Z','31':'ZZ',
            '50':'AA','51':'A','54':'D','57':'G','61':'K','63':'M','66':'P',
            '69':'S','71':'AB','72':'AC','73':'AD','74':'AE','75':'AF',
            '76':'AG','77':'AH','78':'AJ'}

    i = str(int(coord[0]))
    y = coord[1]
    try:
        x = rowdict[i]
    except KeyError:
        print('Update rowdict immediately')
        print(str(coord)+'=(0,0)')
        x,y = '0','0'

    return x+str(y)


dataDirectory = ROOT_DIR+'/Data'

fnames = import_fnames()
header = pd.DataFrame(['Filename','Our Coordinates','Ticketed Spot','PCB Num','220Amp','440Amp','880Amp','1760Amp','3520Amp']).T

db = pd.read_csv('DataBase.csv')
dbfiles = db['0']


if __name__ == '__main__':
    for fname in fnames:
        counter = 0
        for item in dbfiles[1:]:
            if str(item) == (fname):
                counter += 1
            else:
                pass

        if counter == 0:
            coord = [ fname[3:5] , fname[6:8] ]
            row = pd.DataFrame([fname,coord,kcoord(coord)]).T
            db = db.T.reset_index(drop=True).T
            db = db.append(row,ignore_index=True)
        else:
            pass

    print(db)
    #db.to_csv('DataBase.csv')

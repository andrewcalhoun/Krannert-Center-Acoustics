# -*- coding: utf-8 -*-
"""
@author: Andrew Calhoun
         University of Illinois at Urbana-Champaign
Created on Apr 4 2019
Last edited on Apr 28 2019
"""


import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from definitions import ROOT_DIR
from get_data import get_data


seats = pd.DataFrame([['50,02',5388,3966,7.16915],['50,04',5421,3938,7.16915],['50,06',5454,3910,7.16915],['50,08',5487,3882,7.16915],['50,10',5520,3854,7.16915],['50,12',5553,3826,7.16915],
                      ['71,02',5577,3688,6.05155],['71,04',5590,3641,6.05155],['71,06',5602,3594,6.05155],['71,08',5615,3547,6.05155],['71,10',5628,3500,6.05155],['71,12',5641,3453,6.05155],
                      ['72,02',5565,3345,6.20395],['72,04',5574,3302,6.20395],['72,06',5583,3259,6.20395],['72,08',5592,3216,6.20395],['72,10',5601,3173,6.20395],['72,12',5610,3130,6.20395],['72,14',5619,3087,6.20395],
                      ['73,02',5526,3030,5.74675],['73,04',5570,2983,5.74675],['73,06',5578,2936,5.74675],['73,08',5586,2889,5.74675],['73,10',5594,2642,5.74675],
                      ['74,02',5550,2737,5.44195],['74,04',5555,2690,5.44195],['74,06',5560,2643,5.44195],['74,08',5565,2596,5.44195],['74,10',5570,2549,5.44195],
                      ['75,02',5532,2447,5.28955],['75,04',5534,2402,5.28955],['75,06',5536,2357,5.28955],['75,08',5539,2312,5.28955],['75,10',5541,2267,5.28955],
                      ['76,02',5513,2178,5.13715],['76,04',5513,2139,5.13715],['76,06',5513,2100,5.13715],['76,08',5513,2061,5.13715],['76,10',5513,2022,5.13715],['76,12',5513,1983,5.13715],
                      ['77,02',5483,1866,5.28955],['77,04',5482,1820,5.28955],['77,06',5480,1773,5.28955],['77,08',5479,1727,5.28955],['77,10',5478,1680,5.28955],['77,12',5476,1634,5.28955],
                      ['78,02',5449,1554,5.59435],['78,04',5446,1513,5.59435],['78,06',5442,1472,5.59435],['78,08',5438,1431,5.59435],['78,10',5434,1390,5.59435],['78,12',5431,1350,5.59435]]) #734' +
                      #seat numbers and their x/y coordinates from the speaker
                      #x and y are in px and z is in meters

"""control_amp = pd.DataFrame(
[['50,02',34.36829873221232,33.63709765752245,34.14650244812518,31.126910378755273,18.974114075390236],['50,04',34.44522340141297,33.87810348863756,34.11112697804574,31.304100973584685,20.341106602438987],['50,06',34.51132161461205,34.07799992940128,33.78909691626572,30.890895529335836,20.49253858361509],['50,08',34.37866203235057,34.138713479500886,33.74994448553672,32.31793465102539,25.842634760984136],['50,10',34.83316735183677,33.50412441707899,33.66116966564869,31.215036680717517,24.799666959787203],['50,12',34.14069021386735,33.72197853760362,34.002284031320876,31.171212502889656,25.02591084163573],
['71,02',34.552509188358165,34.12957192285656,34.1222441547068,31.89412766458135,26.583440840424213],['71,04',34.08182021096324,33.73796299843532,32.89954938269791,31.21359163858737,27.892143043235183],['71,06',34.20009487252534,33.75818591947185,32.96031988806842,31.59902063641593,24.888438416406114],['71,08',34.10304007288187,33.792429931956526,33.0051116719151,31.848670360296637,19.26821774303133],['71,10',34.213428620938146,33.82027886649036,33.49842450202019,31.5896782878782,16.895774651406573],['71,12',34.26322223230798,33.896492290328354,33.8169129117389,30.956777145903686,15.643748595601979],
['72,02',34.0704163129031,33.84496997011928,33.933761400992005,31.09263595097828,15.462456141914657],['72,04',33.977897047925,33.80866756213175,33.83716906787797,32.14794011917329,16.423409632288948],['72,06',34.2026358841733,33.62877520971292,33.68415580351412,31.24066529532303,15.84791562492969],['72,08',34.017755194742804,33.77721448569512,33.65050949748919,32.195054627504526,16.16412169481948],['72,10',33.95542194973033,33.86102659950843,33.481829655122894,32.11442463534856,16.80879378640933],['72,12',34.01527692743862,33.97871878863936,33.868796819676525,32.27251631984032,16.773700735218856],['72,14',34.010033768164476,33.739544877425395,33.65568550723588,31.31375336294154,16.973253876597155],
['73,02',34.154393529322604,33.587230321977174,33.628552809931904,31.230435335715583,14.126118716092302],['73,04',34.08403054818137,34.13721933166125,34.371237518358015,31.62282233263025,17.705025183870372],['73,06',34.08837941962866,34.01846495546206,33.75957575736831,31.03867646155673,17.319825332008364],['73,08',34.12665503675393,34.07337012327044,33.237279165488374,32.07067164010365,15.51919800349936],['73,10',33.88811122888433,33.83542997837977,33.61469082947239,31.232167476901555,15.066654059628762],
['74,02',34.13702238957084,33.5591338884035,33.65748490155618,31.045490599851643,14.39060968943697],['74,04',34.004856981220996,33.64437336657496,33.11059875137973,31.270370237110267,13.085983559244168],['74,06',33.87684323588503,33.42294928075557,33.924234549193244,30.570074801193055,13.882830994422605],['74,08',33.85673694030927,33.438453136117076,33.567210439050804,32.87911941082722,23.08347388850147],['74,10',33.921188153887734,33.5165397355469,33.181138333823164,30.50235966112129,26.06907825331616],
['75,02',33.97912022000583,33.44633544121484,33.174096434417756,30.468314011180595,27.863730533451307],['75,04',33.893216782641865,33.46168135415376,33.59258588083667,31.32702427776421,20.448345567359397],['75,06',33.9467564396651,33.48669904751038,33.31531122078206,30.819226044321866,19.24875693103766],['75,08',17.775252862090525,30.344422217279618,33.91382841983653,31.038677272306472,10.771682850739046],['75,10',18.32329873970222,30.99542832994943,33.77521261803849,31.274724492512775,12.038318080279888],
['76,02',17.945016187111282,30.318433278607532,33.93299680149861,31.834216435686002,12.139410787315454],['76,04',18.19814100728527,30.035186632174135,34.014985159966635,31.796709116232154,14.583746209387003],['76,06',18.357669071240085,30.443471027654052,33.88044099541727,31.891001793483756,13.915243296939726],['76,08',18.334878188911333,29.531826684939148,33.610192126908395,31.503587242064654,14.156277883241524],['76,10',17.8743071846868,28.934778477225592,33.59229963177932,31.914993896643978,14.874165276093121],['76,12',18.943588624644836,29.142828784722184,33.56387729824388,30.88686218566369,14.451705323236775],
['77,02',18.193903057749694,30.0437020047154,33.74510902438884,32.511715603062136,14.619092496420636],['77,04',18.12439244036089,30.27199194431238,33.863854233343325,31.713761801378666,14.29361533463382],['77,06',17.897063786915936,29.143989916441416,33.85194657111382,30.73351638303444,12.45713585135429],['77,08',17.792248633172463,28.033903991210398,33.76499300374255,31.9807070475064,12.990931175092646],['77,10',18.527456337071964,29.44853477923478,33.538237206064316,31.141683419947707,12.826395827176457],['77,12',18.228243528177476,29.22198781921791,33.64261866065041,31.66200192404496,13.051165605576635],
['78,02',17.830545027793466,28.341896964077097,33.86991696046459,32.136512041916866,13.293004836783645],['78,04',18.93563082285607,28.867510373038584,33.3718516974052,31.624743661956654,12.873302170829417],['78,06',19.017027322715872,30.44072909358427,33.74379737828621,31.286870658493388,12.681381112983056],['78,08',17.707407260361485,28.504864765871712,33.61692785639331,31.27200014875304,12.422523546199239],['78,10',18.45504449547843,28.488991766499975,33.508583695606184,31.178867994879266,12.166365427822491],['78,12',17.674412891810125,28.569128510132156,33.06120468439372,30.592719428074275,11.711473566904893]])
#averaged rms amplitudes from the shure microphone on stage

scaled_amp_bounce = pd.DataFrame([['50,02',0.0,0.0,0.0,0.0,0.0],['50,04',0.0,0.0,0.0,0.0,0.0],['50,06',0.0,0.0,0.0,0.0,0.0],['50,08',0.0,0.0,0.0,0.0,0.0],['50,10',0.0,0.0,0.0,0.0,0.0],['50,12',0.0,0.0,0.0,0.0,0.0],
                                ['71,02',0.0,0.0,0.0,0.0,0.0],['71,04',0.0,0.0,0.0,0.0,0.0],['71,06',0.0,0.0,0.0,0.0,0.0],['71,08',0.0,0.0,0.0,0.0,0.0],['71,10',0.0,0.0,0.0,0.0,0.0],['71,12',0.0,0.0,0.0,0.0,0.0],
                                ['72,02',0.0,0.0,0.0,0.0,0.0],['72,04',0.0,0.0,0.0,0.0,0.0],['72,06',0.0,0.0,0.0,0.0,0.0],['72,08',0.0,0.0,0.0,0.0,0.0],['72,10',0.0,0.0,0.0,0.0,0.0],['72,12',0.0,0.0,0.0,0.0,0.0],['72,14',0.0,0.0,0.0,0.0,0.0],
                                ['73,02',0.0,0.0,0.0,0.0,0.0],['73,04',0.0,0.0,0.0,0.0,0.0],['73,06',0.0,0.0,0.0,0.0,0.0],['73,08',0.0,0.0,0.0,0.0,0.0],['73,10',0.0,0.0,0.0,0.0,0.0],
                                ['74,02',0.0,0.0,0.0,0.0,0.0],['74,04',0.0,0.0,0.0,0.0,0.0],['74,06',0.0,0.0,0.0,0.0,0.0],['74,08',0.0,0.0,0.0,0.0,0.0],['74,10',0.0,0.0,0.0,0.0,0.0],
                                ['75,02',0.0,0.0,0.0,0.0,0.0],['75,04',0.0,0.0,0.0,0.0,0.0],['75,06',0.0,0.0,0.0,0.0,0.0],['75,08',0.0,0.0,0.0,0.0,0.0],['75,10',0.0,0.0,0.0,0.0,0.0],
                                ['76,02',0.0,0.0,0.0,0.0,0.0],['76,04',0.0,0.0,0.0,0.0,0.0],['76,06',0.0,0.0,0.0,0.0,0.0],['76,08',0.0,0.0,0.0,0.0,0.0],['76,10',0.0,0.0,0.0,0.0,0.0],['76,12',0.0,0.0,0.0,0.0,0.0],
                                ['77,02',0.0,0.0,0.0,0.0,0.0],['77,04',0.0,0.0,0.0,0.0,0.0],['77,06',0.0,0.0,0.0,0.0,0.0],['77,08',0.0,0.0,0.0,0.0,0.0],['77,10',0.0,0.0,0.0,0.0,0.0],['77,12',0.0,0.0,0.0,0.0,0.0],
                                ['78,02',0.0,0.0,0.0,0.0,0.0],['78,04',0.0,0.0,0.0,0.0,0.0],['78,06',0.0,0.0,0.0,0.0,0.0],['78,08',0.0,0.0,0.0,0.0,0.0],['78,10',0.0,0.0,0.0,0.0,0.0],['78,12',0.0,0.0,0.0,0.0,0.0]])
#init placeholder scaled array for the amplitudes based off a "one bounce model"

scaled_amp_direct = pd.DataFrame([['50,02',0.0,0.0,0.0,0.0,0.0],['50,04',0.0,0.0,0.0,0.0,0.0],['50,06',0.0,0.0,0.0,0.0,0.0],['50,08',0.0,0.0,0.0,0.0,0.0],['50,10',0.0,0.0,0.0,0.0,0.0],['50,12',0.0,0.0,0.0,0.0,0.0],
                                  ['71,02',0.0,0.0,0.0,0.0,0.0],['71,04',0.0,0.0,0.0,0.0,0.0],['71,06',0.0,0.0,0.0,0.0,0.0],['71,08',0.0,0.0,0.0,0.0,0.0],['71,10',0.0,0.0,0.0,0.0,0.0],['71,12',0.0,0.0,0.0,0.0,0.0],
                                  ['72,02',0.0,0.0,0.0,0.0,0.0],['72,04',0.0,0.0,0.0,0.0,0.0],['72,06',0.0,0.0,0.0,0.0,0.0],['72,08',0.0,0.0,0.0,0.0,0.0],['72,10',0.0,0.0,0.0,0.0,0.0],['72,12',0.0,0.0,0.0,0.0,0.0],['72,14',0.0,0.0,0.0,0.0,0.0],
                                  ['73,02',0.0,0.0,0.0,0.0,0.0],['73,04',0.0,0.0,0.0,0.0,0.0],['73,06',0.0,0.0,0.0,0.0,0.0],['73,08',0.0,0.0,0.0,0.0,0.0],['73,10',0.0,0.0,0.0,0.0,0.0],
                                  ['74,02',0.0,0.0,0.0,0.0,0.0],['74,04',0.0,0.0,0.0,0.0,0.0],['74,06',0.0,0.0,0.0,0.0,0.0],['74,08',0.0,0.0,0.0,0.0,0.0],['74,10',0.0,0.0,0.0,0.0,0.0],
                                  ['75,02',0.0,0.0,0.0,0.0,0.0],['75,04',0.0,0.0,0.0,0.0,0.0],['75,06',0.0,0.0,0.0,0.0,0.0],['75,08',0.0,0.0,0.0,0.0,0.0],['75,10',0.0,0.0,0.0,0.0,0.0],
                                  ['76,02',0.0,0.0,0.0,0.0,0.0],['76,04',0.0,0.0,0.0,0.0,0.0],['76,06',0.0,0.0,0.0,0.0,0.0],['76,08',0.0,0.0,0.0,0.0,0.0],['76,10',0.0,0.0,0.0,0.0,0.0],['76,12',0.0,0.0,0.0,0.0,0.0],
                                  ['77,02',0.0,0.0,0.0,0.0,0.0],['77,04',0.0,0.0,0.0,0.0,0.0],['77,06',0.0,0.0,0.0,0.0,0.0],['77,08',0.0,0.0,0.0,0.0,0.0],['77,10',0.0,0.0,0.0,0.0,0.0],['77,12',0.0,0.0,0.0,0.0,0.0],
                                  ['78,02',0.0,0.0,0.0,0.0,0.0],['78,04',0.0,0.0,0.0,0.0,0.0],['78,06',0.0,0.0,0.0,0.0,0.0],['78,08',0.0,0.0,0.0,0.0,0.0],['78,10',0.0,0.0,0.0,0.0,0.0],['78,12',0.0,0.0,0.0,0.0,0.0]])
#init placeholder scaled array for the amplitudes based off the direct wave interference
This whole comment has been depreciated
"""

freqs = [220,440,880,1760,3520] #list of frequencies tested
convert = 0.01214782608 #m/px #conversion factor for px to meters

speaker1_px = [4801,1546,0] #dummy variable for now, z axis should always be zero
speaker2_px = [4725,1546,0] #dummy variable for now, z axis should always be zero

def wavelength(freq):
    """simple function to convert frequency values to wavlength in meters"""
    return 343/freq


def direct_interference(camp,seat,speaker1_px,speaker2_px,freq):
    """Function to find the interference of two speakers at a given location"""
    """variables seat, speaker1, and speaker2 should be a 1x3 vector in units (px,px,m)"""
    t2 = time.time() #find the start time so we can see how long this fucntion takes to run

    x1 = abs(seat[0]-speaker1_px[0])*convert #x,y and z differences between speaker1_px and the seat
    y1 = abs(seat[1]-speaker1_px[1])*convert #convert x and y to meters
    z1 = abs(seat[2]-speaker1_px[2])
    x2 = abs(seat[0]-speaker2_px[0])*convert #x,y and z differences between speaker2 and the seat
    y2 = abs(seat[1]-speaker2_px[1])*convert #convert x and y to meters
    z2 = abs(seat[2]-speaker2_px[2])

    L1 = np.sqrt(x1**2 + y1**2 + z1**2) #calc the direct distance between speaker1_px and the seat in meters
    L2 = np.sqrt(x2**2 + y2**2 + z2**2) #calc the direct distance between speaker2 and the seat in meters
    dL = abs(L1 - L2) #calc the difference between the two distances

    omega = ( (2*np.pi)*dL ) / wavelength(freq) #find the number of wavelengths off the wave from speaker2 is

    factor = 2 #1 for 1/r falloff and 2 for 1/r^2 falloff
    direct_amp = ( camp/(L1**factor) ) + ( camp/(L2**factor) ) * np.cos(omega) #scale the amplitude as a factor of 1/r^2 and account for the phase shift of the second wave

    print( 'direct_int time: '+str(time.time()-t2) ) #print thte calculation time

    return direct_amp #return the scaled amplitude


def generate_walls():
    """This function generates graphable lists of the x/y coordinates of the wall boundaries of the krannert main floor"""
    """This only generates the coordinates of the north side wall"""
    t1 = time.time() #this function can take a while to run so we ask for the start time
    file = ROOT_DIR+'/new_mainOverlay.png' #this is the png overlay of the walls, generated in gimp using the architechtural drawings
    img = Image.open(file) #open the image using the PIL module
    imgarray = np.asarray(img) #convert this image to a numpy array

    imgx = np.flip(np.linspace(3500,5000,1499)) #these are the x-vals we want to look over
                                                #this is fliped so we look from the inside out
                                                #it would take too long to look at all x-vals
    wallx = [] #init the final x-val list
    wally = [] #init the final y-val list
    for i in range(1220,4060): #look over all the y-vals in the image that are useful (the beginning and end of the image is just a sea of black)
        bufferx = [] #reset the per line list
        buffery = [] #need the y because we need
        for u in imgx:
            x = int(u) #make sure these values are integers (np.linspace create vals like 3.0 and 15.0)
            y = int(i)
            if imgarray[y,x] != 0:
                bufferx.append(x) #append the first nonzero x-val in each line starting from the center and moving out
                buffery.append(y) #append its associated y-val
            else:
                continue #pass values that are 0
        wallx.append(bufferx[0]) #append the first nonzero x-value in each line to the total list
        wally.append(buffery[0]) #append the y-val as well

    print('generate_walls time: '+str(time.time()-t1)) #print how long this shit took
    return [wallx,wally] #return our lists of the walls x/y values


def angle(slope):
    """This takes the slope of our line and returns its angle relative to the x-axis
    m=0 would return 0 and if the line were vertical the it would return pi/2"""
    return np.arctan(slope) #arctan because soh cah [toa] opposite/adjacent is also rise/run. Convenient!


def normal(vary_num,wallx,wally):

    buff = 20 #number of points to on either side of the central point to fit to
    fit = np.polyfit(wallx[vary_num-buff:vary_num+buff],wally[vary_num-buff:vary_num+buff],1)

    normal = -1/(fit[0])

    return [angle(normal),normal]


def plot_norm(final_num,wallx,wally):
    [angle,norm] = normal(final_num,wallx,wally)
    x = [wallx[final_num],wallx[final_num]+1]
    y = [wally[final_num],wally[final_num]+norm]
    fit = np.polyfit(x,y,1)

    return fit


def vary(walls,seat_px,speaker_px):

    [wallx,wally] = walls
    dAngle = []
    for vary_num in range(20,len(wally)-20):
        vary_point = [ wallx[vary_num],wally[vary_num] ]
        line1 = np.polyfit((speaker_px[0],vary_point[0]),(speaker_px[1],vary_point[1]),1)
        line2 = np.polyfit((seat_px[0],vary_point[0]),(seat_px[1],vary_point[1]),1)
        angle1 = angle(line1[0])
        angle2 = angle(line2[0])
        [norm_angle,norm] = normal(vary_num,wallx,wally)

        incident_angle = abs(norm_angle-angle1)
        reflected_angle = abs(angle2-norm_angle)
        dAngle.append([abs(incident_angle - reflected_angle),vary_num])


    dAngle.sort()
    final_num = dAngle[0][1]
    final_point = [ wallx[final_num],wally[final_num] ]
    #returns in px
    return final_point #this is a tuple, see 2 blocks prior


def vary_plot(seat,speaker):
    """Same code as vary() but with plotting functionality"""
    [wallx,wally] = generate_walls()
    dAngle = []
    for vary_num in range(20,len(wally)-20):
        vary_point = [ wallx[vary_num],wally[vary_num] ]
        print('vary_num: '+str(vary_num))
        print('vary_point: '+str(vary_point))
        line1 = np.polyfit((speaker[0],vary_point[0]),(speaker[1],vary_point[1]),1)
        line2 = np.polyfit((seat[0],vary_point[0]),(seat[1],vary_point[1]),1)
        angle1 = angle(line1[0])
        angle2 = angle(line2[0])
        [norm_angle,norm] = normal(vary_num,wallx,wally)

        incident_angle = abs(norm_angle-angle1)
        reflected_angle = abs(angle2-norm_angle)
        dAngle.append([abs(incident_angle - reflected_angle),vary_num])


    dAngle.sort()
    final_num = dAngle[0][1]
    final_point = [ wallx[final_num],wally[final_num] ]

    """First new stuff from vary()"""
    finline1 = np.polyfit((speaker[0],final_point[0]),(speaker[1],final_point[1]),1) #fit a line from the speaker to the final point
    finline2 = np.polyfit((seat[0],final_point[0]),(seat[1],final_point[1]),1) #fit a line from the seat to the final point


    plt.plot(wallx,wally) #plot the walls
    fit1 = np.poly1d(finline1) #create the function for the speaker line
    fit2 = np.poly1d(finline2) #create the function for the seat line
    normfit = np.poly1d( plot_norm(final_num,wallx,wally) ) #create the function for the normal line
    x = np.linspace(0,1999,2000)
    plt.plot(x,fit1(x)) #plot the speaker straight line
    plt.plot(x,fit2(x)) #plot the seat straight line
    plt.plot(x,normfit(x)) #plot the seat normal line
    plt.plot(seat[0],seat[1],'o') #plot the seat position as a dot
    plt.plot(speaker[0],speaker[1],'o') #plot the speaker position as a dot
    plt.plot(final_point[0],final_point[1],'o') #plot the final point position as a dot
    plt.show() #show dat shit


def z_axis(vp_x,seat,speaker):
    #vp_x in px

    a = 1/( (speaker[0]-vp_x)*convert )
    b = 1/( (seat[0]-vp_x)*convert )
    c = seat[2]/( (seat[0]-vp_x)*convert )

    vp_z = c / (a+b)
    #returns meters
    return vp_z


def distance(start,end):
    #everything should be in meters
    #start and end are both 1x3 vectors (x,y,z)
    x = abs( end[0]-start[0] )
    y = abs( end[1]-start[1] )
    z = abs( end[2]-start[2] )

    dist = np.sqrt( x**2 + y**2 + z**2 )

    return dist


def second_wave(walls,seat_px,speaker_px):
    #seat_px and speaker_px are in (px,px,m)
    [vp_x,vp_y] = vary(walls,seat_px,speaker_px) #get the vary_point x and y coordinates in px
    vp_z = z_axis(vp_x,seat_px,speaker_px) #get the vary_point z coordinate in meters

    vp = [vp_x*convert,vp_y*convert,vp_z] #convert the x and y coordinates to meters

    seat_m = [seat_px[0]*convert,seat_px[1]*convert,seat_px[2]] #everything in meters
    speaker_m = [speaker_px[0]*convert,speaker_px[1]*convert,speaker_px[2]] #everything in meters

    dist1 = distance(speaker_m,vp)
    dist2 = distance(vp,seat_m)

    #returns meters
    return (dist1+dist2)


def mult_interference(walls,camp,seat_px,speaker1_px,speaker2_px,freq):
    #seat_px and speaker1/2 are in units (px,px,m)
    time_start = time.time()

    swave1 = second_wave(walls,seat_px,speaker1_px) #distance in meters
    swave2 = second_wave(walls,seat_px,speaker2_px) #distance in meters

    seat_m = [seat_px[0]*convert,seat_px[1]*convert,seat_px[2]] #seat position in meters , z entry should be zero
    speaker1_m = [speaker1_px[0]*convert,speaker1_px[1]*convert,speaker1_px[2]] #speaker1_px position in meters , z entry should be zero
    speaker2_m = [speaker2_px[0]*convert,speaker2_px[1]*convert,speaker2_px[2]] #speaker2_px position in meters , z entry should be zero

    pwave1 = distance(seat_m,speaker1_m) #distance in meters
    pwave2 = distance(seat_m,speaker2_m) #distance in meters

    dL1 = abs(pwave1 - pwave2) #distance differences
    dL2 = abs(pwave1 - swave1)
    dL3 = abs(pwave1 - swave2)


    lamb = wavelength(freq)
    omega1 = ( (2*np.pi)*dL1 ) / lamb #find the number of wavelengths off the wave from speaker2 is
    omega2 = ( (2*np.pi)*dL2 ) / lamb
    omega3 = ( (2*np.pi)*dL3 ) / lamb

    factor = 2 #1 for 1/r falloff and 2 for 1/r^2 falloff
    scaled_amp_bounce = (camp/(pwave1**factor)) + (( camp/(pwave2**factor) )*np.cos(omega1)) + (( camp/(swave1**factor) )*np.cos(omega2)) + (( camp/(swave2**factor) )*np.cos(omega3))

    print( 'mult_int time: '+str(time.time()-time_start) )

    return scaled_amp_bounce

if __name__ == '__main__':

    print('')
    start_time = time.time()

    walls = generate_walls()

    for i in range(0,len(seats)): #loop over all seats (50ish)
        srms = pd.DataFrame([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]],index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],columns=['Scaled Amp','Nothing','Also Nothing'])
        for u in range(0,len(freqs)): #loop over all frequencies (5)

            seat_num = seats[0][i] #get the seat number from the seat dataframe
            seat_px = [seats[1][i],seats[2][i],seats[3][i]] #get the x/y/z coordinates of the seat from the seat dataframe

            print( 'seat num: '+str(seats[0][i]) )
            print('seat position:')             #Print Helpful info
            print(seat_px)

            camps = get_data(seat_num,freqs[u]) #Takes from the crms, the three camps from the seat and frequency specified, then divides each of them by 2

            print( 'frequency:'+str(freqs[u]) )
            print('camps: ')
            print(camps)

            for s in range(0,len(camps)): #loop over all tones in each frequency (3)
                samp = mult_interference(walls,camps[s],seat_px,speaker1_px,speaker2_px,freqs[u]) #find the scaled amplitude, seat_px/speaker1,speaker2 are in (px,px,m)
                print('samp: '+str(samp)) #print helpful info
                print('seat px: ')
                print(seat_px)
                print('')
                srms.at[1+(3*u)+s,'Scaled Amp'] = abs(samp) #add the scaled amplitude value to the dataframe
            print('')
        srms.to_csv(ROOT_DIR+'/Data/srms_bounce/kDA'+seat_num[0:2]+'#'+seat_num[3:6]+'.csv') #save a new dataframe for every seat, with the file name as the seat info

    for i in range(0,len(seats)):
        srms_direct = pd.DataFrame([[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0],[0.0,0.0,0.0]],index=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],columns=['Scaled Amp','Nothing','Also Nothing'])
        for u in range(0,len(freqs)):

            seat_num = seats[0][i] #get the seat number from the seat dataframe
            seat_px = [seats[1][i],seats[2][i],seats[3][i]] #get the x/y/z coordinates of the seat from the seat dataframe


            camps = get_data(seat_num,freqs[u]) #Takes from the crms, the three camps from the seat and frequency specified, then divides each of them by 2

            for s in range(0,len(camps)): #loop over all tones in each frequency (3)
                samp = direct_interference(camps[s],seat_px,speaker1_px,speaker2_px,freqs[u]) #find the scaled amplitude, seat_px/speaker1,speaker2 are in (px,px,m)
                print('samp: '+str(samp)) #print helpful info
                print('seat px: ')
                print(seat_px)
                print('')
                srms_direct.at[1+(3*u)+s,'Scaled Amp'] = abs(samp) #abs(samp) #add the scaled amplitude value to the dataframe
                print(str(1+(3*u)+s))
                #time.sleep(5)
            print('')
        srms_direct.to_csv(ROOT_DIR+'/Data/srms_direct/kDA'+seat_num[0:2]+'#'+seat_num[3:6]+'.csv') #save a new dataframe for every seat, with the file name as the seat info


    print('Total Time: '+str(time.time()-start_time))

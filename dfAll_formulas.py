# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:28:43 2017

@author: ehindinger
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:16:19 2017

@author: ehindinger
"""

import pandas as pd
import numpy as np
import seaborn as sns
import os
import itertools as it
from natsort import natsorted
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import random
from scipy import stats


def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret  # [n - 1:] / n


def getRandomFiles(path):
    '''Returns a random filename, chosen among the files of the given path.'''
    files = os.listdir(path)
    file_list = []
    for i in range(19):
        index = random.randrange(0, len(files))
        a = files[index]
        file_list.append(a)
    return file_list


one1 = [1] * 30
one2 = [2] * 30
one3 = [3] * 30
one4 = [4] * 30
one5 = [5] * 30
one6 = [6] * 30
one7 = [7] * 30
one8 = [8] * 30
one9 = [9] * 30
one10 = [10] * 30
one11 = [11] * 30
one12 = [12] * 30
one13 = [13] * 30
one14 = [14] * 30
one15 = [15] * 30
one16 = [16] * 30
one17 = [17] * 30
one18 = [18] * 30
one19 = [19] * 30
one20 = [20] * 30
one21 = [21] * 30
one22 = [22] * 30
one23 = [23] * 30
one24 = [24] * 30
one25 = [25] * 30
one26 = [26] * 30
one27 = [27] * 30
one28 = [28] * 30
one29 = [29] * 30
one30 = [30] * 30
one31 = [31] * 30
one32 = [32] * 30
one33 = [33] * 30
one34 = [34] * 30
one35 = [35] * 30
one36 = [36] * 30
one37 = [37] * 30
one38 = [38] * 30
one39 = [39] * 30
one40 = [40] * 30
one41 = [41] * 30
one42 = [42] * 30
one43 = [43] * 30
one44 = [44] * 30
one45 = [45] * 30
one46 = [46] * 30
one47 = [47] * 30
one48 = [48] * 30
one49 = [49] * 30
one50 = [50] * 30
one51 = [51] * 30
one52 = [52] * 30
one53 = [53] * 30
one54 = [54] * 30
one55 = [55] * 30
one56 = [56] * 30
one57 = [57] * 30
one58 = [58] * 30
one59 = [59] * 30
one60 = [60] * 30

second = list(it.chain(one1, one2, one3, one4, one5, one6, one7, one8, one9,
                       one10, one11, one12, one13, one14, one15, one16, one17,
                       one18, one19, one20, one21, one22, one23, one24, one25,
                       one26, one27, one28, one29, one30, one31, one32, one33,
                       one34, one35, one36, one37, one38, one39, one40, one41,
                       one42, one43, one44, one45, one46, one47, one48, one49,
                       one50, one51, one52, one53, one54, one55, one56, one57,
                       one58, one59, one60))
seconds = second * 8

min1 = [1] * 1800
min2 = [2] * 1800
min3 = [3] * 1800
min4 = [4] * 1800
min5 = [5] * 1800
min6 = [6] * 1800
min7 = [7] * 1800
min8 = [8] * 1800

minute = list(it.chain(min1, min2, min3, min4, min5, min6, min7, min8))

light = ['L'] * 1800
dark = ['D'] * 1800

condition = list(it.chain(light, dark, light, dark, light, dark, light, dark))

    expo = []
    for x in range(1, 461):
        n = [x] * 46080
        expo = list(it.chain(expo, n))
    df = all_traces.copy()
    
def buildfish(directory, index):
    '''
    This function reads three csv files: pre-treatment, 1h incubation and
    24h incubation. It reads only column H distance, concats, then turns
    into a pivot table for multi-indexing
    '''
    pre = os.listdir(directory + '/20 conc/pre-treatment files')
    inc_1h = os.listdir(directory + '/20 conc/1h incubation files')
    inc_24h = os.listdir(directory + '/20 conc/24h incubation files')

    # choose appropriate filepaths
    filepath0 = directory + '/20 conc/pre-treatment files/' + pre[index]
    filepath1 = directory + '/20 conc/1h incubation files/' + inc_1h[index]
    filepath24 = directory + '/20 conc/24h incubation files/' + inc_24h[index]
    # read spreadsheet and turn into df
    df1 = pd.read_csv(filepath0, skiprows=35, skipfooter=8, engine='python')
    if len(df1.columns) == 9:
        df1 = df1.drop(df1.columns[[0, 1, 2, 3, 4, 5, 6, 8]], axis=1)
    elif len(df1.columns) == 12:
        df1 = df1.drop(df1.columns[[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]], axis=1)
    # change column name
    df1.columns = ['dist0']
    # replaces all dashes by 0
    df1 = df1.replace(to_replace='-', value=0, regex=True)
    # changes data frame column type to float
    df1 = df1.astype(np.float)

    # read spreadsheet and turn into df
    df2 = pd.read_csv(filepath1, skiprows=35, skipfooter=8, engine='python')
    # drop all unnecessary columns
    if len(df2.columns) == 9:
        df2 = df2.drop(df2.columns[[0, 1, 2, 3, 4, 5, 6, 8]], axis=1)
    elif len(df2.columns) == 12:
        df2 = df2.drop(df2.columns[[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]], axis=1)
    # change column name
    df2.columns = ['dist1']
    # replaces all dashes by 0
    df2 = df2.replace(to_replace='-', value=0, regex=True)
    # changes data frame column type to float
    df2 = df2.astype(np.float)

    # read spreadsheet and turn into df
    df3 = pd.read_csv(filepath24, skiprows=35, skipfooter=8, engine='python')
    # drop all unnecessary columns
    if len(df3.columns) == 9:
        df3 = df3.drop(df3.columns[[0, 1, 2, 3, 4, 5, 6, 8]], axis=1)
    elif len(df3.columns) == 12:
        df3 = df3.drop(df3.columns[[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]], axis=1)
    # change column name
    df3.columns = ['dist24']
    # replaces all dashes by 0
    df3 = df3.replace(to_replace='-', value=0, regex=True)
    # changes data frame column type to float
    # df3['dist 24'] = df3['dist 24'].apply(pd.to_numeric)
    df3 = df3.astype(np.float)

    df = pd.concat([df1, df2, df3], axis=1)

    # adds seconds and minute column
    df['second'] = seconds
    df['minute'] = minute
    df['condition'] = condition

    return df


def buildfish7(directory, index):
    '''
    This function reads three csv files: pre-treatment, 1h incubation and
    24h incubation. It reads only column H distance, concats, then turns
    into a pivot table for multi-indexing
    '''
    pre = os.listdir(directory + '/7 conc/pre-treatment files')
    inc_1h = os.listdir(directory + '/7 conc/1h incubation files')
    inc_24h = os.listdir(directory + '/7 conc/24h incubation files')

    # choose appropriate filepaths
    filepath0 = directory + '/7 conc/pre-treatment files/' + pre[index]
    filepath1 = directory + '/7 conc/1h incubation files/' + inc_1h[index]
    filepath24 = directory + '/7 conc/24h incubation files/' + inc_24h[index]
    # read spreadsheet and turn into df
    df1 = pd.read_csv(filepath0, skiprows=35, skipfooter=8, engine='python')
    # drop all unnecessary columns
    df1 = df1.drop(df1.columns[[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]], axis=1)
    # change column name
    df1.columns = ['dist0']
    # replaces all dashes by 0
    df1 = df1.replace(to_replace='-', value=0, regex=True)
    # changes data frame column type to float
    df1 = df1.astype(np.float)

    # read spreadsheet and turn into df
    df2 = pd.read_csv(filepath1, skiprows=35, skipfooter=8, engine='python')
    # drop all unnecessary columns
    df2 = df2.drop(df2.columns[[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]], axis=1)
    # change column name
    df2.columns = ['dist1']
    # replaces all dashes by 0
    df2 = df2.replace(to_replace='-', value=0, regex=True)
    # changes data frame column type to float
    df2 = df2.astype(np.float)

    # read spreadsheet and turn into df
    df3 = pd.read_csv(filepath24, skiprows=35, skipfooter=8, engine='python')
    # drop all unnecessary columns
    df3 = df3.drop(df3.columns[[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]], axis=1)
    # change column name
    df3.columns = ['dist24']
    # replaces all dashes by 0
    df3 = df3.replace(to_replace='-', value=0, regex=True)
    # changes data frame column type to float
    # df3['dist 24'] = df3['dist 24'].apply(pd.to_numeric)
    df3 = df3.astype(np.float)

    df = pd.concat([df1, df2, df3], axis=1)

    # adds seconds and minute column
    df['second'] = seconds
    df['minute'] = minute
    df['condition'] = condition

    return df

#==============================================================================
# def big_dataframe(animals):
#     dfAll = animals[0].copy()
#     dfAll['animal'] = 1
#     dfAll['genotype'] = 'gr'
#     dfAll['frame'] = range(1, dfAll.shape[0]+1)
#     for i in range(1, len(animals)):
#         temp = animals[i].copy()
#         temp['animal'] = i+1
#     #    temp['time']=series
#         temp['frame'] = range(1, temp.shape[0]+1)
#         if i < 48:
#             temp['genotype'] = 'gr'
#         else:
#             temp['genotype'] = 'het'
#     #    temp['dist 0']=moving_average(temp['dist 0'].values,30)
#         dfAll = pd.concat([dfAll, temp])
#     return dfAll
# 
# 
# def trans(i):
#     panel = pd.Panel(i)
#     df = panel.mean(axis=0)
#     df = df.reset_index()
#     series = pd.date_range('1/1/2017 00:00:01', periods=df.shape[0], freq='1S')
#     df['frame'] = series
#     df = df.set_index(series)
#     return df
# 
# 
# def big_dataframe_resampled(animals):
#     n = 0
#     i = 0
#     gr = {}
#     het = {}
#     for i in range(len(animals)):
#         temp = animals[i].copy()
#         temp['frame'] = range(1, temp.shape[0]+1)
#         if i < 48:
#             temp['genotype'] = 'gr'
#             gr_temp = temp.groupby(['genotype', 'minute', 'second']).sum()
#             gr[n] = gr_temp
#         else:
#             temp['genotype'] = 'het'
#             het_temp = temp.groupby(['genotype', 'minute', 'second']).sum()
#             het[n] = het_temp
#         n += 1
#         i += 1
#     all_gr = trans(gr)
#     all_het = trans(het)
#     result = pd.concat([all_gr, all_het])
#     return result
#==============================================================================

ph1 = [1] * 10
ph2 = [2] * 10
ph3 = [3] * 10
ph4 = [4] * 10
ph5 = [5] * 10
ph6 = [6] * 10

pha = list(it.chain(ph1, ph2, ph3, ph4, ph5, ph6))
phase = pha * 8

s1 = [3] * 3
s2 = [4] * 7

secph = list(it.chain(s1, s2, s1, s2, s1, s2, s1, s2, s1, s2, s1, s2))
secphase = secph * 8


def big_dataframe_resampled_2(animals):
    i = 0
    a = 1
    gr_all = pd.DataFrame()
    het_all = pd.DataFrame()
    for i in range(len(animals)):
        temp = animals[i].copy()
        temp['frame'] = range(1, temp.shape[0]+1)
        if i < 48:
            temp['genotype'] = 'gr'
            gr_temp = temp.groupby(['genotype', 'minute', 'second']).sum()
            gr_temp['animal'] = a
            gr_temp = gr_temp.reset_index()
            series = pd.date_range('1/1/2017 00:00:02', periods=gr_temp.shape[0], freq='1S')
            gr_temp['frame'] = series
            gr_temp['10sphase']  = phase
            gr_all = pd.concat([gr_all, gr_temp])
        else:
            temp['genotype'] = 'het'
            het_temp = temp.groupby(['genotype', 'minute', 'second']).sum()
            het_temp['animal'] = a
            het_temp = het_temp.reset_index()
            series = pd.date_range('1/1/2017 00:00:02', periods=het_temp.shape[0], freq='1S')
            het_temp['frame'] = series
            het_temp['10sphase']  = phase
            het_all = pd.concat([het_all, het_temp])
        n += 1
        i += 1
        a += 1
    result = pd.concat([gr_all, het_all])
    return result


def add_conc(df):
    df = df.reset_index()
    t = [20] * (len(df.index) / 2)
    w = [10] * (len(df.index) / 2)
    o = list(it.chain(t, w))
    df['conc'] = o
    return df


def frame_resampled(animals, output):
    i = 0
    a = 1
    gr_all = pd.DataFrame()
    het_all = pd.DataFrame()
    for i in range(len(animals)):
        temp = animals[i].copy()
        temp['frame'] = range(1, temp.shape[0]+1)
        temp['animal'] = a
        gb = temp.groupby('minute')
        gb.groups
        fr_temp = pd.DataFrame()
        start = 0
        if output == 2:
            stop = 59
        elif output == 1:
            stop = 29
        else:
            pass
        for x in range(1, len(gb)+1):
            group = gb.get_group(x).copy()
            df = group.loc[start:stop].copy()
            df['frame'] = np.arange(1, len(df.index)+1)
            series = pd.date_range('1/1/2017 00:00:02', periods=df.shape[0], freq='1S')
            df['time'] = series
            fr_temp = pd.concat([fr_temp, df])
            start += 1800
            stop += 1800
        if i < 48:
            fr_temp['genotype'] = 'gr'
            gr_all = pd.concat([gr_all, fr_temp])
        else:
            fr_temp['genotype'] = 'het'
            het_all = pd.concat([het_all, fr_temp])
        i += 1
        a += 1
    result = pd.concat([gr_all, het_all])
    return result


def prepare_all_traces(dataframe):
    df = dataframe.copy()
    means = df.groupby(['minute', 'second', 'genotype', 'animal'])['dist0'].mean().reset_index()
    m = means.groupby('animal')
    m.groups
    dff = pd.DataFrame()
    for x in range(1, len(m)+1):
        group = m.get_group(x).copy()
        series = pd.date_range('1/1/2017 00:00:02', periods=480, freq='1S')
        group['frame'] = series
        dff = pd.concat([dff, group])
    return dff



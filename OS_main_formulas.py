# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 21:10:40 2017

@author: ehindinger
"""
import pandas as pd
import numpy as np
import itertools as it
from scipy import stats
import os

''' To modify the seconds that are being analysed, change below. '''

start = '2'
stop = '11'

''' From here on, do not modify. '''
def make_lookup_table(filename):
    oscreen = pd.read_excel(filename, parse_cols=[0, 2, 3], skip_footer=5,
                            names=['Compound', 'Plate', 'Number'])
    oscreen['Plate'] = oscreen['Plate'].apply(lambda x: '0{}'.format(x) if len(str(x))==1 else str(x))
    oscreen['OS Code'] = oscreen['Plate'] + oscreen['Number']
    oscreen = oscreen.drop(['Plate', 'Number'], axis=1)
    oscreen['Compound'] = oscreen['Compound'].str.title()
    oscreen = oscreen.set_index('OS Code')
    multi_dic = oscreen.to_dict(orient='dict')
    look_up_dictionary = multi_dic['Compound']
    return look_up_dictionary


def name_finder(dictionary, com_code):
    for k, v in dictionary.iteritems():
        if k == com_code:
            return v

# makes seconds list
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


def buildfish_7(directory, index):
    '''
    This function reads three csv files: pre-treatment, 1h incubation and
    24h incubation. It reads only column H distance, concats, then turns
    into a pivot table for multi-indexing
    '''
    pre = os.listdir(directory + '/pre-treatment files')
    inc_1h = os.listdir(directory + '/1h incubation files')
    inc_24h = os.listdir(directory + '/24h incubation files')

    # choose appropriate filepaths
    filepath0 = directory + '/pre-treatment files/' + pre[index]
    filepath1 = directory + '/1h incubation files/' + inc_1h[index]
    filepath24 = directory + '/24h incubation files/' + inc_24h[index]
    # read spreadsheet and turn into df
    df1 = pd.read_csv(filepath0, skiprows=35, skipfooter=8, engine='python')
    # drop all unnecessary columns
    df1 = df1.drop(df1.columns[[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]], axis=1)
    # change column name
    df1.columns = ['dist 0']
    # replaces all dashes by 0
    df1 = df1.replace(to_replace='-', value=0, regex=True)
    # changes data frame column type to float
    df1 = df1.astype(np.float)

    # read spreadsheet and turn into df
    df2 = pd.read_csv(filepath1, skiprows=35, skipfooter=8, engine='python')
    # drop all unnecessary columns
    df2 = df2.drop(df2.columns[[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]], axis=1)
    # change column name
    df2.columns = ['dist 1']
    # replaces all dashes by 0
    df2 = df2.replace(to_replace='-', value=0, regex=True)
    # changes data frame column type to float
    df2 = df2.astype(np.float)

    # read spreadsheet and turn into df
    df3 = pd.read_csv(filepath24, skiprows=35, skipfooter=8, engine='python')
    # drop all unnecessary columns
    df3 = df3.drop(df3.columns[[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]], axis=1)
    # change column name
    df3.columns = ['dist 24']
    # replaces all dashes by 0
    df3 = df3.replace(to_replace='-', value=0, regex=True)
    # changes data frame column type to float
    # df3['dist 24'] = df3['dist 24'].apply(pd.to_numeric)
    df3 = df3.astype(np.float)

    df = pd.concat([df1, df2, df3], axis=1)

    # adds seconds and minute column
    df['Second'] = seconds
    df['Minute'] = minute
    df['Condition'] = condition
    # takes all data, multiindexes by minute and second, computes mean + sem
    pivot = df.pivot_table(values=['dist 0', 'dist 1', 'dist 24'],
                           index=['Condition', 'Minute', 'Second'],
                           aggfunc=[np.sum])
    pivot.columns = pivot.columns.get_level_values(0)
    pivot.columns = ['dist 0', 'dist 1', 'dist 24']
    return pivot


def buildfish_20(directory, index):
    '''
    This function reads three csv files: pre-treatment, 1h incubation and
    24h incubation. It reads only column H distance, concats, then turns
    into a pivot table for multi-indexing
    '''
    # choose appropriate filepaths
    pre = os.listdir(directory + '/pre-treatment files')
    inc_1h = os.listdir(directory + '/1h incubation files')
    inc_24h = os.listdir(directory + '/24h incubation files')

    # choose appropriate filepaths
    filepath0 = directory + '/pre-treatment files/' + pre[index]
    filepath1 = directory + '/1h incubation files/' + inc_1h[index]
    filepath24 = directory + '/24h incubation files/' + inc_24h[index]
    # read spreadsheet and turn into df
    df1 = pd.read_csv(filepath0, skiprows=35, skipfooter=8, engine='python')
    # drop all unnecessary columns
    if len(df1.columns) == 9:
        df1 = df1.drop(df1.columns[[0, 1, 2, 3, 4, 5, 6, 8]], axis=1)
    elif len(df1.columns) == 12:
        df1 = df1.drop(df1.columns[[0, 1, 2, 3, 4, 5, 6, 8, 9, 10, 11]], axis=1)
    # change column name
    df1.columns = ['dist 0']
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
    df2.columns = ['dist 1']
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
    df3.columns = ['dist 24']
    # replaces all dashes by 0
    df3 = df3.replace(to_replace='-', value=0, regex=True)
    # changes data frame column type to float
    df3 = df3.astype(np.float)

    df = pd.concat([df1, df2, df3], axis=1)

    # adds seconds and minute column
    df['Second'] = seconds
    df['Minute'] = minute
    df['Condition'] = condition
    # takes all data, multiindexes by minute and second, computes mean + sem
    pivot = df.pivot_table(values=['dist 0', 'dist 1', 'dist 24'],
                           index=['Condition', 'Minute', 'Second'],
                           aggfunc=[np.sum])
    pivot.columns = pivot.columns.get_level_values(0)
    pivot.columns = ['dist 0', 'dist 1', 'dist 24']
    return pivot


def final_ctr(fish1, fish2, fish3, fish4, fish5, fish6, fish7, fish8):
    dist0 = pd.concat([fish1['dist 0'], fish2['dist 0'], fish3['dist 0'],
                       fish4['dist 0'], fish5['dist 0'], fish6['dist 0'],
                       fish7['dist 0'], fish8['dist 0']], axis=1)
    df0 = dist0.mean(axis=1).to_frame()
    df0_sem = dist0.sem(axis=1).to_frame()

    dist1 = pd.concat([fish1['dist 1'], fish2['dist 1'], fish3['dist 1'],
                       fish4['dist 1'], fish5['dist 1'], fish6['dist 1'],
                       fish7['dist 1'], fish8['dist 1']], axis=1)
    df1 = dist1.mean(axis=1).to_frame()
    df1_sem = dist1.sem(axis=1).to_frame()

    dist24 = pd.concat([fish1['dist 24'], fish2['dist 24'], fish3['dist 24'],
                        fish4['dist 24'], fish5['dist 24'], fish6['dist 24'],
                        fish7['dist 24'], fish8['dist 24']], axis=1)
    df24 = dist24.mean(axis=1).to_frame()
    df24_sem = dist24.sem(axis=1).to_frame()

    final = pd.concat([df0, df1, df24, df0_sem, df1_sem, df24_sem], axis=1)
    final.columns = ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem', 'dist 1 sem',
                     'dist 24 sem']

    dtp1 = final.loc[('D', [2]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    dtp2 = final.loc[('D', [4]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    dtp3 = final.loc[('D', [6]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    dtp4 = final.loc[('D', [8]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')

    ltp1 = final.loc[('L', [1]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    ltp2 = final.loc[('L', [3]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    ltp3 = final.loc[('L', [5]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    ltp4 = final.loc[('L', [7]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    
    result = pd.concat([dtp1, dtp2, dtp3, dtp4, ltp1, ltp2, ltp3, ltp4], axis=1)
    result.columns = ['D tp1 dist 0', 'D tp1 dist 1', 'D tp1 dist 24',
                      'D tp1 sem 0', 'D tp1 sem 1', 'D tp1 sem 24',
                      'D tp2 dist 0', 'D tp2 dist 1', 'D tp2 dist 24',
                      'D tp2 sem 0', 'D tp2 sem 1', 'D tp2 sem 24',
                      'D tp3 dist 0', 'D tp3 dist 1', 'D tp3 dist 24',
                      'D tp3 sem 0', 'D tp3 sem 1', 'D tp3 sem 24',
                      'D tp4 dist 0', 'D tp4 dist 1', 'D tp4 dist 24',
                      'D tp4 sem 0', 'D tp4 sem 1', 'D tp4 sem 24',
                      'L tp1 dist 0', 'L tp1 dist 1', 'L tp1 dist 24',
                      'L tp1 sem 0', 'L tp1 sem 1', 'L tp1 sem 24',
                      'L tp2 dist 0', 'L tp2 dist 1', 'L tp2 dist 24',
                      'L tp2 sem 0', 'L tp2 sem 1', 'L tp2 sem 24',
                      'L tp3 dist 0', 'L tp3 dist 1', 'L tp3 dist 24',
                      'L tp3 sem 0', 'L tp3 sem 1', 'L tp3 sem 24',
                      'L tp4 dist 0', 'L tp4 dist 1', 'L tp4 dist 24',
                      'L tp4 sem 0', 'L tp4 sem 1', 'L tp4 sem 24']
    return result


def final_com(fish1, fish2, fish3, fish4):
    dist0 = pd.concat([fish1['dist 0'], fish2['dist 0'], fish3['dist 0'],
                       fish4['dist 0']], axis=1)
    df0 = dist0.mean(axis=1).to_frame()
    df0_sem = dist0.sem(axis=1).to_frame()

    dist1 = pd.concat([fish1['dist 1'], fish2['dist 1'], fish3['dist 1'],
                       fish4['dist 1']], axis=1)
    df1 = dist1.mean(axis=1).to_frame()
    df1_sem = dist1.sem(axis=1).to_frame()

    dist24 = pd.concat([fish1['dist 24'], fish2['dist 24'], fish3['dist 24'],
                        fish4['dist 24']], axis=1)
    df24 = dist24.mean(axis=1).to_frame()
    df24_sem = dist24.sem(axis=1).to_frame()

    final = pd.concat([df0, df1, df24, df0_sem, df1_sem, df24_sem], axis=1)
    final.columns = ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem', 'dist 1 sem',
                     'dist 24 sem']

    dtp1 = final.loc[('D', [2]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    dtp2 = final.loc[('D', [4]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    dtp3 = final.loc[('D', [6]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    dtp4 = final.loc[('D', [8]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')

    ltp1 = final.loc[('L', [1]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    ltp2 = final.loc[('L', [3]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    ltp3 = final.loc[('L', [5]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    ltp4 = final.loc[('L', [7]), ['dist 0', 'dist 1', 'dist 24', 'dist 0 sem',
                                  'dist 1 sem', 'dist 24 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')

    result = pd.concat([dtp1, dtp2, dtp3, dtp4, ltp1, ltp2, ltp3, ltp4],
                       axis=1)
    result.columns = ['D tp1 dist 0', 'D tp1 dist 1', 'D tp1 dist 24',
                      'D tp1 sem 0', 'D tp1 sem 1', 'D tp1 sem 24',
                      'D tp2 dist 0', 'D tp2 dist 1', 'D tp2 dist 24',
                      'D tp2 sem 0', 'D tp2 sem 1', 'D tp2 sem 24',
                      'D tp3 dist 0', 'D tp3 dist 1', 'D tp3 dist 24',
                      'D tp3 sem 0', 'D tp3 sem 1', 'D tp3 sem 24',
                      'D tp4 dist 0', 'D tp4 dist 1', 'D tp4 dist 24',
                      'D tp4 sem 0', 'D tp4 sem 1', 'D tp4 sem 24',
                      'L tp1 dist 0', 'L tp1 dist 1', 'L tp1 dist 24',
                      'L tp1 sem 0', 'L tp1 sem 1', 'L tp1 sem 24',
                      'L tp2 dist 0', 'L tp2 dist 1', 'L tp2 dist 24',
                      'L tp2 sem 0', 'L tp2 sem 1', 'L tp2 sem 24',
                      'L tp3 dist 0', 'L tp3 dist 1', 'L tp3 dist 24',
                      'L tp3 sem 0', 'L tp3 sem 1', 'L tp3 sem 24',
                      'L tp4 dist 0', 'L tp4 dist 1', 'L tp4 dist 24',
                      'L tp4 sem 0', 'L tp4 sem 1', 'L tp4 sem 24']
    return result


def pooled(fish1, fish2, fish3, fish4, fish5, fish6, fish7, fish8, fish9,
           fish10, fish11, fish12, fish13, fish14, fish15, fish16, fish17,
           fish18, fish19, fish20, fish21, fish22, fish23, fish24, fish25,
           fish26, fish27, fish28, fish29, fish30, fish31, fish32, fish33,
           fish34, fish35, fish36, fish37, fish38, fish39, fish40, fish41,
           fish42, fish43, fish44, fish45, fish46, fish47, fish48):
    dist0 = pd.concat([fish1['dist 0'], fish2['dist 0'], fish3['dist 0'],
                       fish4['dist 0'], fish5['dist 0'], fish6['dist 0'],
                       fish7['dist 0'], fish8['dist 0'], fish9['dist 0'],
                       fish10['dist 0'], fish11['dist 0'], fish12['dist 0'],
                       fish13['dist 0'], fish14['dist 0'], fish15['dist 0'],
                       fish16['dist 0'], fish17['dist 0'], fish18['dist 0'],
                       fish19['dist 0'], fish20['dist 0'], fish21['dist 0'],
                       fish22['dist 0'], fish23['dist 0'], fish24['dist 0'],
                       fish25['dist 0'], fish26['dist 0'], fish27['dist 0'],
                       fish28['dist 0'], fish29['dist 0'], fish30['dist 0'],
                       fish31['dist 0'], fish32['dist 0'], fish33['dist 0'],
                       fish34['dist 0'], fish35['dist 0'], fish36['dist 0'],
                       fish37['dist 0'], fish38['dist 0'], fish39['dist 0'],
                       fish40['dist 0'], fish41['dist 0'], fish42['dist 0'],
                       fish43['dist 0'], fish44['dist 0'], fish45['dist 0'],
                       fish46['dist 0'], fish47['dist 0'], fish48['dist 0']],
                      axis=1)
    df0 = dist0.mean(axis=1).to_frame()
    df0_sem = dist0.sem(axis=1).to_frame()

    final = pd.concat([df0, df0_sem], axis=1)
    final.columns = ['dist 0', 'dist 0 sem']
    
    dtp1 = final.loc[('D', [2]), ['dist 0', 'dist 0 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    dtp2 = final.loc[('D', [4]), ['dist 0', 'dist 0 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    dtp3 = final.loc[('D', [6]), ['dist 0', 'dist 0 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    dtp4 = final.loc[('D', [8]), ['dist 0', 'dist 0 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')

    ltp1 = final.loc[('L', [1]), ['dist 0', 'dist 0 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    ltp2 = final.loc[('L', [3]), ['dist 0', 'dist 0 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    ltp3 = final.loc[('L', [5]), ['dist 0', 'dist 0 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    ltp4 = final.loc[('L', [7]), ['dist 0', 'dist 0 sem']].reset_index().drop(['Condition', 'Minute'], axis=1).set_index('Second')
    
    result = pd.concat([dtp1, dtp2, dtp3, dtp4, ltp1, ltp2, ltp3, ltp4],
                       axis=1)
    result.columns = ['D tp1 dist 0', 'D tp1 sem 0', 'D tp2 dist 0',
                      'D tp2 sem 0', 'D tp3 dist 0', 'D tp3 sem 0',
                      'D tp4 dist 0', 'D tp4 sem 0', 'L tp1 dist 0',
                      'L tp1 sem 0', 'L tp2 dist 0', 'L tp2 sem 0',
                      'L tp3 dist 0', 'L tp3 sem 0', 'L tp4 dist 0',
                      'L tp4 sem 0']
    return result


def new_buildfish(buildfish):
    # OLD BUILDFISH FUNCTION STARTS HERE
    '''
    Second part of the function splits into L and D, computes mean for seconds
    specified
    '''
    pivot = buildfish.copy(deep=True)
    timepoints = ['tp1', 'tp2', 'tp3', 'tp4']
    # polish light condition
    l_a1 = pivot.loc[('L', [1, 3, 5, 7], [int(start), int(stop)]),
                     ['dist 0', 'dist 1', 'dist 24']].groupby(level=1).sum()
    # flattens column levels
    l_a1.columns = l_a1.columns.get_level_values(0)
    # change columns name
    l_a1.columns = ['L mean 0', 'L mean 1', 'L mean 24']
    # gets rid of index
    l_a1.reset_index(level=0, inplace=True)
    # adds timepoints
    l_a1['TP'] = timepoints
    # deletes minutes column
    l_a1.drop('Minute', axis=1, inplace=True)
    # sets timepoints as index
    polished_l = l_a1.set_index('TP')

    # polish dark condition
    d_a1 = pivot.loc[('D', [2, 4, 6, 8], [int(start), int(stop)]),
                     ['dist 0', 'dist 1', 'dist 24']].groupby(level=1).sum()
    # flattens column levels
    d_a1.columns = d_a1.columns.get_level_values(0)
    # change columns name
    d_a1.columns = ['D mean 0', 'D mean 1', 'D mean 24']
    # gets rid of index
    d_a1.reset_index(level=0, inplace=True)
    # adds timepoints
    d_a1['TP'] = timepoints
    # deletes minutes column
    d_a1.drop('Minute', axis=1, inplace=True)
    # sets timepoints as index
    polished_d = d_a1.set_index('TP')

    # combine light and dark
    result = pd.concat([polished_l, polished_d], axis=1,
                       join_axes=[polished_l.index])
    return result

fi1 = ['fish1'] * 4
fi2 = ['fish2'] * 4
fi3 = ['fish3'] * 4
fi4 = ['fish4'] * 4
fi5 = ['fish5'] * 4
fi6 = ['fish6'] * 4
fi7 = ['fish7'] * 4
fi8 = ['fish8'] * 4

ctr_group = list(it.chain(fi1, fi2, fi3, fi4, fi5, fi6, fi7, fi8))
com_group = list(it.chain(fi1, fi2, fi3, fi4))


def ctr_intogroups(fish1, fish2, fish3, fish4, fish5, fish6, fish7, fish8):
    # create concat
    concat_trial = pd.concat([fish1, fish2, fish3, fish4, fish5, fish6, fish7, fish8])
    # add fish column
    concat_trial['Fish'] = ctr_group
    # sort minute index
    sorted_trial = concat_trial.sort_index()
    return sorted_trial


def com_intogroups(fish1, fish2, fish3, fish4):
    # create concat
    concat_trial = pd.concat([fish1, fish2, fish3, fish4])
    # add fish column
    concat_trial['Fish'] = com_group
    # sort minute index
    sorted_trial = concat_trial.sort_index()
    return sorted_trial


def ind_csv(gr_ctr_in, het_ctr_in, gr_com_in, het_com_in, filepath):
    '''
    this function builds a dataframe with gr ctr, het ctr, gr com, het com
    and writes a csv file
    '''
    # make copies so original data is not transformed
    gr_ctr = gr_ctr_in.copy(deep=True)
    het_ctr = het_ctr_in.copy(deep=True)
    gr_com = gr_com_in.copy(deep=True)
    het_com = het_com_in.copy(deep=True)
    # reset indices
    gr_ctr.reset_index(level=0, inplace=True)
    het_ctr.reset_index(level=0, inplace=True)
    gr_com.reset_index(level=0, inplace=True)
    het_com.reset_index(level=0, inplace=True)
    # split each into groups by groupy
    gr_ctr['TP'].unique()
    gr_ctr = gr_ctr.groupby('TP')
    gr_ctr.groups
    het_ctr['TP'].unique()
    het_ctr = het_ctr.groupby('TP')
    het_ctr.groups
    gr_com['TP'].unique()
    gr_com = gr_com.groupby('TP')
    gr_com.groups
    het_com['TP'].unique()
    het_com = het_com.groupby('TP')
    het_com.groups
    # variables for tps, resets indices to start from 0
    gr_ctr_tp1 = gr_ctr.get_group('tp1').set_index(np.arange(8))
    gr_ctr_tp2 = gr_ctr.get_group('tp2').set_index(np.arange(8))
    gr_ctr_tp3 = gr_ctr.get_group('tp3').set_index(np.arange(8))
    gr_ctr_tp4 = gr_ctr.get_group('tp4').set_index(np.arange(8))
    het_ctr_tp1 = het_ctr.get_group('tp1').set_index(np.arange(8))
    het_ctr_tp2 = het_ctr.get_group('tp2').set_index(np.arange(8))
    het_ctr_tp3 = het_ctr.get_group('tp3').set_index(np.arange(8))
    het_ctr_tp4 = het_ctr.get_group('tp4').set_index(np.arange(8))
    gr_com_tp1 = gr_com.get_group('tp1').set_index(np.arange(4))
    gr_com_tp2 = gr_com.get_group('tp2').set_index(np.arange(4))
    gr_com_tp3 = gr_com.get_group('tp3').set_index(np.arange(4))
    gr_com_tp4 = gr_com.get_group('tp4').set_index(np.arange(4))
    het_com_tp1 = het_com.get_group('tp1').set_index(np.arange(4))
    het_com_tp2 = het_com.get_group('tp2').set_index(np.arange(4))
    het_com_tp3 = het_com.get_group('tp3').set_index(np.arange(4))
    het_com_tp4 = het_com.get_group('tp4').set_index(np.arange(4))
    # concat per tp
    tp1 = pd.concat([gr_ctr_tp1, het_ctr_tp1, gr_com_tp1, het_com_tp1], axis=1,
                    join_axes=[gr_ctr_tp1.index])
    tp2 = pd.concat([gr_ctr_tp2, het_ctr_tp2, gr_com_tp2, het_com_tp2], axis=1,
                    join_axes=[gr_ctr_tp2.index])
    tp3 = pd.concat([gr_ctr_tp3, het_ctr_tp3, gr_com_tp3, het_com_tp3], axis=1,
                    join_axes=[gr_ctr_tp3.index])
    tp4 = pd.concat([gr_ctr_tp4, het_ctr_tp4, gr_com_tp4, het_com_tp4], axis=1,
                    join_axes=[gr_ctr_tp4.index])
    # concat to one
    result = pd.concat([tp1, tp2, tp3, tp4])
    result.columns = ['gr ctr TP', 'gr ctr L 0', 'gr ctr L 1', 'gr ctr L 24',
                      'gr ctr D 0', 'gr ctr D 1', 'gr ctr D 24', 'gr ctr fish',
                      'het ctr TP', 'het ctr L 0', 'het ctr L 1',
                      'het ctr L 24', 'het ctr D 0', 'het ctr D 1',
                      'het ctr D 24', 'het ctr fish', 'gr com TP',
                      'gr com L 0', 'gr com L 1', 'gr com L 24', 'gr com D 0',
                      'gr com D 1', 'gr com D 24', 'gr com fish', 'het com TP',
                      'het com L 0', 'het com L 1', 'het com L 24',
                      'het com D 0', 'het com D 1', 'het com D 24',
                      'het com fish']
    result = result.drop(result.columns[[8, 16, 24]], axis=1)
    result = result.set_index('gr ctr TP')
    result = result.replace({np.nan: '-'}, regex=True)
    # write to csv
    result.to_csv(filepath)


def filler(dataframe):
    zeros = dataframe.apply(lambda column: (column == 0).sum()).to_frame().T
    if len(dataframe.index) == 8:
        for identifier, values in dataframe.iteritems():
            if zeros[identifier].iloc[0] in range(1, 5):
                # less than half the fish died, replaced by mean
                mean = float(values.sum())/float((values != 0).sum())
                values = values.replace(to_replace=0, value=mean)
            elif zeros[identifier].iloc[0] in range(5, 9):
                # too many fish have died, hence the whole column was made 0
                values = values * 0
            else:
                pass
            dataframe[identifier] = values
        return dataframe
    elif len(dataframe.index) == 4:
        for identifier, values in dataframe.iteritems():
            if zeros[identifier].iloc[0] in range(1, 3):
                # less than half the fish died, replaced by mean
                mean = float(values.sum())/float((values != 0).sum())
                values = values.replace(to_replace=0, value=mean)
            elif zeros[identifier].iloc[0] in range(3, 5):
                # too many fish have died, hence the whole column was made 0
                values = values * 0
            else:
                pass
            dataframe[identifier] = values
        return dataframe

def match(dataframe1, dataframe2):
    mean = dataframe1.mean().to_frame().T
    df1 = dataframe1.copy(deep=True)
    df2 = dataframe2.copy(deep=True)
    for identifier, values in df1.iteritems():
        if mean[identifier].iloc[0] == 0 or mean[identifier].iloc[0] == 0.0:
            if len(df1.index) == 4:
                df2[identifier] = [0] * 4
            elif len(df1.index) == 8:
                df2[identifier] = [0] * 8
            elif len(df1.index) == 1:
                df2[identifier] = [0]
        else:
            pass
    return df2


def pivoter(sorted_trial):
    '''
    This function takes one group as an input (gr ctr, or het com1...) and
    replaces any dead fish (0 values) by the mean of the other fish in the
    timepoint group, then concats.
    The second part of the function creates a pivot table with the means and
    standard error of the mean for each timepoint.
    '''
    # make copy of dataframe so original input is not modified
    df = sorted_trial.copy(deep=True)
    # reset index to become a column
    df.reset_index(level=0, inplace=True)
    # groupby
    df['TP'].unique()
    gb = df.groupby('TP')
    gb.groups
    # work on individual groups: replaces 0 by nan, replaces nan by group mean
    tp1 = filler(gb.get_group('tp1').set_index('TP'))
    tp2 = filler(gb.get_group('tp2').set_index('TP'))
    tp3 = filler(gb.get_group('tp3').set_index('TP'))
    tp4 = filler(gb.get_group('tp4').set_index('TP'))
    # concats time points
    reformed = pd.concat([tp1, tp2, tp3, tp4])
    reformed.reset_index(level=0, inplace=True)
    # computes mean per timepoint
    pivot_trial = reformed.pivot_table(values=['L mean 0', 'L mean 1',
                                               'L mean 24', 'D mean 0',
                                               'D mean 1', 'D mean 24'],
                                       index=['TP'],
                                       aggfunc=[np.mean, stats.sem])
    # flattens column labels to one level
    pivot_trial.columns = pivot_trial.columns.get_level_values(1)
    # renames columns
    pivot_trial.columns = ['D mean 0', 'D mean 1', 'D mean 24', 'L mean 0',
                           'L mean 1', 'L mean 24', 'D sem 0', 'D sem 1',
                           'D sem 24', 'L sem 0', 'L sem 1', 'L sem 24']
    return pivot_trial


def group_csv(in1, in2, in3, in4, savename):
    '''
    This function takes four pivot table groups and a filename, and concats
    on the horizontal axis.
    '''
    group1 = in1.copy(deep=True)
    group2 = in2.copy(deep=True)
    group3 = in3.copy(deep=True)
    group4 = in4.copy(deep=True)
    group1.columns = ['gr ctr D avg 0', 'gr ctr D avg 1', 'gr ctr D avg 24',
                      'gr ctr L avg 0', 'gr ctr L avg 1', 'gr ctr L avg 24',
                      'gr ctr D sem 0', 'gr ctr D sem 1', 'gr ctr D sem 24',
                      'gr ctr L sem 0', 'gr ctr L sem 1', 'gr ctr L sem 24']
    group2.columns = ['het ctr D avg 0', 'het ctr D avg 1', 'het ctr D avg 24',
                      'het ctr L avg 0', 'het ctr L avg 1', 'het ctr L avg 24',
                      'het ctr D sem 0', 'het ctr D sem 1', 'het ctr D sem 24',
                      'het ctr L sem 0', 'het ctr L sem 1', 'het ctr L sem 24']
    group3.columns = ['gr com D avg 0', 'gr com D avg 1', 'gr com D avg 24',
                      'gr com L avg 0', 'gr com L avg 1', 'gr com L avg 24',
                      'gr com D sem 0', 'gr com D sem 1', 'gr com D sem 24',
                      'gr com L sem 0', 'gr com L sem 1', 'gr com L sem 24']
    group4.columns = ['het com D avg 0', 'het com D avg 1', 'het com D avg 24',
                      'het com L avg 0', 'het com L avg 1', 'het com L avg 24',
                      'het com D sem 0', 'het com D sem 1', 'het com D sem 24',
                      'het com L sem 0', 'het com L sem 1', 'het com L sem 24']
    new = pd.concat([group1, group2, group3, group4], axis=1).T
    new.to_csv(savename)


def normalisation_csv(in_gr_ctr, in_het_ctr, in_gr_com, in_het_com, startrow,
                      endrow, savename):
    '''
    This function calculates the absolute change between 2 groups, then avg.
    Startrow and endrow define which timepoints are averaged, then df is
    saved as a csv file.
    '''
    gr_com = in_gr_com.copy(deep=True)
    gr_ctr = in_gr_ctr.copy(deep=True)
    het_com = in_het_com.copy(deep=True)
    het_ctr = in_het_ctr.copy(deep=True)

    # split into 0 and 1/24
    gr_com_0 = pd.concat([gr_com['D mean 0'], gr_com['L mean 0']], axis=1)
    gr_ctr_0 = pd.concat([gr_ctr['D mean 0'], gr_ctr['L mean 0']], axis=1)
    het_com_0 = pd.concat([het_com['D mean 0'], het_com['L mean 0']], axis=1)
    het_ctr_0 = pd.concat([het_ctr['D mean 0'], het_ctr['L mean 0']], axis=1)

    gr_com_rest = pd.concat([gr_com['D mean 1'], gr_com['L mean 1'],
                             gr_com['D mean 24'], gr_com['L mean 24']], axis=1)
    het_ctr_rest = pd.concat([het_ctr['D mean 1'], het_ctr['L mean 1'],
                              het_ctr['D mean 24'], het_ctr['L mean 24']],
                             axis=1)

    gr_com_0_m = match(het_com_0, gr_com_0)
    het_com_0_m = match(gr_com_0, het_com_0)
    gr_ctr_0_m = match(het_ctr_0, gr_ctr_0)
    het_ctr_0_m = match(gr_ctr_0, het_ctr_0)
    gr_com_rest_m = match(het_ctr_rest, gr_com_rest)
    het_ctr_rest_m = match(gr_com_rest, het_ctr_rest)

    a = het_ctr_0_m.subtract(gr_ctr_0_m, axis=1)
    b = het_com_0_m.subtract(gr_com_0_m, axis=1)
    c = het_ctr_rest_m.subtract(gr_com_rest_m, axis=1)

    # collapse
    df = pd.concat([a, b, c], axis=1)
    df['count'] = [1] * 4
    df.columns = ['D 0 Het ctr - GR ctr', 'L 0 Het ctr - GR ctr',
                  'D 0 Het com - GR com', 'L 0 Het com - GR com',
                  'D 1 Het ctr - GR com', 'L 1 Het ctr - GR com',
                  'D 24 Het ctr - GR com', 'L 24 Het ctr - GR com', 'count']
    cut = df.iloc[range(int(startrow), int(endrow))]
    result = pd.pivot_table(cut, values=['D 0 Het ctr - GR ctr',
                                         'L 0 Het ctr - GR ctr',
                                         'D 0 Het com - GR com',
                                         'L 0 Het com - GR com',
                                         'D 1 Het ctr - GR com',
                                         'L 1 Het ctr - GR com',
                                         'D 24 Het ctr - GR com',
                                         'L 24 Het ctr - GR com'],
                            index='count', dropna=False)

    # add together
    result.columns = result.columns.get_level_values(0)
    result.columns = ['D 0 Het ctr - GR ctr', 'L 0 Het ctr - GR ctr',
                      'D 0 Het com - GR com', 'L 0 Het com - GR com',
                      'D 1 Het ctr - GR com', 'L 1 Het ctr - GR com',
                      'D 24 Het ctr - GR com', 'L 24 Het ctr - GR com']
    result.to_csv(savename)


def absolute_change(gr_ctr, het_ctr, gr_com, het_com, startrow, endrow):
    '''
    This function takes the pivoter output, and calculates the absolute change,
    e.g. gr drug 1 - gr drug 0, gr ctr 1 - gr ctr 0,
            gr drug 24 - gr drug 0, gr ctr 24 - gr ctr 0
    '''
    # assembles 3 dataframes for pre-treatment, 1h incubation, 24 incubation
    time0 = pd.concat([gr_ctr['L mean 0'], gr_ctr['D mean 0'],
                       het_ctr['L mean 0'], het_ctr['D mean 0'],
                       gr_com['L mean 0'], gr_com['D mean 0'],
                       het_com['L mean 0'], het_com['D mean 0']], axis=1)
    time0.columns = ['gr ctr L', 'gr ctr D', 'het ctr L', 'het ctr D',
                     'gr com L', 'gr com D', 'het com L', 'het com D']
    time1 = pd.concat([gr_ctr['L mean 1'], gr_ctr['D mean 1'],
                       het_ctr['L mean 1'], het_ctr['D mean 1'],
                       gr_com['L mean 1'], gr_com['D mean 1'],
                       het_com['L mean 1'], het_com['D mean 1']], axis=1)
    time1.columns = ['gr ctr L', 'gr ctr D', 'het ctr L', 'het ctr D',
                     'gr com L', 'gr com D', 'het com L', 'het com D']
    time24 = pd.concat([gr_ctr['L mean 24'], gr_ctr['D mean 24'],
                        het_ctr['L mean 24'], het_ctr['D mean 24'],
                        gr_com['L mean 24'], gr_com['D mean 24'],
                        het_com['L mean 24'], het_com['D mean 24']], axis=1)
    time24.columns = ['gr ctr L', 'gr ctr D', 'het ctr L', 'het ctr D',
                      'gr com L', 'gr com D', 'het com L', 'het com D']
    time1 = match(time0, time1)
    time01 = match(time1, time0)
    time24 = match(time0, time24)
    time024 = match(time24, time0)
    # subtraction time: within fish between time points, now for 1h
    diff1 = time1.subtract(time01, axis=1)
    cut1 = diff1.iloc[range(int(startrow), int(endrow))]

    # subtraction time: within fish between time points, now for 24
    diff24 = time24.subtract(time024, axis=1)
    cut24 = diff24.iloc[range(int(startrow), int(endrow))]
    result = pd.concat([cut1, cut24], axis=1).mean().to_frame().T
    result.columns = ['gr ctr L 1', 'gr ctr D 1', 'het ctr L 1', 'het ctr D 1',
                      'gr com L 1', 'gr com D 1', 'het com L 1', 'het com D 1',
                      'gr ctr L 24', 'gr ctr D 24', 'het ctr L 24',
                      'het ctr D 24', 'gr com L 24', 'gr com D 24',
                      'het com L 24', 'het com D 24']
    return result


def relative_change(absolute_change):
    '''
    This function takes the pivoter output, and calculates the relative change,
    e.g. D1-0 = (gr drug 1 - gr drug 0) - (gr ctr 1 - gr ctr 0)
         D24-0 = (gr drug 24 - gr drug 0) - (gr ctr 24 - gr ctr 0)
    and saves to a csv file.
    '''
    absolute = absolute_change.copy(deep=True)
    # assembles 2 dataframes for com, ctr
    com = pd.concat([absolute['gr com D 1'], absolute['gr com D 24'],
                     absolute['gr com L 1'], absolute['gr com L 24'],
                     absolute['het com D 1'], absolute['het com D 24'],
                     absolute['het com L 1'], absolute['het com L 24']],
                    axis=1)
    com.columns = ['gr D 1', 'gr D 24', 'gr L 1', 'gr L 24', 'het D 1',
                   'het D 24', 'het L 1', 'het L 24']
    ctr = pd.concat([absolute['gr ctr D 1'], absolute['gr ctr D 24'],
                     absolute['gr ctr L 1'], absolute['gr ctr L 24'],
                     absolute['het ctr D 1'], absolute['het ctr D 24'],
                     absolute['het ctr L 1'], absolute['het ctr L 24']],
                    axis=1)
    ctr.columns = ['gr D 1', 'gr D 24', 'gr L 1', 'gr L 24', 'het D 1',
                   'het D 24', 'het L 1', 'het L 24']
    com = match(ctr, com)
    ctr = match(com, ctr)
    interresult = com.subtract(ctr, axis=1)
    interresult = interresult.replace(0, np.nan)
    count = [1]
    interresult['count'] = count
    result = pd.pivot_table(interresult, values=['gr D 1', 'gr D 24', 'gr L 1',
                                                 'gr L 24', 'het D 1',
                                                 'het D 24', 'het L 1',
                                                 'het L 24'], index='count',
                            dropna=False)
    return result

def transform(gr_com, het_com):
    copied1 = gr_com.copy(deep=True)
    copied2 = het_com.copy(deep=True)
    gr = copied1.mean().to_frame().T
    result1 = pd.concat([pd.concat([gr['D mean 0'], gr['D mean 1'], gr['D mean 24']]),
                        pd.concat([gr['D sem 0'], gr['D sem 1'], gr['D sem 24']]),
                        pd.concat([gr['L mean 0'], gr['L mean 1'], gr['L mean 24']]),
                        pd.concat([gr['L sem 0'], gr['L sem 1'], gr['L sem 24']])], axis=1)
    result1.columns = ['gr D mean', 'gr D sem', 'gr L mean', 'gr L sem']
    het = copied2.mean().to_frame().T
    result2 = pd.concat([pd.concat([het['D mean 0'], het['D mean 1'], het['D mean 24']]),
                        pd.concat([het['D sem 0'], het['D sem 1'], het['D sem 24']]),
                        pd.concat([het['L mean 0'], het['L mean 1'], het['L mean 24']]),
                        pd.concat([het['L sem 0'], het['L sem 1'], het['L sem 24']])], axis=1)
    result2.columns = ['het D mean', 'het D sem', 'het L mean', 'het L sem']
    result = pd.concat([result1, result2], axis=1)
    result = result.set_index(np.arange(1, 4))
    return result


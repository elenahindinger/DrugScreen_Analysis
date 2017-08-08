# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:29:28 2017

@author: ehindinger
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 17:13:36 2017

@author: ehindinger
"""

import pandas as pd
import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import itertools as it
import os
from natsort import natsorted
from formulas import *
from plots import *
from u_stats import *
# import random

os_path = r'I:/Elena H/DoseR_Analysis/OS new analysis/CSV FILES'
out_path = r'I:/Elena H/DoseR_Analysis/random 100/final/'

# selected = getRandomFiles(os_path)
x = 1
all_stats60 = pd.DataFrame()
all_stats10 = pd.DataFrame()
all_stats1 = pd.DataFrame()
all_traces = pd.DataFrame()
all_startle = pd.DataFrame()
filelist = natsorted(os.listdir(os_path))

for i in filelist:
    print str(i) + ' is number ' + str(x)
    main_dir = os_path + '/' + i + '/'

    a1 = buildfish(main_dir, 0)
    a10 = buildfish(main_dir, 1)
    a11 = buildfish(main_dir, 2)
    a12 = buildfish(main_dir, 3)
    a2 = buildfish(main_dir, 4)
    a3 = buildfish(main_dir, 5)
    a4 = buildfish(main_dir, 6)
    a5 = buildfish(main_dir, 7)
    a6 = buildfish(main_dir, 8)
    a7 = buildfish(main_dir, 9)
    a8 = buildfish(main_dir, 10)
    a9 = buildfish(main_dir, 11)
    b1 = buildfish(main_dir, 12)
    b10 = buildfish(main_dir, 13)
    b11 = buildfish(main_dir, 14)
    b12 = buildfish(main_dir, 15)
    b2 = buildfish(main_dir, 16)
    b3 = buildfish(main_dir, 17)
    b4 = buildfish(main_dir, 18)
    b5 = buildfish(main_dir, 19)
    b6 = buildfish(main_dir, 20)
    b7 = buildfish(main_dir, 21)
    b8 = buildfish(main_dir, 22)
    b9 = buildfish(main_dir, 23)
    c1 = buildfish(main_dir, 24)
    c10 = buildfish(main_dir, 25)
    c11 = buildfish(main_dir, 26)
    c12 = buildfish(main_dir, 27)
    c2 = buildfish(main_dir, 28)
    c3 = buildfish(main_dir, 29)
    c4 = buildfish(main_dir, 30)
    c5 = buildfish(main_dir, 31)
    c6 = buildfish(main_dir, 32)
    c7 = buildfish(main_dir, 33)
    c8 = buildfish(main_dir, 34)
    c9 = buildfish(main_dir, 35)
    d1 = buildfish(main_dir, 36)
    d10 = buildfish(main_dir, 37)
    d11 = buildfish(main_dir, 38)
    d12 = buildfish(main_dir, 39)
    d2 = buildfish(main_dir, 40)
    d3 = buildfish(main_dir, 41)
    d4 = buildfish(main_dir, 42)
    d5 = buildfish(main_dir, 43)
    d6 = buildfish(main_dir, 44)
    d7 = buildfish(main_dir, 45)
    d8 = buildfish(main_dir, 46)
    d9 = buildfish(main_dir, 47)
    e1 = buildfish(main_dir, 48)
    e10 = buildfish(main_dir, 49)
    e11 = buildfish(main_dir, 50)
    e12 = buildfish(main_dir, 51)
    e2 = buildfish(main_dir, 52)
    e3 = buildfish(main_dir, 53)
    e4 = buildfish(main_dir, 54)
    e5 = buildfish(main_dir, 55)
    e6 = buildfish(main_dir, 56)
    e7 = buildfish(main_dir, 57)
    e8 = buildfish(main_dir, 58)
    e9 = buildfish(main_dir, 59)
    f1 = buildfish(main_dir, 60)
    f10 = buildfish(main_dir, 61)
    f11 = buildfish(main_dir, 62)
    f12 = buildfish(main_dir, 63)
    f2 = buildfish(main_dir, 64)
    f3 = buildfish(main_dir, 65)
    f4 = buildfish(main_dir, 66)
    f5 = buildfish(main_dir, 67)
    f6 = buildfish(main_dir, 68)
    f7 = buildfish(main_dir, 69)
    f8 = buildfish(main_dir, 70)
    f9 = buildfish(main_dir, 71)
    g1 = buildfish(main_dir, 72)
    g10 = buildfish(main_dir, 73)
    g11 = buildfish(main_dir, 74)
    g12 = buildfish(main_dir, 75)
    g2 = buildfish(main_dir, 76)
    g3 = buildfish(main_dir, 77)
    g4 = buildfish(main_dir, 78)
    g5 = buildfish(main_dir, 79)
    g6 = buildfish(main_dir, 80)
    g7 = buildfish(main_dir, 81)
    g8 = buildfish(main_dir, 82)
    g9 = buildfish(main_dir, 83)
    h1 = buildfish(main_dir, 84)
    h10 = buildfish(main_dir, 85)
    h11 = buildfish(main_dir, 86)
    h12 = buildfish(main_dir, 87)
    h2 = buildfish(main_dir, 88)
    h3 = buildfish(main_dir, 89)
    h4 = buildfish(main_dir, 90)
    h5 = buildfish(main_dir, 91)
    h6 = buildfish(main_dir, 92)
    h7 = buildfish(main_dir, 93)
    h8 = buildfish(main_dir, 94)
    h9 = buildfish(main_dir, 95)

    animals = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12,
               b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12,
               c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12,
               d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12,
               e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12,
               f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12,
               g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12,
               h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12]

    # dfAll = big_dataframe(animals)
    # dfAll_resampled = big_dataframe_resampled(animals)
    dfAll_resampled_2 = big_dataframe_resampled_2(animals)
    all_traces = pd.concat([all_traces, dfAll_resampled_2])
    df_frames_2 = frame_resampled(animals, output=2)
    df_frames_1 = frame_resampled(animals, output=1)
    all_startle = pd.concat([all_startle, df_frames_1])

    trace_plot(dfAll_resampled_2, out_path, name=str(i), conc='20', n=48)
    trace_plot_frames_2sec(df_frames_2, out_path, name=str(i), conc='20', sec='2')
    trace_plot_frames_2sec(df_frames_1, out_path, name=str(i), conc='20', sec='1')

    stat60 = ttest(dfAll_resampled_2, plate_name=str(i), phase=60)
    stat10 = ttest(dfAll_resampled_2, plate_name=str(i), phase=10)
    all_stats60 = pd.concat([all_stats60, stat60])
    all_stats10 = pd.concat([all_stats10, stat10])
    
    stats_1 = ttest_frames(df_frames_1, plate_name=str(i))
    all_stats1 = pd.concat([all_stats1, stats_1])
    x += 1

x = 1
for i in filelist:
    print str(i) + ' is number ' + str(x)
    main_dir = os_path + '/' + i + '/'

    a1 = buildfish7(main_dir, 0)
    a10 = buildfish7(main_dir, 1)
    a11 = buildfish7(main_dir, 2)
    a12 = buildfish7(main_dir, 3)
    a2 = buildfish7(main_dir, 4)
    a3 = buildfish7(main_dir, 5)
    a4 = buildfish7(main_dir, 6)
    a5 = buildfish7(main_dir, 7)
    a6 = buildfish7(main_dir, 8)
    a7 = buildfish7(main_dir, 9)
    a8 = buildfish7(main_dir, 10)
    a9 = buildfish7(main_dir, 11)
    b1 = buildfish7(main_dir, 12)
    b10 = buildfish7(main_dir, 13)
    b11 = buildfish7(main_dir, 14)
    b12 = buildfish7(main_dir, 15)
    b2 = buildfish7(main_dir, 16)
    b3 = buildfish7(main_dir, 17)
    b4 = buildfish7(main_dir, 18)
    b5 = buildfish7(main_dir, 19)
    b6 = buildfish7(main_dir, 20)
    b7 = buildfish7(main_dir, 21)
    b8 = buildfish7(main_dir, 22)
    b9 = buildfish7(main_dir, 23)
    c1 = buildfish7(main_dir, 24)
    c10 = buildfish7(main_dir, 25)
    c11 = buildfish7(main_dir, 26)
    c12 = buildfish7(main_dir, 27)
    c2 = buildfish7(main_dir, 28)
    c3 = buildfish7(main_dir, 29)
    c4 = buildfish7(main_dir, 30)
    c5 = buildfish7(main_dir, 31)
    c6 = buildfish7(main_dir, 32)
    c7 = buildfish7(main_dir, 33)
    c8 = buildfish7(main_dir, 34)
    c9 = buildfish7(main_dir, 35)
    d1 = buildfish7(main_dir, 36)
    d10 = buildfish7(main_dir, 37)
    d11 = buildfish7(main_dir, 38)
    d12 = buildfish7(main_dir, 39)
    d2 = buildfish7(main_dir, 40)
    d3 = buildfish7(main_dir, 41)
    d4 = buildfish7(main_dir, 42)
    d5 = buildfish7(main_dir, 43)
    d6 = buildfish7(main_dir, 44)
    d7 = buildfish7(main_dir, 45)
    d8 = buildfish7(main_dir, 46)
    d9 = buildfish7(main_dir, 47)
    e1 = buildfish7(main_dir, 48)
    e10 = buildfish7(main_dir, 49)
    e11 = buildfish7(main_dir, 50)
    e12 = buildfish7(main_dir, 51)
    e2 = buildfish7(main_dir, 52)
    e3 = buildfish7(main_dir, 53)
    e4 = buildfish7(main_dir, 54)
    e5 = buildfish7(main_dir, 55)
    e6 = buildfish7(main_dir, 56)
    e7 = buildfish7(main_dir, 57)
    e8 = buildfish7(main_dir, 58)
    e9 = buildfish7(main_dir, 59)
    f1 = buildfish7(main_dir, 60)
    f10 = buildfish7(main_dir, 61)
    f11 = buildfish7(main_dir, 62)
    f12 = buildfish7(main_dir, 63)
    f2 = buildfish7(main_dir, 64)
    f3 = buildfish7(main_dir, 65)
    f4 = buildfish7(main_dir, 66)
    f5 = buildfish7(main_dir, 67)
    f6 = buildfish7(main_dir, 68)
    f7 = buildfish7(main_dir, 69)
    f8 = buildfish7(main_dir, 70)
    f9 = buildfish7(main_dir, 71)
    g1 = buildfish7(main_dir, 72)
    g10 = buildfish7(main_dir, 73)
    g11 = buildfish7(main_dir, 74)
    g12 = buildfish7(main_dir, 75)
    g2 = buildfish7(main_dir, 76)
    g3 = buildfish7(main_dir, 77)
    g4 = buildfish7(main_dir, 78)
    g5 = buildfish7(main_dir, 79)
    g6 = buildfish7(main_dir, 80)
    g7 = buildfish7(main_dir, 81)
    g8 = buildfish7(main_dir, 82)
    g9 = buildfish7(main_dir, 83)
    h1 = buildfish7(main_dir, 84)
    h10 = buildfish7(main_dir, 85)
    h11 = buildfish7(main_dir, 86)
    h12 = buildfish7(main_dir, 87)
    h2 = buildfish7(main_dir, 88)
    h3 = buildfish7(main_dir, 89)
    h4 = buildfish7(main_dir, 90)
    h5 = buildfish7(main_dir, 91)
    h6 = buildfish7(main_dir, 92)
    h7 = buildfish7(main_dir, 93)
    h8 = buildfish7(main_dir, 94)
    h9 = buildfish7(main_dir, 95)

    animals = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11, a12,
               b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12,
               c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12,
               d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12,
               e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12,
               f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12,
               g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12,
               h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12]

    # dfAll = big_dataframe(animals)
    # dfAll_resampled = big_dataframe_resampled(animals)
    dfAll_resampled_2 = big_dataframe_resampled_2(animals)
    all_traces = pd.concat([all_traces, dfAll_resampled_2])
    df_frames_2 = frame_resampled(animals, output=2)
    df_frames_1 = frame_resampled(animals, output=1)
    all_startle = pd.concat([all_startle, df_frames_1])

    trace_plot(dfAll_resampled_2, out_path, name=str(i), conc='7', n=48)
    trace_plot_frames_2sec(df_frames_2, out_path, name=str(i), conc='7', sec='2')
    trace_plot_frames_2sec(df_frames_1, out_path, name=str(i), conc='7', sec='1')

    stat60 = ttest(dfAll_resampled_2, plate_name=str(i), phase=60)
    stat10 = ttest(dfAll_resampled_2, plate_name=str(i), phase=10)
    all_stats60 = pd.concat([all_stats60, stat60])
    all_stats10 = pd.concat([all_stats10, stat10])
    
    stats_1 = ttest_frames(df_frames_1, plate_name=str(i))
    all_stats1 = pd.concat([all_stats1, stats_1])
    x += 1

print 'Done with iterations.'

all_stats_10 = add_conc(all_stats10)
all_stats_60 = add_conc(all_stats60)
all_stats_1 = add_conc(all_stats1)

savename60 = out_path + 'all_stats_60.csv'
all_stats_60.to_csv(savename60)

savename10 = out_path + 'all_stats_10.csv'
all_stats_10.to_csv(savename10)

savename1 = out_path + 'all_stats_1.csv'
all_stats_1.to_csv(savename1)

frequency_count_plot(all_stats_60, out_path, phase=60, info='condition')

pk = all_stats_10.groupby('phase')
pk.groups
ph1 = pk.get_group(1)
frequency_count_plot(ph1, out_path, phase='ph1', info='condition')

frequency_count_plot(all_stats_1, out_path, phase='startle', info='condition')
frequency_count_plot(all_stats_1, out_path, phase='startle', info='delay')

plot_each_phase(all_stats_10, out_path)


all_traces_mean = prepare_all_traces(all_traces)
trace_plot(all_traces_mean, out_path, name='all', conc='experiments', n=22080)
trace_plot_frames_2sec(all_startle, out_path, name='all', conc='experiments', n=22080)

print 'Saved frequency plots.'
#==============================================================================
# ''' From selfcounted observations '''
# di = {'Condition': ['GR > Het', 'GR = Het', 'GR < Het', 'Misc'],
#       'Frequency': [17, 59, 9, 15]}
# df = pd.DataFrame(data=di, index=np.arange(1, 5))
# frequency_bar_plot(df, out_path)
# frequency_pie_plot(df, out_path)
#==============================================================================



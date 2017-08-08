# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 15:41:05 2017

@author: ehindinger
"""

import pandas as pd
import numpy as np
import os
from combo_plotmaker import relative_plotmaker, absolute_plotmaker, plotmaker_means
from DoseR_lookup import doser_lookup_table, find_name
from natsort import natsorted

analysed = '1-60'
startrow = '1'
endrow = '4'
tps = '2-4'

# dictionary to find corresponding compound codes
f1 = r'P:/OS new analysis test/Compounds_Lookup_Table.xlsx'
f2 = r'I:/Elena H/DoseR_Analysis/Original_Screen/Initial Screen_Lookup Table.xlsx'

doser = pd.read_excel(f1, parse_cols=[0, 1], names=['Name', 'DoseR Code'])
oscreen = pd.read_excel(f2, parse_cols=[0, 2, 3], skip_footer=5,
                        names=['Name', 'Plate', 'Number'])
oscreen['Plate'] = oscreen['Plate'].apply(lambda x: '0{}'.format(x) if len(str(x))==1 else str(x))
oscreen['OS Code'] = oscreen['Plate'] + oscreen['Number']
oscreen = oscreen.drop(['Plate', 'Number'], axis=1)
df = pd.merge(oscreen, doser, on='Name')
df['Name'] = df['Name'].str.title()
df = df.set_index('DoseR Code')
code_dict = df.to_dict(orient='dict')

def find_name_or_code(dictionary, com_code, output):
    if output == 'Com Name':
        sub_dict = dictionary['Name']
    elif output == 'OS Code':
        sub_dict = dictionary['OS Code']
    for k, v in sub_dict.iteritems():
        if k == com_code:
            return v

# input directories
os_location = r'P:/OS new analysis test/OS Processed Output/1-60 s'
doser_location = r'P:/OS new analysis test/DoseR Processed Output/11 C03/1-60 sec'

# output directories
parent_folder = r'P:/OS new analysis test/combo output/60s'


def combo_plots(in_dir, out_dir):
    file_list = natsorted(os.listdir(in_dir))
    for i in file_list:
        doser_code = i
        print 'Combining ' + i
        os_code = find_name_or_code(code_dict, doser_code, output='OS Code')
    
        # output directories
        new_folder = out_dir + '/' + doser_code
        if not os.path.exists(new_folder):
            os.makedirs(new_folder)
    
        new_path_1 = new_folder + '/' + doser_code + '_relative_change_all.tiff'
        new_path_2 = new_folder + '/' + doser_code + '_absolute_change_all.tiff'
        new_path_3 = new_folder + '/' + doser_code + '_average_and_SEM_all.tiff'

        com_name = find_name_or_code(code_dict, doser_code, output='Com Name')
        a = os_location + '/' + os_code + '/' + os_code
        rel_os_7 = a + '_7uM_relative_change.csv'
        rel_os_20 = a + '_20uM_relative_change.csv'

        b = doser_location + '/' + doser_code + '/'
        r = '_relative_change.csv'
        rel_doser_01 = b + '0.1 uM' + '/' + doser_code + '_0.1uM' + r
        rel_doser_1 = b + '1 uM' + '/' + doser_code + '_1uM' + r
        rel_doser_10 = b + '10 uM' + '/' + doser_code + '_10uM' + r
        rel_doser_50 = b + '50 uM' + '/' + doser_code + '_50uM' + r
        rel_doser_100 = b + '100 uM' + '/' + doser_code + '_100uM' + r

        rel_7 = pd.read_csv(rel_os_7, index_col=[0])
        rel_20 = pd.read_csv(rel_os_20, index_col=[0])

        rel_01 = pd.read_csv(rel_doser_01, index_col=[0])
        rel_1 = pd.read_csv(rel_doser_1, index_col=[0])
        rel_10 = pd.read_csv(rel_doser_10, index_col=[0])
        rel_50 = pd.read_csv(rel_doser_50, index_col=[0])
        rel_100 = pd.read_csv(rel_doser_100, index_col=[0])

        relative = pd.concat([rel_01, rel_1, rel_7, rel_10, rel_20, rel_50, rel_100]).set_index(np.arange(7))

        relative_plotmaker(relative, com_name, analysed, tps, new_path_1)

        abs_os_7 = a + '_7uM_absolute_change.csv'
        abs_os_20 = a + '_20uM_absolute_change.csv'

        ab = '_absolute_change.csv'
        abs_doser_01 = b + '0.1 uM' + '/' + doser_code + '_0.1uM' + ab
        abs_doser_1 = b + '1 uM' + '/' + doser_code + '_1uM' + ab
        abs_doser_10 = b + '10 uM' + '/' + doser_code + '_10uM' + ab
        abs_doser_50 = b + '50 uM' + '/' + doser_code + '_50uM' + ab
        abs_doser_100 = b + '100 uM' + '/' + doser_code + '_100uM' + ab

        abs_7 = pd.read_csv(abs_os_7, index_col=[0])
        abs_20 = pd.read_csv(abs_os_20, index_col=[0])

        abs_01 = pd.read_csv(abs_doser_01, index_col=[0])
        abs_1 = pd.read_csv(abs_doser_1, index_col=[0])
        abs_10 = pd.read_csv(abs_doser_10, index_col=[0])
        abs_50 = pd.read_csv(abs_doser_50, index_col=[0])
        abs_100 = pd.read_csv(abs_doser_100, index_col=[0])

        absolute = pd.concat([abs_01, abs_1, abs_7, abs_10, abs_20, abs_50, abs_100]).set_index(np.arange(7))

        absolute_plotmaker(absolute, com_name, analysed, tps, new_path_2)

        m_os_7 = a + '_7uM_group_avg_per_tp.csv'
        m_os_20 = a + '_20uM_group_avg_per_tp.csv'

        m = '_group_avg_per_tp.csv'
        m_doser_01 = b + '0.1 uM' + '/' + doser_code + '_0.1uM' + m
        m_doser_1 = b + '1 uM' + '/' + doser_code + '_1uM' + m
        m_doser_10 = b + '10 uM' + '/' + doser_code + '_10uM' + m
        m_doser_50 = b + '50 uM' + '/' + doser_code + '_50uM' + m
        m_doser_100 = b + '100 uM' + '/' + doser_code + '_100uM' + m

        m_7 = pd.read_csv(m_os_7, index_col=[0]).T
        m_20 = pd.read_csv(m_os_20, index_col=[0]).T

        m_01 = pd.read_csv(m_doser_01, index_col=[0]).T
        m_1 = pd.read_csv(m_doser_1, index_col=[0]).T
        m_10 = pd.read_csv(m_doser_10, index_col=[0]).T
        m_50 = pd.read_csv(m_doser_50, index_col=[0]).T
        m_100 = pd.read_csv(m_doser_100, index_col=[0]).T

        mean_7 = m_7.iloc[range(int(startrow), int(endrow))].mean().to_frame().T
        mean_20 = m_20.iloc[range(int(startrow), int(endrow))].mean().to_frame().T
        mean_01 = m_01.iloc[range(int(startrow), int(endrow))].mean().to_frame().T
        mean_1 = m_1.iloc[range(int(startrow), int(endrow))].mean().to_frame().T
        mean_10 = m_10.iloc[range(int(startrow), int(endrow))].mean().to_frame().T
        mean_50 = m_50.iloc[range(int(startrow), int(endrow))].mean().to_frame().T
        mean_100 = m_100.iloc[range(int(startrow), int(endrow))].mean().to_frame().T

        plotmaker_means(mean_01, mean_1, mean_7, mean_10, mean_20, mean_50,
                        mean_100, com_name, analysed, tps, new_path_3)

combo_plots(doser_location, parent_folder)

# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 14:37:36 2017

@author: ehindinger
"""

import os
from natsort import natsorted
from DoseR_plotmaker import plotmaker_abs_avg, plotmaker_seconds, relative_plotmaker
from DoseR_plotmaker import plotmaker_seconds_pooled, absolute_plotmaker
from DoseR_plotmaker import group_trace_graph, plotmaker_means, group_trace_graph_seconds
from DoseR_main_formulas import buildfish, intogroups, ind_csv, pivoter, sum_by_seconds
from DoseR_main_formulas import group, normalisation_csv, relative_change, group_traces
from DoseR_main_formulas import new_buildfish, pooled, final, absolute_change
from DoseR_lookup import doser_lookup_table, find_name

''' This section should be left constant, but can be modified '''

# seconds to be analysed following light change, can be modified in formula script
analysed = '1-60'
# timepoints to be averaged for absolute and relative change
# rows are 0 indexed so tp1=0, tp2=1, tp3=2, tp4=3
# function uses range, so to use all timepoints, do starttp=0, endtp=4
# tps utilised by graphs, here indexing starts at 1 again!
starttp = '1'
endtp = '4'
tps = '2-4'

conc1 = '0.1'
conc2 = '1'
conc3 = '10'
conc4 = '50'
conc5 = '100'

# grabs the look up table and extracts file names
xlfile = r'P:/OS new analysis test/Compounds_Lookup_Table.xlsx'
compounds = doser_lookup_table(xlfile, output='compound')

''' CHANGE INPUT FOLDER BELOW '''

# location of input files (with forward slash at end)
input_dir = r'P:/OS new analysis test/DoseR Split Output/'
output_dir = r'P:/OS new analysis test/DoseR Processed Output/11 C03/1-60 sec/'


def megafunc(in_dir, out_dir):
    input_list = natsorted(os.listdir(in_dir))
    for i in input_list:
        main_dir = in_dir + i
        plate_code = i
        print plate_code + ' is being processed.'

        ''' Makes output folder '''
 
        new_folder = out_dir + i

        ''' FROM THIS POINT ON DO NOT MODIFY '''

        # compound names and codes
        com_name = find_name(compounds, plate_code)

        new_filename_1 = plate_code + '_0.1uM_individual_values.csv'
        new_filename_2 = plate_code + '_1uM_individual_values.csv'
        new_filename_3 = plate_code + '_10uM_individual_values.csv'
        new_filename_4 = plate_code + '_50uM_individual_values.csv'
        new_filename_5 = plate_code + '_100uM_individual_values.csv'

        # group averages per timepoint
        new_filename_6 = plate_code + '_0.1uM_group_avg_per_tp.csv'
        new_filename_7 = plate_code + '_1uM_group_avg_per_tp.csv'
        new_filename_8 = plate_code + '_10uM_group_avg_per_tp.csv'
        new_filename_9 = plate_code + '_50uM_group_avg_per_tp.csv'
        new_filename_10 = plate_code + '_100uM_group_avg_per_tp.csv'

        # average distance per timepoint graphs
        new_filename_11 = plate_code + '_0.1uM_graph_avg_dist_per_tp.tiff'
        new_filename_12 = plate_code + '_1uM_graph_avg_dist_per_tp.tiff'
        new_filename_13 = plate_code + '_10uM_graph_avg_dist_per_tp.tiff'
        new_filename_14 = plate_code + '_50uM_graph_avg_dist_per_tp.tiff'
        new_filename_15 = plate_code + '_100uM_graph_avg_dist_per_tp.tiff'

        # absolute change
        new_filename_16 = plate_code + '_0.1uM_normalised.csv'
        new_filename_17 = plate_code + '_1uM_normalised.csv'
        new_filename_18 = plate_code + '_10uM_normalised.csv'
        new_filename_19 = plate_code + '_50uM_normalised.csv'
        new_filename_20 = plate_code + '_100uM_normalised.csv'

        # absolute change
        new_filename_39 = plate_code + '_0.1uM_absolute_change.csv'
        new_filename_40 = plate_code + '_1uM_absolute_change.csv'
        new_filename_41 = plate_code + '_10uM_absolute_change.csv'
        new_filename_42 = plate_code + '_50uM_absolute_change.csv'
        new_filename_43 = plate_code + '_100uM_absolute_change.csv'

        # relative change
        new_filename_21 = plate_code + '_0.1uM_relative_change.csv'
        new_filename_22 = plate_code + '_1uM_relative_change.csv'
        new_filename_23 = plate_code + '_10uM_relative_change.csv'
        new_filename_24 = plate_code + '_50uM_relative_change.csv'
        new_filename_25 = plate_code + '_100uM_relative_change.csv'

        # seconds plot
        new_filename_26 = plate_code + '_0.1uM_graph_avg_dist_seconds.tiff'
        new_filename_27 = plate_code + '_1uM_graph_avg_dist_seconds.tiff'
        new_filename_28 = plate_code + '_10uM_graph_avg_dist_seconds.tiff'
        new_filename_29 = plate_code + '_50uM_graph_avg_dist_seconds.tiff'
        new_filename_30 = plate_code + '_100uM_graph_avg_dist_seconds.tiff'

        # seconds_pooled plot
        new_filename_31 = plate_code + '_0.1uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_32 = plate_code + '_1uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_33 = plate_code + '_10uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_34 = plate_code + '_50uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_35 = plate_code + '_100uM_graph_avg_dist_seconds_pooled.tiff'

        # all concentration plots
        new_filename_36 = plate_code + '_absolute_change.tiff'
        new_filename_37 = plate_code + '_relative_change.tiff'
        new_filename_38 = plate_code + '_average_and_SEM.tiff'

        # trace graphs
        new_filename_44 = plate_code + '_trace_graph_frames.tiff'
        new_filename_45 = plate_code + '_trace_graph_seconds.tiff'

        # makes new folders for each compound
        new_folder_1 = new_folder + '/0.1 uM'
        if not os.path.exists(new_folder_1):
            os.makedirs(new_folder_1)

        new_folder_2 = new_folder + '/1 uM'
        if not os.path.exists(new_folder_2):
            os.makedirs(new_folder_2)

        new_folder_3 = new_folder + '/10 uM'
        if not os.path.exists(new_folder_3):
            os.makedirs(new_folder_3)

        new_folder_4 = new_folder + '/50 uM'
        if not os.path.exists(new_folder_4):
            os.makedirs(new_folder_4)

        new_folder_5 = new_folder + '/100 uM'
        if not os.path.exists(new_folder_5):
            os.makedirs(new_folder_5)

        # selects location for csv files
        # individual values
        new_path_1 = new_folder_1 + '/' + new_filename_1
        new_path_2 = new_folder_2 + '/' + new_filename_2
        new_path_3 = new_folder_3 + '/' + new_filename_3
        new_path_4 = new_folder_4 + '/' + new_filename_4
        new_path_5 = new_folder_5 + '/' + new_filename_5
        # group averages per tp
        new_path_6 = new_folder_1 + '/' + new_filename_6
        new_path_7 = new_folder_2 + '/' + new_filename_7
        new_path_8 = new_folder_3 + '/' + new_filename_8
        new_path_9 = new_folder_4 + '/' + new_filename_9
        new_path_10 = new_folder_5 + '/' + new_filename_10
        # graph for avg dist per tp
        new_path_11 = new_folder_1 + '/' + new_filename_11
        new_path_12 = new_folder_2 + '/' + new_filename_12
        new_path_13 = new_folder_3 + '/' + new_filename_13
        new_path_14 = new_folder_4 + '/' + new_filename_14
        new_path_15 = new_folder_5 + '/' + new_filename_15
        # normalised  path
        new_path_16 = new_folder_1 + '/' + new_filename_16
        new_path_17 = new_folder_2 + '/' + new_filename_17
        new_path_18 = new_folder_3 + '/' + new_filename_18
        new_path_19 = new_folder_4 + '/' + new_filename_19
        new_path_20 = new_folder_5 + '/' + new_filename_20
        # absolute change path
        new_path_39 = new_folder_1 + '/' + new_filename_39
        new_path_40 = new_folder_2 + '/' + new_filename_40
        new_path_41 = new_folder_3 + '/' + new_filename_41
        new_path_42 = new_folder_4 + '/' + new_filename_42
        new_path_43 = new_folder_5 + '/' + new_filename_43
        # relative change path
        new_path_21 = new_folder_1 + '/' + new_filename_21
        new_path_22 = new_folder_2 + '/' + new_filename_22
        new_path_23 = new_folder_3 + '/' + new_filename_23
        new_path_24 = new_folder_4 + '/' + new_filename_24
        new_path_25 = new_folder_5 + '/' + new_filename_25
        # seconds plot path
        new_path_26 = new_folder_1 + '/' + new_filename_26
        new_path_27 = new_folder_2 + '/' + new_filename_27
        new_path_28 = new_folder_3 + '/' + new_filename_28
        new_path_29 = new_folder_4 + '/' + new_filename_29
        new_path_30 = new_folder_5 + '/' + new_filename_30
        # seconds pooled plot path
        new_path_31 = new_folder_1 + '/' + new_filename_31
        new_path_32 = new_folder_2 + '/' + new_filename_32
        new_path_33 = new_folder_3 + '/' + new_filename_33
        new_path_34 = new_folder_4 + '/' + new_filename_34
        new_path_35 = new_folder_5 + '/' + new_filename_35
        # all concentration graphs
        new_path_36 = new_folder + '/' + new_filename_36
        new_path_37 = new_folder + '/' + new_filename_37
        new_path_38 = new_folder + '/' + new_filename_38
        # trace graphs
        new_path_44 = new_folder + '/' + new_filename_44
        new_path_45 = new_folder + '/' + new_filename_45     

        print '     Reading input files ...'
        # reads csv files, builds fish
        a1_p1 = buildfish(main_dir, 0)
        a10_p1 = buildfish(main_dir, 1)
        a11_p1 = buildfish(main_dir, 2)
        a12_p1 = buildfish(main_dir, 3)
        a2_p1 = buildfish(main_dir, 4)
        a3_p1 = buildfish(main_dir, 5)
        a4_p1 = buildfish(main_dir, 6)
        a5_p1 = buildfish(main_dir, 7)
        a6_p1 = buildfish(main_dir, 8)
        a7_p1 = buildfish(main_dir, 9)
        a8_p1 = buildfish(main_dir, 10)
        a9_p1 = buildfish(main_dir, 11)
        b1_p1 = buildfish(main_dir, 12)
        b10_p1 = buildfish(main_dir, 13)
        b11_p1 = buildfish(main_dir, 14)
        b12_p1 = buildfish(main_dir, 15)
        b2_p1 = buildfish(main_dir, 16)
        b3_p1 = buildfish(main_dir, 17)
        b4_p1 = buildfish(main_dir, 18)
        b5_p1 = buildfish(main_dir, 19)
        b6_p1 = buildfish(main_dir, 20)
        b7_p1 = buildfish(main_dir, 21)
        b8_p1 = buildfish(main_dir, 22)
        b9_p1 = buildfish(main_dir, 23)
        c1_p1 = buildfish(main_dir, 24)
        c10_p1 = buildfish(main_dir, 25)
        c11_p1 = buildfish(main_dir, 26)
        c12_p1 = buildfish(main_dir, 27)
        c2_p1 = buildfish(main_dir, 28)
        c3_p1 = buildfish(main_dir, 29)
        c4_p1 = buildfish(main_dir, 30)
        c5_p1 = buildfish(main_dir, 31)
        c6_p1 = buildfish(main_dir, 32)
        c7_p1 = buildfish(main_dir, 33)
        c8_p1 = buildfish(main_dir, 34)
        c9_p1 = buildfish(main_dir, 35)
        d1_p1 = buildfish(main_dir, 36)
        d10_p1 = buildfish(main_dir, 37)
        d11_p1 = buildfish(main_dir, 38)
        d12_p1 = buildfish(main_dir, 39)
        d2_p1 = buildfish(main_dir, 40)
        d3_p1 = buildfish(main_dir, 41)
        d4_p1 = buildfish(main_dir, 42)
        d5_p1 = buildfish(main_dir, 43)
        d6_p1 = buildfish(main_dir, 44)
        d7_p1 = buildfish(main_dir, 45)
        d8_p1 = buildfish(main_dir, 46)
        d9_p1 = buildfish(main_dir, 47)
        e1_p1 = buildfish(main_dir, 48)
        e10_p1 = buildfish(main_dir, 49)
        e11_p1 = buildfish(main_dir, 50)
        e12_p1 = buildfish(main_dir, 51)
        e2_p1 = buildfish(main_dir, 52)
        e3_p1 = buildfish(main_dir, 53)
        e4_p1 = buildfish(main_dir, 54)
        e5_p1 = buildfish(main_dir, 55)
        e6_p1 = buildfish(main_dir, 56)
        e7_p1 = buildfish(main_dir, 57)
        e8_p1 = buildfish(main_dir, 58)
        e9_p1 = buildfish(main_dir, 59)
        f1_p1 = buildfish(main_dir, 60)
        f10_p1 = buildfish(main_dir, 61)
        f11_p1 = buildfish(main_dir, 62)
        f12_p1 = buildfish(main_dir, 63)
        f2_p1 = buildfish(main_dir, 64)
        f3_p1 = buildfish(main_dir, 65)
        f4_p1 = buildfish(main_dir, 66)
        f5_p1 = buildfish(main_dir, 67)
        f6_p1 = buildfish(main_dir, 68)
        f7_p1 = buildfish(main_dir, 69)
        f8_p1 = buildfish(main_dir, 70)
        f9_p1 = buildfish(main_dir, 71)
        g1_p1 = buildfish(main_dir, 72)
        g10_p1 = buildfish(main_dir, 73)
        g11_p1 = buildfish(main_dir, 74)
        g12_p1 = buildfish(main_dir, 75)
        g2_p1 = buildfish(main_dir, 76)
        g3_p1 = buildfish(main_dir, 77)
        g4_p1 = buildfish(main_dir, 78)
        g5_p1 = buildfish(main_dir, 79)
        g6_p1 = buildfish(main_dir, 80)
        g7_p1 = buildfish(main_dir, 81)
        g8_p1 = buildfish(main_dir, 82)
        g9_p1 = buildfish(main_dir, 83)
        h1_p1 = buildfish(main_dir, 84)
        h10_p1 = buildfish(main_dir, 85)
        h11_p1 = buildfish(main_dir, 86)
        h12_p1 = buildfish(main_dir, 87)
        h2_p1 = buildfish(main_dir, 88)
        h3_p1 = buildfish(main_dir, 89)
        h4_p1 = buildfish(main_dir, 90)
        h5_p1 = buildfish(main_dir, 91)
        h6_p1 = buildfish(main_dir, 92)
        h7_p1 = buildfish(main_dir, 93)
        h8_p1 = buildfish(main_dir, 94)
        h9_p1 = buildfish(main_dir, 95)

        gr_ctr_f = group_traces(a1_p1, b1_p1, c1_p1, d1_p1,
                                a2_p1, b2_p1, c2_p1, d2_p1,
                                a3_p1, b3_p1, c3_p1, d3_p1,
                                a4_p1, b4_p1, c4_p1, d4_p1,
                                a5_p1, b5_p1, c5_p1, d5_p1,
                                a6_p1, b6_p1, c6_p1, d6_p1,
                                a7_p1, b7_p1, c7_p1, d7_p1,
                                a8_p1, b8_p1, c8_p1, d8_p1,
                                a9_p1, b9_p1, c9_p1, d9_p1,
                                a10_p1, b10_p1, c10_p1, d10_p1,
                                a11_p1, b11_p1, c11_p1, d11_p1,
                                a12_p1, b12_p1, c12_p1, d12_p1)
        het_ctr_f = group_traces(e1_p1, f1_p1, g1_p1, h1_p1,
                                e2_p1, f2_p1, g2_p1, h2_p1,
                                e3_p1, f3_p1, g3_p1, h3_p1,
                                e4_p1, f4_p1, g4_p1, h4_p1,
                                e5_p1, f5_p1, g5_p1, h5_p1,
                                e6_p1, f6_p1, g6_p1, h6_p1,
                                e7_p1, f7_p1, g7_p1, h7_p1,
                                e8_p1, f8_p1, g8_p1, h8_p1,
                                e9_p1, f9_p1, g9_p1, h9_p1,
                                e10_p1, f10_p1, g10_p1, h10_p1,
                                e11_p1, f11_p1, g11_p1, h11_p1,
                                e12_p1, f12_p1, g12_p1, h12_p1)

        group_trace_graph(gr_ctr_f, het_ctr_f, new_path_44)

        a1_p2 = sum_by_seconds(a1_p1)
        a10_p2 = sum_by_seconds(a10_p1)
        a11_p2 = sum_by_seconds(a11_p1)
        a12_p2 = sum_by_seconds(a12_p1)
        a2_p2 = sum_by_seconds(a2_p1)
        a3_p2 = sum_by_seconds(a3_p1)
        a4_p2 = sum_by_seconds(a4_p1)
        a5_p2 = sum_by_seconds(a5_p1)
        a6_p2 = sum_by_seconds(a6_p1)
        a7_p2 = sum_by_seconds(a7_p1)
        a8_p2 = sum_by_seconds(a8_p1)
        a9_p2 = sum_by_seconds(a9_p1)
        b1_p2 = sum_by_seconds(b1_p1)
        b10_p2 = sum_by_seconds(b10_p1)
        b11_p2 = sum_by_seconds(b11_p1)
        b12_p2 = sum_by_seconds(b12_p1)
        b2_p2 = sum_by_seconds(b2_p1)
        b3_p2 = sum_by_seconds(b3_p1)
        b4_p2 = sum_by_seconds(b4_p1)
        b5_p2 = sum_by_seconds(b5_p1)
        b6_p2 = sum_by_seconds(b6_p1)
        b7_p2 = sum_by_seconds(b7_p1)
        b8_p2 = sum_by_seconds(b8_p1)
        b9_p2 = sum_by_seconds(b9_p1)
        c1_p2 = sum_by_seconds(c1_p1)
        c10_p2 = sum_by_seconds(c10_p1)
        c11_p2 = sum_by_seconds(c11_p1)
        c12_p2 = sum_by_seconds(c12_p1)
        c2_p2 = sum_by_seconds(c2_p1)
        c3_p2 = sum_by_seconds(c3_p1)
        c4_p2 = sum_by_seconds(c4_p1)
        c5_p2 = sum_by_seconds(c5_p1)
        c6_p2 = sum_by_seconds(c6_p1)
        c7_p2 = sum_by_seconds(c7_p1)
        c8_p2 = sum_by_seconds(c8_p1)
        c9_p2 = sum_by_seconds(c9_p1)
        d1_p2 = sum_by_seconds(d1_p1)
        d10_p2 = sum_by_seconds(d10_p1)
        d11_p2 = sum_by_seconds(d11_p1)
        d12_p2 = sum_by_seconds(d12_p1)
        d2_p2 = sum_by_seconds(d2_p1)
        d3_p2 = sum_by_seconds(d3_p1)
        d4_p2 = sum_by_seconds(d4_p1)
        d5_p2 = sum_by_seconds(d5_p1)
        d6_p2 = sum_by_seconds(d6_p1)
        d7_p2 = sum_by_seconds(d7_p1)
        d8_p2 = sum_by_seconds(d8_p1)
        d9_p2 = sum_by_seconds(d9_p1)
        e1_p2 = sum_by_seconds(e1_p1)
        e10_p2 = sum_by_seconds(e10_p1)
        e11_p2 = sum_by_seconds(e11_p1)
        e12_p2 = sum_by_seconds(e12_p1)
        e2_p2 = sum_by_seconds(e2_p1)
        e3_p2 = sum_by_seconds(e3_p1)
        e4_p2 = sum_by_seconds(e4_p1)
        e5_p2 = sum_by_seconds(e5_p1)
        e6_p2 = sum_by_seconds(e6_p1)
        e7_p2 = sum_by_seconds(e7_p1)
        e8_p2 = sum_by_seconds(e8_p1)
        e9_p2 = sum_by_seconds(e9_p1)
        f1_p2 = sum_by_seconds(f1_p1)
        f10_p2 = sum_by_seconds(f10_p1)
        f11_p2 = sum_by_seconds(f11_p1)
        f12_p2 = sum_by_seconds(f12_p1)
        f2_p2 = sum_by_seconds(f2_p1)
        f3_p2 = sum_by_seconds(f3_p1)
        f4_p2 = sum_by_seconds(f4_p1)
        f5_p2 = sum_by_seconds(f5_p1)
        f6_p2 = sum_by_seconds(f6_p1)
        f7_p2 = sum_by_seconds(f7_p1)
        f8_p2 = sum_by_seconds(f8_p1)
        f9_p2 = sum_by_seconds(f9_p1)
        g1_p2 = sum_by_seconds(g1_p1)
        g10_p2 = sum_by_seconds(g10_p1)
        g11_p2 = sum_by_seconds(g11_p1)
        g12_p2 = sum_by_seconds(g12_p1)
        g2_p2 = sum_by_seconds(g2_p1)
        g3_p2 = sum_by_seconds(g3_p1)
        g4_p2 = sum_by_seconds(g4_p1)
        g5_p2 = sum_by_seconds(g5_p1)
        g6_p2 = sum_by_seconds(g6_p1)
        g7_p2 = sum_by_seconds(g7_p1)
        g8_p2 = sum_by_seconds(g8_p1)
        g9_p2 = sum_by_seconds(g9_p1)
        h1_p2 = sum_by_seconds(h1_p1)
        h10_p2 = sum_by_seconds(h10_p1)
        h11_p2 = sum_by_seconds(h11_p1)
        h12_p2 = sum_by_seconds(h12_p1)
        h2_p2 = sum_by_seconds(h2_p1)
        h3_p2 = sum_by_seconds(h3_p1)
        h4_p2 = sum_by_seconds(h4_p1)
        h5_p2 = sum_by_seconds(h5_p1)
        h6_p2 = sum_by_seconds(h6_p1)
        h7_p2 = sum_by_seconds(h7_p1)
        h8_p2 = sum_by_seconds(h8_p1)
        h9_p2 = sum_by_seconds(h9_p1)

        gr_ctr_s = group_traces(a1_p2, b1_p2, c1_p2, d1_p2,
                                a2_p2, b2_p2, c2_p2, d2_p2,
                                a3_p2, b3_p2, c3_p2, d3_p2,
                                a4_p2, b4_p2, c4_p2, d4_p2,
                                a5_p2, b5_p2, c5_p2, d5_p2,
                                a6_p2, b6_p2, c6_p2, d6_p2,
                                a7_p2, b7_p2, c7_p2, d7_p2,
                                a8_p2, b8_p2, c8_p2, d8_p2,
                                a9_p2, b9_p2, c9_p2, d9_p2,
                                a10_p2, b10_p2, c10_p2, d10_p2,
                                a11_p2, b11_p2, c11_p2, d11_p2,
                                a12_p2, b12_p2, c12_p2, d12_p2)
        het_ctr_s = group_traces(e1_p2, f1_p2, g1_p2, h1_p2,
                                e2_p2, f2_p2, g2_p2, h2_p2,
                                e3_p2, f3_p2, g3_p2, h3_p2,
                                e4_p2, f4_p2, g4_p2, h4_p2,
                                e5_p2, f5_p2, g5_p2, h5_p2,
                                e6_p2, f6_p2, g6_p2, h6_p2,
                                e7_p2, f7_p2, g7_p2, h7_p2,
                                e8_p2, f8_p2, g8_p2, h8_p2,
                                e9_p2, f9_p2, g9_p2, h9_p2,
                                e10_p2, f10_p2, g10_p2, h10_p2,
                                e11_p2, f11_p2, g11_p2, h11_p2,
                                e12_p2, f12_p2, g12_p2, h12_p2)

        group_trace_graph_seconds(gr_ctr_s, het_ctr_s, new_path_45)

        print '     Computing analysis ...'

        ''' Insert Section on seconds plots '''

        gr_ctr = final(a1_p2, b1_p2, c1_p2, d1_p2, a12_p2,
                       b12_p2, c12_p2, d12_p2)
        het_ctr = final(e1_p2, f1_p2, g1_p2, h1_p2, e12_p2,
                        f12_p2, g12_p2, h12_p2)
        gr_com1 = final(a2_p2, b2_p2, c2_p2, d2_p2, a3_p2, b3_p2, c3_p2,
                        d3_p2)
        het_com1 = final(e2_p2, f2_p2, g2_p2, h2_p2, e3_p2, f3_p2, g3_p2,
                         h3_p2)
        gr_com2 = final(a4_p2, b4_p2, c4_p2, d4_p2, a5_p2, b5_p2, c5_p2,
                        d5_p2)
        het_com2 = final(e4_p2, f4_p2, g4_p2, h4_p2, e5_p2, f5_p2, g5_p2,
                         h5_p2)
        gr_com3 = final(a6_p2, b6_p2, c6_p2, d6_p2, a7_p2, b7_p2, c7_p2,
                        d7_p2)
        het_com3 = final(e6_p2, f6_p2, g6_p2, h6_p2, e7_p2, f7_p2, g7_p2,
                         h7_p2)
        gr_com4 = final(a8_p2, b8_p2, c8_p2, d8_p2, a9_p2, b9_p2, c9_p2,
                        d9_p2)
        het_com4 = final(e8_p2, f8_p2, g8_p2, h8_p2, e9_p2, f9_p2, g9_p2,
                         h9_p2)
        gr_com5 = final(a10_p2, b10_p2, c10_p2, d10_p2, a11_p2, b11_p2, c11_p2,
                        d11_p2)
        het_com5 = final(e10_p2, f10_p2, g10_p2, h10_p2, e11_p2, f11_p2,
                         g11_p2, h11_p2)

        ''' take mean of all grs, hets n=48 '''

        gr_dist0 = pooled(a1_p2, b1_p2, c1_p2, d1_p2, a2_p2, b2_p2, c2_p2,
                          d2_p2, a3_p2, b3_p2, c3_p2, d3_p2, a4_p2, b4_p2,
                          c4_p2, d4_p2, a5_p2, b5_p2, c5_p2, d5_p2, a6_p2,
                          b6_p2, c6_p2, d6_p2, a7_p2, b7_p2, c7_p2, d7_p2,
                          a8_p2, b8_p2, c8_p2, d8_p2, a9_p2, b9_p2, c9_p2,
                          d9_p2, a10_p2, b10_p2, c10_p2, d10_p2, a11_p2,
                          b11_p2, c11_p2, d11_p2, a12_p2, b12_p2, c12_p2,
                          d12_p2)

        het_dist0 = pooled(e1_p2, f1_p2, g1_p2, h1_p2, e2_p2, f2_p2, g2_p2,
                           h2_p2, e3_p2, f3_p2, g3_p2, h3_p2, e4_p2, f4_p2,
                           g4_p2, h4_p2, e5_p2, f5_p2, g5_p2, h5_p2, e6_p2,
                           f6_p2, g6_p2, h6_p2, e7_p2, f7_p2, g7_p2, h7_p2,
                           e8_p2, f8_p2, g8_p2, h8_p2, e9_p2, f9_p2, g9_p2,
                           h9_p2, e10_p2, f10_p2, g10_p2, h10_p2, e11_p2,
                           f11_p2, g11_p2, h11_p2, e12_p2, f12_p2, g12_p2,
                           h12_p2)

        plotmaker_seconds(gr_ctr, het_ctr, gr_com1, het_com1, conc1,
                          com_name, new_path_26)
        plotmaker_seconds(gr_ctr, het_ctr, gr_com2, het_com2, conc2,
                          com_name, new_path_27)
        plotmaker_seconds(gr_ctr, het_ctr, gr_com3, het_com3, conc3,
                          com_name, new_path_28)
        plotmaker_seconds(gr_ctr, het_ctr, gr_com4, het_com4, conc4,
                          com_name, new_path_29)
        plotmaker_seconds(gr_ctr, het_ctr, gr_com5, het_com5, conc5,
                          com_name, new_path_30)

        plotmaker_seconds_pooled(gr_dist0, het_dist0, gr_ctr, het_ctr,
                                 gr_com1, het_com1, conc1, com_name,
                                 new_path_31)
        plotmaker_seconds_pooled(gr_dist0, het_dist0, gr_ctr, het_ctr,
                                 gr_com2, het_com2, conc2, com_name,
                                 new_path_32)
        plotmaker_seconds_pooled(gr_dist0, het_dist0, gr_ctr, het_ctr,
                                 gr_com3, het_com3, conc3, com_name,
                                 new_path_33)
        plotmaker_seconds_pooled(gr_dist0, het_dist0, gr_ctr, het_ctr,
                                 gr_com4, het_com4, conc4, com_name,
                                 new_path_34)
        plotmaker_seconds_pooled(gr_dist0, het_dist0, gr_ctr, het_ctr,
                                 gr_com5, het_com5, conc5, com_name,
                                 new_path_35)

        a1 = new_buildfish(a1_p2)
        a10 = new_buildfish(a10_p2)
        a11 = new_buildfish(a11_p2)
        a12 = new_buildfish(a12_p2)
        a2 = new_buildfish(a2_p2)
        a3 = new_buildfish(a3_p2)
        a4 = new_buildfish(a4_p2)
        a5 = new_buildfish(a5_p2)
        a6 = new_buildfish(a6_p2)
        a7 = new_buildfish(a7_p2)
        a8 = new_buildfish(a8_p2)
        a9 = new_buildfish(a9_p2)
        b1 = new_buildfish(b1_p2)
        b10 = new_buildfish(b10_p2)
        b11 = new_buildfish(b11_p2)
        b12 = new_buildfish(b12_p2)
        b2 = new_buildfish(b2_p2)
        b3 = new_buildfish(b3_p2)
        b4 = new_buildfish(b4_p2)
        b5 = new_buildfish(b5_p2)
        b6 = new_buildfish(b6_p2)
        b7 = new_buildfish(b7_p2)
        b8 = new_buildfish(b8_p2)
        b9 = new_buildfish(b9_p2)
        c1 = new_buildfish(c1_p2)
        c10 = new_buildfish(c10_p2)
        c11 = new_buildfish(c11_p2)
        c12 = new_buildfish(c12_p2)
        c2 = new_buildfish(c2_p2)
        c3 = new_buildfish(c3_p2)
        c4 = new_buildfish(c4_p2)
        c5 = new_buildfish(c5_p2)
        c6 = new_buildfish(c6_p2)
        c7 = new_buildfish(c7_p2)
        c8 = new_buildfish(c8_p2)
        c9 = new_buildfish(c9_p2)
        d1 = new_buildfish(d1_p2)
        d10 = new_buildfish(d10_p2)
        d11 = new_buildfish(d11_p2)
        d12 = new_buildfish(d12_p2)
        d2 = new_buildfish(d2_p2)
        d3 = new_buildfish(d3_p2)
        d4 = new_buildfish(d4_p2)
        d5 = new_buildfish(d5_p2)
        d6 = new_buildfish(d6_p2)
        d7 = new_buildfish(d7_p2)
        d8 = new_buildfish(d8_p2)
        d9 = new_buildfish(d9_p2)
        e1 = new_buildfish(e1_p2)
        e10 = new_buildfish(e10_p2)
        e11 = new_buildfish(e11_p2)
        e12 = new_buildfish(e12_p2)
        e2 = new_buildfish(e2_p2)
        e3 = new_buildfish(e3_p2)
        e4 = new_buildfish(e4_p2)
        e5 = new_buildfish(e5_p2)
        e6 = new_buildfish(e6_p2)
        e7 = new_buildfish(e7_p2)
        e8 = new_buildfish(e8_p2)
        e9 = new_buildfish(e9_p2)
        f1 = new_buildfish(f1_p2)
        f10 = new_buildfish(f10_p2)
        f11 = new_buildfish(f11_p2)
        f12 = new_buildfish(f12_p2)
        f2 = new_buildfish(f2_p2)
        f3 = new_buildfish(f3_p2)
        f4 = new_buildfish(f4_p2)
        f5 = new_buildfish(f5_p2)
        f6 = new_buildfish(f6_p2)
        f7 = new_buildfish(f7_p2)
        f8 = new_buildfish(f8_p2)
        f9 = new_buildfish(f9_p2)
        g1 = new_buildfish(g1_p2)
        g10 = new_buildfish(g10_p2)
        g11 = new_buildfish(g11_p2)
        g12 = new_buildfish(g12_p2)
        g2 = new_buildfish(g2_p2)
        g3 = new_buildfish(g3_p2)
        g4 = new_buildfish(g4_p2)
        g5 = new_buildfish(g5_p2)
        g6 = new_buildfish(g6_p2)
        g7 = new_buildfish(g7_p2)
        g8 = new_buildfish(g8_p2)
        g9 = new_buildfish(g9_p2)
        h1 = new_buildfish(h1_p2)
        h10 = new_buildfish(h10_p2)
        h11 = new_buildfish(h11_p2)
        h12 = new_buildfish(h12_p2)
        h2 = new_buildfish(h2_p2)
        h3 = new_buildfish(h3_p2)
        h4 = new_buildfish(h4_p2)
        h5 = new_buildfish(h5_p2)
        h6 = new_buildfish(h6_p2)
        h7 = new_buildfish(h7_p2)
        h8 = new_buildfish(h8_p2)
        h9 = new_buildfish(h9_p2)

        '''
        this selects dark, min 2-8, all seconds, mean distance
        a1.loc[('D', [2, 4, 6, 8]), 'mean']

        this selects dark, min 2-8, all seconds, sem distance
        a1.loc[('D', [2, 4, 6, 8]), 'sem']

        this selects light, min 1-7, all seconds, mean distance
        a1.loc[('L', [1, 3, 5, 7]), 'mean']

        this selects light, min 1-7, all seconds, mean distance
        a1.loc[('L', [1, 3, 5, 7]), 'sem']

        this selects dark, min 2-8, second 1, mean distance
        a1.loc[('D', [2, 4, 6, 8], [1]), 'mean']

        this selects dark, min 2-8, seconds 1-2, mean distance
        a1.loc[('D', [2, 4, 6, 8], [1, 2]), 'mean']

        '''

        ''' This section sorts individual fish into their respective group '''

        gr_ctr_ind = intogroups(a1, b1, c1, d1, a12, b12, c12, d12)
        het_ctr_ind = intogroups(e1, f1, g1, h1, e12, f12, g12, h12)
        gr_com1_ind = intogroups(a2, b2, c2, d2, a3, b3, c3, d3)
        gr_com2_ind = intogroups(a4, b4, c4, d4, a5, b5, c5, d5)
        gr_com3_ind = intogroups(a6, b6, c6, d6, a7, b7, c7, d7)
        gr_com4_ind = intogroups(a8, b8, c8, d8, a9, b9, c9, d9)
        gr_com5_ind = intogroups(a10, b10, c10, d10, a11, b11, c11, d11)
        het_com1_ind = intogroups(e2, f2, g2, h2, e3, f3, g3, h3)
        het_com2_ind = intogroups(e4, f4, g4, h4, e5, f5, g5, h5)
        het_com3_ind = intogroups(e6, f6, g6, h6, e7, f7, g7, h7)
        het_com4_ind = intogroups(e8, f8, g8, h8, e9, f9, g9, h9)
        het_com5_ind = intogroups(e10, f10, g10, h10, e11, f11, g11, h11)

        ind_csv(gr_ctr_ind, het_ctr_ind, gr_com1_ind, het_com1_ind,
                new_path_1)
        ind_csv(gr_ctr_ind, het_ctr_ind, gr_com2_ind, het_com2_ind,
                new_path_2)
        ind_csv(gr_ctr_ind, het_ctr_ind, gr_com3_ind, het_com3_ind,
                new_path_3)
        ind_csv(gr_ctr_ind, het_ctr_ind, gr_com4_ind, het_com4_ind,
                new_path_4)
        ind_csv(gr_ctr_ind, het_ctr_ind, gr_com5_ind, het_com5_ind,
                new_path_5)

        ''' This section makes pivot tables per condition '''

        gr_ctr_piv = pivoter(gr_ctr_ind)
        het_ctr_piv = pivoter(het_ctr_ind)

        gr_com1_piv = pivoter(gr_com1_ind)
        gr_com2_piv = pivoter(gr_com2_ind)
        gr_com3_piv = pivoter(gr_com3_ind)
        gr_com4_piv = pivoter(gr_com4_ind)
        gr_com5_piv = pivoter(gr_com5_ind)

        het_com1_piv = pivoter(het_com1_ind)
        het_com2_piv = pivoter(het_com2_ind)
        het_com3_piv = pivoter(het_com3_ind)
        het_com4_piv = pivoter(het_com4_ind)
        het_com5_piv = pivoter(het_com5_ind)

        ''' Make means with error bars plot '''

        plotmaker_means(gr_ctr_piv, het_ctr_piv, gr_com1_piv, gr_com2_piv,
                        gr_com3_piv, gr_com4_piv, gr_com5_piv, het_com1_piv,
                        het_com2_piv, het_com3_piv, het_com4_piv, het_com5_piv,
                        com_name, analysed, tps, new_path_38)

        ''' This section concerns group averages per time point '''

        group(gr_ctr_piv, het_ctr_piv, gr_com1_piv, het_com1_piv, new_path_6)
        group(gr_ctr_piv, het_ctr_piv, gr_com2_piv, het_com2_piv, new_path_7)
        group(gr_ctr_piv, het_ctr_piv, gr_com3_piv, het_com3_piv, new_path_8)
        group(gr_ctr_piv, het_ctr_piv, gr_com4_piv, het_com4_piv, new_path_9)
        group(gr_ctr_piv, het_ctr_piv, gr_com5_piv, het_com5_piv, new_path_10)

        ''' This section makes average plots '''

        plotmaker_abs_avg(gr_ctr_piv, het_ctr_piv, gr_com1_piv,
                          het_com1_piv, conc1, com_name, analysed,
                          new_path_11)
        plotmaker_abs_avg(gr_ctr_piv, het_ctr_piv, gr_com2_piv,
                          het_com2_piv, conc2, com_name, analysed,
                          new_path_12)
        plotmaker_abs_avg(gr_ctr_piv, het_ctr_piv, gr_com3_piv,
                          het_com3_piv, conc3, com_name, analysed,
                          new_path_13)
        plotmaker_abs_avg(gr_ctr_piv, het_ctr_piv, gr_com4_piv,
                          het_com4_piv, conc4, com_name, analysed,
                          new_path_14)
        plotmaker_abs_avg(gr_ctr_piv, het_ctr_piv, gr_com5_piv,
                          het_com5_piv, conc5, com_name, analysed,
                          new_path_15)

        ''' This section concerns absolute change'''

        com1_abs = absolute_change(gr_ctr_piv, het_ctr_piv, gr_com1_piv,
                                   het_com1_piv, starttp, endtp)
        com2_abs = absolute_change(gr_ctr_piv, het_ctr_piv, gr_com2_piv,
                                   het_com2_piv, starttp, endtp)
        com3_abs = absolute_change(gr_ctr_piv, het_ctr_piv, gr_com3_piv,
                                   het_com3_piv, starttp, endtp)
        com4_abs = absolute_change(gr_ctr_piv, het_ctr_piv, gr_com4_piv,
                                   het_com4_piv, starttp, endtp)
        com5_abs = absolute_change(gr_ctr_piv, het_ctr_piv, gr_com5_piv,
                                   het_com5_piv, starttp, endtp)

        com1_abs.to_csv(new_path_39)
        com2_abs.to_csv(new_path_40)
        com3_abs.to_csv(new_path_41)
        com4_abs.to_csv(new_path_42)
        com5_abs.to_csv(new_path_43)

        absolute_plotmaker(com1_abs, com2_abs, com3_abs, com4_abs, com5_abs,
                           com_name, analysed, tps, new_path_36)

        ''' This section concerns normalisation csvs'''

        normalisation_csv(gr_ctr_piv, het_ctr_piv, gr_com1_piv,
                          het_com1_piv, starttp, endtp, new_path_16)
        normalisation_csv(gr_ctr_piv, het_ctr_piv, gr_com2_piv,
                          het_com2_piv, starttp, endtp, new_path_17)
        normalisation_csv(gr_ctr_piv, het_ctr_piv, gr_com3_piv,
                          het_com3_piv, starttp, endtp, new_path_18)
        normalisation_csv(gr_ctr_piv, het_ctr_piv, gr_com4_piv,
                          het_com4_piv, starttp, endtp, new_path_19)
        normalisation_csv(gr_ctr_piv, het_ctr_piv, gr_com5_piv,
                          het_com5_piv, starttp, endtp, new_path_20)

        ''' This sections concerns relative change '''

        com1_rel = relative_change(com1_abs)
        com2_rel = relative_change(com2_abs)
        com3_rel = relative_change(com3_abs)
        com4_rel = relative_change(com4_abs)
        com5_rel = relative_change(com5_abs)

        relative_plotmaker(com1_rel, com2_rel, com3_rel, com4_rel, com5_rel,
                           com_name, analysed, tps, new_path_37)

        com1_rel.to_csv(new_path_21)
        com2_rel.to_csv(new_path_22)
        com3_rel.to_csv(new_path_23)
        com4_rel.to_csv(new_path_24)
        com5_rel.to_csv(new_path_25)

        print '     Plate ' + i + ' is done.'

megafunc(input_dir, output_dir)

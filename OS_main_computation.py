# -*- coding: utf-8 -*-
"""
Created on Fri Mar 03 14:37:36 2017

@author: ehindinger
"""

import os
from natsort import natsorted
from OS_plotmaker import plotmaker_abs_avg, plotmaker_seconds, absolute_plotmaker
from OS_plotmaker import plotmaker_seconds_pooled, plotmaker_means, relative_plotmaker
from OS_main_formulas import buildfish_7, buildfish_20, ctr_intogroups
from OS_main_formulas import com_intogroups, ind_csv, pivoter
from OS_main_formulas import group_csv, absolute_change
from OS_main_formulas import make_lookup_table, name_finder, final_com
from OS_main_formulas import new_buildfish, pooled, final_ctr
from OS_main_formulas import normalisation_csv, relative_change

''' This section should be left constant, but can be modified '''

# seconds to be analysed following light change, can be modified in formula script
analysed = '2-11'
# timepoints to be averaged for absolute and relative change
# rows are 0 indexed so tp1=0, tp2=1, tp3=2, tp4=3
# function uses range, so to use all timepoints, do starttp=0, endtp=4
starttp = '1'
endtp = '4'
tps = '2-4'
conc_7 = '7'
conc_20 = '20'

# grabs the look up table and extracts file names
xlfile_lookuptable = r'I:\Elena H\DoseR_Analysis\Original_Screen\Initial Screen_Lookup Table.xlsx'
look_up_dictionary = make_lookup_table(xlfile_lookuptable)

''' CHANGE INPUT FOLDER BELOW '''

# location of input files (with forward slash at end)
input_dir = r'P:/OS new analysis test/OS Split Output/'
entire_list = natsorted(os.listdir(input_dir))
output_dir = r'P:/OS new analysis test/OS Processed Output/1-60 s/'


def megafunc(input_list, out_dir):
    for i in input_list:
        main_dir_7 = input_dir + i + '/7 conc'
        main_dir_20 = input_dir + i + '/20 conc'
        plate_code = i
        print plate_code + ' is being processed.'

        ''' CHANGE OUTPUT FOLDER BELOW '''

        new_folder = out_dir

        ''' FROM THIS POINT ON DO NOT MODIFY '''

        # compound names and codes
        com1_code = plate_code + '02'
        com1_name = name_finder(look_up_dictionary, com1_code)
        com2_code = plate_code + '03'
        com2_name = name_finder(look_up_dictionary, com2_code)
        com3_code = plate_code + '04'
        com3_name = name_finder(look_up_dictionary, com3_code)
        com4_code = plate_code + '05'
        com4_name = name_finder(look_up_dictionary, com4_code)
        com5_code = plate_code + '06'
        com5_name = name_finder(look_up_dictionary, com5_code)
        com6_code = plate_code + '07'
        com6_name = name_finder(look_up_dictionary, com6_code)
        com7_code = plate_code + '08'
        com7_name = name_finder(look_up_dictionary, com7_code)
        com8_code = plate_code + '09'
        com8_name = name_finder(look_up_dictionary, com8_code)
        com9_code = plate_code + '10'
        com9_name = name_finder(look_up_dictionary, com9_code)
        com10_code = plate_code + '11'
        com10_name = name_finder(look_up_dictionary, com10_code)

        ''' Section for new filenames '''

        # individual fish values
        new_filename_1 = com1_code + '_7uM_individual_values.csv'
        new_filename_2 = com2_code + '_7uM_individual_values.csv'
        new_filename_3 = com3_code + '_7uM_individual_values.csv'
        new_filename_4 = com4_code + '_7uM_individual_values.csv'
        new_filename_5 = com5_code + '_7uM_individual_values.csv'
        new_filename_6 = com6_code + '_7uM_individual_values.csv'
        new_filename_7 = com7_code + '_7uM_individual_values.csv'
        new_filename_8 = com8_code + '_7uM_individual_values.csv'
        new_filename_9 = com9_code + '_7uM_individual_values.csv'
        new_filename_10 = com10_code + '_7uM_individual_values.csv'
        new_filename_51 = com1_code + '_20uM_individual_values.csv'
        new_filename_52 = com2_code + '_20uM_individual_values.csv'
        new_filename_53 = com3_code + '_20uM_individual_values.csv'
        new_filename_54 = com4_code + '_20uM_individual_values.csv'
        new_filename_55 = com5_code + '_20uM_individual_values.csv'
        new_filename_56 = com6_code + '_20uM_individual_values.csv'
        new_filename_57 = com7_code + '_20uM_individual_values.csv'
        new_filename_58 = com8_code + '_20uM_individual_values.csv'
        new_filename_59 = com9_code + '_20uM_individual_values.csv'
        new_filename_60 = com10_code + '_20uM_individual_values.csv'
        # group averages per timepoint
        new_filename_11 = com1_code + '_7uM_group_avg_per_tp.csv'
        new_filename_12 = com2_code + '_7uM_group_avg_per_tp.csv'
        new_filename_13 = com3_code + '_7uM_group_avg_per_tp.csv'
        new_filename_14 = com4_code + '_7uM_group_avg_per_tp.csv'
        new_filename_15 = com5_code + '_7uM_group_avg_per_tp.csv'
        new_filename_16 = com6_code + '_7uM_group_avg_per_tp.csv'
        new_filename_17 = com7_code + '_7uM_group_avg_per_tp.csv'
        new_filename_18 = com8_code + '_7uM_group_avg_per_tp.csv'
        new_filename_19 = com9_code + '_7uM_group_avg_per_tp.csv'
        new_filename_20 = com10_code + '_7uM_group_avg_per_tp.csv'
        new_filename_61 = com1_code + '_20uM_group_avg_per_tp.csv'
        new_filename_62 = com2_code + '_20uM_group_avg_per_tp.csv'
        new_filename_63 = com3_code + '_20uM_group_avg_per_tp.csv'
        new_filename_64 = com4_code + '_20uM_group_avg_per_tp.csv'
        new_filename_65 = com5_code + '_20uM_group_avg_per_tp.csv'
        new_filename_66 = com6_code + '_20uM_group_avg_per_tp.csv'
        new_filename_67 = com7_code + '_20uM_group_avg_per_tp.csv'
        new_filename_68 = com8_code + '_20uM_group_avg_per_tp.csv'
        new_filename_69 = com9_code + '_20uM_group_avg_per_tp.csv'
        new_filename_70 = com10_code + '_20uM_group_avg_per_tp.csv'
        # average distance per timepoint graphs
        new_filename_21 = com1_code + '_7uM_graph_avg_dist_per_tp.tiff'
        new_filename_22 = com2_code + '_7uM_graph_avg_dist_per_tp.tiff'
        new_filename_23 = com3_code + '_7uM_graph_avg_dist_per_tp.tiff'
        new_filename_24 = com4_code + '_7uM_graph_avg_dist_per_tp.tiff'
        new_filename_25 = com5_code + '_7uM_graph_avg_dist_per_tp.tiff'
        new_filename_26 = com6_code + '_7uM_graph_avg_dist_per_tp.tiff'
        new_filename_27 = com7_code + '_7uM_graph_avg_dist_per_tp.tiff'
        new_filename_28 = com8_code + '_7uM_graph_avg_dist_per_tp.tiff'
        new_filename_29 = com9_code + '_7uM_graph_avg_dist_per_tp.tiff'
        new_filename_30 = com10_code + '_7uM_graph_avg_dist_per_tp.tiff'
        new_filename_71 = com1_code + '_20uM_graph_avg_dist_per_tp.tiff'
        new_filename_72 = com2_code + '_20uM_graph_avg_dist_per_tp.tiff'
        new_filename_73 = com3_code + '_20uM_graph_avg_dist_per_tp.tiff'
        new_filename_74 = com4_code + '_20uM_graph_avg_dist_per_tp.tiff'
        new_filename_75 = com5_code + '_20uM_graph_avg_dist_per_tp.tiff'
        new_filename_76 = com6_code + '_20uM_graph_avg_dist_per_tp.tiff'
        new_filename_77 = com7_code + '_20uM_graph_avg_dist_per_tp.tiff'
        new_filename_78 = com8_code + '_20uM_graph_avg_dist_per_tp.tiff'
        new_filename_79 = com9_code + '_20uM_graph_avg_dist_per_tp.tiff'
        new_filename_80 = com10_code + '_20uM_graph_avg_dist_per_tp.tiff'
        # normalised files
        new_filename_31 = com1_code + '_7uM_normalised.csv'
        new_filename_32 = com2_code + '_7uM_normalised.csv'
        new_filename_33 = com3_code + '_7uM_normalised.csv'
        new_filename_34 = com4_code + '_7uM_normalised.csv'
        new_filename_35 = com5_code + '_7uM_normalised.csv'
        new_filename_36 = com6_code + '_7uM_normalised.csv'
        new_filename_37 = com7_code + '_7uM_normalised.csv'
        new_filename_38 = com8_code + '_7uM_normalised.csv'
        new_filename_39 = com9_code + '_7uM_normalised.csv'
        new_filename_40 = com10_code + '_7uM_normalised.csv'
        new_filename_81 = com1_code + '_20uM_normalised.csv'
        new_filename_82 = com2_code + '_20uM_normalised.csv'
        new_filename_83 = com3_code + '_20uM_normalised.csv'
        new_filename_84 = com4_code + '_20uM_normalised.csv'
        new_filename_85 = com5_code + '_20uM_normalised.csv'
        new_filename_86 = com6_code + '_20uM_normalised.csv'
        new_filename_87 = com7_code + '_20uM_normalised.csv'
        new_filename_88 = com8_code + '_20uM_normalised.csv'
        new_filename_89 = com9_code + '_20uM_normalised.csv'
        new_filename_90 = com10_code + '_20uM_normalised.csv'        
        # absolute change
        new_filename_171 = com1_code + '_7uM_absolute_change.csv'
        new_filename_172 = com2_code + '_7uM_absolute_change.csv'
        new_filename_173 = com3_code + '_7uM_absolute_change.csv'
        new_filename_174 = com4_code + '_7uM_absolute_change.csv'
        new_filename_175 = com5_code + '_7uM_absolute_change.csv'
        new_filename_176 = com6_code + '_7uM_absolute_change.csv'
        new_filename_177 = com7_code + '_7uM_absolute_change.csv'
        new_filename_178 = com8_code + '_7uM_absolute_change.csv'
        new_filename_179 = com9_code + '_7uM_absolute_change.csv'
        new_filename_180 = com10_code + '_7uM_absolute_change.csv'
        new_filename_181 = com1_code + '_20uM_absolute_change.csv'
        new_filename_182 = com2_code + '_20uM_absolute_change.csv'
        new_filename_183 = com3_code + '_20uM_absolute_change.csv'
        new_filename_184 = com4_code + '_20uM_absolute_change.csv'
        new_filename_185 = com5_code + '_20uM_absolute_change.csv'
        new_filename_186 = com6_code + '_20uM_absolute_change.csv'
        new_filename_187 = com7_code + '_20uM_absolute_change.csv'
        new_filename_188 = com8_code + '_20uM_absolute_change.csv'
        new_filename_189 = com9_code + '_20uM_absolute_change.csv'
        new_filename_190 = com10_code + '_20uM_absolute_change.csv'
        # relative change
        new_filename_41 = com1_code + '_7uM_relative_change.csv'
        new_filename_42 = com2_code + '_7uM_relative_change.csv'
        new_filename_43 = com3_code + '_7uM_relative_change.csv'
        new_filename_44 = com4_code + '_7uM_relative_change.csv'
        new_filename_45 = com5_code + '_7uM_relative_change.csv'
        new_filename_46 = com6_code + '_7uM_relative_change.csv'
        new_filename_47 = com7_code + '_7uM_relative_change.csv'
        new_filename_48 = com8_code + '_7uM_relative_change.csv'
        new_filename_49 = com9_code + '_7uM_relative_change.csv'
        new_filename_50 = com10_code + '_7uM_relative_change.csv'
        new_filename_91 = com1_code + '_20uM_relative_change.csv'
        new_filename_92 = com2_code + '_20uM_relative_change.csv'
        new_filename_93 = com3_code + '_20uM_relative_change.csv'
        new_filename_94 = com4_code + '_20uM_relative_change.csv'
        new_filename_95 = com5_code + '_20uM_relative_change.csv'
        new_filename_96 = com6_code + '_20uM_relative_change.csv'
        new_filename_97 = com7_code + '_20uM_relative_change.csv'
        new_filename_98 = com8_code + '_20uM_relative_change.csv'
        new_filename_99 = com9_code + '_20uM_relative_change.csv'
        new_filename_100 = com10_code + '_20uM_relative_change.csv'
        # seconds plot
        new_filename_101 = com1_code + '_7uM_graph_avg_dist_seconds.tiff'
        new_filename_102 = com2_code + '_7uM_graph_avg_dist_seconds.tiff'
        new_filename_103 = com3_code + '_7uM_graph_avg_dist_seconds.tiff'
        new_filename_104 = com4_code + '_7uM_graph_avg_dist_seconds.tiff'
        new_filename_105 = com5_code + '_7uM_graph_avg_dist_seconds.tiff'
        new_filename_106 = com6_code + '_7uM_graph_avg_dist_seconds.tiff'
        new_filename_107 = com7_code + '_7uM_graph_avg_dist_seconds.tiff'
        new_filename_108 = com8_code + '_7uM_graph_avg_dist_seconds.tiff'
        new_filename_109 = com9_code + '_7uM_graph_avg_dist_seconds.tiff'
        new_filename_110 = com10_code + '_7uM_graph_avg_dist_seconds.tiff'
        new_filename_111 = com1_code + '_20uM_graph_avg_dist_seconds.tiff'
        new_filename_112 = com2_code + '_20uM_graph_avg_dist_seconds.tiff'
        new_filename_113 = com3_code + '_20uM_graph_avg_dist_seconds.tiff'
        new_filename_114 = com4_code + '_20uM_graph_avg_dist_seconds.tiff'
        new_filename_115 = com5_code + '_20uM_graph_avg_dist_seconds.tiff'
        new_filename_116 = com6_code + '_20uM_graph_avg_dist_seconds.tiff'
        new_filename_117 = com7_code + '_20uM_graph_avg_dist_seconds.tiff'
        new_filename_118 = com8_code + '_20uM_graph_avg_dist_seconds.tiff'
        new_filename_119 = com9_code + '_20uM_graph_avg_dist_seconds.tiff'
        new_filename_120 = com10_code + '_20uM_graph_avg_dist_seconds.tiff'
        # seconds_pooled plot
        new_filename_121 = com1_code + '_7uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_122 = com2_code + '_7uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_123 = com3_code + '_7uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_124 = com4_code + '_7uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_125 = com5_code + '_7uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_126 = com6_code + '_7uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_127 = com7_code + '_7uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_128 = com8_code + '_7uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_129 = com9_code + '_7uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_130 = com10_code + '_7uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_131 = com1_code + '_20uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_132 = com2_code + '_20uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_133 = com3_code + '_20uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_134 = com4_code + '_20uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_135 = com5_code + '_20uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_136 = com6_code + '_20uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_137 = com7_code + '_20uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_138 = com8_code + '_20uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_139 = com9_code + '_20uM_graph_avg_dist_seconds_pooled.tiff'
        new_filename_140 = com10_code + '_20uM_graph_avg_dist_seconds_pooled.tiff'
        # general drug plots
        new_filename_141 = com1_code + '_absolute_change.tiff'
        new_filename_142 = com2_code + '_absolute_change.tiff'
        new_filename_143 = com3_code + '_absolute_change.tiff'
        new_filename_144 = com4_code + '_absolute_change.tiff'
        new_filename_145 = com5_code + '_absolute_change.tiff'
        new_filename_146 = com6_code + '_absolute_change.tiff'
        new_filename_147 = com7_code + '_absolute_change.tiff'
        new_filename_148 = com8_code + '_absolute_change.tiff'
        new_filename_149 = com9_code + '_absolute_change.tiff'
        new_filename_150 = com10_code + '_absolute_change.tiff'

        new_filename_151 = com1_code + '_relative_change.tiff'
        new_filename_152 = com2_code + '_relative_change.tiff'
        new_filename_153 = com3_code + '_relative_change.tiff'
        new_filename_154 = com4_code + '_relative_change.tiff'
        new_filename_155 = com5_code + '_relative_change.tiff'
        new_filename_156 = com6_code + '_relative_change.tiff'
        new_filename_157 = com7_code + '_relative_change.tiff'
        new_filename_158 = com8_code + '_relative_change.tiff'
        new_filename_159 = com9_code + '_relative_change.tiff'
        new_filename_160 = com10_code + '_relative_change.tiff'

        new_filename_161 = com1_code + '_means_with_SEM.tiff'
        new_filename_162 = com2_code + '_means_with_SEM.tiff'
        new_filename_163 = com3_code + '_means_with_SEM.tiff'
        new_filename_164 = com4_code + '_means_with_SEM.tiff'
        new_filename_165 = com5_code + '_means_with_SEM.tiff'
        new_filename_166 = com6_code + '_means_with_SEM.tiff'
        new_filename_167 = com7_code + '_means_with_SEM.tiff'
        new_filename_168 = com8_code + '_means_with_SEM.tiff'
        new_filename_169 = com9_code + '_means_with_SEM.tiff'
        new_filename_170 = com10_code + '_means_with_SEM.tiff'

        # makes new folders for each compound
        new_folder_1 = new_folder + '/' + com1_code
        if not os.path.exists(new_folder_1):
            os.makedirs(new_folder_1)

        new_folder_2 = new_folder + '/' + com2_code
        if not os.path.exists(new_folder_2):
            os.makedirs(new_folder_2)

        new_folder_3 = new_folder + '/' + com3_code
        if not os.path.exists(new_folder_3):
            os.makedirs(new_folder_3)

        new_folder_4 = new_folder + '/' + com4_code
        if not os.path.exists(new_folder_4):
            os.makedirs(new_folder_4)

        new_folder_5 = new_folder + '/' + com5_code
        if not os.path.exists(new_folder_5):
            os.makedirs(new_folder_5)

        new_folder_6 = new_folder + '/' + com6_code
        if not os.path.exists(new_folder_6):
            os.makedirs(new_folder_6)

        new_folder_7 = new_folder + '/' + com7_code
        if not os.path.exists(new_folder_7):
            os.makedirs(new_folder_7)

        new_folder_8 = new_folder + '/' + com8_code
        if not os.path.exists(new_folder_8):
            os.makedirs(new_folder_8)

        new_folder_9 = new_folder + '/' + com9_code
        if not os.path.exists(new_folder_9):
            os.makedirs(new_folder_9)

        new_folder_10 = new_folder + '/' + com10_code
        if not os.path.exists(new_folder_10):
            os.makedirs(new_folder_10)

        # selects location for csv files
        # individual values
        new_path_1 = new_folder_1 + '/' + new_filename_1
        new_path_2 = new_folder_2 + '/' + new_filename_2
        new_path_3 = new_folder_3 + '/' + new_filename_3
        new_path_4 = new_folder_4 + '/' + new_filename_4
        new_path_5 = new_folder_5 + '/' + new_filename_5
        new_path_6 = new_folder_6 + '/' + new_filename_6
        new_path_7 = new_folder_7 + '/' + new_filename_7
        new_path_8 = new_folder_8 + '/' + new_filename_8
        new_path_9 = new_folder_9 + '/' + new_filename_9
        new_path_10 = new_folder_10 + '/' + new_filename_10
        new_path_51 = new_folder_1 + '/' + new_filename_51
        new_path_52 = new_folder_2 + '/' + new_filename_52
        new_path_53 = new_folder_3 + '/' + new_filename_53
        new_path_54 = new_folder_4 + '/' + new_filename_54
        new_path_55 = new_folder_5 + '/' + new_filename_55
        new_path_56 = new_folder_6 + '/' + new_filename_56
        new_path_57 = new_folder_7 + '/' + new_filename_57
        new_path_58 = new_folder_8 + '/' + new_filename_58
        new_path_59 = new_folder_9 + '/' + new_filename_59
        new_path_60 = new_folder_10 + '/' + new_filename_60
        # group averages per tp
        new_path_11 = new_folder_1 + '/' + new_filename_11
        new_path_12 = new_folder_2 + '/' + new_filename_12
        new_path_13 = new_folder_3 + '/' + new_filename_13
        new_path_14 = new_folder_4 + '/' + new_filename_14
        new_path_15 = new_folder_5 + '/' + new_filename_15
        new_path_16 = new_folder_6 + '/' + new_filename_16
        new_path_17 = new_folder_7 + '/' + new_filename_17
        new_path_18 = new_folder_8 + '/' + new_filename_18
        new_path_19 = new_folder_9 + '/' + new_filename_19
        new_path_20 = new_folder_10 + '/' + new_filename_20
        new_path_61 = new_folder_1 + '/' + new_filename_61
        new_path_62 = new_folder_2 + '/' + new_filename_62
        new_path_63 = new_folder_3 + '/' + new_filename_63
        new_path_64 = new_folder_4 + '/' + new_filename_64
        new_path_65 = new_folder_5 + '/' + new_filename_65
        new_path_66 = new_folder_6 + '/' + new_filename_66
        new_path_67 = new_folder_7 + '/' + new_filename_67
        new_path_68 = new_folder_8 + '/' + new_filename_68
        new_path_69 = new_folder_9 + '/' + new_filename_69
        new_path_70 = new_folder_10 + '/' + new_filename_70
        # graph for avg dist per tp
        new_path_21 = new_folder_1 + '/' + new_filename_21
        new_path_22 = new_folder_2 + '/' + new_filename_22
        new_path_23 = new_folder_3 + '/' + new_filename_23
        new_path_24 = new_folder_4 + '/' + new_filename_24
        new_path_25 = new_folder_5 + '/' + new_filename_25
        new_path_26 = new_folder_6 + '/' + new_filename_26
        new_path_27 = new_folder_7 + '/' + new_filename_27
        new_path_28 = new_folder_8 + '/' + new_filename_28
        new_path_29 = new_folder_9 + '/' + new_filename_29
        new_path_30 = new_folder_10 + '/' + new_filename_30
        new_path_71 = new_folder_1 + '/' + new_filename_71
        new_path_72 = new_folder_2 + '/' + new_filename_72
        new_path_73 = new_folder_3 + '/' + new_filename_73
        new_path_74 = new_folder_4 + '/' + new_filename_74
        new_path_75 = new_folder_5 + '/' + new_filename_75
        new_path_76 = new_folder_6 + '/' + new_filename_76
        new_path_77 = new_folder_7 + '/' + new_filename_77
        new_path_78 = new_folder_8 + '/' + new_filename_78
        new_path_79 = new_folder_9 + '/' + new_filename_79
        new_path_80 = new_folder_10 + '/' + new_filename_80
        # absolute change path
        new_path_31 = new_folder_1 + '/' + new_filename_31
        new_path_32 = new_folder_2 + '/' + new_filename_32
        new_path_33 = new_folder_3 + '/' + new_filename_33
        new_path_34 = new_folder_4 + '/' + new_filename_34
        new_path_35 = new_folder_5 + '/' + new_filename_35
        new_path_36 = new_folder_6 + '/' + new_filename_36
        new_path_37 = new_folder_7 + '/' + new_filename_37
        new_path_38 = new_folder_8 + '/' + new_filename_38
        new_path_39 = new_folder_9 + '/' + new_filename_39
        new_path_40 = new_folder_10 + '/' + new_filename_40
        new_path_81 = new_folder_1 + '/' + new_filename_81
        new_path_82 = new_folder_2 + '/' + new_filename_82
        new_path_83 = new_folder_3 + '/' + new_filename_83
        new_path_84 = new_folder_4 + '/' + new_filename_84
        new_path_85 = new_folder_5 + '/' + new_filename_85
        new_path_86 = new_folder_6 + '/' + new_filename_86
        new_path_87 = new_folder_7 + '/' + new_filename_87
        new_path_88 = new_folder_8 + '/' + new_filename_88
        new_path_89 = new_folder_9 + '/' + new_filename_89
        new_path_90 = new_folder_10 + '/' + new_filename_90
        # relative change path
        new_path_41 = new_folder_1 + '/' + new_filename_41
        new_path_42 = new_folder_2 + '/' + new_filename_42
        new_path_43 = new_folder_3 + '/' + new_filename_43
        new_path_44 = new_folder_4 + '/' + new_filename_44
        new_path_45 = new_folder_5 + '/' + new_filename_45
        new_path_46 = new_folder_6 + '/' + new_filename_46
        new_path_47 = new_folder_7 + '/' + new_filename_47
        new_path_48 = new_folder_8 + '/' + new_filename_48
        new_path_49 = new_folder_9 + '/' + new_filename_49
        new_path_50 = new_folder_10 + '/' + new_filename_50
        new_path_91 = new_folder_1 + '/' + new_filename_91
        new_path_92 = new_folder_2 + '/' + new_filename_92
        new_path_93 = new_folder_3 + '/' + new_filename_93
        new_path_94 = new_folder_4 + '/' + new_filename_94
        new_path_95 = new_folder_5 + '/' + new_filename_95
        new_path_96 = new_folder_6 + '/' + new_filename_96
        new_path_97 = new_folder_7 + '/' + new_filename_97
        new_path_98 = new_folder_8 + '/' + new_filename_98
        new_path_99 = new_folder_9 + '/' + new_filename_99
        new_path_100 = new_folder_10 + '/' + new_filename_100
        # seconds plot path
        new_path_101 = new_folder_1 + '/' + new_filename_101
        new_path_102 = new_folder_2 + '/' + new_filename_102
        new_path_103 = new_folder_3 + '/' + new_filename_103
        new_path_104 = new_folder_4 + '/' + new_filename_104
        new_path_105 = new_folder_5 + '/' + new_filename_105
        new_path_106 = new_folder_6 + '/' + new_filename_106
        new_path_107 = new_folder_7 + '/' + new_filename_107
        new_path_108 = new_folder_8 + '/' + new_filename_108
        new_path_109 = new_folder_9 + '/' + new_filename_109
        new_path_110 = new_folder_10 + '/' + new_filename_110
        new_path_111 = new_folder_1 + '/' + new_filename_111
        new_path_112 = new_folder_2 + '/' + new_filename_112
        new_path_113 = new_folder_3 + '/' + new_filename_113
        new_path_114 = new_folder_4 + '/' + new_filename_114
        new_path_115 = new_folder_5 + '/' + new_filename_115
        new_path_116 = new_folder_6 + '/' + new_filename_116
        new_path_117 = new_folder_7 + '/' + new_filename_117
        new_path_118 = new_folder_8 + '/' + new_filename_118
        new_path_119 = new_folder_9 + '/' + new_filename_119
        new_path_120 = new_folder_10 + '/' + new_filename_120
        # seconds pooled plot path
        new_path_121 = new_folder_1 + '/' + new_filename_121
        new_path_122 = new_folder_2 + '/' + new_filename_122
        new_path_123 = new_folder_3 + '/' + new_filename_123
        new_path_124 = new_folder_4 + '/' + new_filename_124
        new_path_125 = new_folder_5 + '/' + new_filename_125
        new_path_126 = new_folder_6 + '/' + new_filename_126
        new_path_127 = new_folder_7 + '/' + new_filename_127
        new_path_128 = new_folder_8 + '/' + new_filename_128
        new_path_129 = new_folder_9 + '/' + new_filename_129
        new_path_130 = new_folder_10 + '/' + new_filename_130
        new_path_131 = new_folder_1 + '/' + new_filename_131
        new_path_132 = new_folder_2 + '/' + new_filename_132
        new_path_133 = new_folder_3 + '/' + new_filename_133
        new_path_134 = new_folder_4 + '/' + new_filename_134
        new_path_135 = new_folder_5 + '/' + new_filename_135
        new_path_136 = new_folder_6 + '/' + new_filename_136
        new_path_137 = new_folder_7 + '/' + new_filename_137
        new_path_138 = new_folder_8 + '/' + new_filename_138
        new_path_139 = new_folder_9 + '/' + new_filename_139
        new_path_140 = new_folder_10 + '/' + new_filename_140
        # absolute change plot paths
        new_path_141 = new_folder_1 + '/' + new_filename_141
        new_path_142 = new_folder_2 + '/' + new_filename_142
        new_path_143 = new_folder_3 + '/' + new_filename_143
        new_path_144 = new_folder_4 + '/' + new_filename_144
        new_path_145 = new_folder_5 + '/' + new_filename_145
        new_path_146 = new_folder_6 + '/' + new_filename_146
        new_path_147 = new_folder_7 + '/' + new_filename_147
        new_path_148 = new_folder_8 + '/' + new_filename_148
        new_path_149 = new_folder_9 + '/' + new_filename_149
        new_path_150 = new_folder_10 + '/' + new_filename_150
        # relative change plot paths
        new_path_151 = new_folder_1 + '/' + new_filename_151
        new_path_152 = new_folder_2 + '/' + new_filename_152
        new_path_153 = new_folder_3 + '/' + new_filename_153
        new_path_154 = new_folder_4 + '/' + new_filename_154
        new_path_155 = new_folder_5 + '/' + new_filename_155
        new_path_156 = new_folder_6 + '/' + new_filename_156
        new_path_157 = new_folder_7 + '/' + new_filename_157
        new_path_158 = new_folder_8 + '/' + new_filename_158
        new_path_159 = new_folder_9 + '/' + new_filename_159
        new_path_160 = new_folder_10 + '/' + new_filename_160
        # means with SEM path
        new_path_161 = new_folder_1 + '/' + new_filename_161
        new_path_162 = new_folder_2 + '/' + new_filename_162
        new_path_163 = new_folder_3 + '/' + new_filename_163
        new_path_164 = new_folder_4 + '/' + new_filename_164
        new_path_165 = new_folder_5 + '/' + new_filename_165
        new_path_166 = new_folder_6 + '/' + new_filename_166
        new_path_167 = new_folder_7 + '/' + new_filename_167
        new_path_168 = new_folder_8 + '/' + new_filename_168
        new_path_169 = new_folder_9 + '/' + new_filename_169
        new_path_170 = new_folder_10 + '/' + new_filename_170
        # absolute files
        new_path_171 = new_folder_1 + '/' + new_filename_171
        new_path_172 = new_folder_2 + '/' + new_filename_172
        new_path_173 = new_folder_3 + '/' + new_filename_173
        new_path_174 = new_folder_4 + '/' + new_filename_174
        new_path_175 = new_folder_5 + '/' + new_filename_175
        new_path_176 = new_folder_6 + '/' + new_filename_176
        new_path_177 = new_folder_7 + '/' + new_filename_177
        new_path_178 = new_folder_8 + '/' + new_filename_178
        new_path_179 = new_folder_9 + '/' + new_filename_179
        new_path_180 = new_folder_10 + '/' + new_filename_180
        new_path_181 = new_folder_1 + '/' + new_filename_181
        new_path_182 = new_folder_2 + '/' + new_filename_182
        new_path_183 = new_folder_3 + '/' + new_filename_183
        new_path_184 = new_folder_4 + '/' + new_filename_184
        new_path_185 = new_folder_5 + '/' + new_filename_185
        new_path_186 = new_folder_6 + '/' + new_filename_186
        new_path_187 = new_folder_7 + '/' + new_filename_187
        new_path_188 = new_folder_8 + '/' + new_filename_188
        new_path_189 = new_folder_9 + '/' + new_filename_189
        new_path_190 = new_folder_10 + '/' + new_filename_190

        print '     Reading input files ...'
        # reads csv files, builds fish
        a1_7_p1 = buildfish_7(main_dir_7, 0)
        a10_7_p1 = buildfish_7(main_dir_7, 1)
        a11_7_p1 = buildfish_7(main_dir_7, 2)
        a12_7_p1 = buildfish_7(main_dir_7, 3)
        a2_7_p1 = buildfish_7(main_dir_7, 4)
        a3_7_p1 = buildfish_7(main_dir_7, 5)
        a4_7_p1 = buildfish_7(main_dir_7, 6)
        a5_7_p1 = buildfish_7(main_dir_7, 7)
        a6_7_p1 = buildfish_7(main_dir_7, 8)
        a7_7_p1 = buildfish_7(main_dir_7, 9)
        a8_7_p1 = buildfish_7(main_dir_7, 10)
        a9_7_p1 = buildfish_7(main_dir_7, 11)
        b1_7_p1 = buildfish_7(main_dir_7, 12)
        b10_7_p1 = buildfish_7(main_dir_7, 13)
        b11_7_p1 = buildfish_7(main_dir_7, 14)
        b12_7_p1 = buildfish_7(main_dir_7, 15)
        b2_7_p1 = buildfish_7(main_dir_7, 16)
        b3_7_p1 = buildfish_7(main_dir_7, 17)
        b4_7_p1 = buildfish_7(main_dir_7, 18)
        b5_7_p1 = buildfish_7(main_dir_7, 19)
        b6_7_p1 = buildfish_7(main_dir_7, 20)
        b7_7_p1 = buildfish_7(main_dir_7, 21)
        b8_7_p1 = buildfish_7(main_dir_7, 22)
        b9_7_p1 = buildfish_7(main_dir_7, 23)
        c1_7_p1 = buildfish_7(main_dir_7, 24)
        c10_7_p1 = buildfish_7(main_dir_7, 25)
        c11_7_p1 = buildfish_7(main_dir_7, 26)
        c12_7_p1 = buildfish_7(main_dir_7, 27)
        c2_7_p1 = buildfish_7(main_dir_7, 28)
        c3_7_p1 = buildfish_7(main_dir_7, 29)
        c4_7_p1 = buildfish_7(main_dir_7, 30)
        c5_7_p1 = buildfish_7(main_dir_7, 31)
        c6_7_p1 = buildfish_7(main_dir_7, 32)
        c7_7_p1 = buildfish_7(main_dir_7, 33)
        c8_7_p1 = buildfish_7(main_dir_7, 34)
        c9_7_p1 = buildfish_7(main_dir_7, 35)
        d1_7_p1 = buildfish_7(main_dir_7, 36)
        d10_7_p1 = buildfish_7(main_dir_7, 37)
        d11_7_p1 = buildfish_7(main_dir_7, 38)
        d12_7_p1 = buildfish_7(main_dir_7, 39)
        d2_7_p1 = buildfish_7(main_dir_7, 40)
        d3_7_p1 = buildfish_7(main_dir_7, 41)
        d4_7_p1 = buildfish_7(main_dir_7, 42)
        d5_7_p1 = buildfish_7(main_dir_7, 43)
        d6_7_p1 = buildfish_7(main_dir_7, 44)
        d7_7_p1 = buildfish_7(main_dir_7, 45)
        d8_7_p1 = buildfish_7(main_dir_7, 46)
        d9_7_p1 = buildfish_7(main_dir_7, 47)
        e1_7_p1 = buildfish_7(main_dir_7, 48)
        e10_7_p1 = buildfish_7(main_dir_7, 49)
        e11_7_p1 = buildfish_7(main_dir_7, 50)
        e12_7_p1 = buildfish_7(main_dir_7, 51)
        e2_7_p1 = buildfish_7(main_dir_7, 52)
        e3_7_p1 = buildfish_7(main_dir_7, 53)
        e4_7_p1 = buildfish_7(main_dir_7, 54)
        e5_7_p1 = buildfish_7(main_dir_7, 55)
        e6_7_p1 = buildfish_7(main_dir_7, 56)
        e7_7_p1 = buildfish_7(main_dir_7, 57)
        e8_7_p1 = buildfish_7(main_dir_7, 58)
        e9_7_p1 = buildfish_7(main_dir_7, 59)
        f1_7_p1 = buildfish_7(main_dir_7, 60)
        f10_7_p1 = buildfish_7(main_dir_7, 61)
        f11_7_p1 = buildfish_7(main_dir_7, 62)
        f12_7_p1 = buildfish_7(main_dir_7, 63)
        f2_7_p1 = buildfish_7(main_dir_7, 64)
        f3_7_p1 = buildfish_7(main_dir_7, 65)
        f4_7_p1 = buildfish_7(main_dir_7, 66)
        f5_7_p1 = buildfish_7(main_dir_7, 67)
        f6_7_p1 = buildfish_7(main_dir_7, 68)
        f7_7_p1 = buildfish_7(main_dir_7, 69)
        f8_7_p1 = buildfish_7(main_dir_7, 70)
        f9_7_p1 = buildfish_7(main_dir_7, 71)
        g1_7_p1 = buildfish_7(main_dir_7, 72)
        g10_7_p1 = buildfish_7(main_dir_7, 73)
        g11_7_p1 = buildfish_7(main_dir_7, 74)
        g12_7_p1 = buildfish_7(main_dir_7, 75)
        g2_7_p1 = buildfish_7(main_dir_7, 76)
        g3_7_p1 = buildfish_7(main_dir_7, 77)
        g4_7_p1 = buildfish_7(main_dir_7, 78)
        g5_7_p1 = buildfish_7(main_dir_7, 79)
        g6_7_p1 = buildfish_7(main_dir_7, 80)
        g7_7_p1 = buildfish_7(main_dir_7, 81)
        g8_7_p1 = buildfish_7(main_dir_7, 82)
        g9_7_p1 = buildfish_7(main_dir_7, 83)
        h1_7_p1 = buildfish_7(main_dir_7, 84)
        h10_7_p1 = buildfish_7(main_dir_7, 85)
        h11_7_p1 = buildfish_7(main_dir_7, 86)
        h12_7_p1 = buildfish_7(main_dir_7, 87)
        h2_7_p1 = buildfish_7(main_dir_7, 88)
        h3_7_p1 = buildfish_7(main_dir_7, 89)
        h4_7_p1 = buildfish_7(main_dir_7, 90)
        h5_7_p1 = buildfish_7(main_dir_7, 91)
        h6_7_p1 = buildfish_7(main_dir_7, 92)
        h7_7_p1 = buildfish_7(main_dir_7, 93)
        h8_7_p1 = buildfish_7(main_dir_7, 94)
        h9_7_p1 = buildfish_7(main_dir_7, 95)

        a1_20_p1 = buildfish_20(main_dir_20, 0)
        a10_20_p1 = buildfish_20(main_dir_20, 1)
        a11_20_p1 = buildfish_20(main_dir_20, 2)
        a12_20_p1 = buildfish_20(main_dir_20, 3)
        a2_20_p1 = buildfish_20(main_dir_20, 4)
        a3_20_p1 = buildfish_20(main_dir_20, 5)
        a4_20_p1 = buildfish_20(main_dir_20, 6)
        a5_20_p1 = buildfish_20(main_dir_20, 7)
        a6_20_p1 = buildfish_20(main_dir_20, 8)
        a7_20_p1 = buildfish_20(main_dir_20, 9)
        a8_20_p1 = buildfish_20(main_dir_20, 10)
        a9_20_p1 = buildfish_20(main_dir_20, 11)
        b1_20_p1 = buildfish_20(main_dir_20, 12)
        b10_20_p1 = buildfish_20(main_dir_20, 13)
        b11_20_p1 = buildfish_20(main_dir_20, 14)
        b12_20_p1 = buildfish_20(main_dir_20, 15)
        b2_20_p1 = buildfish_20(main_dir_20, 16)
        b3_20_p1 = buildfish_20(main_dir_20, 17)
        b4_20_p1 = buildfish_20(main_dir_20, 18)
        b5_20_p1 = buildfish_20(main_dir_20, 19)
        b6_20_p1 = buildfish_20(main_dir_20, 20)
        b7_20_p1 = buildfish_20(main_dir_20, 21)
        b8_20_p1 = buildfish_20(main_dir_20, 22)
        b9_20_p1 = buildfish_20(main_dir_20, 23)
        c1_20_p1 = buildfish_20(main_dir_20, 24)
        c10_20_p1 = buildfish_20(main_dir_20, 25)
        c11_20_p1 = buildfish_20(main_dir_20, 26)
        c12_20_p1 = buildfish_20(main_dir_20, 27)
        c2_20_p1 = buildfish_20(main_dir_20, 28)
        c3_20_p1 = buildfish_20(main_dir_20, 29)
        c4_20_p1 = buildfish_20(main_dir_20, 30)
        c5_20_p1 = buildfish_20(main_dir_20, 31)
        c6_20_p1 = buildfish_20(main_dir_20, 32)
        c7_20_p1 = buildfish_20(main_dir_20, 33)
        c8_20_p1 = buildfish_20(main_dir_20, 34)
        c9_20_p1 = buildfish_20(main_dir_20, 35)
        d1_20_p1 = buildfish_20(main_dir_20, 36)
        d10_20_p1 = buildfish_20(main_dir_20, 37)
        d11_20_p1 = buildfish_20(main_dir_20, 38)
        d12_20_p1 = buildfish_20(main_dir_20, 39)
        d2_20_p1 = buildfish_20(main_dir_20, 40)
        d3_20_p1 = buildfish_20(main_dir_20, 41)
        d4_20_p1 = buildfish_20(main_dir_20, 42)
        d5_20_p1 = buildfish_20(main_dir_20, 43)
        d6_20_p1 = buildfish_20(main_dir_20, 44)
        d7_20_p1 = buildfish_20(main_dir_20, 45)
        d8_20_p1 = buildfish_20(main_dir_20, 46)
        d9_20_p1 = buildfish_20(main_dir_20, 47)
        e1_20_p1 = buildfish_20(main_dir_20, 48)
        e10_20_p1 = buildfish_20(main_dir_20, 49)
        e11_20_p1 = buildfish_20(main_dir_20, 50)
        e12_20_p1 = buildfish_20(main_dir_20, 51)
        e2_20_p1 = buildfish_20(main_dir_20, 52)
        e3_20_p1 = buildfish_20(main_dir_20, 53)
        e4_20_p1 = buildfish_20(main_dir_20, 54)
        e5_20_p1 = buildfish_20(main_dir_20, 55)
        e6_20_p1 = buildfish_20(main_dir_20, 56)
        e7_20_p1 = buildfish_20(main_dir_20, 57)
        e8_20_p1 = buildfish_20(main_dir_20, 58)
        e9_20_p1 = buildfish_20(main_dir_20, 59)
        f1_20_p1 = buildfish_20(main_dir_20, 60)
        f10_20_p1 = buildfish_20(main_dir_20, 61)
        f11_20_p1 = buildfish_20(main_dir_20, 62)
        f12_20_p1 = buildfish_20(main_dir_20, 63)
        f2_20_p1 = buildfish_20(main_dir_20, 64)
        f3_20_p1 = buildfish_20(main_dir_20, 65)
        f4_20_p1 = buildfish_20(main_dir_20, 66)
        f5_20_p1 = buildfish_20(main_dir_20, 67)
        f6_20_p1 = buildfish_20(main_dir_20, 68)
        f7_20_p1 = buildfish_20(main_dir_20, 69)
        f8_20_p1 = buildfish_20(main_dir_20, 70)
        f9_20_p1 = buildfish_20(main_dir_20, 71)
        g1_20_p1 = buildfish_20(main_dir_20, 72)
        g10_20_p1 = buildfish_20(main_dir_20, 73)
        g11_20_p1 = buildfish_20(main_dir_20, 74)
        g12_20_p1 = buildfish_20(main_dir_20, 75)
        g2_20_p1 = buildfish_20(main_dir_20, 76)
        g3_20_p1 = buildfish_20(main_dir_20, 77)
        g4_20_p1 = buildfish_20(main_dir_20, 78)
        g5_20_p1 = buildfish_20(main_dir_20, 79)
        g6_20_p1 = buildfish_20(main_dir_20, 80)
        g7_20_p1 = buildfish_20(main_dir_20, 81)
        g8_20_p1 = buildfish_20(main_dir_20, 82)
        g9_20_p1 = buildfish_20(main_dir_20, 83)
        h1_20_p1 = buildfish_20(main_dir_20, 84)
        h10_20_p1 = buildfish_20(main_dir_20, 85)
        h11_20_p1 = buildfish_20(main_dir_20, 86)
        h12_20_p1 = buildfish_20(main_dir_20, 87)
        h2_20_p1 = buildfish_20(main_dir_20, 88)
        h3_20_p1 = buildfish_20(main_dir_20, 89)
        h4_20_p1 = buildfish_20(main_dir_20, 90)
        h5_20_p1 = buildfish_20(main_dir_20, 91)
        h6_20_p1 = buildfish_20(main_dir_20, 92)
        h7_20_p1 = buildfish_20(main_dir_20, 93)
        h8_20_p1 = buildfish_20(main_dir_20, 94)
        h9_20_p1 = buildfish_20(main_dir_20, 95)

        ''' Insert Section on seconds plots '''

        print '     Computing analysis ...'

        gr_ctr_7 = final_ctr(a1_7_p1, b1_7_p1, c1_7_p1, d1_7_p1, a12_7_p1,
                             b12_7_p1, c12_7_p1, d12_7_p1)
        het_ctr_7 = final_ctr(e1_7_p1, f1_7_p1, g1_7_p1, h1_7_p1, e12_7_p1,
                              f12_7_p1, g12_7_p1, h12_7_p1)
        gr_com1_7 = final_com(a2_7_p1, b2_7_p1, c2_7_p1, d2_7_p1)
        het_com1_7 = final_com(e2_7_p1, f2_7_p1, g2_7_p1, h2_7_p1)
        gr_com2_7 = final_com(a3_7_p1, b3_7_p1, c3_7_p1, d3_7_p1)
        het_com2_7 = final_com(e3_7_p1, f3_7_p1, g3_7_p1, h3_7_p1)
        gr_com3_7 = final_com(a4_7_p1, b4_7_p1, c4_7_p1, d4_7_p1)
        het_com3_7 = final_com(e4_7_p1, f4_7_p1, g4_7_p1, h4_7_p1)
        gr_com4_7 = final_com(a5_7_p1, b5_7_p1, c5_7_p1, d5_7_p1)
        het_com4_7 = final_com(e5_7_p1, f5_7_p1, g5_7_p1, h5_7_p1)
        gr_com5_7 = final_com(a6_7_p1, b6_7_p1, c6_7_p1, d6_7_p1)
        het_com5_7 = final_com(e6_7_p1, f6_7_p1, g6_7_p1, h6_7_p1)
        gr_com6_7 = final_com(a7_7_p1, b7_7_p1, c7_7_p1, d7_7_p1)
        het_com6_7 = final_com(e7_7_p1, f7_7_p1, g7_7_p1, h7_7_p1)
        gr_com7_7 = final_com(a8_7_p1, b8_7_p1, c8_7_p1, d8_7_p1)
        het_com7_7 = final_com(e8_7_p1, f8_7_p1, g8_7_p1, h8_7_p1)
        gr_com8_7 = final_com(a9_7_p1, b9_7_p1, c9_7_p1, d9_7_p1)
        het_com8_7 = final_com(e9_7_p1, f9_7_p1, g9_7_p1, h9_7_p1)
        gr_com9_7 = final_com(a10_7_p1, b10_7_p1, c10_7_p1, d10_7_p1)
        het_com9_7 = final_com(e10_7_p1, f10_7_p1, g10_7_p1, h10_7_p1)
        gr_com10_7 = final_com(a11_7_p1, b11_7_p1, c11_7_p1, d11_7_p1)
        het_com10_7 = final_com(e11_7_p1, f11_7_p1, g11_7_p1, h11_7_p1)

        gr_ctr_20 = final_ctr(a1_20_p1, b1_20_p1, c1_20_p1, d1_20_p1,
                              a12_20_p1, b12_20_p1, c12_20_p1, d12_20_p1)
        het_ctr_20 = final_ctr(e1_20_p1, f1_20_p1, g1_20_p1, h1_20_p1,
                               e12_20_p1, f12_20_p1, g12_20_p1, h12_20_p1)
        gr_com1_20 = final_com(a2_20_p1, b2_20_p1, c2_20_p1, d2_20_p1)
        het_com1_20 = final_com(e2_20_p1, f2_20_p1, g2_20_p1, h2_20_p1)
        gr_com2_20 = final_com(a3_20_p1, b3_20_p1, c3_20_p1, d3_20_p1)
        het_com2_20 = final_com(e3_20_p1, f3_20_p1, g3_20_p1, h3_20_p1)
        gr_com3_20 = final_com(a4_20_p1, b4_20_p1, c4_20_p1, d4_20_p1)
        het_com3_20 = final_com(e4_20_p1, f4_20_p1, g4_20_p1, h4_20_p1)
        gr_com4_20 = final_com(a5_20_p1, b5_20_p1, c5_20_p1, d5_20_p1)
        het_com4_20 = final_com(e5_20_p1, f5_20_p1, g5_20_p1, h5_20_p1)
        gr_com5_20 = final_com(a6_20_p1, b6_20_p1, c6_20_p1, d6_20_p1)
        het_com5_20 = final_com(e6_20_p1, f6_20_p1, g6_20_p1, h6_20_p1)
        gr_com6_20 = final_com(a7_20_p1, b7_20_p1, c7_20_p1, d7_20_p1)
        het_com6_20 = final_com(e7_20_p1, f7_20_p1, g7_20_p1, h7_20_p1)
        gr_com7_20 = final_com(a8_20_p1, b8_20_p1, c8_20_p1, d8_20_p1)
        het_com7_20 = final_com(e8_20_p1, f8_20_p1, g8_20_p1, h8_20_p1)
        gr_com8_20 = final_com(a9_20_p1, b9_20_p1, c9_20_p1, d9_20_p1)
        het_com8_20 = final_com(e9_20_p1, f9_20_p1, g9_20_p1, h9_20_p1)
        gr_com9_20 = final_com(a10_20_p1, b10_20_p1, c10_20_p1, d10_20_p1)
        het_com9_20 = final_com(e10_20_p1, f10_20_p1, g10_20_p1, h10_20_p1)
        gr_com10_20 = final_com(a11_20_p1, b11_20_p1, c11_20_p1, d11_20_p1)
        het_com10_20 = final_com(e11_20_p1, f11_20_p1, g11_20_p1, h11_20_p1)

        gr_dist0_7 = pooled(a1_7_p1, b1_7_p1, c1_7_p1, d1_7_p1, a2_7_p1,
                            b2_7_p1, c2_7_p1, d2_7_p1, a3_7_p1, b3_7_p1,
                            c3_7_p1, d3_7_p1, a4_7_p1, b4_7_p1, c4_7_p1,
                            d4_7_p1, a5_7_p1, b5_7_p1, c5_7_p1, d5_7_p1,
                            a6_7_p1, b6_7_p1, c6_7_p1, d6_7_p1, a7_7_p1,
                            b7_7_p1, c7_7_p1, d7_7_p1, a8_7_p1, b8_7_p1,
                            c8_7_p1, d8_7_p1, a9_7_p1, b9_7_p1, c9_7_p1,
                            d9_7_p1, a10_7_p1, b10_7_p1, c10_7_p1, d10_7_p1,
                            a11_7_p1, b11_7_p1, c11_7_p1, d11_7_p1, a12_7_p1,
                            b12_7_p1, c12_7_p1, d12_7_p1)

        het_dist0_7 = pooled(e1_7_p1, f1_7_p1, g1_7_p1, h1_7_p1, e2_7_p1,
                             f2_7_p1, g2_7_p1, h2_7_p1, e3_7_p1, f3_7_p1,
                             g3_7_p1, h3_7_p1, e4_7_p1, f4_7_p1, g4_7_p1,
                             h4_7_p1, e5_7_p1, f5_7_p1, g5_7_p1, h5_7_p1,
                             e6_7_p1, f6_7_p1, g6_7_p1, h6_7_p1, e7_7_p1,
                             f7_7_p1, g7_7_p1, h7_7_p1, e8_7_p1, f8_7_p1,
                             g8_7_p1, h8_7_p1, e9_7_p1, f9_7_p1, g9_7_p1,
                             h9_7_p1, e10_7_p1, f10_7_p1, g10_7_p1, h10_7_p1,
                             e11_7_p1, f11_7_p1, g11_7_p1, h11_7_p1, e12_7_p1,
                             f12_7_p1, g12_7_p1, h12_7_p1)

        gr_dist0_20 = pooled(a1_20_p1, b1_20_p1, c1_20_p1, d1_20_p1, a2_20_p1,
                             b2_20_p1, c2_20_p1, d2_20_p1, a3_20_p1, b3_20_p1,
                             c3_20_p1, d3_20_p1, a4_20_p1, b4_20_p1, c4_20_p1,
                             d4_20_p1, a5_20_p1, b5_20_p1, c5_20_p1, d5_20_p1,
                             a6_20_p1, b6_20_p1, c6_20_p1, d6_20_p1, a7_20_p1,
                             b7_20_p1, c7_20_p1, d7_20_p1, a8_20_p1, b8_20_p1,
                             c8_20_p1, d8_20_p1, a9_20_p1, b9_20_p1, c9_20_p1,
                             d9_20_p1, a10_20_p1, b10_20_p1, c10_20_p1,
                             d10_20_p1, a11_20_p1, b11_20_p1, c11_20_p1,
                             d11_20_p1, a12_20_p1, b12_20_p1, c12_20_p1,
                             d12_20_p1)

        het_dist0_20 = pooled(e1_20_p1, f1_20_p1, g1_20_p1, h1_20_p1, e2_20_p1,
                              f2_20_p1, g2_20_p1, h2_20_p1, e3_20_p1, f3_20_p1,
                              g3_20_p1, h3_20_p1, e4_20_p1, f4_20_p1, g4_20_p1,
                              h4_20_p1, e5_20_p1, f5_20_p1, g5_20_p1, h5_20_p1,
                              e6_20_p1, f6_20_p1, g6_20_p1, h6_20_p1, e7_20_p1,
                              f7_20_p1, g7_20_p1, h7_20_p1, e8_20_p1, f8_20_p1,
                              g8_20_p1, h8_20_p1, e9_20_p1, f9_20_p1, g9_20_p1,
                              h9_20_p1, e10_20_p1, f10_20_p1, g10_20_p1,
                              h10_20_p1, e11_20_p1, f11_20_p1, g11_20_p1,
                              h11_20_p1, e12_20_p1, f12_20_p1, g12_20_p1,
                              h12_20_p1)

        plotmaker_seconds(gr_ctr_7, het_ctr_7, gr_com1_7, het_com1_7, conc_7,
                          com1_name, new_path_101)
        plotmaker_seconds(gr_ctr_7, het_ctr_7, gr_com2_7, het_com2_7, conc_7,
                          com2_name, new_path_102)
        plotmaker_seconds(gr_ctr_7, het_ctr_7, gr_com3_7, het_com3_7, conc_7,
                          com3_name, new_path_103)
        plotmaker_seconds(gr_ctr_7, het_ctr_7, gr_com4_7, het_com4_7, conc_7,
                          com4_name, new_path_104)
        plotmaker_seconds(gr_ctr_7, het_ctr_7, gr_com5_7, het_com5_7, conc_7,
                          com5_name, new_path_105)
        plotmaker_seconds(gr_ctr_7, het_ctr_7, gr_com6_7, het_com6_7, conc_7,
                          com6_name, new_path_106)
        plotmaker_seconds(gr_ctr_7, het_ctr_7, gr_com7_7, het_com7_7, conc_7,
                          com7_name, new_path_107)
        plotmaker_seconds(gr_ctr_7, het_ctr_7, gr_com8_7, het_com8_7, conc_7,
                          com8_name, new_path_108)
        plotmaker_seconds(gr_ctr_7, het_ctr_7, gr_com9_7, het_com9_7, conc_7,
                          com9_name, new_path_109)
        plotmaker_seconds(gr_ctr_7, het_ctr_7, gr_com10_7, het_com10_7, conc_7,
                          com10_name, new_path_110)

        plotmaker_seconds(gr_ctr_20, het_ctr_20, gr_com1_20, het_com1_20,
                          conc_20, com1_name, new_path_111)
        plotmaker_seconds(gr_ctr_20, het_ctr_20, gr_com2_20, het_com2_20,
                          conc_20, com2_name, new_path_112)
        plotmaker_seconds(gr_ctr_20, het_ctr_20, gr_com3_20, het_com3_20,
                          conc_20, com3_name, new_path_113)
        plotmaker_seconds(gr_ctr_20, het_ctr_20, gr_com4_20, het_com4_20,
                          conc_20, com4_name, new_path_114)
        plotmaker_seconds(gr_ctr_20, het_ctr_20, gr_com5_20, het_com5_20,
                          conc_20, com5_name, new_path_115)
        plotmaker_seconds(gr_ctr_20, het_ctr_20, gr_com6_20, het_com6_20,
                          conc_20, com6_name, new_path_116)
        plotmaker_seconds(gr_ctr_20, het_ctr_20, gr_com7_20, het_com7_20,
                          conc_20, com7_name, new_path_117)
        plotmaker_seconds(gr_ctr_20, het_ctr_20, gr_com8_20, het_com8_20,
                          conc_20, com8_name, new_path_118)
        plotmaker_seconds(gr_ctr_20, het_ctr_20, gr_com9_20, het_com9_20,
                          conc_20, com9_name, new_path_119)
        plotmaker_seconds(gr_ctr_20, het_ctr_20, gr_com10_20, het_com10_20,
                          conc_20, com10_name, new_path_120)

        plotmaker_seconds_pooled(gr_dist0_7, het_dist0_7, gr_ctr_7, het_ctr_7,
                                 gr_com1_7, het_com1_7, conc_7, com1_name,
                                 new_path_121)
        plotmaker_seconds_pooled(gr_dist0_7, het_dist0_7, gr_ctr_7, het_ctr_7,
                                 gr_com2_7, het_com2_7, conc_7, com2_name,
                                 new_path_122)
        plotmaker_seconds_pooled(gr_dist0_7, het_dist0_7, gr_ctr_7, het_ctr_7,
                                 gr_com3_7, het_com3_7, conc_7, com3_name,
                                 new_path_123)
        plotmaker_seconds_pooled(gr_dist0_7, het_dist0_7, gr_ctr_7, het_ctr_7,
                                 gr_com4_7, het_com4_7, conc_7, com4_name,
                                 new_path_124)
        plotmaker_seconds_pooled(gr_dist0_7, het_dist0_7, gr_ctr_7, het_ctr_7,
                                 gr_com5_7, het_com5_7, conc_7, com5_name,
                                 new_path_125)
        plotmaker_seconds_pooled(gr_dist0_7, het_dist0_7, gr_ctr_7, het_ctr_7,
                                 gr_com6_7, het_com6_7, conc_7, com6_name,
                                 new_path_126)
        plotmaker_seconds_pooled(gr_dist0_7, het_dist0_7, gr_ctr_7, het_ctr_7,
                                 gr_com7_7, het_com7_7, conc_7, com7_name,
                                 new_path_127)
        plotmaker_seconds_pooled(gr_dist0_7, het_dist0_7, gr_ctr_7, het_ctr_7,
                                 gr_com8_7, het_com8_7, conc_7, com8_name,
                                 new_path_128)
        plotmaker_seconds_pooled(gr_dist0_7, het_dist0_7, gr_ctr_7, het_ctr_7,
                                 gr_com9_7, het_com9_7, conc_7, com9_name,
                                 new_path_129)
        plotmaker_seconds_pooled(gr_dist0_7, het_dist0_7, gr_ctr_7, het_ctr_7,
                                 gr_com10_7, het_com10_7, conc_7, com10_name,
                                 new_path_130)

        plotmaker_seconds_pooled(gr_dist0_20, het_dist0_20, gr_ctr_20,
                                 het_ctr_20, gr_com1_20, het_com1_20, conc_20,
                                 com1_name, new_path_131)
        plotmaker_seconds_pooled(gr_dist0_20, het_dist0_20, gr_ctr_20,
                                 het_ctr_20, gr_com2_20, het_com2_20, conc_20,
                                 com2_name, new_path_132)
        plotmaker_seconds_pooled(gr_dist0_20, het_dist0_20, gr_ctr_20,
                                 het_ctr_20, gr_com3_20, het_com3_20, conc_20,
                                 com3_name, new_path_133)
        plotmaker_seconds_pooled(gr_dist0_20, het_dist0_20, gr_ctr_20,
                                 het_ctr_20, gr_com4_20, het_com4_20, conc_20,
                                 com4_name, new_path_134)
        plotmaker_seconds_pooled(gr_dist0_20, het_dist0_20, gr_ctr_20,
                                 het_ctr_20, gr_com5_20, het_com5_20, conc_20,
                                 com5_name, new_path_135)
        plotmaker_seconds_pooled(gr_dist0_20, het_dist0_20, gr_ctr_20,
                                 het_ctr_20, gr_com6_20, het_com6_20, conc_20,
                                 com6_name, new_path_136)
        plotmaker_seconds_pooled(gr_dist0_20, het_dist0_20, gr_ctr_20,
                                 het_ctr_20, gr_com7_20, het_com7_20, conc_20,
                                 com7_name, new_path_137)
        plotmaker_seconds_pooled(gr_dist0_20, het_dist0_20, gr_ctr_20,
                                 het_ctr_20, gr_com8_20, het_com8_20, conc_20,
                                 com8_name, new_path_138)
        plotmaker_seconds_pooled(gr_dist0_20, het_dist0_20, gr_ctr_20,
                                 het_ctr_20, gr_com9_20, het_com9_20, conc_20,
                                 com9_name, new_path_139)
        plotmaker_seconds_pooled(gr_dist0_20, het_dist0_20, gr_ctr_20,
                                 het_ctr_20, gr_com10_20, het_com10_20,
                                 conc_20, com10_name, new_path_140)

        a1_7 = new_buildfish(a1_7_p1)
        a10_7 = new_buildfish(a10_7_p1)
        a11_7 = new_buildfish(a11_7_p1)
        a12_7 = new_buildfish(a12_7_p1)
        a2_7 = new_buildfish(a2_7_p1)
        a3_7 = new_buildfish(a3_7_p1)
        a4_7 = new_buildfish(a4_7_p1)
        a5_7 = new_buildfish(a5_7_p1)
        a6_7 = new_buildfish(a6_7_p1)
        a7_7 = new_buildfish(a7_7_p1)
        a8_7 = new_buildfish(a8_7_p1)
        a9_7 = new_buildfish(a9_7_p1)
        b1_7 = new_buildfish(b1_7_p1)
        b10_7 = new_buildfish(b10_7_p1)
        b11_7 = new_buildfish(b11_7_p1)
        b12_7 = new_buildfish(b12_7_p1)
        b2_7 = new_buildfish(b2_7_p1)
        b3_7 = new_buildfish(b3_7_p1)
        b4_7 = new_buildfish(b4_7_p1)
        b5_7 = new_buildfish(b5_7_p1)
        b6_7 = new_buildfish(b6_7_p1)
        b7_7 = new_buildfish(b7_7_p1)
        b8_7 = new_buildfish(b8_7_p1)
        b9_7 = new_buildfish(b9_7_p1)
        c1_7 = new_buildfish(c1_7_p1)
        c10_7 = new_buildfish(c10_7_p1)
        c11_7 = new_buildfish(c11_7_p1)
        c12_7 = new_buildfish(c12_7_p1)
        c2_7 = new_buildfish(c2_7_p1)
        c3_7 = new_buildfish(c3_7_p1)
        c4_7 = new_buildfish(c4_7_p1)
        c5_7 = new_buildfish(c5_7_p1)
        c6_7 = new_buildfish(c6_7_p1)
        c7_7 = new_buildfish(c7_7_p1)
        c8_7 = new_buildfish(c8_7_p1)
        c9_7 = new_buildfish(c9_7_p1)
        d1_7 = new_buildfish(d1_7_p1)
        d10_7 = new_buildfish(d10_7_p1)
        d11_7 = new_buildfish(d11_7_p1)
        d12_7 = new_buildfish(d12_7_p1)
        d2_7 = new_buildfish(d2_7_p1)
        d3_7 = new_buildfish(d3_7_p1)
        d4_7 = new_buildfish(d4_7_p1)
        d5_7 = new_buildfish(d5_7_p1)
        d6_7 = new_buildfish(d6_7_p1)
        d7_7 = new_buildfish(d7_7_p1)
        d8_7 = new_buildfish(d8_7_p1)
        d9_7 = new_buildfish(d9_7_p1)
        e1_7 = new_buildfish(e1_7_p1)
        e10_7 = new_buildfish(e10_7_p1)
        e11_7 = new_buildfish(e11_7_p1)
        e12_7 = new_buildfish(e12_7_p1)
        e2_7 = new_buildfish(e2_7_p1)
        e3_7 = new_buildfish(e3_7_p1)
        e4_7 = new_buildfish(e4_7_p1)
        e5_7 = new_buildfish(e5_7_p1)
        e6_7 = new_buildfish(e6_7_p1)
        e7_7 = new_buildfish(e7_7_p1)
        e8_7 = new_buildfish(e8_7_p1)
        e9_7 = new_buildfish(e9_7_p1)
        f1_7 = new_buildfish(f1_7_p1)
        f10_7 = new_buildfish(f10_7_p1)
        f11_7 = new_buildfish(f11_7_p1)
        f12_7 = new_buildfish(f12_7_p1)
        f2_7 = new_buildfish(f2_7_p1)
        f3_7 = new_buildfish(f3_7_p1)
        f4_7 = new_buildfish(f4_7_p1)
        f5_7 = new_buildfish(f5_7_p1)
        f6_7 = new_buildfish(f6_7_p1)
        f7_7 = new_buildfish(f7_7_p1)
        f8_7 = new_buildfish(f8_7_p1)
        f9_7 = new_buildfish(f9_7_p1)
        g1_7 = new_buildfish(g1_7_p1)
        g10_7 = new_buildfish(g10_7_p1)
        g11_7 = new_buildfish(g11_7_p1)
        g12_7 = new_buildfish(g12_7_p1)
        g2_7 = new_buildfish(g2_7_p1)
        g3_7 = new_buildfish(g3_7_p1)
        g4_7 = new_buildfish(g4_7_p1)
        g5_7 = new_buildfish(g5_7_p1)
        g6_7 = new_buildfish(g6_7_p1)
        g7_7 = new_buildfish(g7_7_p1)
        g8_7 = new_buildfish(g8_7_p1)
        g9_7 = new_buildfish(g9_7_p1)
        h1_7 = new_buildfish(h1_7_p1)
        h10_7 = new_buildfish(h10_7_p1)
        h11_7 = new_buildfish(h11_7_p1)
        h12_7 = new_buildfish(h12_7_p1)
        h2_7 = new_buildfish(h2_7_p1)
        h3_7 = new_buildfish(h3_7_p1)
        h4_7 = new_buildfish(h4_7_p1)
        h5_7 = new_buildfish(h5_7_p1)
        h6_7 = new_buildfish(h6_7_p1)
        h7_7 = new_buildfish(h7_7_p1)
        h8_7 = new_buildfish(h8_7_p1)
        h9_7 = new_buildfish(h9_7_p1)

        a1_20 = new_buildfish(a1_20_p1)
        a10_20 = new_buildfish(a10_20_p1)
        a11_20 = new_buildfish(a11_20_p1)
        a12_20 = new_buildfish(a12_20_p1)
        a2_20 = new_buildfish(a2_20_p1)
        a3_20 = new_buildfish(a3_20_p1)
        a4_20 = new_buildfish(a4_20_p1)
        a5_20 = new_buildfish(a5_20_p1)
        a6_20 = new_buildfish(a6_20_p1)
        a7_20 = new_buildfish(a7_20_p1)
        a8_20 = new_buildfish(a8_20_p1)
        a9_20 = new_buildfish(a9_20_p1)
        b1_20 = new_buildfish(b1_20_p1)
        b10_20 = new_buildfish(b10_20_p1)
        b11_20 = new_buildfish(b11_20_p1)
        b12_20 = new_buildfish(b12_20_p1)
        b2_20 = new_buildfish(b2_20_p1)
        b3_20 = new_buildfish(b3_20_p1)
        b4_20 = new_buildfish(b4_20_p1)
        b5_20 = new_buildfish(b5_20_p1)
        b6_20 = new_buildfish(b6_20_p1)
        b7_20 = new_buildfish(b7_20_p1)
        b8_20 = new_buildfish(b8_20_p1)
        b9_20 = new_buildfish(b9_20_p1)
        c1_20 = new_buildfish(c1_20_p1)
        c10_20 = new_buildfish(c10_20_p1)
        c11_20 = new_buildfish(c11_20_p1)
        c12_20 = new_buildfish(c12_20_p1)
        c2_20 = new_buildfish(c2_20_p1)
        c3_20 = new_buildfish(c3_20_p1)
        c4_20 = new_buildfish(c4_20_p1)
        c5_20 = new_buildfish(c5_20_p1)
        c6_20 = new_buildfish(c6_20_p1)
        c7_20 = new_buildfish(c7_20_p1)
        c8_20 = new_buildfish(c8_20_p1)
        c9_20 = new_buildfish(c9_20_p1)
        d1_20 = new_buildfish(d1_20_p1)
        d10_20 = new_buildfish(d10_20_p1)
        d11_20 = new_buildfish(d11_20_p1)
        d12_20 = new_buildfish(d12_20_p1)
        d2_20 = new_buildfish(d2_20_p1)
        d3_20 = new_buildfish(d3_20_p1)
        d4_20 = new_buildfish(d4_20_p1)
        d5_20 = new_buildfish(d5_20_p1)
        d6_20 = new_buildfish(d6_20_p1)
        d7_20 = new_buildfish(d7_20_p1)
        d8_20 = new_buildfish(d8_20_p1)
        d9_20 = new_buildfish(d9_20_p1)
        e1_20 = new_buildfish(e1_20_p1)
        e10_20 = new_buildfish(e10_20_p1)
        e11_20 = new_buildfish(e11_20_p1)
        e12_20 = new_buildfish(e12_20_p1)
        e2_20 = new_buildfish(e2_20_p1)
        e3_20 = new_buildfish(e3_20_p1)
        e4_20 = new_buildfish(e4_20_p1)
        e5_20 = new_buildfish(e5_20_p1)
        e6_20 = new_buildfish(e6_20_p1)
        e7_20 = new_buildfish(e7_20_p1)
        e8_20 = new_buildfish(e8_20_p1)
        e9_20 = new_buildfish(e9_20_p1)
        f1_20 = new_buildfish(f1_20_p1)
        f10_20 = new_buildfish(f10_20_p1)
        f11_20 = new_buildfish(f11_20_p1)
        f12_20 = new_buildfish(f12_20_p1)
        f2_20 = new_buildfish(f2_20_p1)
        f3_20 = new_buildfish(f3_20_p1)
        f4_20 = new_buildfish(f4_20_p1)
        f5_20 = new_buildfish(f5_20_p1)
        f6_20 = new_buildfish(f6_20_p1)
        f7_20 = new_buildfish(f7_20_p1)
        f8_20 = new_buildfish(f8_20_p1)
        f9_20 = new_buildfish(f9_20_p1)
        g1_20 = new_buildfish(g1_20_p1)
        g10_20 = new_buildfish(g10_20_p1)
        g11_20 = new_buildfish(g11_20_p1)
        g12_20 = new_buildfish(g12_20_p1)
        g2_20 = new_buildfish(g2_20_p1)
        g3_20 = new_buildfish(g3_20_p1)
        g4_20 = new_buildfish(g4_20_p1)
        g5_20 = new_buildfish(g5_20_p1)
        g6_20 = new_buildfish(g6_20_p1)
        g7_20 = new_buildfish(g7_20_p1)
        g8_20 = new_buildfish(g8_20_p1)
        g9_20 = new_buildfish(g9_20_p1)
        h1_20 = new_buildfish(h1_20_p1)
        h10_20 = new_buildfish(h10_20_p1)
        h11_20 = new_buildfish(h11_20_p1)
        h12_20 = new_buildfish(h12_20_p1)
        h2_20 = new_buildfish(h2_20_p1)
        h3_20 = new_buildfish(h3_20_p1)
        h4_20 = new_buildfish(h4_20_p1)
        h5_20 = new_buildfish(h5_20_p1)
        h6_20 = new_buildfish(h6_20_p1)
        h7_20 = new_buildfish(h7_20_p1)
        h8_20 = new_buildfish(h8_20_p1)
        h9_20 = new_buildfish(h9_20_p1)

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

        gr_ctr_ind_7 = ctr_intogroups(a1_7, b1_7, c1_7, d1_7, a12_7, b12_7,
                                      c12_7, d12_7)
        het_ctr_ind_7 = ctr_intogroups(e1_7, f1_7, g1_7, h1_7, e12_7, f12_7,
                                       g12_7, h12_7)
        gr_com1_ind_7 = com_intogroups(a2_7, b2_7, c2_7, d2_7)
        gr_com2_ind_7 = com_intogroups(a3_7, b3_7, c3_7, d3_7)
        gr_com3_ind_7 = com_intogroups(a4_7, b4_7, c4_7, d4_7)
        gr_com4_ind_7 = com_intogroups(a5_7, b5_7, c5_7, d5_7)
        gr_com5_ind_7 = com_intogroups(a6_7, b6_7, c6_7, d6_7)
        gr_com6_ind_7 = com_intogroups(a7_7, b7_7, c7_7, d7_7)
        gr_com7_ind_7 = com_intogroups(a8_7, b8_7, c8_7, d8_7)
        gr_com8_ind_7 = com_intogroups(a9_7, b9_7, c9_7, d9_7)
        gr_com9_ind_7 = com_intogroups(a10_7, b10_7, c10_7, d10_7)
        gr_com10_ind_7 = com_intogroups(a11_7, b11_7, c11_7, d11_7)
        het_com1_ind_7 = com_intogroups(e2_7, f2_7, g2_7, h2_7)
        het_com2_ind_7 = com_intogroups(e3_7, f3_7, g3_7, h3_7)
        het_com3_ind_7 = com_intogroups(e4_7, f4_7, g4_7, h4_7)
        het_com4_ind_7 = com_intogroups(e5_7, f5_7, g5_7, h5_7)
        het_com5_ind_7 = com_intogroups(e6_7, f6_7, g6_7, h6_7)
        het_com6_ind_7 = com_intogroups(e7_7, f7_7, g7_7, h7_7)
        het_com7_ind_7 = com_intogroups(e8_7, f8_7, g8_7, h8_7)
        het_com8_ind_7 = com_intogroups(e9_7, f9_7, g9_7, h9_7)
        het_com9_ind_7 = com_intogroups(e10_7, f10_7, g10_7, h10_7)
        het_com10_ind_7 = com_intogroups(e11_7, f11_7, g11_7, h11_7)

        gr_ctr_ind_20 = ctr_intogroups(a1_20, b1_20, c1_20, d1_20, a12_20,
                                       b12_20, c12_20, d12_20)
        het_ctr_ind_20 = ctr_intogroups(e1_20, f1_20, g1_20, h1_20, e12_20,
                                        f12_20, g12_20, h12_20)
        gr_com1_ind_20 = com_intogroups(a2_20, b2_20, c2_20, d2_20)
        gr_com2_ind_20 = com_intogroups(a3_20, b3_20, c3_20, d3_20)
        gr_com3_ind_20 = com_intogroups(a4_20, b4_20, c4_20, d4_20)
        gr_com4_ind_20 = com_intogroups(a5_20, b5_20, c5_20, d5_20)
        gr_com5_ind_20 = com_intogroups(a6_20, b6_20, c6_20, d6_20)
        gr_com6_ind_20 = com_intogroups(a7_20, b7_20, c7_20, d7_20)
        gr_com7_ind_20 = com_intogroups(a8_20, b8_20, c8_20, d8_20)
        gr_com8_ind_20 = com_intogroups(a9_20, b9_20, c9_20, d9_20)
        gr_com9_ind_20 = com_intogroups(a10_20, b10_20, c10_20, d10_20)
        gr_com10_ind_20 = com_intogroups(a11_20, b11_20, c11_20, d11_20)
        het_com1_ind_20 = com_intogroups(e2_20, f2_20, g2_20, h2_20)
        het_com2_ind_20 = com_intogroups(e3_20, f3_20, g3_20, h3_20)
        het_com3_ind_20 = com_intogroups(e4_20, f4_20, g4_20, h4_20)
        het_com4_ind_20 = com_intogroups(e5_20, f5_20, g5_20, h5_20)
        het_com5_ind_20 = com_intogroups(e6_20, f6_20, g6_20, h6_20)
        het_com6_ind_20 = com_intogroups(e7_20, f7_20, g7_20, h7_20)
        het_com7_ind_20 = com_intogroups(e8_20, f8_20, g8_20, h8_20)
        het_com8_ind_20 = com_intogroups(e9_20, f9_20, g9_20, h9_20)
        het_com9_ind_20 = com_intogroups(e10_20, f10_20, g10_20, h10_20)
        het_com10_ind_20 = com_intogroups(e11_20, f11_20, g11_20, h11_20)

        ''' Writing individual csv files '''

        ind_csv(gr_ctr_ind_7, het_ctr_ind_7, gr_com1_ind_7, het_com1_ind_7,
                new_path_1)
        ind_csv(gr_ctr_ind_7, het_ctr_ind_7, gr_com2_ind_7, het_com2_ind_7,
                new_path_2)
        ind_csv(gr_ctr_ind_7, het_ctr_ind_7, gr_com3_ind_7, het_com3_ind_7,
                new_path_3)
        ind_csv(gr_ctr_ind_7, het_ctr_ind_7, gr_com4_ind_7, het_com4_ind_7,
                new_path_4)
        ind_csv(gr_ctr_ind_7, het_ctr_ind_7, gr_com5_ind_7, het_com5_ind_7,
                new_path_5)
        ind_csv(gr_ctr_ind_7, het_ctr_ind_7, gr_com6_ind_7, het_com6_ind_7,
                new_path_6)
        ind_csv(gr_ctr_ind_7, het_ctr_ind_7, gr_com7_ind_7, het_com7_ind_7,
                new_path_7)
        ind_csv(gr_ctr_ind_7, het_ctr_ind_7, gr_com8_ind_7, het_com8_ind_7,
                new_path_8)
        ind_csv(gr_ctr_ind_7, het_ctr_ind_7, gr_com9_ind_7, het_com9_ind_7,
                new_path_9)
        ind_csv(gr_ctr_ind_7, het_ctr_ind_7, gr_com10_ind_7, het_com10_ind_7,
                new_path_10)

        ind_csv(gr_ctr_ind_20, het_ctr_ind_20, gr_com1_ind_20, het_com1_ind_20,
                new_path_51)
        ind_csv(gr_ctr_ind_20, het_ctr_ind_20, gr_com2_ind_20, het_com2_ind_20,
                new_path_52)
        ind_csv(gr_ctr_ind_20, het_ctr_ind_20, gr_com3_ind_20, het_com3_ind_20,
                new_path_53)
        ind_csv(gr_ctr_ind_20, het_ctr_ind_20, gr_com4_ind_20, het_com4_ind_20,
                new_path_54)
        ind_csv(gr_ctr_ind_20, het_ctr_ind_20, gr_com5_ind_20, het_com5_ind_20,
                new_path_55)
        ind_csv(gr_ctr_ind_20, het_ctr_ind_20, gr_com6_ind_20, het_com6_ind_20,
                new_path_56)
        ind_csv(gr_ctr_ind_20, het_ctr_ind_20, gr_com7_ind_20, het_com7_ind_20,
                new_path_57)
        ind_csv(gr_ctr_ind_20, het_ctr_ind_20, gr_com8_ind_20, het_com8_ind_20,
                new_path_58)
        ind_csv(gr_ctr_ind_20, het_ctr_ind_20, gr_com9_ind_20, het_com9_ind_20,
                new_path_59)
        ind_csv(gr_ctr_ind_20, het_ctr_ind_20, gr_com10_ind_20,
                het_com10_ind_20, new_path_60)

        ''' This section makes pivot tables per condition '''

        gr_ctr_piv_7 = pivoter(gr_ctr_ind_7)
        het_ctr_piv_7 = pivoter(het_ctr_ind_7)
        gr_com1_piv_7 = pivoter(gr_com1_ind_7)
        gr_com2_piv_7 = pivoter(gr_com2_ind_7)
        gr_com3_piv_7 = pivoter(gr_com3_ind_7)
        gr_com4_piv_7 = pivoter(gr_com4_ind_7)
        gr_com5_piv_7 = pivoter(gr_com5_ind_7)
        gr_com6_piv_7 = pivoter(gr_com6_ind_7)
        gr_com7_piv_7 = pivoter(gr_com7_ind_7)
        gr_com8_piv_7 = pivoter(gr_com8_ind_7)
        gr_com9_piv_7 = pivoter(gr_com9_ind_7)
        gr_com10_piv_7 = pivoter(gr_com10_ind_7)
        het_com1_piv_7 = pivoter(het_com1_ind_7)
        het_com2_piv_7 = pivoter(het_com2_ind_7)
        het_com3_piv_7 = pivoter(het_com3_ind_7)
        het_com4_piv_7 = pivoter(het_com4_ind_7)
        het_com5_piv_7 = pivoter(het_com5_ind_7)
        het_com6_piv_7 = pivoter(het_com6_ind_7)
        het_com7_piv_7 = pivoter(het_com7_ind_7)
        het_com8_piv_7 = pivoter(het_com8_ind_7)
        het_com9_piv_7 = pivoter(het_com9_ind_7)
        het_com10_piv_7 = pivoter(het_com10_ind_7)

        gr_ctr_piv_20 = pivoter(gr_ctr_ind_20)
        het_ctr_piv_20 = pivoter(het_ctr_ind_20)
        gr_com1_piv_20 = pivoter(gr_com1_ind_20)
        gr_com2_piv_20 = pivoter(gr_com2_ind_20)
        gr_com3_piv_20 = pivoter(gr_com3_ind_20)
        gr_com4_piv_20 = pivoter(gr_com4_ind_20)
        gr_com5_piv_20 = pivoter(gr_com5_ind_20)
        gr_com6_piv_20 = pivoter(gr_com6_ind_20)
        gr_com7_piv_20 = pivoter(gr_com7_ind_20)
        gr_com8_piv_20 = pivoter(gr_com8_ind_20)
        gr_com9_piv_20 = pivoter(gr_com9_ind_20)
        gr_com10_piv_20 = pivoter(gr_com10_ind_20)
        het_com1_piv_20 = pivoter(het_com1_ind_20)
        het_com2_piv_20 = pivoter(het_com2_ind_20)
        het_com3_piv_20 = pivoter(het_com3_ind_20)
        het_com4_piv_20 = pivoter(het_com4_ind_20)
        het_com5_piv_20 = pivoter(het_com5_ind_20)
        het_com6_piv_20 = pivoter(het_com6_ind_20)
        het_com7_piv_20 = pivoter(het_com7_ind_20)
        het_com8_piv_20 = pivoter(het_com8_ind_20)
        het_com9_piv_20 = pivoter(het_com9_ind_20)
        het_com10_piv_20 = pivoter(het_com10_ind_20)

        ''' Make means with error bars plots '''

        plotmaker_means(gr_ctr_piv_7, het_ctr_piv_7, gr_ctr_piv_20,
                        het_ctr_piv_20, gr_com1_piv_7, gr_com1_piv_20,
                        het_com1_piv_7, het_com1_piv_20, com1_name, analysed,
                        tps, new_path_161)

        plotmaker_means(gr_ctr_piv_7, het_ctr_piv_7, gr_ctr_piv_20,
                        het_ctr_piv_20, gr_com2_piv_7, gr_com2_piv_20,
                        het_com2_piv_7, het_com2_piv_20, com2_name, analysed,
                        tps, new_path_162)

        plotmaker_means(gr_ctr_piv_7, het_ctr_piv_7, gr_ctr_piv_20,
                        het_ctr_piv_20, gr_com3_piv_7, gr_com3_piv_20,
                        het_com3_piv_7, het_com3_piv_20, com3_name, analysed,
                        tps, new_path_163)

        plotmaker_means(gr_ctr_piv_7, het_ctr_piv_7, gr_ctr_piv_20,
                        het_ctr_piv_20, gr_com4_piv_7, gr_com4_piv_20,
                        het_com4_piv_7, het_com4_piv_20, com4_name, analysed,
                        tps, new_path_164)

        plotmaker_means(gr_ctr_piv_7, het_ctr_piv_7, gr_ctr_piv_20,
                        het_ctr_piv_20, gr_com5_piv_7, gr_com5_piv_20,
                        het_com5_piv_7, het_com5_piv_20, com5_name, analysed,
                        tps, new_path_165)

        plotmaker_means(gr_ctr_piv_7, het_ctr_piv_7, gr_ctr_piv_20,
                        het_ctr_piv_20, gr_com6_piv_7, gr_com6_piv_20,
                        het_com6_piv_7, het_com6_piv_20, com6_name, analysed,
                        tps, new_path_166)

        plotmaker_means(gr_ctr_piv_7, het_ctr_piv_7, gr_ctr_piv_20,
                        het_ctr_piv_20, gr_com7_piv_7, gr_com7_piv_20,
                        het_com7_piv_7, het_com7_piv_20, com7_name, analysed,
                        tps, new_path_167)

        plotmaker_means(gr_ctr_piv_7, het_ctr_piv_7, gr_ctr_piv_20,
                        het_ctr_piv_20, gr_com8_piv_7, gr_com8_piv_20,
                        het_com8_piv_7, het_com8_piv_20, com8_name, analysed,
                        tps, new_path_168)

        plotmaker_means(gr_ctr_piv_7, het_ctr_piv_7, gr_ctr_piv_20,
                        het_ctr_piv_20, gr_com9_piv_7, gr_com9_piv_20,
                        het_com9_piv_7, het_com9_piv_20, com9_name, analysed,
                        tps, new_path_169)

        plotmaker_means(gr_ctr_piv_7, het_ctr_piv_7, gr_ctr_piv_20,
                        het_ctr_piv_20, gr_com10_piv_7, gr_com10_piv_20,
                        het_com10_piv_7, het_com10_piv_20, com10_name,
                        analysed, tps, new_path_170)

        ''' This section concerns group averages per time point '''

        group_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com1_piv_7, het_com1_piv_7,
                  new_path_11)
        group_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com2_piv_7, het_com2_piv_7,
                  new_path_12)
        group_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com3_piv_7, het_com3_piv_7,
                  new_path_13)
        group_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com4_piv_7, het_com4_piv_7,
                  new_path_14)
        group_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com5_piv_7, het_com5_piv_7,
                  new_path_15)
        group_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com6_piv_7, het_com6_piv_7,
                  new_path_16)
        group_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com7_piv_7, het_com7_piv_7,
                  new_path_17)
        group_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com8_piv_7, het_com8_piv_7,
                  new_path_18)
        group_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com9_piv_7, het_com9_piv_7,
                  new_path_19)
        group_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com10_piv_7, het_com10_piv_7,
                  new_path_20)

        group_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com1_piv_20,
                  het_com1_piv_20, new_path_61)
        group_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com2_piv_20,
                  het_com2_piv_20, new_path_62)
        group_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com3_piv_20,
                  het_com3_piv_20, new_path_63)
        group_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com4_piv_20,
                  het_com4_piv_20, new_path_64)
        group_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com5_piv_20,
                  het_com5_piv_20, new_path_65)
        group_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com6_piv_20,
                  het_com6_piv_20, new_path_66)
        group_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com7_piv_20,
                  het_com7_piv_20, new_path_67)
        group_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com8_piv_20,
                  het_com8_piv_20, new_path_68)
        group_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com9_piv_20,
                  het_com9_piv_20, new_path_69)
        group_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com10_piv_20,
                  het_com10_piv_20, new_path_70)

        ''' This section makes average plots '''

        plotmaker_abs_avg(gr_ctr_piv_7, het_ctr_piv_7, gr_com1_piv_7,
                          het_com1_piv_7, conc_7, com1_name, analysed,
                          new_path_21)
        plotmaker_abs_avg(gr_ctr_piv_7, het_ctr_piv_7, gr_com2_piv_7,
                          het_com2_piv_7, conc_7, com2_name, analysed,
                          new_path_22)
        plotmaker_abs_avg(gr_ctr_piv_7, het_ctr_piv_7, gr_com3_piv_7,
                          het_com3_piv_7, conc_7, com3_name, analysed,
                          new_path_23)
        plotmaker_abs_avg(gr_ctr_piv_7, het_ctr_piv_7, gr_com4_piv_7,
                          het_com4_piv_7, conc_7, com4_name, analysed,
                          new_path_24)
        plotmaker_abs_avg(gr_ctr_piv_7, het_ctr_piv_7, gr_com5_piv_7,
                          het_com5_piv_7, conc_7, com5_name, analysed,
                          new_path_25)
        plotmaker_abs_avg(gr_ctr_piv_7, het_ctr_piv_7, gr_com6_piv_7,
                          het_com6_piv_7, conc_7, com6_name, analysed,
                          new_path_26)
        plotmaker_abs_avg(gr_ctr_piv_7, het_ctr_piv_7, gr_com7_piv_7,
                          het_com7_piv_7, conc_7, com7_name, analysed,
                          new_path_27)
        plotmaker_abs_avg(gr_ctr_piv_7, het_ctr_piv_7, gr_com8_piv_7,
                          het_com8_piv_7, conc_7, com8_name, analysed,
                          new_path_28)
        plotmaker_abs_avg(gr_ctr_piv_7, het_ctr_piv_7, gr_com9_piv_7,
                          het_com9_piv_7, conc_7, com9_name, analysed,
                          new_path_29)
        plotmaker_abs_avg(gr_ctr_piv_7, het_ctr_piv_7, gr_com10_piv_7,
                          het_com10_piv_7, conc_7, com10_name, analysed,
                          new_path_30)

        plotmaker_abs_avg(gr_ctr_piv_20, het_ctr_piv_20, gr_com1_piv_20,
                          het_com1_piv_20, conc_20, com1_name, analysed,
                          new_path_71)
        plotmaker_abs_avg(gr_ctr_piv_20, het_ctr_piv_20, gr_com2_piv_20,
                          het_com2_piv_20, conc_20, com2_name, analysed,
                          new_path_72)
        plotmaker_abs_avg(gr_ctr_piv_20, het_ctr_piv_20, gr_com3_piv_20,
                          het_com3_piv_20, conc_20, com3_name, analysed,
                          new_path_73)
        plotmaker_abs_avg(gr_ctr_piv_20, het_ctr_piv_20, gr_com4_piv_20,
                          het_com4_piv_20, conc_20, com4_name, analysed,
                          new_path_74)
        plotmaker_abs_avg(gr_ctr_piv_20, het_ctr_piv_20, gr_com5_piv_20,
                          het_com5_piv_20, conc_20, com5_name, analysed,
                          new_path_75)
        plotmaker_abs_avg(gr_ctr_piv_20, het_ctr_piv_20, gr_com6_piv_20,
                          het_com6_piv_20, conc_20, com6_name, analysed,
                          new_path_76)
        plotmaker_abs_avg(gr_ctr_piv_20, het_ctr_piv_20, gr_com7_piv_20,
                          het_com7_piv_20, conc_20, com7_name, analysed,
                          new_path_77)
        plotmaker_abs_avg(gr_ctr_piv_20, het_ctr_piv_20, gr_com8_piv_20,
                          het_com8_piv_20, conc_20, com8_name, analysed,
                          new_path_78)
        plotmaker_abs_avg(gr_ctr_piv_20, het_ctr_piv_20, gr_com9_piv_20,
                          het_com9_piv_20, conc_20, com9_name, analysed,
                          new_path_79)
        plotmaker_abs_avg(gr_ctr_piv_20, het_ctr_piv_20, gr_com10_piv_20,
                          het_com10_piv_20, conc_20, com10_name, analysed,
                          new_path_80)

        ''' This section concerns absolute change'''

        com1_abs_7 = absolute_change(gr_ctr_piv_7, het_ctr_piv_7,
                                     gr_com1_piv_7, het_com1_piv_7, starttp,
                                     endtp)
        com2_abs_7 = absolute_change(gr_ctr_piv_7, het_ctr_piv_7,
                                     gr_com2_piv_7, het_com2_piv_7, starttp,
                                     endtp)
        com3_abs_7 = absolute_change(gr_ctr_piv_7, het_ctr_piv_7,
                                     gr_com3_piv_7, het_com3_piv_7, starttp,
                                     endtp)
        com4_abs_7 = absolute_change(gr_ctr_piv_7, het_ctr_piv_7,
                                     gr_com4_piv_7, het_com4_piv_7, starttp,
                                     endtp)
        com5_abs_7 = absolute_change(gr_ctr_piv_7, het_ctr_piv_7,
                                     gr_com5_piv_7, het_com5_piv_7, starttp,
                                     endtp)
        com6_abs_7 = absolute_change(gr_ctr_piv_7, het_ctr_piv_7,
                                     gr_com6_piv_7, het_com6_piv_7, starttp,
                                     endtp)
        com7_abs_7 = absolute_change(gr_ctr_piv_7, het_ctr_piv_7,
                                     gr_com7_piv_7, het_com7_piv_7, starttp,
                                     endtp)
        com8_abs_7 = absolute_change(gr_ctr_piv_7, het_ctr_piv_7,
                                     gr_com8_piv_7, het_com8_piv_7, starttp,
                                     endtp)
        com9_abs_7 = absolute_change(gr_ctr_piv_7, het_ctr_piv_7,
                                     gr_com9_piv_7, het_com9_piv_7, starttp,
                                     endtp)
        com10_abs_7 = absolute_change(gr_ctr_piv_7, het_ctr_piv_7,
                                      gr_com10_piv_7, het_com10_piv_7, starttp,
                                      endtp)

        com1_abs_20 = absolute_change(gr_ctr_piv_20, het_ctr_piv_20,
                                      gr_com1_piv_20, het_com1_piv_20, starttp,
                                      endtp)
        com2_abs_20 = absolute_change(gr_ctr_piv_20, het_ctr_piv_20,
                                      gr_com2_piv_20, het_com2_piv_20, starttp,
                                      endtp)
        com3_abs_20 = absolute_change(gr_ctr_piv_20, het_ctr_piv_20,
                                      gr_com3_piv_20, het_com3_piv_20, starttp,
                                      endtp)
        com4_abs_20 = absolute_change(gr_ctr_piv_20, het_ctr_piv_20,
                                      gr_com4_piv_20, het_com4_piv_20, starttp,
                                      endtp)
        com5_abs_20 = absolute_change(gr_ctr_piv_20, het_ctr_piv_20,
                                      gr_com5_piv_20, het_com5_piv_20, starttp,
                                      endtp)
        com6_abs_20 = absolute_change(gr_ctr_piv_20, het_ctr_piv_20,
                                      gr_com6_piv_20, het_com6_piv_20, starttp,
                                      endtp)
        com7_abs_20 = absolute_change(gr_ctr_piv_20, het_ctr_piv_20,
                                      gr_com7_piv_20, het_com7_piv_20, starttp,
                                      endtp)
        com8_abs_20 = absolute_change(gr_ctr_piv_20, het_ctr_piv_20,
                                      gr_com8_piv_20, het_com8_piv_20, starttp,
                                      endtp)
        com9_abs_20 = absolute_change(gr_ctr_piv_20, het_ctr_piv_20,
                                      gr_com9_piv_20, het_com9_piv_20, starttp,
                                      endtp)
        com10_abs_20 = absolute_change(gr_ctr_piv_20, het_ctr_piv_20,
                                       gr_com10_piv_20, het_com10_piv_20,
                                       starttp, endtp)

        com1_abs_7.to_csv(new_path_171)
        com2_abs_7.to_csv(new_path_172)
        com3_abs_7.to_csv(new_path_173)
        com4_abs_7.to_csv(new_path_174)
        com5_abs_7.to_csv(new_path_175)
        com6_abs_7.to_csv(new_path_176)
        com7_abs_7.to_csv(new_path_177)
        com8_abs_7.to_csv(new_path_178)
        com9_abs_7.to_csv(new_path_179)
        com10_abs_7.to_csv(new_path_180)

        com1_abs_20.to_csv(new_path_181)
        com2_abs_20.to_csv(new_path_182)
        com3_abs_20.to_csv(new_path_183)
        com4_abs_20.to_csv(new_path_184)
        com5_abs_20.to_csv(new_path_185)
        com6_abs_20.to_csv(new_path_186)
        com7_abs_20.to_csv(new_path_187)
        com8_abs_20.to_csv(new_path_188)
        com9_abs_20.to_csv(new_path_189)
        com10_abs_20.to_csv(new_path_190)

        absolute_plotmaker(com1_abs_7, com1_abs_20, com1_name, analysed, tps,
                           new_path_141)
        absolute_plotmaker(com2_abs_7, com2_abs_20, com2_name, analysed, tps,
                           new_path_142)
        absolute_plotmaker(com3_abs_7, com3_abs_20, com3_name, analysed, tps,
                           new_path_143)
        absolute_plotmaker(com4_abs_7, com4_abs_20, com4_name, analysed, tps,
                           new_path_144)
        absolute_plotmaker(com5_abs_7, com5_abs_20, com5_name, analysed, tps,
                           new_path_145)
        absolute_plotmaker(com6_abs_7, com6_abs_20, com6_name, analysed, tps,
                           new_path_146)
        absolute_plotmaker(com7_abs_7, com7_abs_20, com7_name, analysed, tps,
                           new_path_147)
        absolute_plotmaker(com8_abs_7, com8_abs_20, com8_name, analysed, tps,
                           new_path_148)
        absolute_plotmaker(com9_abs_7, com9_abs_20, com9_name, analysed, tps,
                           new_path_149)
        absolute_plotmaker(com10_abs_7, com10_abs_20, com10_name, analysed,
                           tps, new_path_150)

        ''' This section covers normalisation csvs. '''

        normalisation_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com1_piv_7,
                          het_com1_piv_7, starttp, endtp, new_path_31)
        normalisation_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com2_piv_7,
                          het_com2_piv_7, starttp, endtp, new_path_32)
        normalisation_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com3_piv_7,
                          het_com3_piv_7, starttp, endtp, new_path_33)
        normalisation_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com4_piv_7,
                          het_com4_piv_7, starttp, endtp, new_path_34)
        normalisation_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com5_piv_7,
                          het_com5_piv_7, starttp, endtp, new_path_35)
        normalisation_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com6_piv_7,
                          het_com6_piv_7, starttp, endtp, new_path_36)
        normalisation_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com7_piv_7,
                          het_com7_piv_7, starttp, endtp, new_path_37)
        normalisation_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com8_piv_7,
                          het_com8_piv_7, starttp, endtp, new_path_38)
        normalisation_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com9_piv_7,
                          het_com9_piv_7, starttp, endtp, new_path_39)
        normalisation_csv(gr_ctr_piv_7, het_ctr_piv_7, gr_com10_piv_7,
                          het_com10_piv_7, starttp, endtp, new_path_40)

        normalisation_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com1_piv_20,
                          het_com1_piv_20, starttp, endtp, new_path_81)
        normalisation_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com2_piv_20,
                          het_com2_piv_20, starttp, endtp, new_path_82)
        normalisation_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com3_piv_20,
                          het_com3_piv_20, starttp, endtp, new_path_83)
        normalisation_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com4_piv_20,
                          het_com4_piv_20, starttp, endtp, new_path_84)
        normalisation_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com5_piv_20,
                          het_com5_piv_20, starttp, endtp, new_path_85)
        normalisation_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com6_piv_20,
                          het_com6_piv_20, starttp, endtp, new_path_86)
        normalisation_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com7_piv_20,
                          het_com7_piv_20, starttp, endtp, new_path_87)
        normalisation_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com8_piv_20,
                          het_com8_piv_20, starttp, endtp, new_path_88)
        normalisation_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com9_piv_20,
                          het_com9_piv_20, starttp, endtp, new_path_89)
        normalisation_csv(gr_ctr_piv_20, het_ctr_piv_20, gr_com10_piv_20,
                          het_com10_piv_20, starttp, endtp, new_path_90)

        ''' This sections concerns relative change '''

        com1_rel_7 = relative_change(com1_abs_7)
        com2_rel_7 = relative_change(com2_abs_7)
        com3_rel_7 = relative_change(com3_abs_7)
        com4_rel_7 = relative_change(com4_abs_7)
        com5_rel_7 = relative_change(com5_abs_7)
        com6_rel_7 = relative_change(com6_abs_7)
        com7_rel_7 = relative_change(com7_abs_7)
        com8_rel_7 = relative_change(com8_abs_7)
        com9_rel_7 = relative_change(com9_abs_7)
        com10_rel_7 = relative_change(com10_abs_7)

        com1_rel_7.to_csv(new_path_41)
        com2_rel_7.to_csv(new_path_42)
        com3_rel_7.to_csv(new_path_43)
        com4_rel_7.to_csv(new_path_44)
        com5_rel_7.to_csv(new_path_45)
        com6_rel_7.to_csv(new_path_46)
        com7_rel_7.to_csv(new_path_47)
        com8_rel_7.to_csv(new_path_48)
        com9_rel_7.to_csv(new_path_49)
        com10_rel_7.to_csv(new_path_50)

        com1_rel_20 = relative_change(com1_abs_20)
        com2_rel_20 = relative_change(com2_abs_20)
        com3_rel_20 = relative_change(com3_abs_20)
        com4_rel_20 = relative_change(com4_abs_20)
        com5_rel_20 = relative_change(com5_abs_20)
        com6_rel_20 = relative_change(com6_abs_20)
        com7_rel_20 = relative_change(com7_abs_20)
        com8_rel_20 = relative_change(com8_abs_20)
        com9_rel_20 = relative_change(com9_abs_20)
        com10_rel_20 = relative_change(com10_abs_20)

        com1_rel_20.to_csv(new_path_91)
        com2_rel_20.to_csv(new_path_92)
        com3_rel_20.to_csv(new_path_93)
        com4_rel_20.to_csv(new_path_94)
        com5_rel_20.to_csv(new_path_95)
        com6_rel_20.to_csv(new_path_96)
        com7_rel_20.to_csv(new_path_97)
        com8_rel_20.to_csv(new_path_98)
        com9_rel_20.to_csv(new_path_99)
        com10_rel_20.to_csv(new_path_100)

        relative_plotmaker(com1_rel_7, com1_rel_20, com1_name, analysed, tps,
                           new_path_151)
        relative_plotmaker(com2_rel_7, com2_rel_20, com2_name, analysed, tps,
                           new_path_152)
        relative_plotmaker(com3_rel_7, com3_rel_20, com3_name, analysed, tps,
                           new_path_153)
        relative_plotmaker(com4_rel_7, com4_rel_20, com4_name, analysed, tps,
                           new_path_154)
        relative_plotmaker(com5_rel_7, com5_rel_20, com5_name, analysed, tps,
                           new_path_155)
        relative_plotmaker(com6_rel_7, com6_rel_20, com6_name, analysed, tps,
                           new_path_156)
        relative_plotmaker(com7_rel_7, com7_rel_20, com7_name, analysed, tps,
                           new_path_157)
        relative_plotmaker(com8_rel_7, com8_rel_20, com8_name, analysed, tps,
                           new_path_158)
        relative_plotmaker(com9_rel_7, com9_rel_20, com9_name, analysed, tps,
                           new_path_159)
        relative_plotmaker(com10_rel_7, com10_rel_20, com10_name, analysed,
                           tps, new_path_160)

        print '     Plate ' + i + ' is done.'

megafunc(entire_list, output_dir)

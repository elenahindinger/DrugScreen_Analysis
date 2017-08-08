# -*- coding: utf-8 -*-
"""
Created on Thu Mar 09 18:43:01 2017

@author: ehindinger
"""

import os
import win32com.client
from natsort import natsorted
from DoseR_lookup import doser_lookup_table, find_v

main_dir = r'P:/OS new analysis test/FRT2/FRT2 Excel Files'
output_dir = r'P:\OS new analysis test\FRT2\FRT2 CSV Files'

xlfile = r'P:/OS new analysis test/Compounds_Lookup_Table.xlsx'
codes = doser_lookup_table(xlfile, output='code')
compounds = doser_lookup_table(xlfile, output='compound')
assigned = doser_lookup_table(xlfile, output='assigned')


def export_to_csv(input_folder, output_folder):
    file_list = natsorted(os.listdir(input_folder))
    for i in file_list:
        testfile = input_folder + '/' + i
        plate_code = find_v(codes, i, com_code=None)
        trial_no = str(find_v(assigned, i, plate_code))
        plate_folder = output_folder + '/' + plate_code
        if not os.path.exists(plate_folder):
            os.makedirs(plate_folder)

        # creates folder for pre, 1h, 24h files
        if trial_no == '1':
            inc_folder = plate_folder + '/' + 'pre-treatment files'
            if not os.path.exists(inc_folder):
                os.makedirs(inc_folder)
        elif trial_no == '2':
            inc_folder = plate_folder + '/' + '1h incubation files'
            if not os.path.exists(inc_folder):
                os.makedirs(inc_folder)
        elif trial_no == '3':
            inc_folder = plate_folder + '/' + '24h incubation files'
            if not os.path.exists(inc_folder):
                os.makedirs(inc_folder)
        else:
            print 'Sorry, there is a problem with the trial number of ' + i
        # Parse worksheets in file
        xl = win32com.client.Dispatch("Excel.Application")
        # xl.Interactive = False
        xl.Visible = False
        print 'Processing file ... ' + i
        xl.Workbooks.Open(testfile, ReadOnly=1)
        for xWs in xl.ActiveWorkbook.Worksheets[range(1, 97)]:
            xWs.Copy()
            new_file = inc_folder + '\Trial_' + trial_no + '_' + xWs.Name + '.csv'
            # print 'Saving ' + new_file[len(new_file)-31:-3]
            xl.ActiveWorkbook.SaveAs(Filename=new_file, FileFormat=24)
            xl.ActiveWorkbook.Saved = True
            xl.ActiveWorkbook.Close()
        print '     Saved successfully.'
        xl.Quit()


export_to_csv(main_dir, output_dir)

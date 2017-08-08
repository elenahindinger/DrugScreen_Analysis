# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 17:29:13 2017

@author: ehindinger
"""

import pandas as pd


def doser_lookup_table(filepath, output):
    df = pd.read_excel(filepath, skiprows=0, skip_footer=6,
                       parse_cols='A,B,C,D,E,F', names=['Compound', 'Code',
                                                        'Date', 'Trial 1',
                                                        'Trial 2', 'Trial 3'])
    df['Compound'] = df['Compound'].str.title()
    df['Date'] = df['Date'].dt.strftime('%d-%m-%y')
    df['Trial 1'] = df['Trial 1'].fillna(0.0).astype(int)
    df['Trial 2'] = df['Trial 2'].fillna(0.0).astype(int)
    df['Trial 3'] = df['Trial 3'].fillna(0.0).astype(int)

    trial = pd.concat([df['Trial 1'], df['Trial 2'], df['Trial 3']], axis=0).to_frame()
    trial.columns = ['Trial']
    date = pd.concat([df['Date'], df['Date'], df['Date']], axis=0).to_frame()
    code = pd.concat([df['Code'], df['Code'], df['Code']], axis=0).to_frame()
    compound = pd.concat([df['Compound'], df['Compound'], df['Compound']], axis=0).to_frame()
    trials = pd.concat([date, code, compound, trial], axis=1).set_index(['Date', 'Trial']).sort_index()

    assigned_trials = pd.concat([code, trial], axis=1).set_index(['Code', 'Trial']).sort_index()
    assigned_trials['Assigned'] = [1, 2, 3] * (len(code.index) / 3)
    extra_dict = assigned_trials.to_dict(orient='dict')

    compounds = pd.concat([df['Code'], df['Compound']], axis=1).set_index(['Code']).sort_index()
    com_dict = compounds.to_dict(orient='dict')

    multi_dic = trials.to_dict(orient='dict')
    code = multi_dic['Code']
    name = com_dict['Compound']
    assigned = extra_dict['Assigned']
    if output == 'code':
        return code
    elif output == 'compound':
        return name
    elif output == 'assigned':
        return assigned
    else:
        print 'Please specify output.'


def find_v(dictionary, filename, com_code):
    date = filename[23:31]
    trial = int(filename[41:43])
    for k, v in dictionary.iteritems():
        if k[0] == date and k[1] == trial:
            return v
        elif k[0] == com_code and k[1] == trial:
            return v


def find_name(dictionary, com_code):
    for k, v in dictionary.iteritems():
        if k == com_code:
            return v


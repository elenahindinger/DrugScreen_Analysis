# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:29:47 2017

@author: ehindinger
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 10:56:47 2017

@author: ehindinger
"""

from scipy import stats
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import itertools as it

#==============================================================================
# ''' Perform KS test based on genotype separation '''
# gb = k.groupby('genotype')  # split by genotype to separate into gr and hets
# gb.groups
# gr = gb.get_group('gr')
# het = gb.get_group('het')
# gr_array = gr.as_matrix(columns=['dist0_mean'])  # 2D array
# het_array = het.as_matrix(columns=['dist0_mean'])  # 2D array
# grr = gr_array[:, 0]  # 1D array
# hett = het_array[:, 0]  # 1D array
# gr_output = stats.kstest(grr, 'norm', args=(2,))
# het_output = stats.kstest(hett, 'norm', args=(2,))
# to_each_other = stats.ks_2samp(grr, hett)
# genotype_distribution(grr, hett, 'GR', 'Het', 'genotype', out_path) 
#==============================================================================

#==============================================================================
# ''' Perform KS test based on genotype separation '''
# gb = k.groupby('minute')  # split by minute to separate into light and dark
# gb.groups
# l = pd.concat([gb.get_group(1), gb.get_group(3), gb.get_group(5), gb.get_group(7)])
# d = pd.concat([gb.get_group(2), gb.get_group(4), gb.get_group(6), gb.get_group(8)])
# l_array = l.as_matrix(columns=['dist0_mean'])  # 2D array
# d_array = d.as_matrix(columns=['dist0_mean'])  # 2D array
# ll = l_array[:, 0]  # 1D array
# dd = d_array[:, 0]  # 1D array
# l_output = stats.kstest(ll, 'norm', args=(2,))
# d_output = stats.kstest(dd, 'norm', args=(2,))
# to_each_other = stats.ks_2samp(ll, dd)
# genotype_distribution(ll, dd, 'Light', 'Dark', 'light change', out_path)       
#==============================================================================

#==============================================================================
# ''' Perform KS test comparing to scipy normal distribution centered around mean of 2 '''
# a = f.as_matrix(columns=['dist0_mean'])
# al = a[:, 0]
# ks = stats.kstest(al, 'norm', args=(2,))
# # output is KstestResult(statistic=0.13532676198948335, pvalue=9.9675823150846554e-13)
#==============================================================================

#==============================================================================
# ''' Perform KS test comparing to selfmade normal distribution '''
# r = norm.rvs(loc=2, size=1000)
# ks2 = stats.ks_2samp(al, r)
# # output is Ks_2sampResult(statistic=0.13460416666666664, pvalue=2.4125257754700159e-07)
# genotype_distribution(r, al, 'Normal Distribution', 'My data', 'me_vs_norm', out_path)       
#==============================================================================


''' T test results '''
def ttest(df, plate_name, phase):
    if phase == 60:
        # mean for 60 sec per animal
        mean = df.groupby(['minute', 'genotype', 'animal']).mean().drop(df.columns[[2, 4, 5, 8]], axis=1).reset_index()
        mean.columns = ['minute', 'genotype', 'animal', 'dist0_mean']
        # mean and std of all animals
        all_mean = mean.groupby(['minute', 'genotype']).mean().drop(mean.columns[2], axis=1)
        all_std = mean.groupby(['minute', 'genotype']).std().drop(mean.columns[2], axis=1)
        big = pd.concat([all_mean['dist0_mean'], all_std['dist0_mean']], axis=1)
        big.columns = ['dist0_mean', 'dist0_std']
        # to list so can use in t test
        means = big['dist0_mean'].tolist()
        stds = big['dist0_std'].tolist()
        
        # KS test calculation for entire dataset
        a = mean.as_matrix(columns=['dist0_mean'])
        al = a[:, 0]
        ks = stats.kstest(al, 'norm', args=(2,))
        # output is KstestResult(statistic=0.13532676198948335, pvalue=9.9675823150846554e-13)
    
        # levene's test for equal variances
        k = mean.reset_index()
        app = k.groupby('genotype')
        app.groups
        gr = app.get_group('gr')
        het = app.get_group('het')
        gr_array = gr.as_matrix(columns=['dist0_mean'])  # 2D array
        het_array = het.as_matrix(columns=['dist0_mean'])  # 2D array
        grr = gr_array[:, 0]  # 1D array
        hett = het_array[:, 0]  # 1D array
        lev = stats.levene(grr, hett)
        if lev[1] < 0.05:
            no = False
        else:
            no = True
        # compute either normal t-test of Welch's t-test assuming non-equal variances, taken from levene's result!
        minute1 = stats.ttest_ind_from_stats(mean1=means[0], std1 = stds[0], nobs1=48, mean2=means[1], std2=stds[1], nobs2=48, equal_var=no)
        minute2 = stats.ttest_ind_from_stats(mean1=means[2], std1 = stds[2], nobs1=48, mean2=means[3], std2=stds[3], nobs2=48, equal_var=no)
        minute3 = stats.ttest_ind_from_stats(mean1=means[4], std1 = stds[4], nobs1=48, mean2=means[5], std2=stds[5], nobs2=48, equal_var=no)
        minute4 = stats.ttest_ind_from_stats(mean1=means[6], std1 = stds[6], nobs1=48, mean2=means[7], std2=stds[7], nobs2=48, equal_var=no)
        minute5 = stats.ttest_ind_from_stats(mean1=means[8], std1 = stds[8], nobs1=48, mean2=means[9], std2=stds[9], nobs2=48, equal_var=no)
        minute6 = stats.ttest_ind_from_stats(mean1=means[10], std1 = stds[10], nobs1=48, mean2=means[11], std2=stds[11], nobs2=48, equal_var=no)
        minute7 = stats.ttest_ind_from_stats(mean1=means[12], std1 = stds[12], nobs1=48, mean2=means[13], std2=stds[13], nobs2=48, equal_var=no)
        minute8 = stats.ttest_ind_from_stats(mean1=means[14], std1 = stds[14], nobs1=48, mean2=means[15], std2=stds[15], nobs2=48, equal_var=no)
        
        # concatenate all results
        ttest_results = [minute1, minute2, minute3, minute4, minute5, minute6,
                         minute7, minute8]
        # filter for p-values only
        p_values = []
        for i in ttest_results:
            p_values.append(i[1])
    
        # separate into gr and het to add to new dataframe
        k = big.reset_index()
        app = k.groupby('genotype')
        app.groups
        gr = app.get_group('gr')
        het = app.get_group('het')
    
        # build new dataframe containing name of experiment, p-values, gr mean, het mean, condition
        new = pd.DataFrame(np.arange(1, 9), columns=['minute'])
    elif phase == 10:
        mean = df.groupby(['minute', '10sphase', 'genotype', 'animal']).mean().drop(df.columns[[2, 4, 5]], axis=1).reset_index()
        mean.columns = ['minute', '10sphase', 'genotype', 'animal', 'dist0_mean']
        
        # mean and std of all animals
        all_mean = mean.groupby(['minute', '10sphase', 'genotype']).mean().drop(mean.columns[3], axis=1)
        all_std = mean.groupby(['minute', '10sphase', 'genotype']).std().drop(mean.columns[3], axis=1)
        big = pd.concat([all_mean['dist0_mean'], all_std['dist0_mean']], axis=1)
        big.columns = ['dist0_mean', 'dist0_std']
        # to list so can use in t test
        means = big['dist0_mean'].tolist()
        stds = big['dist0_std'].tolist()
        
        # KS test calculation for entire dataset
        a = mean.as_matrix(columns=['dist0_mean'])
        al = a[:, 0]
        ks = stats.kstest(al, 'norm', args=(2,))
        # output is KstestResult(statistic=0.13532676198948335, pvalue=9.9675823150846554e-13)
        
        # levene's test for equal variances
        k = mean.reset_index()
        app = k.groupby('genotype')
        app.groups
        gr = app.get_group('gr')
        het = app.get_group('het')
        gr_array = gr.as_matrix(columns=['dist0_mean'])  # 2D array
        het_array = het.as_matrix(columns=['dist0_mean'])  # 2D array
        grr = gr_array[:, 0]  # 1D array
        hett = het_array[:, 0]  # 1D array
        lev = stats.levene(grr, hett)
        if lev[1] < 0.05:
            no = False
        else:
            no = True
        # compute either normal t-test of Welch's t-test assuming non-equal variances, taken from levene's result!
        m1p1 = stats.ttest_ind_from_stats(mean1=means[0], std1 = stds[0], nobs1=48, mean2=means[1], std2=stds[1], nobs2=48, equal_var=no)
        m1p2 = stats.ttest_ind_from_stats(mean1=means[2], std1 = stds[2], nobs1=48, mean2=means[3], std2=stds[3], nobs2=48, equal_var=no)
        m1p3 = stats.ttest_ind_from_stats(mean1=means[4], std1 = stds[4], nobs1=48, mean2=means[5], std2=stds[5], nobs2=48, equal_var=no)
        m1p4 = stats.ttest_ind_from_stats(mean1=means[6], std1 = stds[6], nobs1=48, mean2=means[7], std2=stds[7], nobs2=48, equal_var=no)
        m1p5 = stats.ttest_ind_from_stats(mean1=means[8], std1 = stds[8], nobs1=48, mean2=means[9], std2=stds[9], nobs2=48, equal_var=no)
        m1p6 = stats.ttest_ind_from_stats(mean1=means[10], std1 = stds[10], nobs1=48, mean2=means[11], std2=stds[11], nobs2=48, equal_var=no)
        
        m2p1 = stats.ttest_ind_from_stats(mean1=means[12], std1 = stds[12], nobs1=48, mean2=means[13], std2=stds[13], nobs2=48, equal_var=no)
        m2p2 = stats.ttest_ind_from_stats(mean1=means[14], std1 = stds[14], nobs1=48, mean2=means[15], std2=stds[15], nobs2=48, equal_var=no)
        m2p3 = stats.ttest_ind_from_stats(mean1=means[16], std1 = stds[16], nobs1=48, mean2=means[17], std2=stds[17], nobs2=48, equal_var=no)
        m2p4 = stats.ttest_ind_from_stats(mean1=means[18], std1 = stds[18], nobs1=48, mean2=means[19], std2=stds[19], nobs2=48, equal_var=no)
        m2p5 = stats.ttest_ind_from_stats(mean1=means[20], std1 = stds[20], nobs1=48, mean2=means[21], std2=stds[21], nobs2=48, equal_var=no)
        m2p6 = stats.ttest_ind_from_stats(mean1=means[22], std1 = stds[22], nobs1=48, mean2=means[23], std2=stds[23], nobs2=48, equal_var=no)
        
        m3p1 = stats.ttest_ind_from_stats(mean1=means[24], std1 = stds[24], nobs1=48, mean2=means[25], std2=stds[25], nobs2=48, equal_var=no)
        m3p2 = stats.ttest_ind_from_stats(mean1=means[26], std1 = stds[26], nobs1=48, mean2=means[27], std2=stds[27], nobs2=48, equal_var=no)
        m3p3 = stats.ttest_ind_from_stats(mean1=means[28], std1 = stds[28], nobs1=48, mean2=means[29], std2=stds[29], nobs2=48, equal_var=no)
        m3p4 = stats.ttest_ind_from_stats(mean1=means[30], std1 = stds[30], nobs1=48, mean2=means[31], std2=stds[31], nobs2=48, equal_var=no)
        m3p5 = stats.ttest_ind_from_stats(mean1=means[32], std1 = stds[32], nobs1=48, mean2=means[33], std2=stds[33], nobs2=48, equal_var=no)
        m3p6 = stats.ttest_ind_from_stats(mean1=means[34], std1 = stds[34], nobs1=48, mean2=means[35], std2=stds[35], nobs2=48, equal_var=no)
        
        m4p1 = stats.ttest_ind_from_stats(mean1=means[36], std1 = stds[36], nobs1=48, mean2=means[37], std2=stds[37], nobs2=48, equal_var=no)
        m4p2 = stats.ttest_ind_from_stats(mean1=means[38], std1 = stds[38], nobs1=48, mean2=means[39], std2=stds[39], nobs2=48, equal_var=no)
        m4p3 = stats.ttest_ind_from_stats(mean1=means[40], std1 = stds[40], nobs1=48, mean2=means[41], std2=stds[41], nobs2=48, equal_var=no)
        m4p4 = stats.ttest_ind_from_stats(mean1=means[42], std1 = stds[42], nobs1=48, mean2=means[43], std2=stds[43], nobs2=48, equal_var=no)
        m4p5 = stats.ttest_ind_from_stats(mean1=means[44], std1 = stds[44], nobs1=48, mean2=means[45], std2=stds[45], nobs2=48, equal_var=no)
        m4p6 = stats.ttest_ind_from_stats(mean1=means[46], std1 = stds[46], nobs1=48, mean2=means[47], std2=stds[47], nobs2=48, equal_var=no)
        
        m5p1 = stats.ttest_ind_from_stats(mean1=means[48], std1 = stds[48], nobs1=48, mean2=means[49], std2=stds[49], nobs2=48, equal_var=no)
        m5p2 = stats.ttest_ind_from_stats(mean1=means[50], std1 = stds[50], nobs1=48, mean2=means[51], std2=stds[51], nobs2=48, equal_var=no)
        m5p3 = stats.ttest_ind_from_stats(mean1=means[52], std1 = stds[52], nobs1=48, mean2=means[53], std2=stds[53], nobs2=48, equal_var=no)
        m5p4 = stats.ttest_ind_from_stats(mean1=means[54], std1 = stds[54], nobs1=48, mean2=means[55], std2=stds[55], nobs2=48, equal_var=no)
        m5p5 = stats.ttest_ind_from_stats(mean1=means[56], std1 = stds[56], nobs1=48, mean2=means[57], std2=stds[57], nobs2=48, equal_var=no)
        m5p6 = stats.ttest_ind_from_stats(mean1=means[58], std1 = stds[58], nobs1=48, mean2=means[59], std2=stds[59], nobs2=48, equal_var=no)
        
        m6p1 = stats.ttest_ind_from_stats(mean1=means[60], std1 = stds[60], nobs1=48, mean2=means[61], std2=stds[61], nobs2=48, equal_var=no)
        m6p2 = stats.ttest_ind_from_stats(mean1=means[62], std1 = stds[62], nobs1=48, mean2=means[63], std2=stds[63], nobs2=48, equal_var=no)
        m6p3 = stats.ttest_ind_from_stats(mean1=means[64], std1 = stds[64], nobs1=48, mean2=means[65], std2=stds[65], nobs2=48, equal_var=no)
        m6p4 = stats.ttest_ind_from_stats(mean1=means[66], std1 = stds[66], nobs1=48, mean2=means[67], std2=stds[67], nobs2=48, equal_var=no)
        m6p5 = stats.ttest_ind_from_stats(mean1=means[68], std1 = stds[68], nobs1=48, mean2=means[69], std2=stds[69], nobs2=48, equal_var=no)
        m6p6 = stats.ttest_ind_from_stats(mean1=means[70], std1 = stds[70], nobs1=48, mean2=means[71], std2=stds[71], nobs2=48, equal_var=no)
        
        m7p1 = stats.ttest_ind_from_stats(mean1=means[72], std1 = stds[72], nobs1=48, mean2=means[73], std2=stds[73], nobs2=48, equal_var=no)
        m7p2 = stats.ttest_ind_from_stats(mean1=means[74], std1 = stds[74], nobs1=48, mean2=means[75], std2=stds[75], nobs2=48, equal_var=no)
        m7p3 = stats.ttest_ind_from_stats(mean1=means[76], std1 = stds[76], nobs1=48, mean2=means[77], std2=stds[77], nobs2=48, equal_var=no)
        m7p4 = stats.ttest_ind_from_stats(mean1=means[78], std1 = stds[78], nobs1=48, mean2=means[79], std2=stds[79], nobs2=48, equal_var=no)
        m7p5 = stats.ttest_ind_from_stats(mean1=means[80], std1 = stds[80], nobs1=48, mean2=means[81], std2=stds[81], nobs2=48, equal_var=no)
        m7p6 = stats.ttest_ind_from_stats(mean1=means[82], std1 = stds[82], nobs1=48, mean2=means[83], std2=stds[83], nobs2=48, equal_var=no)
        
        m8p1 = stats.ttest_ind_from_stats(mean1=means[84], std1 = stds[84], nobs1=48, mean2=means[85], std2=stds[85], nobs2=48, equal_var=no)
        m8p2 = stats.ttest_ind_from_stats(mean1=means[86], std1 = stds[86], nobs1=48, mean2=means[87], std2=stds[87], nobs2=48, equal_var=no)
        m8p3 = stats.ttest_ind_from_stats(mean1=means[88], std1 = stds[88], nobs1=48, mean2=means[89], std2=stds[89], nobs2=48, equal_var=no)
        m8p4 = stats.ttest_ind_from_stats(mean1=means[90], std1 = stds[90], nobs1=48, mean2=means[91], std2=stds[91], nobs2=48, equal_var=no)
        m8p5 = stats.ttest_ind_from_stats(mean1=means[92], std1 = stds[92], nobs1=48, mean2=means[93], std2=stds[93], nobs2=48, equal_var=no)
        m8p6 = stats.ttest_ind_from_stats(mean1=means[94], std1 = stds[94], nobs1=48, mean2=means[95], std2=stds[95], nobs2=48, equal_var=no)
        
        m1p1, m1p2, m1p3, m1p4, m1p5, m1p6,
        m2p1, m2p2, m2p3, m2p4, m2p5, m2p6,
        m3p1, m3p2, m3p3, m3p4, m3p5, m3p6,
        m4p1, m4p2, m4p3, m4p4, m4p5, m4p6,
        m5p1, m5p2, m5p3, m5p4, m5p5, m5p6,
        m6p1, m6p2, m6p3, m6p4, m6p5, m6p6,
        m7p1, m7p2, m7p3, m7p4, m7p5, m7p6,
        m8p1, m8p2, m8p3, m8p4, m8p5, m8p6
        # concatenate all results
        ttest_results = [m1p1, m1p2, m1p3, m1p4, m1p5, m1p6,
                         m2p1, m2p2, m2p3, m2p4, m2p5, m2p6,
                         m3p1, m3p2, m3p3, m3p4, m3p5, m3p6,
                         m4p1, m4p2, m4p3, m4p4, m4p5, m4p6,
                         m5p1, m5p2, m5p3, m5p4, m5p5, m5p6,
                         m6p1, m6p2, m6p3, m6p4, m6p5, m6p6,
                         m7p1, m7p2, m7p3, m7p4, m7p5, m7p6,
                         m8p1, m8p2, m8p3, m8p4, m8p5, m8p6]
        # filter for p-values only
        p_values = []
        for i in ttest_results:
            p_values.append(i[1])
        
        # separate into gr and het to add to new dataframe
        k = big.reset_index()
        app = k.groupby('genotype')
        app.groups
        gr = app.get_group('gr')
        het = app.get_group('het')
        
        # build new dataframe containing name of experiment, p-values, gr mean, het mean, condition
        m1 = [1] * 6
        m2 = [2] * 6
        m3 = [3] * 6
        m4 = [4] * 6
        m5 = [5] * 6
        m6 = [6] * 6
        m7 = [7] * 6
        m8 = [8] * 6
        minute = list(it.chain(m1, m2, m3, m4, m5, m6, m7, m8))
        phase = [1, 2, 3, 4, 5, 6] * 8
        new = pd.DataFrame(minute, columns=['minute'])
        new['phase'] = phase
    else:
        pass
    new['plate'] = plate_name
    new['pvalue'] = p_values
    if phase == 60:
        new = new.set_index(['plate', 'minute'])
    elif phase == 10:
        new = new.set_index(['plate', 'minute', 'phase'])
    new['gr'] = gr['dist0_mean'].values
    new['het'] = het['dist0_mean'].values
    condition = []
    for row in new.iterrows():
        data = row[1]
        if data[0] < 0.05:
            if data[1] > data[2]:
                condition.append('GR > Het')
            else:
                condition.append('GR < Het')
        elif data[0] > 0.05:
            condition.append('GR = Het')
        else:
            pass
    new['condition'] = condition
    return new


def ttest_frames(dataframe, plate_name):
    df = dataframe.copy()
    df = df.drop(df.columns[[1, 2, 3, 5, 8]], axis=1)
    df = df.set_index(['minute', 'genotype', 'animal'])
    maxval = df[df['dist0'] == df.groupby(level=[0,1,2])['dist0'].transform(max)].reset_index().sort_values(['minute', 'genotype'], ascending=True).set_index(['minute', 'genotype', 'animal']).groupby(level=[0,1,2]).head(1)
    # mean for 60 sec per animal
    df = maxval.copy().reset_index()
    mean = df.groupby(['minute', 'genotype']).mean().drop(['animal', 'frame'], axis=1)
    std = df.groupby(['minute', 'genotype']).std().drop(['animal', 'frame'], axis=1)
    mod = df.groupby(['minute', 'genotype']).agg(lambda x: stats.mode(x)[0][0]).drop(['animal', 'dist0'], axis=1)
    big = pd.concat([mean['dist0'], std['dist0'], mod['frame']], axis=1)
    big.columns = ['dist0_mean', 'dist0_std', 'frame_mod']
    # to list so can use in t test
    means = big['dist0_mean'].tolist()
    stds = big['dist0_std'].tolist()
    
    # KS test calculation for entire dataset
    a = mean.as_matrix(columns=['dist0'])
    al = a[:, 0]
    ks = stats.kstest(al, 'norm', args=(0.9,))
    # output is KstestResult(statistic=0.13532676198948335, pvalue=9.9675823150846554e-13)

    # levene's test for equal variances
    k = mean.reset_index()
    app = k.groupby('genotype')
    app.groups
    gr = app.get_group('gr')
    het = app.get_group('het')
    gr_array = gr.as_matrix(columns=['dist0'])  # 2D array
    het_array = het.as_matrix(columns=['dist0'])  # 2D array
    grr = gr_array[:, 0]  # 1D array
    hett = het_array[:, 0]  # 1D array
    lev = stats.levene(grr, hett)
    if lev[1] < 0.05:
        no = False
    else:
        no = True
    # compute either normal t-test of Welch's t-test assuming non-equal variances, taken from levene's result!
    minute1 = stats.ttest_ind_from_stats(mean1=means[0], std1 = stds[0], nobs1=48, mean2=means[1], std2=stds[1], nobs2=48, equal_var=no)
    minute2 = stats.ttest_ind_from_stats(mean1=means[2], std1 = stds[2], nobs1=48, mean2=means[3], std2=stds[3], nobs2=48, equal_var=no)
    minute3 = stats.ttest_ind_from_stats(mean1=means[4], std1 = stds[4], nobs1=48, mean2=means[5], std2=stds[5], nobs2=48, equal_var=no)
    minute4 = stats.ttest_ind_from_stats(mean1=means[6], std1 = stds[6], nobs1=48, mean2=means[7], std2=stds[7], nobs2=48, equal_var=no)
    minute5 = stats.ttest_ind_from_stats(mean1=means[8], std1 = stds[8], nobs1=48, mean2=means[9], std2=stds[9], nobs2=48, equal_var=no)
    minute6 = stats.ttest_ind_from_stats(mean1=means[10], std1 = stds[10], nobs1=48, mean2=means[11], std2=stds[11], nobs2=48, equal_var=no)
    minute7 = stats.ttest_ind_from_stats(mean1=means[12], std1 = stds[12], nobs1=48, mean2=means[13], std2=stds[13], nobs2=48, equal_var=no)
    minute8 = stats.ttest_ind_from_stats(mean1=means[14], std1 = stds[14], nobs1=48, mean2=means[15], std2=stds[15], nobs2=48, equal_var=no)
    
    # concatenate all results
    ttest_results = [minute1, minute2, minute3, minute4, minute5, minute6,
                     minute7, minute8]
    # filter for p-values only
    p_values = []
    for i in ttest_results:
        p_values.append(i[1])

    # separate into gr and het to add to new dataframe
    k = big.reset_index()
    app = k.groupby('genotype')
    app.groups
    gr = app.get_group('gr')
    het = app.get_group('het')

    # build new dataframe containing name of experiment, p-values, gr mean, het mean, condition
    new = pd.DataFrame(np.arange(1, 9), columns=['minute'])
    new['plate'] = plate_name
    new['pvalue'] = p_values
    new = new.set_index(['plate', 'minute'])
    new['gr'] = gr['dist0_mean'].values
    new['gr_frame'] = gr['frame_mod'].values
    new['het'] = het['dist0_mean'].values
    new['het_frame'] = het['frame_mod'].values
    condition = []
    for row in new.iterrows():
        data = row[1]
        if data[0] < 0.05:
            if data[1] > data[3]:
                condition.append('GR > Het')
            else:
                condition.append('GR < Het')
        elif data[0] > 0.05:
            condition.append('GR = Het')
        else:
            pass
    delay = []
    for row in new.iterrows():
        data = row[1]
        if data[2] > data[4]:
            delay.append('Het -> GR')
        elif data[2] < data[4]:
            delay.append('GR -> Het')
        else:
            delay.append('n.d.')
    new['condition'] = condition
    new['delay'] = delay
    return new


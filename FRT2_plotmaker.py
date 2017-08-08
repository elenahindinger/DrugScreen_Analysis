# -*- coding: utf-8 -*-
"""
Created on Thu Apr 13 09:12:48 2017

@author: ehindinger
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 19:04:25 2017

@author: ehindinger
"""
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from FRT2_formulas import transform_01


def plotmaker_abs_avg(gr_ctr, het_ctr, gr_com, het_com, conc,
                      drugname, sec_analysed, savename):
    # make copies for safety
    cop1 = gr_ctr.copy(deep=True)
    cop2 = het_ctr.copy(deep=True)
    cop3 = gr_com.copy(deep=True)
    cop4 = het_com.copy(deep=True)
    # make all 0s NaN
    in_gr_ctr = cop1.replace(to_replace=0, value=np.nan)
    in_gr_com = cop3.replace(to_replace=0, value=np.nan)
    in_het_ctr = cop2.replace(to_replace=0, value=np.nan)
    in_het_com = cop4.replace(to_replace=0, value=np.nan)
    # x axis values
    timepoints = np.arange(1, 5)

    # makes general plot outline
    f, ((ax1, ax2, ax3), (ax4, ax5, ax6)) = plt.subplots(2, 3, sharex=True,
                                                         sharey='row',
                                                         figsize=(12, 6))
    plt.subplots_adjust(wspace=0.2, hspace=0.2, top=0.87)
    plt.suptitle('Average distance moved per timepoint at ' + conc +
                 'uM ' + drugname, fontsize='x-large')
    plt.minorticks_off()
    plt.xticks(timepoints)
    plt.margins(0.1, 0.1)
    ax = [ax1, ax2, ax3, ax4, ax5, ax6]
    for i in ax:
        i.tick_params(top='off', right='off')

    # fills ax1: light condition pre-treatment
    ax1.errorbar(timepoints, in_gr_com['L mean 0'], yerr=in_gr_com['L sem 0'],
                 ecolor='brown', color='brown', label='gr drug')
    ax1.errorbar(timepoints, in_gr_ctr['L mean 0'], yerr=in_gr_ctr['L sem 0'],
                 color='goldenrod', ecolor='goldenrod', label='gr ctr')
    ax1.errorbar(timepoints, in_het_com['L mean 0'],
                 yerr=in_het_com['L sem 0'],
                 ecolor='k', color='k', label='het drug')
    ax1.errorbar(timepoints, in_het_ctr['L mean 0'],
                 yerr=in_het_ctr['L sem 0'],
                 color='grey', ecolor='grey', label='het ctr')
    ax1.set_ylabel('Light, Distance (mm)')
    ax1.set_title('Pre-Treatment', fontsize=10)

    # fills ax2: light condition 1h incubation
    ax2.errorbar(timepoints, in_gr_com['L mean 1'], yerr=in_gr_com['L sem 1'],
                 ecolor='brown', color='brown', label='gr drug')
    ax2.errorbar(timepoints, in_gr_ctr['L mean 1'], yerr=in_gr_ctr['L sem 1'],
                 color='goldenrod', ecolor='goldenrod', label='gr ctr')
    ax2.errorbar(timepoints, in_het_com['L mean 1'],
                 yerr=in_het_com['L sem 1'],
                 ecolor='k', color='k', label='het drug')
    ax2.errorbar(timepoints, in_het_ctr['L mean 1'],
                 yerr=in_het_ctr['L sem 1'],
                 color='grey', ecolor='grey', label='het ctr')
    ax2.set_title('Incubation Time 1h', fontsize=10)

    # fills ax3: light condition 24h incubation
    ax3.errorbar(timepoints, in_gr_com['L mean 24'],
                 yerr=in_gr_com['L sem 24'],
                 ecolor='brown', color='brown', label='gr drug')
    ax3.errorbar(timepoints, in_gr_ctr['L mean 24'],
                 yerr=in_gr_ctr['L sem 24'],
                 color='goldenrod', ecolor='goldenrod', label='gr ctr')
    ax3.errorbar(timepoints, in_het_com['L mean 24'],
                 yerr=in_het_com['L sem 24'],
                 ecolor='k', color='k', label='het drug')
    ax3.errorbar(timepoints, in_het_ctr['L mean 24'],
                 yerr=in_het_ctr['L sem 24'],
                 color='grey', ecolor='grey', label='het ctr')
    ax3.set_title('Incubation Time 24h', fontsize=10)
    ax3.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.6, 0.3),
               borderaxespad=0, title=(sec_analysed + ' sec analysed'))

    # fills ax4: dark condition pre-treatment
    ax4.errorbar(timepoints, in_gr_com['D mean 0'], yerr=in_gr_com['D sem 0'],
                 ecolor='brown', color='brown', label='gr drug')
    ax4.errorbar(timepoints, in_gr_ctr['D mean 0'], yerr=in_gr_ctr['D sem 0'],
                 color='goldenrod', ecolor='goldenrod', label='gr ctr')
    ax4.errorbar(timepoints, in_het_com['D mean 0'],
                 yerr=in_het_com['D sem 0'],
                 ecolor='k', color='k', label='het drug')
    ax4.errorbar(timepoints, in_het_ctr['D mean 0'],
                 yerr=in_het_ctr['D sem 0'],
                 color='grey', ecolor='grey', label='het ctr')
    ax4.set_xlabel('Timepoint')
    ax4.set_ylabel('Dark, Distance (mm)')

    # fills ax5: dark condition 1h incubation
    ax5.errorbar(timepoints, in_gr_com['D mean 1'], yerr=in_gr_com['D sem 1'],
                 ecolor='brown', color='brown', label='gr drug')
    ax5.errorbar(timepoints, in_gr_ctr['D mean 1'], yerr=in_gr_ctr['D sem 1'],
                 color='goldenrod', ecolor='goldenrod', label='gr ctr')
    ax5.errorbar(timepoints, in_het_com['D mean 1'],
                 yerr=in_het_com['D sem 1'],
                 ecolor='k', color='k', label='het drug')
    ax5.errorbar(timepoints, in_het_ctr['D mean 1'],
                 yerr=in_het_ctr['D sem 1'],
                 color='grey', ecolor='grey', label='het ctr')
    ax5.set_xlabel('Timepoint')

    # fills ax6: dark condition 24h incubation
    ax6.errorbar(timepoints, in_gr_com['D mean 24'],
                 yerr=in_gr_com['D sem 24'],
                 ecolor='brown', color='brown', label='gr drug')
    ax6.errorbar(timepoints, in_gr_ctr['D mean 24'],
                 yerr=in_gr_ctr['D sem 24'],
                 color='goldenrod', ecolor='goldenrod', label='gr ctr')
    ax6.errorbar(timepoints, in_het_com['D mean 24'],
                 yerr=in_het_com['D sem 24'],
                 ecolor='k', color='k', label='het drug')
    ax6.errorbar(timepoints, in_het_ctr['D mean 24'],
                 yerr=in_het_ctr['D sem 24'],
                 color='grey', ecolor='grey', label='het ctr')
    ax6.set_xlabel('Timepoint')

    # save figure
    f.savefig(savename, bbox_inches='tight')
    plt.close('all')


def plotmaker_seconds(gr_ctr, het_ctr, gr_com, het_com, conc, drugname,
                      savename):
    in_gr_ctr = gr_ctr.copy(deep=True)
    in_het_ctr = het_ctr.copy(deep=True)
    in_gr_com = gr_com.copy(deep=True)
    in_het_com = het_com.copy(deep=True)

    timepoints = np.arange(1, 61)

    f, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9), (ax10, ax11, ax12),
        (ax13, ax14, ax15), (ax16, ax17, ax18), (ax19, ax20, ax21),
        (ax22, ax23, ax24)) = plt.subplots(nrows=8, ncols=3, sharey='all',
                                           figsize=(15, 30))
    plt.subplots_adjust(wspace=0.1, hspace=0.3, top=0.95)
    plt.suptitle('Average distance moved per second at ' + conc +
                 'uM ' + drugname, fontsize='x-large')
    plt.minorticks_off()
    plt.margins(0.01, 0.01)
    ax = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12, ax13,
          ax14, ax15, ax16, ax17, ax18, ax19, ax20,
          ax21, ax22, ax23, ax24]
    for i in ax:
        i.tick_params(top='off', right='off', which='both')
        i.set_xlabel('Seconds')

    # fills ax1: light condition pre-treatment, tp1
    ax1.plot(timepoints, in_gr_com['L tp1 dist 0'], color='brown',
             label='gr drug')
    ax1.plot(timepoints, in_gr_ctr['L tp1 dist 0'], color='goldenrod',
             label='gr ctr')
    ax1.plot(timepoints, in_het_com['L tp1 dist 0'], color='k',
             label='het drug')
    ax1.plot(timepoints, in_het_ctr['L tp1 dist 0'], color='grey',
             label='het ctr')
    ax1.set_ylabel('Distance (mm)')
    ax1.set_title('Pre-Treatment', fontsize=10)

    # fills ax2: light condition 1h incubation, tp1
    ax2.plot(timepoints, in_gr_com['L tp1 dist 1'], color='brown',
             label='gr drug')
    ax2.plot(timepoints, in_gr_ctr['L tp1 dist 1'], color='goldenrod',
             label='gr ctr')
    ax2.plot(timepoints, in_het_com['L tp1 dist 1'], color='k',
             label='het drug')
    ax2.plot(timepoints, in_het_ctr['L tp1 dist 1'], color='grey',
             label='het ctr')
    ax2.set_title('Incubation Time 1h', fontsize=10)

    # fills ax3: light condition 24h incubation, tp1
    ax3.plot(timepoints, in_gr_com['L tp1 dist 24'], color='brown',
             label='gr drug')
    ax3.plot(timepoints, in_gr_ctr['L tp1 dist 24'], color='goldenrod',
             label='gr ctr')
    ax3.plot(timepoints, in_het_com['L tp1 dist 24'], color='k',
             label='het drug')
    ax3.plot(timepoints, in_het_ctr['L tp1 dist 24'], color='grey',
             label='het ctr')
    ax3.set_title('Incubation Time 24h', fontsize=10)
    ax3.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
               borderaxespad=0, title=('TP1, Light Condition'))

    # fills ax4: Dark condition pre-treatment, tp1
    ax4.plot(timepoints, in_gr_com['D tp1 dist 0'], color='brown',
             label='gr drug')
    ax4.plot(timepoints, in_gr_ctr['D tp1 dist 0'], color='goldenrod',
             label='gr ctr')
    ax4.plot(timepoints, in_het_com['D tp1 dist 0'], color='k',
             label='het drug')
    ax4.plot(timepoints, in_het_ctr['D tp1 dist 0'], color='grey',
             label='het ctr')
    ax4.set_ylabel('Distance (mm)')

    # fills ax5: Dark condition 1h incubation, tp1
    ax5.plot(timepoints, in_gr_com['D tp1 dist 1'], color='brown',
             label='gr drug')
    ax5.plot(timepoints, in_gr_ctr['D tp1 dist 1'], color='goldenrod',
             label='gr ctr')
    ax5.plot(timepoints, in_het_com['D tp1 dist 1'], color='k',
             label='het drug')
    ax5.plot(timepoints, in_het_ctr['D tp1 dist 1'], color='grey',
             label='het ctr')

    # fills ax6: Dark condition 24h incubation, tp1
    ax6.plot(timepoints, in_gr_com['D tp1 dist 24'], color='brown',
             label='gr drug')
    ax6.plot(timepoints, in_gr_ctr['D tp1 dist 24'], color='goldenrod',
             label='gr ctr')
    ax6.plot(timepoints, in_het_com['D tp1 dist 24'], color='k',
             label='het drug')
    ax6.plot(timepoints, in_het_ctr['D tp1 dist 24'], color='grey',
             label='het ctr')
    ax6.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
               borderaxespad=0, title=('TP1, Dark Condition'))

    # fills ax7: light condition pre-treatment, tp2
    ax7.plot(timepoints, in_gr_com['L tp2 dist 0'], color='brown',
             label='gr drug')
    ax7.plot(timepoints, in_gr_ctr['L tp2 dist 0'], color='goldenrod',
             label='gr ctr')
    ax7.plot(timepoints, in_het_com['L tp2 dist 0'], color='k',
             label='het drug')
    ax7.plot(timepoints, in_het_ctr['L tp2 dist 0'], color='grey',
             label='het ctr')
    ax7.set_ylabel('Distance (mm)')

    # fills ax8: light condition 1h incubation, tp2
    ax8.plot(timepoints, in_gr_com['L tp2 dist 1'], color='brown',
             label='gr drug')
    ax8.plot(timepoints, in_gr_ctr['L tp2 dist 1'], color='goldenrod',
             label='gr ctr')
    ax8.plot(timepoints, in_het_com['L tp2 dist 1'], color='k',
             label='het drug')
    ax8.plot(timepoints, in_het_ctr['L tp2 dist 1'], color='grey',
             label='het ctr')

    # fills ax9: light condition 24h incubation, tp2
    ax9.plot(timepoints, in_gr_com['L tp2 dist 24'], color='brown',
             label='gr drug')
    ax9.plot(timepoints, in_gr_ctr['L tp2 dist 24'], color='goldenrod',
             label='gr ctr')
    ax9.plot(timepoints, in_het_com['L tp2 dist 24'], color='k',
             label='het drug')
    ax9.plot(timepoints, in_het_ctr['L tp2 dist 24'], color='grey',
             label='het ctr')
    ax9.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
               borderaxespad=0, title=('TP2, Light Condition'))

    # fills ax10: Dark condition pre-treatment, tp2
    ax10.plot(timepoints, in_gr_com['D tp2 dist 0'], color='brown',
              label='gr drug')
    ax10.plot(timepoints, in_gr_ctr['D tp2 dist 0'], color='goldenrod',
              label='gr ctr')
    ax10.plot(timepoints, in_het_com['D tp2 dist 0'], color='k',
              label='het drug')
    ax10.plot(timepoints, in_het_ctr['D tp2 dist 0'], color='grey',
              label='het ctr')
    ax10.set_ylabel('Distance (mm)')

    # fills ax11: Dark condition 1h incubation, tp2
    ax11.plot(timepoints, in_gr_com['D tp2 dist 1'], color='brown',
              label='gr drug')
    ax11.plot(timepoints, in_gr_ctr['D tp2 dist 1'], color='goldenrod',
              label='gr ctr')
    ax11.plot(timepoints, in_het_com['D tp2 dist 1'], color='k',
              label='het drug')
    ax11.plot(timepoints, in_het_ctr['D tp2 dist 1'], color='grey',
              label='het ctr')

    # fills ax12: Dark condition 24h incubation, tp2
    ax12.plot(timepoints, in_gr_com['D tp2 dist 24'], color='brown',
              label='gr drug')
    ax12.plot(timepoints, in_gr_ctr['D tp2 dist 24'], color='goldenrod',
              label='gr ctr')
    ax12.plot(timepoints, in_het_com['D tp2 dist 24'], color='k',
              label='het drug')
    ax12.plot(timepoints, in_het_ctr['D tp2 dist 24'], color='grey',
              label='het ctr')
    ax12.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
                borderaxespad=0, title=('TP2, Dark Condition'))

    # fills ax13: light condition pre-treatment, tp3
    ax13.plot(timepoints, in_gr_com['L tp3 dist 0'], color='brown',
              label='gr drug')
    ax13.plot(timepoints, in_gr_ctr['L tp3 dist 0'], color='goldenrod',
              label='gr ctr')
    ax13.plot(timepoints, in_het_com['L tp3 dist 0'], color='k',
              label='het drug')
    ax13.plot(timepoints, in_het_ctr['L tp3 dist 0'], color='grey',
              label='het ctr')
    ax13.set_ylabel('Distance (mm)')

    # fills ax14: light condition 1h incubation, tp3
    ax14.plot(timepoints, in_gr_com['L tp3 dist 1'], color='brown',
              label='gr drug')
    ax14.plot(timepoints, in_gr_ctr['L tp3 dist 1'], color='goldenrod',
              label='gr ctr')
    ax14.plot(timepoints, in_het_com['L tp3 dist 1'], color='k',
              label='het drug')
    ax14.plot(timepoints, in_het_ctr['L tp3 dist 1'], color='grey',
              label='het ctr')

    # fills ax15: light condition 24h incubation, tp3
    ax15.plot(timepoints, in_gr_com['L tp3 dist 24'], color='brown',
              label='gr drug')
    ax15.plot(timepoints, in_gr_ctr['L tp3 dist 24'], color='goldenrod',
              label='gr ctr')
    ax15.plot(timepoints, in_het_com['L tp3 dist 24'], color='k',
              label='het drug')
    ax15.plot(timepoints, in_het_ctr['L tp3 dist 24'], color='grey',
              label='het ctr')
    ax15.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
                borderaxespad=0, title=('TP3, Light Condition'))

    # fills ax16: Dark condition pre-treatment, tp3
    ax16.plot(timepoints, in_gr_com['D tp3 dist 0'], color='brown',
              label='gr drug')
    ax16.plot(timepoints, in_gr_ctr['D tp3 dist 0'], color='goldenrod',
              label='gr ctr')
    ax16.plot(timepoints, in_het_com['D tp3 dist 0'], color='k',
              label='het drug')
    ax16.plot(timepoints, in_het_ctr['D tp3 dist 0'], color='grey',
              label='het ctr')
    ax16.set_ylabel('Distance (mm)')

    # fills ax17: Dark condition 1h incubation, tp3
    ax17.plot(timepoints, in_gr_com['D tp3 dist 1'], color='brown',
              label='gr drug')
    ax17.plot(timepoints, in_gr_ctr['D tp3 dist 1'], color='goldenrod',
              label='gr ctr')
    ax17.plot(timepoints, in_het_com['D tp3 dist 1'], color='k',
              label='het drug')
    ax17.plot(timepoints, in_het_ctr['D tp3 dist 1'], color='grey',
              label='het ctr')

    # fills ax18: Dark condition 24h incubation, tp3
    ax18.plot(timepoints, in_gr_com['D tp3 dist 24'], color='brown',
              label='gr drug')
    ax18.plot(timepoints, in_gr_ctr['D tp3 dist 24'], color='goldenrod',
              label='gr ctr')
    ax18.plot(timepoints, in_het_com['D tp3 dist 24'], color='k',
              label='het drug')
    ax18.plot(timepoints, in_het_ctr['D tp3 dist 24'], color='grey',
              label='het ctr')
    ax18.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
                borderaxespad=0, title=('TP3, Dark Condition'))

    # fills ax19: light condition pre-treatment, tp4
    ax19.plot(timepoints, in_gr_com['L tp4 dist 0'], color='brown',
              label='gr drug')
    ax19.plot(timepoints, in_gr_ctr['L tp4 dist 0'], color='goldenrod',
              label='gr ctr')
    ax19.plot(timepoints, in_het_com['L tp4 dist 0'], color='k',
              label='het drug')
    ax19.plot(timepoints, in_het_ctr['L tp4 dist 0'], color='grey',
              label='het ctr')
    ax19.set_ylabel('Distance (mm)')

    # fills ax20: light condition 1h incubation, tp4
    ax20.plot(timepoints, in_gr_com['L tp4 dist 1'], color='brown',
              label='gr drug')
    ax20.plot(timepoints, in_gr_ctr['L tp4 dist 1'], color='goldenrod',
              label='gr ctr')
    ax20.plot(timepoints, in_het_com['L tp4 dist 1'], color='k',
              label='het drug')
    ax20.plot(timepoints, in_het_ctr['L tp4 dist 1'], color='grey',
              label='het ctr')

    # fills ax21: light condition 24h incubation, tp4
    ax21.plot(timepoints, in_gr_com['L tp4 dist 24'], color='brown',
              label='gr drug')
    ax21.plot(timepoints, in_gr_ctr['L tp4 dist 24'], color='goldenrod',
              label='gr ctr')
    ax21.plot(timepoints, in_het_com['L tp4 dist 24'], color='k',
              label='het drug')
    ax21.plot(timepoints, in_het_ctr['L tp4 dist 24'], color='grey',
              label='het ctr')
    ax21.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
                borderaxespad=0, title=('TP4, Light Condition'))

    # fills ax22: Dark condition pre-treatment, tp4
    ax22.plot(timepoints, in_gr_com['D tp4 dist 0'], color='brown',
              label='gr drug')
    ax22.plot(timepoints, in_gr_ctr['D tp4 dist 0'], color='goldenrod',
              label='gr ctr')
    ax22.plot(timepoints, in_het_com['D tp4 dist 0'], color='k',
              label='het drug')
    ax22.plot(timepoints, in_het_ctr['D tp4 dist 0'], color='grey',
              label='het ctr')
    ax22.set_ylabel('Distance (mm)')

    # fills ax23: Dark condition 1h incubation, tp4
    ax23.plot(timepoints, in_gr_com['D tp4 dist 1'], color='brown',
              label='gr drug')
    ax23.plot(timepoints, in_gr_ctr['D tp4 dist 1'], color='goldenrod',
              label='gr ctr')
    ax23.plot(timepoints, in_het_com['D tp4 dist 1'], color='k',
              label='het drug')
    ax23.plot(timepoints, in_het_ctr['D tp4 dist 1'], color='grey',
              label='het ctr')

    # fills ax24: Dark condition 24h incubation, tp4
    ax24.plot(timepoints, in_gr_com['D tp4 dist 24'], color='brown',
              label='gr drug')
    ax24.plot(timepoints, in_gr_ctr['D tp4 dist 24'], color='goldenrod',
              label='gr ctr')
    ax24.plot(timepoints, in_het_com['D tp4 dist 24'], color='k',
              label='het drug')
    ax24.plot(timepoints, in_het_ctr['D tp4 dist 24'], color='grey',
              label='het ctr')
    ax24.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
                borderaxespad=0, title=('TP4, Dark Condition'))

    # save figure
    f.savefig(savename, bbox_inches='tight')
    plt.close('all')


def plotmaker_seconds_pooled(gr_ctr_pooled, het_ctr_pooled, gr_ctr, het_ctr,
                             gr_com, het_com, conc, drugname, savename):
    in_gr_ctr = gr_ctr.copy(deep=True)
    in_het_ctr = het_ctr.copy(deep=True)
    in_gr_com = gr_com.copy(deep=True)
    in_het_com = het_com.copy(deep=True)
    in_gr_ctr_pooled = gr_ctr_pooled.copy(deep=True)
    in_het_ctr_pooled = het_ctr_pooled.copy(deep=True)

    timepoints = np.arange(1, 61)

    f, ((ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9), (ax10, ax11, ax12),
        (ax13, ax14, ax15), (ax16, ax17, ax18), (ax19, ax20, ax21),
        (ax22, ax23, ax24)) = plt.subplots(nrows=8, ncols=3, sharey='all',
                                           figsize=(15, 30))
    plt.subplots_adjust(wspace=0.1, hspace=0.2, top=0.95)
    plt.suptitle('Average distance moved per second at ' + conc +
                 'uM ' + drugname, fontsize='x-large')
    plt.minorticks_off()
    plt.margins(0.01, 0.01)
    ax = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10, ax11, ax12, ax13,
          ax14, ax15, ax16, ax17, ax18, ax19, ax20,
          ax21, ax22, ax23, ax24]
    for i in ax:
        i.tick_params(top='off', right='off', which='both')
        i.set_xlabel('Seconds')

    # fills ax1: light condition pre-treatment, tp1
    ax1.plot(timepoints, in_gr_ctr_pooled['L tp1 dist 0'], color='goldenrod',
             label='gr ctr')
    ax1.plot(timepoints, in_het_ctr_pooled['L tp1 dist 0'], color='grey',
             label='het ctr')
    ax1.set_ylabel('Distance (mm)')
    ax1.set_title('Pre-Treatment', fontsize=10)

    # fills ax2: light condition 1h incubation, tp1
    ax2.plot(timepoints, in_gr_com['L tp1 dist 1'], color='brown',
             label='gr drug')
    ax2.plot(timepoints, in_gr_ctr['L tp1 dist 1'], color='goldenrod',
             label='gr ctr')
    ax2.plot(timepoints, in_het_com['L tp1 dist 1'], color='k',
             label='het drug')
    ax2.plot(timepoints, in_het_ctr['L tp1 dist 1'], color='grey',
             label='het ctr')
    ax2.set_title('Incubation Time 1h', fontsize=10)

    # fills ax3: light condition 24h incubation, tp1
    ax3.plot(timepoints, in_gr_com['L tp1 dist 24'], color='brown',
             label='gr drug')
    ax3.plot(timepoints, in_gr_ctr['L tp1 dist 24'], color='goldenrod',
             label='gr ctr')
    ax3.plot(timepoints, in_het_com['L tp1 dist 24'], color='k',
             label='het drug')
    ax3.plot(timepoints, in_het_ctr['L tp1 dist 24'], color='grey',
             label='het ctr')
    ax3.set_title('Incubation Time 24h', fontsize=10)
    ax3.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
               borderaxespad=0, title=('TP1, Light Condition'))

    # fills ax4: Dark condition pre-treatment, tp1
    ax4.plot(timepoints, in_gr_ctr_pooled['D tp1 dist 0'], color='goldenrod',
             label='gr ctr')
    ax4.plot(timepoints, in_het_ctr_pooled['D tp1 dist 0'], color='grey',
             label='het ctr')
    ax4.set_ylabel('Distance (mm)')

    # fills ax5: Dark condition 1h incubation, tp1
    ax5.plot(timepoints, in_gr_com['D tp1 dist 1'], color='brown',
             label='gr drug')
    ax5.plot(timepoints, in_gr_ctr['D tp1 dist 1'], color='goldenrod',
             label='gr ctr')
    ax5.plot(timepoints, in_het_com['D tp1 dist 1'], color='k',
             label='het drug')
    ax5.plot(timepoints, in_het_ctr['D tp1 dist 1'], color='grey',
             label='het ctr')

    # fills ax6: Dark condition 24h incubation, tp1
    ax6.plot(timepoints, in_gr_com['D tp1 dist 24'], color='brown',
             label='gr drug')
    ax6.plot(timepoints, in_gr_ctr['D tp1 dist 24'], color='goldenrod',
             label='gr ctr')
    ax6.plot(timepoints, in_het_com['D tp1 dist 24'], color='k',
             label='het drug')
    ax6.plot(timepoints, in_het_ctr['D tp1 dist 24'], color='grey',
             label='het ctr')
    ax6.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
               borderaxespad=0, title=('TP1, Dark Condition'))

    # fills ax7: light condition pre-treatment, tp2
    ax7.plot(timepoints, in_gr_ctr_pooled['L tp2 dist 0'], color='goldenrod',
             label='gr ctr')
    ax7.plot(timepoints, in_het_ctr_pooled['L tp2 dist 0'], color='grey',
             label='het ctr')
    ax7.set_ylabel('Distance (mm)')

    # fills ax8: light condition 1h incubation, tp2
    ax8.plot(timepoints, in_gr_com['L tp2 dist 1'], color='brown',
             label='gr drug')
    ax8.plot(timepoints, in_gr_ctr['L tp2 dist 1'], color='goldenrod',
             label='gr ctr')
    ax8.plot(timepoints, in_het_com['L tp2 dist 1'], color='k',
             label='het drug')
    ax8.plot(timepoints, in_het_ctr['L tp2 dist 1'], color='grey',
             label='het ctr')

    # fills ax9: light condition 24h incubation, tp2
    ax9.plot(timepoints, in_gr_com['L tp2 dist 24'], color='brown',
             label='gr drug')
    ax9.plot(timepoints, in_gr_ctr['L tp2 dist 24'], color='goldenrod',
             label='gr ctr')
    ax9.plot(timepoints, in_het_com['L tp2 dist 24'], color='k',
             label='het drug')
    ax9.plot(timepoints, in_het_ctr['L tp2 dist 24'], color='grey',
             label='het ctr')
    ax9.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
               borderaxespad=0, title=('TP2, Light Condition'))

    # fills ax10: Dark condition pre-treatment, tp2
    ax10.plot(timepoints, in_gr_ctr_pooled['D tp2 dist 0'], color='goldenrod',
              label='gr ctr')
    ax10.plot(timepoints, in_het_ctr_pooled['D tp2 dist 0'], color='grey',
              label='het ctr')
    ax10.set_ylabel('Distance (mm)')

    # fills ax11: Dark condition 1h incubation, tp2
    ax11.plot(timepoints, in_gr_com['D tp2 dist 1'], color='brown',
              label='gr drug')
    ax11.plot(timepoints, in_gr_ctr['D tp2 dist 1'], color='goldenrod',
              label='gr ctr')
    ax11.plot(timepoints, in_het_com['D tp2 dist 1'], color='k',
              label='het drug')
    ax11.plot(timepoints, in_het_ctr['D tp2 dist 1'], color='grey',
              label='het ctr')

    # fills ax12: Dark condition 24h incubation, tp2
    ax12.plot(timepoints, in_gr_com['D tp2 dist 24'], color='brown',
              label='gr drug')
    ax12.plot(timepoints, in_gr_ctr['D tp2 dist 24'], color='goldenrod',
              label='gr ctr')
    ax12.plot(timepoints, in_het_com['D tp2 dist 24'], color='k',
              label='het drug')
    ax12.plot(timepoints, in_het_ctr['D tp2 dist 24'], color='grey',
              label='het ctr')
    ax12.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
                borderaxespad=0, title=('TP2, Dark Condition'))

    # fills ax13: light condition pre-treatment, tp3
    ax13.plot(timepoints, in_gr_ctr_pooled['L tp3 dist 0'], color='goldenrod',
              label='gr ctr')
    ax13.plot(timepoints, in_het_ctr_pooled['L tp3 dist 0'], color='grey',
              label='het ctr')
    ax13.set_ylabel('Distance (mm)')

    # fills ax14: light condition 1h incubation, tp3
    ax14.plot(timepoints, in_gr_com['L tp3 dist 1'], color='brown',
              label='gr drug')
    ax14.plot(timepoints, in_gr_ctr['L tp3 dist 1'], color='goldenrod',
              label='gr ctr')
    ax14.plot(timepoints, in_het_com['L tp3 dist 1'], color='k',
              label='het drug')
    ax14.plot(timepoints, in_het_ctr['L tp3 dist 1'], color='grey',
              label='het ctr')

    # fills ax15: light condition 24h incubation, tp3
    ax15.plot(timepoints, in_gr_com['L tp3 dist 24'], color='brown',
              label='gr drug')
    ax15.plot(timepoints, in_gr_ctr['L tp3 dist 24'], color='goldenrod',
              label='gr ctr')
    ax15.plot(timepoints, in_het_com['L tp3 dist 24'], color='k',
              label='het drug')
    ax15.plot(timepoints, in_het_ctr['L tp3 dist 24'], color='grey',
              label='het ctr')
    ax15.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
                borderaxespad=0, title=('TP3, Light Condition'))

    # fills ax16: Dark condition pre-treatment, tp3
    ax16.plot(timepoints, in_gr_ctr_pooled['D tp3 dist 0'], color='goldenrod',
              label='gr ctr')
    ax16.plot(timepoints, in_het_ctr_pooled['D tp3 dist 0'], color='grey',
              label='het ctr')
    ax16.set_ylabel('Distance (mm)')

    # fills ax17: Dark condition 1h incubation, tp3
    ax17.plot(timepoints, in_gr_com['D tp3 dist 1'], color='brown',
              label='gr drug')
    ax17.plot(timepoints, in_gr_ctr['D tp3 dist 1'], color='goldenrod',
              label='gr ctr')
    ax17.plot(timepoints, in_het_com['D tp3 dist 1'], color='k',
              label='het drug')
    ax17.plot(timepoints, in_het_ctr['D tp3 dist 1'], color='grey',
              label='het ctr')

    # fills ax18: Dark condition 24h incubation, tp3
    ax18.plot(timepoints, in_gr_com['D tp3 dist 24'], color='brown',
              label='gr drug')
    ax18.plot(timepoints, in_gr_ctr['D tp3 dist 24'], color='goldenrod',
              label='gr ctr')
    ax18.plot(timepoints, in_het_com['D tp3 dist 24'], color='k',
              label='het drug')
    ax18.plot(timepoints, in_het_ctr['D tp3 dist 24'], color='grey',
              label='het ctr')
    ax18.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
                borderaxespad=0, title=('TP3, Dark Condition'))

    # fills ax19: light condition pre-treatment, tp4
    ax19.plot(timepoints, in_gr_ctr_pooled['L tp4 dist 0'], color='goldenrod',
              label='gr ctr')
    ax19.plot(timepoints, in_het_ctr_pooled['L tp4 dist 0'], color='grey',
              label='het ctr')
    ax19.set_ylabel('Distance (mm)')

    # fills ax20: light condition 1h incubation, tp4
    ax20.plot(timepoints, in_gr_com['L tp4 dist 1'], color='brown',
              label='gr drug')
    ax20.plot(timepoints, in_gr_ctr['L tp4 dist 1'], color='goldenrod',
              label='gr ctr')
    ax20.plot(timepoints, in_het_com['L tp4 dist 1'], color='k',
              label='het drug')
    ax20.plot(timepoints, in_het_ctr['L tp4 dist 1'], color='grey',
              label='het ctr')

    # fills ax21: light condition 24h incubation, tp4
    ax21.plot(timepoints, in_gr_com['L tp4 dist 24'], color='brown',
              label='gr drug')
    ax21.plot(timepoints, in_gr_ctr['L tp4 dist 24'], color='goldenrod',
              label='gr ctr')
    ax21.plot(timepoints, in_het_com['L tp4 dist 24'], color='k',
              label='het drug')
    ax21.plot(timepoints, in_het_ctr['L tp4 dist 24'], color='grey',
              label='het ctr')
    ax21.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
                borderaxespad=0, title=('TP4, Light Condition'))

    # fills ax22: Dark condition pre-treatment, tp4
    ax22.plot(timepoints, in_gr_ctr_pooled['D tp4 dist 0'], color='goldenrod',
              label='gr ctr')
    ax22.plot(timepoints, in_het_ctr_pooled['D tp4 dist 0'], color='grey',
              label='het ctr')
    ax22.set_ylabel('Distance (mm)')

    # fills ax23: Dark condition 1h incubation, tp4
    ax23.plot(timepoints, in_gr_com['D tp4 dist 1'], color='brown',
              label='gr drug')
    ax23.plot(timepoints, in_gr_ctr['D tp4 dist 1'], color='goldenrod',
              label='gr ctr')
    ax23.plot(timepoints, in_het_com['D tp4 dist 1'], color='k',
              label='het drug')
    ax23.plot(timepoints, in_het_ctr['D tp4 dist 1'], color='grey',
              label='het ctr')

    # fills ax24: Dark condition 24h incubation, tp4
    ax24.plot(timepoints, in_gr_com['D tp4 dist 24'], color='brown',
              label='gr drug')
    ax24.plot(timepoints, in_gr_ctr['D tp4 dist 24'], color='goldenrod',
              label='gr ctr')
    ax24.plot(timepoints, in_het_com['D tp4 dist 24'], color='k',
              label='het drug')
    ax24.plot(timepoints, in_het_ctr['D tp4 dist 24'], color='grey',
              label='het ctr')
    ax24.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.5, 0.5),
                borderaxespad=0, title=('TP4, Dark Condition'))

    # save figure
    f.savefig(savename, bbox_inches='tight')
    plt.close('all')


def relative_plotmaker(com1, drugname, sec_analysed,
                       tp_analysed, savename):
    # make copy for safety
    cp1 = com1.copy(deep=True)
    # concatenate all absolute dataframe copies
    df = pd.concat([cp1]).set_index(np.arange(1, 2))
    # make all 0s NaN
    rel_com = df.replace(to_replace=0, value=np.nan)
    # x axis values
    timepoints = np.arange(1, 2)

    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True, sharey='all',
                                               figsize=(12, 8))
    plt.suptitle('Average change for ' + drugname + ' relative to DMSO',
                 fontsize='x-large')
    plt.subplots_adjust(wspace=0.2, hspace=0.2, top=0.87)
    plt.minorticks_off()
    plt.xticks(timepoints, ('20'))
    plt.margins(0.1, 0.1)
    ax = [ax1, ax2, ax3, ax4]
    for i in ax:
        i.tick_params(top='off', right='off')

    # fills in subplots for relative
    ax1.plot(timepoints, rel_com['gr L 1'], color='brown', label='gr')
    ax1.plot(timepoints, rel_com['het L 1'], color='k', label='het')
    ax1.set_title('Incubation Time 1h', fontsize=10)
    ax1.set_ylabel('Light, Distance (mm)')

    ax2.plot(timepoints, rel_com['gr L 24'], color='brown', label='gr')
    ax2.plot(timepoints, rel_com['het L 24'], color='k', label='het')
    ax2.set_title('Incubation Time 24h', fontsize=10)
    ax2.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.4, 0.3),
               borderaxespad=0, title=(sec_analysed + ' sec, tp ' + tp_analysed))

    ax3.plot(timepoints, rel_com['gr D 1'], color='brown', label='gr')
    ax3.plot(timepoints, rel_com['het D 1'], color='k', label='het')
    ax3.set_ylabel('Speed (mm/s)')
    ax3.set_xlabel('Concentration (uM)')
    ax3.set_ylabel('Dark, Distance (mm)')

    ax4.plot(timepoints, rel_com['gr D 24'], color='brown', label='gr')
    ax4.plot(timepoints, rel_com['het D 24'], color='k', label='het')
    ax4.set_xlabel('Concentration (uM)')

    f.savefig(savename, bbox_inches='tight')

    plt.close('all')


def absolute_plotmaker(com1, drugname, sec_analysed,
                       tp_analysed, savename):
    # make copy for safety
    cp1 = com1.copy(deep=True)
    # concatenate all absolute dataframe copies
    df = pd.concat([cp1]).set_index(np.arange(1, 2))
    # make all 0s NaN
    abs_com = df.replace(to_replace=0, value=np.nan)
    # x axis values
    timepoints = np.arange(1, 2)

    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True, sharey='all',
                                               figsize=(12, 8))
    plt.suptitle('Average change for ' + drugname + ' compared to DMSO',
                 fontsize='x-large')
    plt.subplots_adjust(wspace=0.2, hspace=0.2, top=0.87)
    plt.minorticks_off()
    plt.xticks(timepoints, ('20'))
    plt.margins(0.1, 0.1)
    ax = [ax1, ax2, ax3, ax4]
    for i in ax:
        i.tick_params(top='off', right='off')

    # fills in subplots for absolute
    ax1.plot(timepoints, abs_com['gr com L 1'], color='brown', label='gr drug')
    ax1.plot(timepoints, abs_com['gr ctr L 1'], color='goldenrod',
             label='gr ctr')
    ax1.plot(timepoints, abs_com['het com L 1'], color='k', label='het drug')
    ax1.plot(timepoints, abs_com['het ctr L 1'], color='grey', label='het ctr')
    ax1.set_title('Incubation Time 1h', fontsize=10)
    ax1.set_ylabel('Light, Distance (mm)')

    ax2.plot(timepoints, abs_com['gr com L 24'], color='brown',
             label='gr drug')
    ax2.plot(timepoints, abs_com['gr ctr L 24'], color='goldenrod',
             label='gr ctr')
    ax2.plot(timepoints, abs_com['het com L 24'], color='k', label='het drug')
    ax2.plot(timepoints, abs_com['het ctr L 24'], color='grey',
             label='het ctr')
    ax2.set_title('Incubation Time 24h', fontsize=10)
    ax2.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.4, 0.3),
               borderaxespad=0, title=(sec_analysed + ' sec, tp ' + tp_analysed))

    ax3.plot(timepoints, abs_com['gr com D 1'], color='brown', label='gr drug')
    ax3.plot(timepoints, abs_com['gr ctr D 1'], color='goldenrod',
             label='gr ctr')
    ax3.plot(timepoints, abs_com['het com D 1'], color='k', label='het drug')
    ax3.plot(timepoints, abs_com['het ctr D 1'], color='grey', label='het ctr')
    ax3.set_xlabel('Concentration (uM)')
    ax3.set_ylabel('Dark, Distance (mm)')

    ax4.plot(timepoints, abs_com['gr com D 24'], color='brown',
             label='gr drug')
    ax4.plot(timepoints, abs_com['gr ctr D 24'], color='goldenrod',
             label='gr ctr')
    ax4.plot(timepoints, abs_com['het com D 24'], color='k', label='het drug')
    ax4.plot(timepoints, abs_com['het ctr D 24'], color='grey',
             label='het ctr')
    ax4.set_xlabel('Concentration (uM)')

    f.savefig(savename, bbox_inches='tight')


def plotmaker_means(gr_ctr, het_ctr, gr_com1, het_com1,
                    drugname, sec_analysed, tp_analysed, savename):
    # make copy for safety
    ctr = transform_01(gr_ctr, het_ctr)
    com1 = transform_01(gr_com1, het_com1)
    # x axis values
    timepoints = np.arange(1, 3)

    f, ((ax1, ax2)) = plt.subplots(1, 2, sharex=True, sharey='all', figsize=(11, 6))
    plt.suptitle('Average distance travelled for ' + drugname + ' compared to DMSO',
                 fontsize='x-large')
    plt.subplots_adjust(wspace=0.2, hspace=0.2, top=0.87)
    plt.minorticks_off()
    plt.xticks(timepoints, ('0', '1', '24'))
    ax = [ax1, ax2]
    for i in ax:
        i.tick_params(top='off', right='off')
    # subplot 1 light, 0.1uM
    ax1.bar(timepoints-0.3, com1['gr L mean'], 0.2, yerr=com1['gr L sem'],
            ecolor='k', color='brown', label='gr drug')
    ax1.bar(timepoints-0.1, ctr['gr L mean'], 0.2, yerr=ctr['gr L sem'],
            ecolor='k', color='goldenrod', label='gr ctr')
    ax1.bar(timepoints+0.1, com1['het L mean'], 0.2, yerr=com1['het L sem'],
            ecolor='k', color='k', label='het drug')
    ax1.bar(timepoints+0.3, ctr['het L mean'], 0.2, yerr=ctr['het L sem'],
            ecolor='k', color='grey', label='het ctr')
    ax1.set_ylabel('Distance (mm)', fontsize=10)
    ax1.set_title('Light Condition', fontsize=10)

    # subplot 6 light, 0.1uM
    ax2.bar(timepoints-0.3, com1['gr D mean'], 0.2, yerr=com1['gr D sem'],
            ecolor='k', color='brown', label='gr drug')
    ax2.bar(timepoints-0.1, ctr['gr D mean'], 0.2, yerr=ctr['gr D sem'],
            ecolor='k', color='goldenrod', label='gr ctr')
    ax2.bar(timepoints+0.1, com1['het D mean'], 0.2, yerr=com1['het D sem'],
            ecolor='k', color='k', label='het drug')
    ax2.bar(timepoints+0.3, ctr['het D mean'], 0.2, yerr=ctr['het D sem'],
            ecolor='k', color='grey', label='het ctr')
    ax2.set_title('Dark Condition', fontsize=10)
    ax2.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.3, 0.5),
               borderaxespad=0, title=('20 uM'))
    # save figure
    f.savefig(savename, bbox_inches='tight')
    plt.close('all')


def group_trace_graph(gr, het, new_path):
    timepoints = np.arange(9000, 23400)

    f, (ax1, ax2) = plt.subplots(2, 1, figsize=(30, 20), sharex=True,
                                 sharey=True)

    plt.subplots_adjust(wspace=0.2, hspace=0.2, top=0.87)
    plt.suptitle('Distance moved per frame pre-treatment', fontsize='x-large')
    plt.minorticks_off()
    plt.xticks(np.arange(min(timepoints), max(timepoints)+1, 300.0),
               rotation=90, fontsize=10)
    ax = [ax1, ax2]
    for i in ax:
        i.tick_params(top='off', right='off')
    ax1.scatter(timepoints, gr['dist 0'], color='brown', label='gr control',
                s=4)
    ax1.set_ylabel('Distance (mm)', fontsize=10)
    ax1.set_xlabel('Frames', fontsize=10)

    ax1.legend(loc=1, fontsize='x-small', bbox_to_anchor=(1, 1),
               borderaxespad=0, title=('n=48'))
    ax2.scatter(timepoints, het['dist 0'], color='k', label='het control', s=4)
    ax2.set_ylabel('Distance (mm)', fontsize=10)
    ax2.set_xlabel('Frames', fontsize=10)

    ax2.legend(loc=1, fontsize='x-small', bbox_to_anchor=(1, 1),
               borderaxespad=0, title=('n=48'))
    f.savefig(new_path, bbox_inches='tight')
    plt.close('all')


def group_trace_graph_seconds(gr, het, new_path):
    timepoints = np.arange(9000, 23400, 30)
    l1 = 9000
    d1 = l1 + 1800
    l2 = d1 + 1800
    d2 = l2 + 1800
    l3 = d2 + 1800
    d3 = l3 + 1800
    l4 = d3 + 1800
    d4 = l4 + 1800
    stop = d4 + 1800

    f, (ax1) = plt.subplots(1, 1, figsize=(20, 10))
    plt.subplots_adjust(wspace=0.2, hspace=0.2, top=0.87)
    plt.suptitle('Distance moved per second', fontsize='x-large')
    plt.minorticks_off()
    plt.xticks(np.arange(min(timepoints), max(timepoints)+1, 300.0),
               rotation=90, fontsize=8)
    ax = [ax1]
    for i in ax:
        i.tick_params(top='off', right='off')
    ax1.plot(timepoints, gr['dist 0'], color='brown', label='gr control')
    ax1.plot(timepoints, het['dist 0'], color='k', label='het control')
    ax1.set_ylabel('Distance (mm)', fontsize=10)
    ax1.set_xlabel('Seconds', fontsize=10)
    ax1.axvspan(l1, d1, color='lightyellow')
    ax1.axvspan(l2, d2, color='lightyellow')
    ax1.axvspan(l3, d3, color='lightyellow')
    ax1.axvspan(l4, d4, color='lightyellow')
    ax1.axvspan(d1, l2, color='lightgrey')
    ax1.axvspan(d2, l3, color='lightgrey')
    ax1.axvspan(d3, l4, color='lightgrey')
    ax1.axvspan(d4, stop, color='lightgrey')
    ax1.legend(loc=1, fontsize='x-small', bbox_to_anchor=(1, 1),
               borderaxespad=0, title=('n=48'))

    f.savefig(new_path, bbox_inches='tight')
    plt.close('all')

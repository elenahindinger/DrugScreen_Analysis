# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 16:55:38 2017

@author: ehindinger
"""

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


def relative_plotmaker(com, drugname, sec_analysed, tp_analysed, savename):
    # make copy for safety
    df = com.copy(deep=True)
    # make all 0s NaN
    rel_com = df.replace(to_replace=0, value=np.nan)
    # x axis values
    timepoints = np.arange(1, 8)

    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True, sharey='all',
                                               figsize=(12, 8))
    plt.suptitle('Average change for ' + drugname + ' relative to DMSO',
                 fontsize='x-large')
    plt.subplots_adjust(wspace=0.2, hspace=0.2, top=0.87)
    plt.minorticks_off()
    plt.xticks(timepoints, ('0.1', '1', '7', '10', '20', '50', '100'))
    plt.margins(0.1, 0.1)
    ax = [ax1, ax2, ax3, ax4]
    for i in ax:
        i.tick_params(top='off', right='off')

    # light 1h
    ax1.plot(timepoints, rel_com['gr L 1'], color='brown', label='gr')
    ax1.plot(timepoints, rel_com['het L 1'], color='k', label='het')
    ax1.scatter(timepoints, rel_com['gr L 1'], color='brown', marker='s',
                label='_a')
    ax1.scatter(timepoints, rel_com['het L 1'], color='k', marker='s',
                label='_a')
    ax1.set_title('Incubation Time 1h', fontsize=10)
    ax1.set_ylabel('Light, Distance (mm)')

    # light 24h
    ax2.plot(timepoints, rel_com['gr L 24'], color='brown', label='gr')
    ax2.plot(timepoints, rel_com['het L 24'], color='k', label='het')
    ax2.scatter(timepoints, rel_com['gr L 24'], color='brown', marker='s',
                label='_a')
    ax2.scatter(timepoints, rel_com['het L 24'], color='k', marker='s',
                label='_a')
    ax2.set_title('Incubation Time 24h', fontsize=10)
    ax2.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.4, 0.3),
               borderaxespad=0, title=(sec_analysed + ' sec, tp ' + tp_analysed))

    # dark 1h
    ax3.plot(timepoints, rel_com['gr D 1'], color='brown', label='gr')
    ax3.plot(timepoints, rel_com['het D 1'], color='k', label='het')
    ax3.scatter(timepoints, rel_com['gr D 1'], color='brown', marker='s',
                label='_a')
    ax3.scatter(timepoints, rel_com['het D 1'], color='k', marker='s',
                label='_a')
    ax3.set_ylabel('Speed (mm/s)')
    ax3.set_xlabel('Concentration (uM)')
    ax3.set_ylabel('Dark, Distance (mm)')

    # dark 24h
    ax4.plot(timepoints, rel_com['gr D 24'], color='brown', label='gr')
    ax4.plot(timepoints, rel_com['het D 24'], color='k', label='het')
    ax4.scatter(timepoints, rel_com['gr D 24'], color='brown', marker='s',
                label='_a')
    ax4.scatter(timepoints, rel_com['het D 24'], color='k', marker='s',
                label='_a')
    ax4.set_xlabel('Concentration (uM)')

    f.savefig(savename, bbox_inches='tight')
    plt.close('all')


def absolute_plotmaker(com, drugname, sec_analysed,
                       tp_analysed, savename):
    # make copy for safety
    df = com.copy(deep=True)
    # make all 0s NaN
    abs_com = df.replace(to_replace=0, value=np.nan)
    # x axis values
    timepoints = np.arange(1, 8)

    f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True, sharey='all',
                                               figsize=(12, 8))
    plt.suptitle('Average change for ' + drugname + ' compared to DMSO',
                 fontsize='x-large')
    plt.subplots_adjust(wspace=0.2, hspace=0.2, top=0.87)
    plt.minorticks_off()
    plt.xticks(timepoints, ('0.1', '1', '7', '10', '20', '50', '100'))
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
    ax1.scatter(timepoints, abs_com['gr com L 1'], color='brown', marker='s',
                label='_a')
    ax1.scatter(timepoints, abs_com['gr ctr L 1'], color='goldenrod',
                marker='s', label='_a')
    ax1.scatter(timepoints, abs_com['het com L 1'], color='k', marker='s',
                label='_a')
    ax1.scatter(timepoints, abs_com['het ctr L 1'], color='grey', marker='s',
                label='_a')
    ax1.set_title('Incubation Time 1h', fontsize=10)
    ax1.set_ylabel('Light, Distance (mm)')

    ax2.plot(timepoints, abs_com['gr com L 24'], color='brown',
             label='gr drug')
    ax2.plot(timepoints, abs_com['gr ctr L 24'], color='goldenrod',
             label='gr ctr')
    ax2.plot(timepoints, abs_com['het com L 24'], color='k', label='het drug')
    ax2.plot(timepoints, abs_com['het ctr L 24'], color='grey',
             label='het ctr')
    ax2.scatter(timepoints, abs_com['gr com L 24'], color='brown', marker='s',
                label='_a')
    ax2.scatter(timepoints, abs_com['gr ctr L 24'], color='goldenrod',
                marker='s', label='_a')
    ax2.scatter(timepoints, abs_com['het com L 24'], color='k', marker='s',
                label='_a')
    ax2.scatter(timepoints, abs_com['het ctr L 24'], color='grey',
                marker='s', label='_a')
    ax2.set_title('Incubation Time 24h', fontsize=10)
    ax2.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.4, 0.3),
               borderaxespad=0, title=(sec_analysed + ' sec, tp ' + tp_analysed))

    ax3.plot(timepoints, abs_com['gr com D 1'], color='brown', label='gr drug')
    ax3.plot(timepoints, abs_com['gr ctr D 1'], color='goldenrod',
             label='gr ctr')
    ax3.plot(timepoints, abs_com['het com D 1'], color='k', label='het drug')
    ax3.plot(timepoints, abs_com['het ctr D 1'], color='grey', label='het ctr')
    ax3.scatter(timepoints, abs_com['gr com D 1'], color='brown', marker='s',
                label='_a')
    ax3.scatter(timepoints, abs_com['gr ctr D 1'], color='goldenrod',
                marker='s', label='_a')
    ax3.scatter(timepoints, abs_com['het com D 1'], color='k', marker='s',
                label='_a')
    ax3.scatter(timepoints, abs_com['het ctr D 1'], color='grey', marker='s',
                label='_a')
    ax3.set_xlabel('Concentration (uM)')
    ax3.set_ylabel('Dark, Distance (mm)')

    ax4.plot(timepoints, abs_com['gr com D 24'], color='brown',
             label='gr drug')
    ax4.plot(timepoints, abs_com['gr ctr D 24'], color='goldenrod',
             label='gr ctr')
    ax4.plot(timepoints, abs_com['het com D 24'], color='k', label='het drug')
    ax4.plot(timepoints, abs_com['het ctr D 24'], color='grey',
             label='het ctr')
    ax4.scatter(timepoints, abs_com['gr com D 24'], color='brown',
                marker='s', label='_a')
    ax4.scatter(timepoints, abs_com['gr ctr D 24'], color='goldenrod',
                marker='s', label='_a')
    ax4.scatter(timepoints, abs_com['het com D 24'], color='k', marker='s',
                label='_a')
    ax4.scatter(timepoints, abs_com['het ctr D 24'], color='grey',
                marker='s', label='_a')
    ax4.set_xlabel('Concentration (uM)')

    f.savefig(savename, bbox_inches='tight')
    plt.close('all')


def transform(old):
    copied = old.copy(deep=True)
    df = copied.mean().to_frame().T
    result = pd.concat([pd.concat([df['gr ctr D avg 0'],
                                   df['gr ctr D avg 1'],
                                   df['gr ctr D avg 24']]),
                        pd.concat([df['gr ctr D sem 0'],
                                   df['gr ctr D sem 1'],
                                   df['gr ctr D sem 24']]),
                        pd.concat([df['het ctr D avg 0'],
                                   df['het ctr D avg 1'],
                                   df['het ctr D avg 24']]),
                        pd.concat([df['het ctr D sem 0'],
                                   df['het ctr D sem 1'],
                                   df['het ctr D sem 24']]),
                        pd.concat([df['gr com D avg 0'],
                                   df['gr com D avg 1'],
                                   df['gr com D avg 24']]),
                        pd.concat([df['gr com D sem 0'],
                                   df['gr com D sem 1'],
                                   df['gr com D sem 24']]),
                        pd.concat([df['het com D avg 0'],
                                   df['het com D avg 1'],
                                   df['het com D avg 24']]),
                        pd.concat([df['het com D sem 0'],
                                   df['het com D sem 1'],
                                   df['het com D sem 24']]),
                        pd.concat([df['gr ctr L avg 0'],
                                   df['gr ctr L avg 1'],
                                   df['gr ctr L avg 24']]),
                        pd.concat([df['gr ctr L sem 0'],
                                   df['gr ctr L sem 1'],
                                   df['gr ctr L sem 24']]),
                        pd.concat([df['het ctr L avg 0'],
                                   df['het ctr L avg 1'],
                                   df['het ctr L avg 24']]),
                        pd.concat([df['het ctr L sem 0'],
                                   df['het ctr L sem 1'],
                                   df['het ctr L sem 24']]),
                        pd.concat([df['gr com L avg 0'],
                                   df['gr com L avg 1'],
                                   df['gr com L avg 24']]),
                        pd.concat([df['gr com L sem 0'],
                                   df['gr com L sem 1'],
                                   df['gr com L sem 24']]),
                        pd.concat([df['het com L avg 0'],
                                   df['het com L avg 1'],
                                   df['het com L avg 24']]),
                        pd.concat([df['het com L sem 0'],
                                   df['het com L sem 1'],
                                   df['het com L sem 24']])], axis=1)
    result.columns = ['gr ctr D mean', 'gr ctr D sem', 'het ctr D mean',
                      'het ctr D sem', 'gr com D mean', 'gr com D sem',
                      'het com D mean', 'het com D sem',  'gr ctr L mean',
                      'gr ctr L sem', 'het ctr L mean', 'het ctr L sem',
                      'gr com L mean', 'gr com L sem', 'het com L mean',
                      'het com L sem']
    new = result.set_index(np.arange(1, 4))
    return new


def plotmaker_means(in1, in2, in3, in4, in5, in6, in7, drugname,
                    sec_analysed, tp_analysed, savename):
    # make copy for safety
    com1 = transform(in1)
    com2 = transform(in2)
    com3 = transform(in3)
    com4 = transform(in4)
    com5 = transform(in5)
    com6 = transform(in6)
    com7 = transform(in7)

    # x axis values
    timepoints = np.arange(1, 4)

    f, ((ax1, ax2, ax3, ax4, ax5, ax6, ax7),
        (ax8, ax9, ax10, ax11, ax12, ax13, ax14)) = plt.subplots(2, 7,
                                                                 sharex=True,
                                                                 sharey='all',
                                                                 figsize=(14, 6))
    plt.suptitle('Average distance travelled for ' + drugname + ' compared to DMSO',
                 fontsize='x-large')
    plt.subplots_adjust(wspace=0.2, hspace=0.2, top=0.87)
    plt.minorticks_off()
    plt.xticks(timepoints, ('0', '1', '24'))
    ax = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10]
    for i in ax:
        i.tick_params(top='off', right='off')

    # subplot 1 light, 0.1uM
    ax1.bar(timepoints-0.3, com1['gr com L mean'], 0.2,
            yerr=com1['gr com L sem'], ecolor='k', color='brown',
            label='gr drug')
    ax1.bar(timepoints-0.1, com1['gr ctr L mean'], 0.2,
            yerr=com1['gr ctr L sem'], ecolor='k', color='goldenrod',
            label='gr ctr')
    ax1.bar(timepoints+0.1, com1['het com L mean'], 0.2,
            yerr=com1['het com L sem'], ecolor='k', color='k',
            label='het drug')
    ax1.bar(timepoints+0.3, com1['het ctr L mean'], 0.2,
            yerr=com1['het ctr L sem'], ecolor='k', color='grey',
            label='het ctr')
    ax1.set_ylabel('Light, Distance (mm)', fontsize=10)
    ax1.set_title('0.1 uM', fontsize=10)

    # subplot 2 light, 1uM
    ax2.bar(timepoints-0.3, com2['gr com L mean'], 0.2,
            yerr=com2['gr com L sem'], ecolor='k', color='brown',
            label='gr drug')
    ax2.bar(timepoints-0.1, com2['gr ctr L mean'], 0.2,
            yerr=com2['gr ctr L sem'], ecolor='k', color='goldenrod',
            label='gr ctr')
    ax2.bar(timepoints+0.1, com2['het com L mean'], 0.2,
            yerr=com2['het com L sem'], ecolor='k', color='k',
            label='het drug')
    ax2.bar(timepoints+0.3, com2['het ctr L mean'], 0.2,
            yerr=com2['het ctr L sem'], ecolor='k', color='grey',
            label='het ctr')
    ax2.set_title('1 uM', fontsize=10)

    # subplot 3 light, 7uM
    ax3.bar(timepoints-0.3, com3['gr com L mean'], 0.2,
            yerr=com3['gr com L sem'], ecolor='k', color='brown',
            label='gr drug')
    ax3.bar(timepoints-0.1, com3['gr ctr L mean'], 0.2,
            yerr=com3['gr ctr L sem'], ecolor='k', color='goldenrod',
            label='gr ctr')
    ax3.bar(timepoints+0.1, com3['het com L mean'], 0.2,
            yerr=com3['het com L sem'], ecolor='k', color='k',
            label='het drug')
    ax3.bar(timepoints+0.3, com3['het ctr L mean'], 0.2,
            yerr=com3['het ctr L sem'], ecolor='k', color='grey',
            label='het ctr')
    ax3.set_title('7 uM', fontsize=10)

    # subplot 4 light 10uM
    ax4.bar(timepoints-0.3, com4['gr com L mean'], 0.2,
            yerr=com4['gr com L sem'], ecolor='k', color='brown',
            label='gr drug')
    ax4.bar(timepoints-0.1, com4['gr ctr L mean'], 0.2,
            yerr=com4['gr ctr L sem'], ecolor='k', color='goldenrod',
            label='gr ctr')
    ax4.bar(timepoints+0.1, com4['het com L mean'], 0.2,
            yerr=com4['het com L sem'], ecolor='k', color='k',
            label='het drug')
    ax4.bar(timepoints+0.3, com4['het ctr L mean'], 0.2,
            yerr=com4['het ctr L sem'], ecolor='k', color='grey',
            label='het ctr')
    ax4.set_title('10 uM', fontsize=10)

    # subplot 5 light 20uM
    ax5.bar(timepoints-0.3, com5['gr com L mean'], 0.2,
            yerr=com5['gr com L sem'], ecolor='k', color='brown',
            label='gr drug')
    ax5.bar(timepoints-0.1, com5['gr ctr L mean'], 0.2,
            yerr=com5['gr ctr L sem'], ecolor='k', color='goldenrod',
            label='gr ctr')
    ax5.bar(timepoints+0.1, com5['het com L mean'], 0.2,
            yerr=com5['het com L sem'], ecolor='k', color='k',
            label='het drug')
    ax5.bar(timepoints+0.3, com5['het ctr L mean'], 0.2,
            yerr=com5['het ctr L sem'], ecolor='k', color='grey',
            label='het ctr')
    ax5.set_title('20 uM', fontsize=10)

    # subplot 6 light 50uM
    ax6.bar(timepoints-0.3, com6['gr com L mean'], 0.2,
            yerr=com6['gr com L sem'], ecolor='k', color='brown',
            label='gr drug')
    ax6.bar(timepoints-0.1, com6['gr ctr L mean'], 0.2,
            yerr=com6['gr ctr L sem'], ecolor='k', color='goldenrod',
            label='gr ctr')
    ax6.bar(timepoints+0.1, com6['het com L mean'], 0.2,
            yerr=com6['het com L sem'], ecolor='k', color='k',
            label='het drug')
    ax6.bar(timepoints+0.3, com6['het ctr L mean'], 0.2,
            yerr=com6['het ctr L sem'], ecolor='k', color='grey',
            label='het ctr')
    ax6.set_title('50 uM', fontsize=10)

    # subplot 7 light 100uM
    ax7.bar(timepoints-0.3, com7['gr com L mean'], 0.2,
            yerr=com7['gr com L sem'], ecolor='k', color='brown',
            label='gr drug')
    ax7.bar(timepoints-0.1, com7['gr ctr L mean'], 0.2,
            yerr=com7['gr ctr L sem'], ecolor='k', color='goldenrod',
            label='gr ctr')
    ax7.bar(timepoints+0.1, com7['het com L mean'], 0.2,
            yerr=com7['het com L sem'], ecolor='k', color='k',
            label='het drug')
    ax7.bar(timepoints+0.3, com7['het ctr L mean'], 0.2,
            yerr=com7['het ctr L sem'], ecolor='k', color='grey',
            label='het ctr')
    ax7.set_title('100 uM', fontsize=10)
    ax7.legend(loc=5, fontsize='x-small', bbox_to_anchor=(2.2, 0.3),
               borderaxespad=0, title=(sec_analysed + ' sec, tp ' + tp_analysed))

    # subplot 8 dark, 0.1uM
    ax8.bar(timepoints-0.3, com1['gr com D mean'], 0.2,
            yerr=com1['gr com D sem'], ecolor='k', color='brown',
            label='gr drug')
    ax8.bar(timepoints-0.1, com1['gr ctr D mean'], 0.2,
            yerr=com1['gr ctr D sem'], ecolor='k', color='goldenrod',
            label='gr ctr')
    ax8.bar(timepoints+0.1, com1['het com D mean'], 0.2,
            yerr=com1['het com D sem'], ecolor='k', color='k',
            label='het drug')
    ax8.bar(timepoints+0.3, com1['het ctr D mean'], 0.2,
            yerr=com1['het ctr D sem'], ecolor='k', color='grey',
            label='het ctr')
    ax8.set_ylabel('Dark, Distance (mm)', fontsize=10)

    # subplot 9 dark, 1uM
    ax9.bar(timepoints-0.3, com2['gr com D mean'], 0.2,
            yerr=com2['gr com D sem'], ecolor='k', color='brown',
            label='gr drug')
    ax9.bar(timepoints-0.1, com2['gr ctr D mean'], 0.2,
            yerr=com2['gr ctr D sem'], ecolor='k', color='goldenrod',
            label='gr ctr')
    ax9.bar(timepoints+0.1, com2['het com D mean'], 0.2,
            yerr=com2['het com D sem'], ecolor='k', color='k',
            label='het drug')
    ax9.bar(timepoints+0.3, com2['het ctr D mean'], 0.2,
            yerr=com2['het ctr D sem'], ecolor='k', color='grey',
            label='het ctr')

    # subplot 10 dark, 7uM
    ax10.bar(timepoints-0.3, com3['gr com D mean'], 0.2,
             yerr=com3['gr com D sem'], ecolor='k', color='brown',
             label='gr drug')
    ax10.bar(timepoints-0.1, com3['gr ctr D mean'], 0.2,
             yerr=com3['gr ctr D sem'], ecolor='k', color='goldenrod',
             label='gr ctr')
    ax10.bar(timepoints+0.1, com3['het com D mean'], 0.2,
             yerr=com3['het com D sem'], ecolor='k', color='k',
             label='het drug')
    ax10.bar(timepoints+0.3, com3['het ctr D mean'], 0.2,
             yerr=com3['het ctr D sem'], ecolor='k', color='grey',
             label='het ctr')

    # subplot 11 dark 10uM
    ax11.bar(timepoints-0.3, com4['gr com D mean'], 0.2,
             yerr=com4['gr com D sem'], ecolor='k', color='brown',
             label='gr drug')
    ax11.bar(timepoints-0.1, com4['gr ctr D mean'], 0.2,
             yerr=com4['gr ctr D sem'], ecolor='k', color='goldenrod',
             label='gr ctr')
    ax11.bar(timepoints+0.1, com4['het com D mean'], 0.2,
             yerr=com4['het com D sem'], ecolor='k', color='k',
             label='het drug')
    ax11.bar(timepoints+0.3, com4['het ctr D mean'], 0.2,
             yerr=com4['het ctr D sem'], ecolor='k', color='grey',
             label='het ctr')
    ax11.set_xlabel('Incubation Time (h)', fontsize=10)

    # subplot 12 dark 20uM
    ax12.bar(timepoints-0.3, com5['gr com D mean'], 0.2,
             yerr=com5['gr com D sem'], ecolor='k', color='brown',
             label='gr drug')
    ax12.bar(timepoints-0.1, com5['gr ctr D mean'], 0.2,
             yerr=com5['gr ctr D sem'], ecolor='k', color='goldenrod',
             label='gr ctr')
    ax12.bar(timepoints+0.1, com5['het com D mean'], 0.2,
             yerr=com5['het com D sem'], ecolor='k', color='k',
             label='het drug')
    ax12.bar(timepoints+0.3, com5['het ctr D mean'], 0.2,
             yerr=com5['het ctr D sem'], ecolor='k', color='grey',
             label='het ctr')

    # subplot 13 dark 50uM
    ax13.bar(timepoints-0.3, com6['gr com D mean'], 0.2,
             yerr=com6['gr com D sem'], ecolor='k', color='brown',
             label='gr drug')
    ax13.bar(timepoints-0.1, com6['gr ctr D mean'], 0.2,
             yerr=com6['gr ctr D sem'], ecolor='k', color='goldenrod',
             label='gr ctr')
    ax13.bar(timepoints+0.1, com6['het com D mean'], 0.2,
             yerr=com6['het com D sem'], ecolor='k', color='k',
             label='het drug')
    ax13.bar(timepoints+0.3, com6['het ctr D mean'], 0.2,
             yerr=com6['het ctr D sem'], ecolor='k', color='grey',
             label='het ctr')

    # subplot 14 dark 100uM
    ax14.bar(timepoints-0.3, com7['gr com D mean'], 0.2,
             yerr=com7['gr com D sem'], ecolor='k', color='brown',
             label='gr drug')
    ax14.bar(timepoints-0.1, com7['gr ctr D mean'], 0.2,
             yerr=com7['gr ctr D sem'], ecolor='k', color='goldenrod',
             label='gr ctr')
    ax14.bar(timepoints+0.1, com7['het com D mean'], 0.2,
             yerr=com7['het com D sem'], ecolor='k', color='k',
             label='het drug')
    ax14.bar(timepoints+0.3, com7['het ctr D mean'], 0.2,
             yerr=com7['het ctr D sem'], ecolor='k', color='grey',
             label='het ctr')

    # save figure
    f.savefig(savename, bbox_inches='tight')
    plt.close('all')

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:24:57 2017

@author: ehindinger
"""

import pandas as pd
import numpy as np
import seaborn as sns
import os
import itertools as it
from natsort import natsorted
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import random
from scipy import stats


def setup(ax):
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5, pad=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.tick_params(which='both', right='off')
    ax.yaxis.set_ticks_position('left')
    ax.tick_params(which='major', width=1.00, length=5, pad=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.xaxis.labelpad = 40
    ax.yaxis.labelpad = 40


def trace_plot(dataframe, outdir, name, conc, n=48):
    df = dataframe.copy(deep=True)
    df['axis'] = (df.frame - df.frame.iat[0])/ np.timedelta64(1, 's')
    ptitle = 'n = ' + str(n)
    sns.set_style('white')
    f, (ax1) = plt.subplots(1, 1, figsize=(15, 10))
    ax1 = sns.tsplot(data=df, time='axis', value='dist0', unit='animal',
                 condition='genotype', ax=ax1)
    ax1.set_xlabel('Seconds', fontsize=18)
    ax1.set_ylabel('Distance (mm)', fontsize=18)
    plt.suptitle('Average total distance travelled per second at baseline', fontsize='xx-large')
    lg = ax1.legend(loc=5, fontsize='x-large', bbox_to_anchor=(1.15, 0.5),
               borderaxespad=0, title=ptitle, frameon=True)
    plt.setp(lg.get_title(),fontsize='xx-large')
    setup(ax1)
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(60))
    ax1.xaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
    mi, ma = ax1.get_ylim()
    lbo = ma - 0.5
    ubo = ma - 0.2
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0, xmax=0.125, color='lightyellow')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.125, xmax=0.25, color='lightgrey')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.25, xmax=0.375, color='lightyellow')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.375, xmax=0.5, color='lightgrey')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.5, xmax=0.625, color='lightyellow')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.625, xmax=0.75, color='lightgrey')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.75, xmax=0.875, color='lightyellow')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.875, xmax=1, color='lightgrey')
    savename = outdir + name + '_' + conc + '_60_seconds_trace.pdf'
    f.savefig(savename, format='pdf', bbox_inches='tight')


#==============================================================================
# def frequency_bar_plot(df, outdir):
#     fig = plt.figure()
#     ax1 = fig.add_subplot(1, 1, 1)
#     ax1 = sns.barplot(x=df['Condition'], y=df['Frequency'], palette='Set1')
#     ax1.set(xlabel='Genotype Comparison', ylabel='No of occurrences')
#     ax1.set_title('Number of occurrences in a random sample of 100 plates at L TP3')
#     ax1.set_ylim(top=max(df['Frequency'].values)+10)
#     for p in ax1.patches:
#         height = p.get_height()
#         ax1.text(p.get_x()+p.get_width()/2.,
#                  height + 2,
#                  '{:1.2f}'.format(height),
#                  ha="center")
#     savename = outdir + 'frequency_bar_plot.png'
#     fig.savefig(savename, format='png', dpi=600)
#     plt.close('all')
# 
# 
# def frequency_pie_plot(df, outdir):
#     fig = plt.figure(figsize=(6, 6), dpi=200)
#     ax = plt.subplot(111)
#     df.plot(y="Frequency", kind='pie', labels=df['Condition'], ax=ax,
#             autopct='%1.1f%%', startangle=180, fontsize=14,
#             title='Percentage of genotype comparisons in a random sample of 100 plates at L TP3')
#     savename = outdir + 'frequency_pied_plot.png'
#     fig.savefig(savename, format='png', dpi=600)
#     plt.close('all')
#==============================================================================


#==============================================================================
# def genotype_distribution(distribution1, distribution2, label1, label2, name, outdir):
#     f, (ax1, ax2) = plt.subplots(1, 2, sharex=True, sharey=True)
#     sns.despine(left=True)
#     sns.set_style('darkgrid')
#     plt.suptitle('Distribution of Observations at Time 0', fontsize='medium')
#     # Plot a histogram and kernel density estimate
#     ax1 = sns.distplot(distribution1, color='b', ax=ax1)
#     ax1.set_xlabel(label1)
#     # Plot a historgram and kernel density estimate
#     ax2 = sns.distplot(distribution2, color='g', ax=ax2)
#     ax2.set_xlabel(label2)
#     plt.tight_layout()
#     savename = outdir + 'distribution_by_' + name + '.png'
#     f.savefig(savename, bbox_inches='tight')
#     plt.close('all')
#==============================================================================


def plot_each_phase(df, outdir):
    table = df.copy(deep=True)
    gb = table.groupby('minute')
    gb.groups
    min1 = gb.get_group(1)
    min2 = gb.get_group(2)
    min3 = gb.get_group(3)
    min4 = gb.get_group(4)
    min5 = gb.get_group(5)
    min6 = gb.get_group(6)
    min7 = gb.get_group(7)
    min8 = gb.get_group(8)
    orderlist = ['GR = Het', 'GR > Het', 'GR < Het']
    f, ((ax1, ax2, ax3, ax4), (ax5, ax6, ax7, ax8)) = plt.subplots(2, 4, sharey=True)
    axes = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]
    plt.suptitle('Number of occurrences in 10s blocks per minute')
    plt.subplots_adjust(wspace=0.2, hspace=0.3, top=0.9)
    ax1 = sns.countplot(x='phase', hue='condition', hue_order=orderlist, data=min1, ax=ax1)
    ax2 = sns.countplot(x='phase', hue='condition', hue_order=orderlist, data=min2, ax=ax2)
    ax3 = sns.countplot(x='phase', hue='condition', hue_order=orderlist, data=min3, ax=ax3)
    ax4 = sns.countplot(x='phase', hue='condition', hue_order=orderlist, data=min4, ax=ax4)
    ax5 = sns.countplot(x='phase', hue='condition', hue_order=orderlist, data=min5, ax=ax5)
    ax6 = sns.countplot(x='phase', hue='condition', hue_order=orderlist, data=min6, ax=ax6)
    ax7 = sns.countplot(x='phase', hue='condition', hue_order=orderlist, data=min7, ax=ax7)
    ax8 = sns.countplot(x='phase', hue='condition', hue_order=orderlist, data=min8, ax=ax8)
    x = 1
    for ax in axes:
        ax.legend_.remove()
        ax.set_xlabel('Minute %s' % (str(x)), fontsize=8)
        ax.set_ylabel('')
        x += 1
    ax4.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.8, 0.3),
               borderaxespad=0, title='Condition', frameon=True)
    ax1.set_ylabel('Count', fontsize=10)
    ax5.set_ylabel('Count', fontsize=10)
    savename = outdir + 'phases_per_minute.png'
    f.savefig(savename, bbox_inches='tight', dpi=600)
    plt.close('all')


def setup_frame(ax):
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.spines['left'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5, pad=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.tick_params(which='both', right='off')
    ax.yaxis.set_ticks_position('left')
    ax.tick_params(which='major', width=1.00, length=5, pad=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.xaxis.labelpad = 20
    ax.yaxis.labelpad = 40

def trace_plot_frames_2sec(dataframe, outdir, name, conc, sec, n=48):
    sns.set_style('white')
    f, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(1, 8, sharey=True, figsize=(25, 15))
    plt.subplots_adjust(top=0.9, wspace=0.2)
    plt.suptitle('Average distance travelled per frame at baseline', fontsize='xx-large')
    df = dataframe.copy(deep=True)
    gb = df.groupby('minute')
    gb.groups
    for x in range(1, len(gb)+1):
        group = gb.get_group(x).copy()
        group['axis'] = (group.time - group.time.iat[0]) / np.timedelta64(1, 's')
        if x == 1:
            ax1 = sns.tsplot(data=group, time='axis', value='dist0',
                             unit='animal', condition='genotype', ax=ax1)
        elif x == 2:
            ax2 = sns.tsplot(data=group, time='axis', value='dist0',
                             unit='animal', condition='genotype', ax=ax2)
        elif x == 3:
            ax3 = sns.tsplot(data=group, time='axis', value='dist0',
                             unit='animal', condition='genotype', ax=ax3)
        elif x == 4:
            ax4 = sns.tsplot(data=group, time='axis', value='dist0',
                             unit='animal', condition='genotype', ax=ax4)
        elif x == 5:
            ax5 = sns.tsplot(data=group, time='axis', value='dist0',
                             unit='animal', condition='genotype', ax=ax5)
        elif x == 6:
            ax6 = sns.tsplot(data=group, time='axis', value='dist0',
                             unit='animal', condition='genotype', ax=ax6)
        elif x == 7:
            ax7 = sns.tsplot(data=group, time='axis', value='dist0',
                             unit='animal', condition='genotype', ax=ax7)
        elif x == 8:
            ax8 = sns.tsplot(data=group, time='axis', value='dist0',
                             unit='animal', condition='genotype', ax=ax8)
        else:
            pass
    axes = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]
    m = 1
    for ax in axes:
        ax.set_xlabel('Frames')
        setup_frame(ax)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
        ax.xaxis.set_minor_locator(ticker.MultipleLocator(1))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
        ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
        ax.legend_.remove()
        ax.set_xlabel('Minute %s' % (str(m)), fontsize=18)
        ax.set_ylabel('')
        m += 1
    n=48
    ptitle = 'n = ' + str(n)
    ax1.spines['left'].set_color('k')
    ax1.set_ylabel('Distance (mm)', fontsize=18)
    lg = ax8.legend(loc=5, fontsize='x-large', bbox_to_anchor=(1.7, 0.5),
               borderaxespad=0, title=ptitle, frameon=True)
    plt.setp(lg.get_title(), fontsize='xx-large')
    mi, ma = ax1.get_ylim()
    lbo = ma - 0.05
    ubo = ma - 0.02
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0, xmax=1, color='lightyellow')
    ax2.axhspan(ymin=lbo, ymax=ubo, xmin=0, xmax=1, color='lightgrey')
    ax3.axhspan(ymin=lbo, ymax=ubo, xmin=0, xmax=1, color='lightyellow')
    ax4.axhspan(ymin=lbo, ymax=ubo, xmin=0, xmax=1, color='lightgrey')
    ax5.axhspan(ymin=lbo, ymax=ubo, xmin=0, xmax=1, color='lightyellow')
    ax6.axhspan(ymin=lbo, ymax=ubo, xmin=0, xmax=1, color='lightgrey')
    ax7.axhspan(ymin=lbo, ymax=ubo, xmin=0, xmax=1, color='lightyellow')
    ax8.axhspan(ymin=lbo, ymax=ubo, xmin=0, xmax=1, color='lightgrey')
    savename = outdir + name + '_' + conc + '_' + sec + '_frames_trace.pdf'
    f.savefig(savename, format='pdf', bbox_inches='tight')
    plt.close('all')


def frequency_count_plot(dataframe, outdir, phase, info):
    df = dataframe.copy(deep=True)
    df = df.reset_index()
    ampli_list = ['GR = Het', 'GR > Het', 'GR < Het']
    delay_list = ['n.d.', 'GR -> Het', 'Het -> GR']

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1)
    if phase == 60:
        ax1.set_title('Number of occurrences for 60s averages')
        savename = outdir + 'frequency_count_plot_60s.png'
    elif phase == 'ph1':
        ax1.set_title('Number of occurrences for first 10s per minute')
        savename = outdir + 'frequency_count_plot_10s_ph1.png'
    elif phase == 'startle':
        ax1.set_title('Number of occurrences for max value of first second')
        savename = outdir + 'frequency_count_plot_startle.png'
    else:
        pass
    if info == 'condition':
        ax1 = sns.countplot(x='minute', hue='condition', hue_order=ampli_list, data=df)
    elif info == 'delay':
        ax1 = sns.countplot(x='minute', hue='delay', hue_order=delay_list, data=df)
        savename = outdir + 'frequency_count_plot_startle_delay.png'
    else:
        pass
    ax1.set(xlabel='Minutes', ylabel='Count')
    ax1.legend(loc=5, fontsize='x-small', bbox_to_anchor=(1.2, 0.5),
               borderaxespad=0, title='Condition', frameon=True)
    fig.savefig(savename, format='png', dpi=600, bbox_inches='tight')
    plt.close('all')


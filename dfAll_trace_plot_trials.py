# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 12:41:01 2017

@author: ehindinger
"""

def setup(ax):
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5, pad=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.tick_params(which='both', right='off')
    ax.yaxis.set_ticks_position('left')
    ax.tick_params(which='major', width=1.00, length=5, pad=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    
# set xticks manually on subplot x axis -> crunches everything to one side
l1 = 0
d1 = l1 + 60
l2 = d1 + 60
d2 = l2 + 60
l3 = d2 + 60
d3 = l3 + 60
l4 = d3 + 60
d4 = l4 + 60
stop = d4 + 60
sns.set_style('white')
f, (ax1) = plt.subplots(1, 1)
ax1 = sns.tsplot(data=df, time='axis', value='dist0', unit='animal',
                 condition='genotype', ax=ax1)
ax1.set(xlabel='Seconds', ylabel='Distance (mm)')
ax1.set_title('Average total distance travelled per second')
setup(ax1)
ax1.xaxis.set_major_locator(ticker.MultipleLocator(60))
ax1.xaxis.set_minor_locator(ticker.MultipleLocator(10))
ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
ax1.axvspan(l1, d1, color='ivory')
ax1.axvspan(l2, d2, color='ivory')
ax1.axvspan(l3, d3, color='ivory')
ax1.axvspan(l4, d4, color='ivory')
ax1.axvspan(d1, l2, color='whitesmoke')
ax1.axvspan(d2, l3, color='whitesmoke')
ax1.axvspan(d3, l4, color='whitesmoke')
ax1.axvspan(d4, stop, color='whitesmoke')


def trace_plot(dataframe, outdir, name, conc, scale):
    df = dataframe.copy(deep=True)
    df['axis'] = (df.frame - df.frame.iat[0])/ np.timedelta64(1, 's')
    sns.set_style('white')
    f, (ax1) = plt.subplots(1, 1, figsize=(15, 10), dpi=600)
    ax1 = sns.tsplot(data=df, time='axis', value='dist0', unit='animal',
                 condition='genotype', ax=ax1)
    if scale == 'seconds':
        ax1.set(xlabel='Seconds', ylabel='Distance (mm)')
        ax1.set_title('Average total distance travelled per second at baseline')
    elif scale == 'frames':
        ax1.set(xlabel='Frames', ylabel='Distance (mm)')
        ax1.set_title('Average distance travelled per frame at baseline')
    ax1.legend(loc=5, fontsize='small', bbox_to_anchor=(1.1, 0.5),
               borderaxespad=0, title='n = 48', frameon=True)
    setup(ax1)
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(60))
    ax1.xaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.1))
    ax1.axhspan(ymin=6.5, ymax=6.8, xmin=0, xmax=0.125, color='lightyellow')
    ax1.axhspan(ymin=6.5, ymax=6.8, xmin=0.125, xmax=0.25, color='lightgrey')
    ax1.axhspan(ymin=6.5, ymax=6.8, xmin=0.25, xmax=0.375, color='lightyellow')
    ax1.axhspan(ymin=6.5, ymax=6.8, xmin=0.375, xmax=0.5, color='lightgrey')
    ax1.axhspan(ymin=6.5, ymax=6.8, xmin=0.5, xmax=0.625, color='lightyellow')
    ax1.axhspan(ymin=6.5, ymax=6.8, xmin=0.625, xmax=0.75, color='lightgrey')
    ax1.axhspan(ymin=6.5, ymax=6.8, xmin=0.75, xmax=0.875, color='lightyellow')
    ax1.axhspan(ymin=6.5, ymax=6.8, xmin=0.875, xmax=1, color='lightgrey')
    savename = outdir + name + '_' + conc + '_seconds_trace_' + scale + '.tiff'
    f.savefig(savename, format='tiff', dpi=600, bbox_inches='tight')
    plt.close('all')


















































''' Works for frames '''



    df = df_frames.copy(deep=True)
    df['axis'] = (df.time - df.time.iat[0])/ np.timedelta64(1, 's')
    sns.set_style('white')
    f, (ax1) = plt.subplots(1, 1)
    plt.subplots_adjust(top=0.9)
    ax1 = sns.tsplot(data=df, time='axis', value='dist0', unit='animal',
                 condition='genotype', ax=ax1)
    ax1.set(xlabel='Frames', ylabel='Distance (mm)')
    plt.suptitle('Average distance travelled per frame at baseline')
    ax1.legend(loc=5, fontsize='small', bbox_to_anchor=(1.2, 0.5),
               borderaxespad=0, title='n = 48', frameon=True)
    setup(ax1)
    ax1.xaxis.set_major_locator(ticker.MultipleLocator(60))
    ax1.xaxis.set_minor_locator(ticker.MultipleLocator(10))
    ax1.yaxis.set_major_locator(ticker.MultipleLocator(0.1))
    ax1.yaxis.set_minor_locator(ticker.MultipleLocator(0.01))
    mi, ma = ax1.get_ylim()
    lbo = ma - 0.05
    ubo = ma - 0.02
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0, xmax=0.125, color='lightyellow')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.125, xmax=0.25, color='lightgrey')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.25, xmax=0.375, color='lightyellow')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.375, xmax=0.5, color='lightgrey')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.5, xmax=0.625, color='lightyellow')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.625, xmax=0.75, color='lightgrey')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.75, xmax=0.875, color='lightyellow')
    ax1.axhspan(ymin=lbo, ymax=ubo, xmin=0.875, xmax=1, color='lightgrey')

    
    
def frame_resampled_2(animals):
    n = 0
    i = 0
    a = 1
    gr_all = pd.DataFrame()
    het_all = pd.DataFrame()
    for i in range(len(animals)):
        temp = animals[i].copy()
        temp['frame'] = range(1, temp.shape[0]+1)
        temp['animal'] = a
        gb = temp.groupby('minute')
        gb.groups
        fr_temp = pd.DataFrame()
        start = 0
        stop = 59
        for x in range(1, len(gb)+1):
            group = gb.get_group(x).copy()
            df = group.loc[start:stop].copy()
            df['frame'] = np.arange(1, 61)
            series = pd.date_range('1/1/2017 00:00:02', periods=df.shape[0], freq='1S')
            df['time'] = series
            fr_temp = pd.concat([fr_temp, df])
            start += 1800
            stop += 1800
        if i < 48:
            fr_temp['genotype'] = 'gr'
            gr_all = pd.concat([gr_all, fr_temp])
        else:
            fr_temp['genotype'] = 'het'
            het_all = pd.concat([het_all, fr_temp])
        n += 1
        i += 1
        a += 1
    result = pd.concat([gr_all, het_all])
    return result



def setup_frame(ax):
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.tick_params(which='major', width=1.00, length=5, pad=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)
    ax.tick_params(which='both', right='off')
    ax.yaxis.set_ticks_position('left')
    ax.tick_params(which='major', width=1.00, length=5, pad=5)
    ax.tick_params(which='minor', width=0.75, length=2.5)


def trace_plot_frames_2sec(dataframe, out_path, conc):
    sns.set_style('white')
    f, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(1, 8, sharey=True, figsize=(25, 15))
    plt.subplots_adjust(top=0.9, wspace=0.3)
    plt.suptitle('Average distance travelled per frame at baseline')
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
        ax.set_xlabel('Minute %s' % (str(m)), fontsize=8)
        ax.set_ylabel('')
        m += 1
    ax1.set_ylabel('Distance (mm)')
    ax8.legend(loc=5, fontsize='small', bbox_to_anchor=(1.5, 0.5),
               borderaxespad=0, title='n = 48', frameon=True)
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
    savename = outdir + name + '_' + conc + '_frames_trace_' + '.tiff'
    f.savefig(savename, format='tiff', dpi=600, bbox_inches='tight')
    plt.close('all')

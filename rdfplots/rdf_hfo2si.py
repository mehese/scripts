#! /usr/bin/env python

from astools.analysis import *
import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator
from scipy.ndimage import filters
from scipy.signal import wiener, filtfilt, butter, gaussian, freqz
from scipy.interpolate import spline, interp1d

import csv

def testGauss(x, y):
    b = gaussian(50, 2.)
    ga = filters.convolve1d(y, b/b.sum())
    #plt.plot(x, ga)
    return ga

colors = ['#008CBA', '#BA2E00', '#278A06', '#994DB3', '#BFB222', '#E0101A', '#1A26AD']

nms = ['hfo2si_c1', 'hfo2si_c1ox', 'hfo2si_c2ox', 'hfo2si_c3ox']
nms = ['hfo2si_c1ox']

pairs = {}

y_main= np.zeros(200) 

for nm in nms:
    s = ReadStruct('../crystal_files/INPUT_'+nm)
    x, y = rdf(s, 200, dist=8.)
    x_main = np.array(x)
    y_main += np.array(y)

    x1, ys = rdf2(s, 200, dist=8.)
    for k in ys:
        if k[-1] in pairs:
            pairs[k[-1]] += np.array(k[:-1])
        else:
            pairs[k[-1]] = np.array(k[:-1])

fig = [None,]*len(pairs)

x_ = np.linspace(np.min(x), np.max(x), 1000)

y_main /= len(nms)
f = interp1d(x, y_main, kind='cubic')

#plt.plot(x_main, y_main)
#plt.plot(x_, f(x_))
minor_locator = MultipleLocator(0.50)
for item, i in zip(pairs.items(), range(len(pairs))):
    nm, yy = item
    print nm
    yy /= len(nms)

    fig[i] = plt.subplot(len(pairs), 1, i+1)
    fig[i].set_xlim([0, 8])
    fig[i].set_ylim([0, max(y_main)])
    fig[i].xaxis.set_minor_locator(minor_locator)
    fig[i].tick_params(which='minor', length=5, width=2)
    fig[i].tick_params(which='major', length=10, width=2, labelsize=15)
    for x in ['top', 'bottom', 'left', 'right']:
        fig[i].spines[x].set_linewidth(2)
    plt.setp(fig[i].get_yticklabels(), visible=False)
    plt.setp(fig[i].get_xticklabels(), visible=False)

    fig[i].plot(x_main, y_main, color=colors[0], linewidth=3,label='total')
    fig[i].plot(x1, yy, color=colors[i+1], linewidth=3, label =nm)
    fig[i].legend(fontsize=22, loc='upper left')
    fig[i].get_legend().get_frame().set_linewidth(2)

plt.setp(fig[i].get_xticklabels(), visible=True)
for tick in fig[i].xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

plt.subplots_adjust(hspace=0)
plt.xlabel(r'Distance [$\mathbf{\AA{}}$]', fontweight='bold', fontsize=25)
plt.gcf().set_size_inches(20., len(pairs)*3.5)
plt.savefig('rdf_hfo2si_tot.png', dpi=100, bbox_inches='tight')
plt.show()

print 'Done'

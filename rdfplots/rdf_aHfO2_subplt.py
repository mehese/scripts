#! /usr/bin/env python2.7

from astools.analysis import rdf, rdf2
from astools.ReadWrite import ReadStruct
import numpy as np
import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator
from scipy.ndimage import filters
from scipy.signal import wiener, filtfilt, butter, gaussian, freqz
from scipy.interpolate import spline, interp1d

import csv

def testGauss(x, y):
    b = gaussian(5, .1)
    ga = filters.convolve1d(y, b/b.sum())
    #plt.plot(x, ga)
    return ga

a = ReadStruct('../crystal_files/INPUT_aHfO2')
x, y = rdf(a, 200, dist=8.)
x_ = np.linspace(np.min(x), np.max(x), 1000)
f = interp1d(x, y, kind='cubic')
y_tot = f(x_)*1.3

print 'Done with total rdf'

x1, ys = rdf2(a, 200, dist=8.)

minor_locator = MultipleLocator(0.1)
for i, c in zip(range(3), ['#AB6A67', '#085D9E', '#C76D28']):
    # create a subplot
    fig = plt.subplot(3, 1, i+1)
    fig.set_xlim([0, 8])
    fig.set_ylim([0,np.max(y_tot)])
    fig.xaxis.set_minor_locator(minor_locator)
    fig.tick_params(which='minor', length=5, width=2)
    fig.tick_params(which='major', length=10, width=2, labelsize=15)
    for x in ['top', 'bottom', 'left', 'right']:
        fig.spines[x].set_linewidth(2)
    
    plt.setp(fig.get_yticklabels(), visible=False)
    plt.setp(fig.get_xticklabels(), visible=False)

    # plot total RDF
    fig.plot(x_, y_tot, color='#ff0000', zorder=0, alpha=1, linewidth=2, label='Total')

    f = interp1d(x1, ys[i][:-1], kind='cubic')
    fig.plot(x_, f(x_)*1.3, label=ys[i][-1]+' pairs', linewidth=3, color=c)


    fig.legend(fontsize=20, loc='upper left')
    fig.get_legend().get_frame().set_linewidth(2)
    print '{} : {}'.format(i, ys[i][-1])



print 'Done with rdfs'
plt.xlabel(r'Distance [$\mathbf{\AA{}}$]', fontweight='bold', fontsize=20)
plt.subplots_adjust(hspace=0)
plt.setp(fig.get_xticklabels(), visible=True)
for tick in fig.xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

plt.gcf().set_size_inches(20., 3*3.5)
plt.savefig('rdf_aHfO2.png', dpi=100, bbox_inches='tight')

plt.show()

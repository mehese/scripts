#! /usr/bin/python2.7

from math import pi, exp
import scipy as sp
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

def lrntz(x, x0, gamma):
	return (1/pi)*(gamma/((x - x0)*(x - x0) + gamma*gamma))

plt.grid('on')
crys = np.loadtxt('RAMSPEC.DAT')
x, y = crys[:,0], crys[:,1]
plt.plot(x, y, color='#BA9500', linewidth=2, label='B3LYP-Figgen')
plt.fill_between(x, y, 0, color='#FFD012', zorder=0)

f2 = open('image2.csv', 'r')
dat_exp = np.loadtxt('image2.csv')
omg_mod, rmn_mod = dat_exp[:,0], dat_exp[:,1]

omega = sp.arange(90, 900, .5)
I_tot = len(omega)*[0.]

I_Wu = len(omega)*[0.]
Wu_peaks =                    [119., 134., 147., 255., 330., 387., 495., 572., 665., 131., 166., 243., 328., 402., 508., 558., 633., 770.] 
Wu_int = map(lambda x: x*290., [1.4 , 2.0 , 2.4 , 1.4 , 1.  , 2.4 , 8.  , 1.3 , 2.  , 1.4 , 1.4 ,  1. , 1.  , 3.4 , 3.  ,   1.,  2. , 0.8  ])

for i in range(len(omega)):
	for j in range(len(Wu_int)):
		I_Wu[i] = I_Wu[i] + Wu_int[j]*lrntz(omega[i], Wu_peaks[j], 5.)  
plt.plot(omega, I_Wu, '-', color='#2233ff', linewidth=2, label = 'LDA-HGH')
plt.plot(omg_mod, rmn_mod/435., '-', color='#ff4422', linewidth=2, label = 'Experimental', zorder=99)

plt.gca().yaxis.set_tick_params(which='major', length=10, width=2)
plt.gca().yaxis.set_ticklabels([])
#plt.yticks([])

plt.gca().xaxis.set_minor_locator(MultipleLocator(10))
plt.gca().xaxis.set_tick_params(which='major', length=10, width=2, labelsize=15)
plt.gca().xaxis.set_tick_params(which='minor', length=5, width=2, labelsize=15)

#plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

#plt.legend(handles=[full, epr, dim_, bdim_], fontsize=16, ncol=4)
plt.legend(fontsize=16)
plt.gca().get_legend().get_frame().set_linewidth(2)
plt.xlim([90,900])
plt.ylim(ymin=0)
plt.xlabel('Wavenumber cm$^\mathbf{-1}$', fontweight='bold', fontsize=16)
plt.ylabel('Raman Intensity [arbitrary units]', fontweight='bold', fontsize=16)

plt.gcf().set_size_inches(20., 7.)
plt.savefig('raman.png', dpi=200, bbox_inches='tight')



#plt.ylabel('Raman Intensity [arbitrary units]')
plt.show()

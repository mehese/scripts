#! /usr/bin/env python

import sys
sys.path.append('/home/eric/Dropbox/astools/')
from analysis import *
import matplotlib.pylab as plt

print 'cell 1...'
cell = ReadStruct('INPUT_c2', 'crystal')
x, y = vertical_density_profile(cell, 1.) 

plt.plot(x, y, 'k-')
plt.xlim([0,cell.coordz])

#plt.title('Si-O RDF', fontweight='bold', fontsize=18) 
#plt.xlabel(r'Distance $\mathbf{\AA}$', fontweight='bold', fontsize=16)
#plt.yticks([])
#
#plt.gca().tick_params(width=2, labelsize=15)
#for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
#    tick.label1.set_fontweight('bold')
#for x in ['top', 'bottom', 'left', 'right']:
#    plt.gca().spines[x].set_linewidth(2)
#
#plt.legend(fontsize=13)
#plt.gcf().set_size_inches(10., 7.)
#plt.savefig('rdf_SiO.png', dpi=100, bbox_inches='tight')
plt.show()

print 'Done'

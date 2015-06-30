#! /usr/bin/env python

import sys
sys.path.append('/home/eric/Dropbox/astools/')
from analysis import *
import matplotlib.pylab as plt

print 'cell 1...'
cell = ReadStruct('INPUT_c1', 'crystal')
x, y = rdf2(cell, 200, dist=3.)
print y[2][-1]
plt.plot(x, y[2][:-1], label='cell 1 fixed boxsize', color='#0066FF', linewidth=1.8, alpha=0.7)

print 'cell 2...'
cell = ReadStruct('INPUT_c2', 'crystal')
x, y = rdf2(cell, 150, dist=3.)
plt.plot(x, y[2][:-1], label='cell 2', color='#FF1919', linewidth=1.8, alpha=0.7)

print 'cell 3...'
cell = ReadStruct('INPUT_c3', 'crystal')
x, y = rdf2(cell, 200, dist=3.)
plt.plot(x, y[2][:-1], label='cell 3', color='#E6E600', linewidth=1.8, alpha=0.7)

print 'cell 4...'
cell = ReadStruct('INPUT_c4', 'crystal')
x, y = rdf2(cell, 200, dist=3.)
plt.plot(x, y[2][:-1], label='cell 4', color='#009999', linewidth=1.8, alpha=0.7)

print 'cell 5...'
cell = ReadStruct('INPUT_c5', 'crystal')
x, y = rdf2(cell, 200, dist=3.)
plt.plot(x, y[2][:-1], label='cell 5', color='#33CC33', linewidth=1.8, alpha=0.7)

print 'cell 6...'
cell = ReadStruct('INPUT_c6', 'crystal')
x, y = rdf2(cell, 200, dist=3.)
plt.plot(x, y[2][:-1], label='cell 6', color='#9966FF', linewidth=1.8, alpha=0.7)

print 'cell 2 ox...'
cell = ReadStruct('INPUT_c2ox', 'crystal')
x, y = rdf2(cell, 200, dist=3.)
plt.plot(x, y[2][:-1], '--', label='cell 2 ox (?)', color='#FF1919', linewidth=1.8, alpha=0.7)

print 'cell 3 ox...'
cell = ReadStruct('INPUT_c3ox', 'crystal')
x, y = rdf2(cell, 200, dist=3.)
plt.plot(x, y[2][:-1], '--', label='cell 3 ox', color='#E6E600', linewidth=1.8, alpha=0.7)

print 'cell 5 ox...'
cell = ReadStruct('INPUT_c5ox', 'crystal')
x, y = rdf2(cell, 200, dist=3.)
plt.plot(x, y[2][:-1], '--', label='cell 5 ox', color='#33CC33', linewidth=1.8, alpha=0.7)



plt.xlim([1.0, 3.])
plt.title('Si-O RDF', fontweight='bold', fontsize=18) 
plt.xlabel(r'Distance $\mathbf{\AA}$', fontweight='bold', fontsize=16)
plt.yticks([])

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)

plt.legend(fontsize=13)
plt.gcf().set_size_inches(10., 7.)
plt.savefig('rdf_SiO.png', dpi=100, bbox_inches='tight')
plt.show()

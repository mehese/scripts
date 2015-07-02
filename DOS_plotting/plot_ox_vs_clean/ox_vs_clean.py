#! /usr/bin/python2.7

import sys
sys.path.append('../')
from atom_pdos_getter import *

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

#print Ef

x, yu, yd =  get_at_pdos('si', 1) 
plt.plot(x, 70*yu, color='#000000', linewidth=3)
plt.plot(x, 70*yd, color='#000000', linewidth=3)

x, y_u, y_d = get_at_pdos('c5', 1, total=True) 
plt.plot(x, y_u, 'b-', label='cell 2: clean Si')
plt.plot(x, y_d, 'b-')
x, y_u, y_d = get_at_pdos('c5ox', 1, total=True) 
plt.plot(x, y_u, 'r-', label='cell 2: oxidised')
plt.plot(x, y_d, 'r-')

print 'Comparisons:\n'
print 'Cell 2'
print integrate_dos(*get_at_pdos('c2',   1, total=True))
print integrate_dos(*get_at_pdos('c2ox', 1, total=True))
print 'Cell 3'
print integrate_dos(*get_at_pdos('c3',   1, total=True))
print integrate_dos(*get_at_pdos('c3ox', 1, total=True))
print 'Cell 5'
print integrate_dos(*get_at_pdos('c5',   1, total=True))
print integrate_dos(*get_at_pdos('c5ox', 1, total=True))
print '\n'

minor_locator = MultipleLocator(1)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

plt.xlabel('Energy (eV)', fontweight='bold', fontsize=16)
plt.xlim([-5, 0])

plt.ylim([-50, 50])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.legend(loc=2, fontsize=16)
plt.gca().get_legend().get_frame().set_linewidth(2)
plt.gcf().set_size_inches(20., 7.)
#plt.savefig('c2_pdos.png', dpi=400, bbox_inches='tight')
plt.show()

print "Done"

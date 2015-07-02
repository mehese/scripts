#! /usr/bin/python2.7

import sys
sys.path.append('../')
from atom_pdos_getter import *

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

print 'Comparisons:\n'
print 'Cell 2'
print 'clean   ', integrate_dos(*get_at_pdos('c2',   1, total=True), emin=-4, emax=-1.8)
print 'oxidised', integrate_dos(*get_at_pdos('c2ox', 1, total=True), emin=-4, emax=-1.8)
print 'Cell 3'
print 'clean   ', integrate_dos(*get_at_pdos('c3',   1, total=True), emin=-4, emax=-1.8)
print 'oxidised', integrate_dos(*get_at_pdos('c3ox', 1, total=True), emin=-4, emax=-1.8)
print 'Cell 5'
print 'clean   ', integrate_dos(*get_at_pdos('c5',   1, total=True), emin=-4, emax=-1.8)
print 'oxidised', integrate_dos(*get_at_pdos('c5ox', 1, total=True), emin=-4, emax=-1.8)
print '\n'


## Uncommend below for Si DOS

#x, yu, yd =  get_at_pdos('si', 1) 
#plt.plot(x, 70*yu, color='#000000', linewidth=3)
#plt.plot(x, 70*yd, color='#000000', linewidth=3)

plt.subplot(3,1,1)
#plot the Si conduction and valence bands
plt.axvspan(-5,-3.313, facecolor='0.85', linewidth=0)
plt.axvspan(-2.27,0.0, facecolor='0.85', linewidth=0)
x, y_u, y_d = get_at_pdos('c2', 1, total=True) 
plt.plot(x, y_u, 'b-', linewidth=2, label='cell 2: clean Si')
plt.plot(x, y_d, 'b-', linewidth=2)
x, y_u, y_d = get_at_pdos('c2ox', 1, total=True) 
plt.plot(x, y_u, 'r-', linewidth=2, label='cell 2: oxidised')
plt.plot(x, y_d, 'r-', linewidth=2)
minor_locator = MultipleLocator(0.10)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

plt.xlim([-5, 0])
plt.ylim([-60, 60])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.legend(loc=2, fontsize=16)
plt.gca().get_legend().get_frame().set_linewidth(2)
plt.gcf().set_size_inches(20., 3.5)

plt.subplot(3,1,2)
#plot the Si conduction and valence bands
plt.axvspan(-5,-3.313, facecolor='0.85', linewidth=0)
plt.axvspan(-2.27,0.0, facecolor='0.85', linewidth=0)
x, y_u, y_d = get_at_pdos('c3', 1, total=True) 
plt.plot(x, y_u, 'b-', linewidth=2, label='cell 3: clean Si')
plt.plot(x, y_d, 'b-', linewidth=2)
x, y_u, y_d = get_at_pdos('c3ox', 1, total=True) 
plt.plot(x, y_u, 'r-', linewidth=2, label='cell 3: oxidised')
plt.plot(x, y_d, 'r-', linewidth=2)
#minor_locator = MultipleLocator(0.25)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

plt.xlim([-5, 0])
plt.ylim([-60, 60])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.legend(loc=2, fontsize=16)
plt.gca().get_legend().get_frame().set_linewidth(2)
plt.gcf().set_size_inches(20., 3.5)

plt.subplot(3,1,3)
#plot the Si conduction and valence bands
plt.axvspan(-5,-3.313, facecolor='0.85', linewidth=0)
plt.axvspan(-2.27,0.0, facecolor='0.85', linewidth=0)
x, y_u, y_d = get_at_pdos('c5', 1, total=True) 
plt.plot(x, y_u, 'b-', linewidth=2, label='cell 5: clean Si')
plt.plot(x, y_d, 'b-', linewidth=2)
x, y_u, y_d = get_at_pdos('c5ox', 1, total=True) 
plt.plot(x, y_u, 'r-', linewidth=2, label='cell 5: oxidised')
plt.plot(x, y_d, 'r-', linewidth=2)
#minor_locator = MultipleLocator(0.25)
plt.gca().xaxis.set_minor_locator(minor_locator)
plt.gca().tick_params(which='minor', length=5, width=2)
plt.gca().tick_params(which='major', length=10, width=2, labelsize=15)

plt.xlim([-5, 0])
plt.ylim([-60, 60])
plt.setp(plt.gca().get_yticklabels(), visible=False)

plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.legend(loc=2, fontsize=16)
plt.gca().get_legend().get_frame().set_linewidth(2)
plt.gcf().set_size_inches(20., 10.5)

plt.xlabel('Energy [eV]', fontweight='bold', fontsize=16)
plt.savefig('dos_clean_ox.png', dpi=400, bbox_inches='tight')
plt.show()

print "Done"

#! /usr/bin/python2.7

import sys
sys.path.append('../')
sys.path.append('../../')
from atom_pdos_getter import *

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator



## Uncommend below for Si DOS

#x, yu, yd =  get_at_pdos('si', 1) 
#plt.plot(x, 70*yu, color='#000000', linewidth=3)
#plt.plot(x, 70*yd, color='#000000', linewidth=3)

minor_locator = MultipleLocator(0.10)

print 'Comparisons:\n'
for i in range(2, 7):
    print 'Cell {}'.format(i)
    v1=integrate_dos(*get_at_pdos('c{}'.format(i) , 1, total=True), emin=-3.313, emax=-2.27)
    v2=integrate_dos(*get_at_pdos('c{}p'.format(i), 1, total=True), emin=-3.313, emax=-2.27)
    print 'clean = {:10.5f} passified = {:10.5f}'.format(v1, v2)       
    print 'improvement = {:5.2f}%'.format((v1-v2)*100/v1)
    plt.subplot(5, 1, i-1)
    #plot the Si conduction and valence bands
    plt.axvspan(-5,-3.313, facecolor='0.85', linewidth=0)
    plt.axvspan(-2.27,0.0, facecolor='0.85', linewidth=0)
    x, y_u, y_d = get_at_pdos('c{}'.format(i) , 1, total=True) 
    plt.plot(x, y_u, 'b-', linewidth=2, label='cell '+str(i)+': clean Si')
    plt.plot(x, y_d, 'b-', linewidth=2)
    x, y_u, y_d = get_at_pdos('c{}p'.format(i), 1, total=True) 
    plt.plot(x, y_u, 'g-', linewidth=2, label='cell '+str(i)+': clean Si + H')
    plt.plot(x, y_d, 'g-', linewidth=2)
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

print 'Saving figure...'
plt.gcf().set_size_inches(20., 17.5)
plt.xlabel('Energy [eV]', fontweight='bold', fontsize=16)
plt.savefig('dos_clean_pass.png', dpi=400, bbox_inches='tight')

print "Done"

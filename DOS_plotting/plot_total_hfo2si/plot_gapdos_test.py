#! /usr/bin/python2.7

import sys
sys.path.append('../')
sys.path.append('../../')
from helping_functions import neighbours_from_file
from atom_pdos_getter import integrate_dos, get_at_pdos
from atom_pdos_getter import *
from astools.ReadWrite import ReadStruct
from astools.analysis import distance
import numpy as np

import matplotlib.pylab as plt
from matplotlib.ticker import MultipleLocator

# Si gap = -3.8, -2
# cell 1     -2.54 -> -0.62
# cell 1 ox  -2.60 -> -0.74
# cell 2 ox  -2.13 -> -0.29
# cell 3 ox  -2.22 -> -0.04



#nms = ['hfo2si_c1']
nms = ['hfo2si_c1', 'hfo2si_c1ox', 'hfo2si_c2ox', 'hfo2si_c3ox']
titles = ['cell 1 (clean)', 'cell 1 (oxidised)', 'cell 2 (oxidised)', 'cell 3 (oxidised)']
fermis = [-0.3915623715, -1.1526262679, -0.5232161378, -0.8299245876]
lims = {'hfo2si_c1':  (-2.54, -0.62), 
        'hfo2si_c1ox':(-2.62, -0.74), 
        'hfo2si_c2ox':(-2.13, -0.32), 
        'hfo2si_c3ox':(-2.22, -0.04)}

sc_lims = {'hfo2si_c1':  (3.3, 7.5), 
           'hfo2si_c1ox':(4.8, 10), 
           'hfo2si_c2ox':(2.8, 7), 
           'hfo2si_c3ox':(3.2, 8.1)}
ox_lims = {'hfo2si_c1':  (13.20, 19.60), 
           'hfo2si_c1ox':(14.50, 21.48), 
           'hfo2si_c2ox':(13.30, 19.45), 
           'hfo2si_c3ox':(13.10, 20.30)}
ks = range(3, 7)
fig = [None,]*len(ks)

x = np.linspace(0, 3*np.pi, 100)

offst = lambda k : k + 3.8

minor_locator = MultipleLocator(0.10)
for i, k, t, Ef in zip(range(len(nms)), nms, titles, fermis):
    fig[i] = plt.subplot(len(ks),1, i+1)
    fig[i].set_xlim([offst(-5), offst(1)])
    fig[i].set_ylim([-50, 50])
    fig[i].xaxis.set_minor_locator(minor_locator)
    fig[i].tick_params(which='minor', length=5, width=2)
    fig[i].tick_params(which='major', length=10, width=2, labelsize=15)
    fig[i].tick_params(which='major', length=10, width=2, labelsize=15)
    for x in ['top', 'bottom', 'left', 'right']:
        fig[i].spines[x].set_linewidth(2)
    plt.setp(fig[i].get_yticklabels(), visible=False)
    plt.setp(fig[i].get_xticklabels(), visible=False)

    fig[i].plot([offst(Ef), offst(Ef)], [-50, +50], color='crimson', linewidth=2,
                zorder=9)
    fig[i].text(-1.1, 40, t, fontsize=18, weight='bold')

plt.setp(fig[i].get_xticklabels(), visible=True)
for tick in fig[i].xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

print 'Done formatting!'

for i, nm in enumerate(nms):
    s = ReadStruct('../../crystal_files/INPUT_'+nm)
    s.normalise()
    vbmax, cbmin = map(offst, lims[nm])
    print nm
    print vbmax, cbmin
    fig[i].axvspan(offst(-5),    vbmax, facecolor='0.85', linewidth=0)
    fig[i].axvspan(    cbmin, offst(1), facecolor='0.85', linewidth=0)
    E, up, down = get_at_pdos(nm, 3, total=True)
    fig[i].plot(offst(E),   up, '-', color='slateblue', linewidth=3)
    fig[i].plot(offst(E), down, '-', color='slateblue', linewidth=3)
    _, u2, d2 = np.zeros(len(E)), np.zeros(len(up)),  np.zeros(len(down))
    print sc_lims[nm][0], sc_lims[nm][1]
    for j, at in enumerate(s.atoms):
        if at.z < sc_lims[nm][0]  or at.z > sc_lims[nm][1]:
            if at.z < ox_lims[nm][0] or at.z > ox_lims[nm][1]:
                x, y1, y2 = get_at_pdos(nm, j+1)
                u2 += y1
                d2 += y2

    fig[i].plot(offst(E), u2, '-', color='crimson', linewidth=3)
    fig[i].plot(offst(E), d2, '-', color='crimson', linewidth=3)
            

    

print 'Done plotting!'
plt.subplots_adjust(hspace=0)
plt.gcf().set_size_inches(20., 4*3.5)
plt.xlabel('Energy [eV]', fontweight='bold', fontsize=16)
plt.savefig('gap_dos_int.png', dpi=200, bbox_inches='tight')

plt.show()

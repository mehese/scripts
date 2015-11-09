#! /usr/bin/python2.7

import sys
sys.path.append('../')
sys.path.append('../../')
from helping_functions import neighbours_from_file, offsets
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
titles = ['cell 1 (unoxidised)', 'cell 1 (oxidised)', 'cell 2 (oxidised)', 'cell 3 (oxidised)']
fermis = [-1.2, -1.1526262679, -0.5232161378, -0.8299245876]
lims = {'hfo2si_c1':  (-2.54, -0.62), 
        'hfo2si_c1ox':(-2.62, -0.74), 
        'hfo2si_c2ox':(-2.48, -0.32), 
        'hfo2si_c3ox':(-2.43, -0.04)}

ks = range(3, 7)
fig = [None,]*len(ks)

x = np.linspace(0, 3*np.pi, 100)


minor_locator = MultipleLocator(0.10)
for i, k, t in zip(range(len(nms)), nms, titles):
    fig[i] = plt.subplot(len(ks),1, i+1)
    fig[i].set_xlim([-1, 3])
    fig[i].set_ylim([-50, 50])
    fig[i].xaxis.set_minor_locator(minor_locator)
    fig[i].tick_params(which='minor', length=5, width=2)
    fig[i].tick_params(which='major', length=10, width=2, labelsize=15)
    fig[i].tick_params(which='major', length=10, width=2, labelsize=15)
    for x in ['top', 'bottom', 'left', 'right']:
        fig[i].spines[x].set_linewidth(2)
    plt.setp(fig[i].get_yticklabels(), visible=False)
    plt.setp(fig[i].get_xticklabels(), visible=False)

    fig[i].plot([offsets[k]['Ef'] - offsets[k]['VBM'], ]*2, [-50, +50], color='crimson', linewidth=3,
                zorder=9)
    fig[i].text(-.9, 36, t, fontsize=22, weight='bold')

plt.setp(fig[i].get_xticklabels(), visible=True)
for tick in fig[i].xaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')

print 'Done formatting!'

for i, nm in enumerate(nms):
    s = ReadStruct('../../crystal_files/INPUT_'+nm)

    o = lambda k : k - offsets[nm]['VBM']
    fig[i].axvspan(-1, 0, facecolor='0.85', linewidth=0)
    fig[i].axvspan(offsets[nm]['CBM']-offsets[nm]['VBM'], 3, facecolor='0.85', linewidth=0)

    
    E, up, down = get_at_pdos(nm, 3, total=True)
    fig[i].plot(o(E),   up, '-', color='slateblue', linewidth=3)
    fig[i].plot(o(E), down, '-', color='slateblue', linewidth=3)

    p1, p2 = np.zeros(600), np.zeros(600)
    for ii, at in enumerate(s.atoms):
        nbs = neighbours_from_file(ii+1, nm) 
        nbs = [nb for nb in nbs if (nb.atom_type == 'Hf' and nb.length < 3.)]
        if at.species == 'Si' and nbs:
            print [(nb.atom_type, nb.length) for nb in nbs] 
            _, u, d =  get_at_pdos(nm, ii+1)
            p1 += u
            p2 += d

    fig[i].plot(o(E),   p1, '-', color='#66FFCC', linewidth=3)
    fig[i].plot(o(E),   p2, '-', color='#66FFCC', linewidth=3)


print 'Done plotting!'
plt.subplots_adjust(hspace=0)
plt.gcf().set_size_inches(20., 4*3.5)
plt.xlabel('Energy [eV]', fontweight='bold', fontsize=25)
plt.savefig('gap_dos_hfo2si.png', dpi=100, bbox_inches='tight')

plt.show()

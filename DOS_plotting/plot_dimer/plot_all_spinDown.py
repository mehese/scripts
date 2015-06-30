#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

totals = []

# CELL 1
c1_Ef = -2.34
c1 = np.loadtxt('c1_57_113.dat')
c1_E, c1_dos_u, c1_57_u, c1_113_u, c1_dos_d, c1_57_d, c1_113_d = tuple(c1[:, i] for i in range(7))
#plt.plot([c1_Ef, c1_Ef], [-70, 70], 'm--', linewidth =2.)
plt.plot(c1_E,-c1_57_d, 'k-', linewidth=1.5)
plt.plot(c1_E,-c1_113_d, 'k-', linewidth=1.5)

# CELL 2
c2_Ef = -2.68
c2 = np.loadtxt('c2_102_114_142.dat')
c2_E, c2_dos_u, c2_102_u, c2_114_u, _, c1_dos_d, c2_102_d, c2_114_d, _ = tuple(c2[:, i] for i in range(9))
plt.plot(c2_E,-c2_102_d, 'k-', linewidth=1.5)
plt.plot(c2_E,-c2_114_d, 'k-', linewidth=1.5)

# CELL 3
c3_Ef = -2.91
c3 = np.loadtxt('c3_73_102_119.dat')
c3_E, c3_dos_u, c3_73_u, _, _, c3_dos_d, c3_73_d, _, _ = tuple(c3[:, i] for i in range(9))
c3 = np.loadtxt('c3_101.dat')
c3_E, c3_dos_u, c3_101_u, c3_dos_d, c3_101_d = tuple(c3[:, i] for i in range(5))
##plt.plot([c3_Ef, c3_Ef], [-70, 70], 'g--', linewidth =2.)
plt.plot(c3_E,-c3_73_d, 'k-', linewidth=1.5)
plt.plot(c3_E,-c3_101_d, 'k-', linewidth=1.5)
#
## CELL 4
#c4_Ef = -2.84
########## N/A #######################
#
# CELL 5
c5_Ef = -2.18
c5 = np.loadtxt('c5_65_82_126.dat')
c5_E, c5_dos_u, c5_65_u, _, _, c5_dos_d, c5_65_d, _, _ = tuple(c5[:, i] for i in range(9))
plt.plot(c5_E,-c5_65_d, 'k-', linewidth=1.5)

# CELL 6
c6_Ef = -2.64
c6 = np.loadtxt('c6_113.dat')
c6_E, c6_dos_u, c6_113_u, c6_dos_d, c6_113_d = tuple(c6[:, i] for i in range(5))
plt.plot(c6_E,-c6_113_d, 'k-', linewidth=1.5)

# CELL 2 OX
c2ox_Ef = -2.41
c2ox = np.loadtxt('c2ox_72_86_126.dat')
c2ox_E, c2ox_dos_u, _, c2ox_86_u, _, c2ox_dos_d, _, c2ox_86_d, _ = tuple(c2ox[:, i] for i in range(9))
plt.plot(c2ox_E,-c2ox_86_d, 'k-', linewidth=1.5)

# CELL 3 OX
c3ox_Ef = -1.99
c3ox = np.loadtxt('c3ox_73_129_135.dat')
c3ox_E, c3ox_dos_u, c3ox_73_u, _, _, c3ox_dos_d, c3ox_73_d, _, _ = tuple(c3ox[:, i] for i in range(9))
##plt.plot([c3ox_Ef, c3ox_Ef], [-70, 70], 'r--', linewidth =2.)
plt.plot(c3ox_E,-c3ox_73_d, 'k-', linewidth=1.5)

# CELL 5 OX
c5ox_Ef = -2.18
c5ox = np.loadtxt('c5ox_78_117_141.dat')
c5ox_E, c5ox_dos_u, _, c5ox_117_u, _, c5ox_dos_d, _, c5ox_117_d, __ = tuple(c5ox[:, i] for i in range(9))
##plt.plot([c5ox_Ef, c5ox_Ef], [-70, 70], 'y--', linewidth =2.)
plt.plot(c5ox_E,-c5ox_117_d, 'k-', linewidth=1.5)

SiBulk = np.loadtxt('state_density_SiBulk.dat')
E_Si, dos_Si = SiBulk[:, 0], SiBulk[:, 1]
plt.plot(E_Si, 10*dos_Si, 'b-', linewidth=2.0, label='bulk Si')
##qz = np.loadtxt('state_density_qz.dat')
#
total = c1_57_d + c1_113_d + \
        c2_102_d + c2_114_d + \
        c3_73_d + c3_101_d + \
        c5_65_d  + \
        c6_113_d + \
        c2ox_86_d + \
        c3ox_73_d + \
        c5ox_117_d
#
plt.plot(c5ox_E,-total, 'g-', linewidth=2., label='total')

plt.title('dimer defects (spin down)') 
plt.xlabel('Energy (eV)')
plt.xlim([-5, 0])
#plt.ylim([0,20])
plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.legend(loc=2, fontsize=18)
plt.gcf().set_size_inches(20., 7.)
plt.savefig('test2png.png', dpi=200, bbox_inches='tight')
plt.show()

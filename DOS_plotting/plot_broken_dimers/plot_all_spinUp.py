#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

totals = []

# CELL 1
c1_Ef = -2.34
c1 = np.loadtxt('c1_107.dat')
c1_E, c1_dos_u, c1_107_u, c1_dos_d, c1_107_d = tuple(c1[:, i] for i in range(5))
#plt.plot([c1_Ef, c1_Ef], [-70, 70], 'm--', linewidth =2.)
plt.plot(c1_E, c1_107_u, 'k-', linewidth=1.5)

# CELL 2
c2_Ef = -2.68
c2 = np.loadtxt('c2_82_120_128.dat')
c2_E, c2_dos_u, c2_82_u, _, _, c1_dos_d, c2_82_d, _, _ = tuple(c2[:, i] for i in range(9))
plt.plot(c2_E, c2_82_u, 'k-', linewidth=1.5)

# CELL 3
c3_Ef = -2.91
c3 = np.loadtxt('c3_66_107_121.dat')
c3_E, c3_dos_u, c3_66_u, _, _, c3_dos_d, c3_66_d, _, _ = tuple(c3[:, i] for i in range(9))
c3 = np.loadtxt('c3_68_73_114_58.dat')
c3_E, c3_dos_u,  _, _, _,c3_58_u, c3_dos_d,  _, _, _,c3_58_d = tuple(c3[:, i] for i in range(11))
##plt.plot([c3_Ef, c3_Ef], [-70, 70], 'g--', linewidth =2.)
plt.plot(c3_E, c3_58_u, 'k-', linewidth=1.5)
plt.plot(c3_E, c3_66_u, 'k-', linewidth=1.5)

# CELL 4
c4_Ef = -2.84
c4 = np.loadtxt('c4_65_119.dat')
c4_E, c4_dos_u, c4_65_u, c4_119_u, c4_dos_d, c4_65_d, c4_119_d = tuple(c4[:, i] for i in range(7))
plt.plot(c4_E, c4_65_u,  'k-', linewidth=1.5)
plt.plot(c4_E, c4_119_u, 'k-', linewidth=1.5)

# CELL 5
c5_Ef = -2.18
c5 = np.loadtxt('c5_65_82_126.dat')
c5_E, c5_dos_u, _, c5_82_u, _, c5_dos_d,  _, c5_82_d, _ = tuple(c5[:, i] for i in range(9))
c5 = np.loadtxt('c5_81_101_102_113.dat')
c5_E, c5_dos_u, _, _, c5_102_u, _, c5_dos_d,  _, _, c5_102_d, _ = tuple(c5[:, i] for i in range(11))
plt.plot(c5_E, c5_82_u,  'k-', linewidth=1.5)
plt.plot(c5_E, c5_102_u, 'k-', linewidth=1.5)

# CELL 6
c6_Ef = -2.64
c6 = np.loadtxt('c6_66_101_119.dat')
c6_E, c6_dos_u, c6_66_u,  c6_101_u, c6_119_u,c6_dos_d, c6_66_d , c6_101_d , c6_119_d = tuple(c6[:, i] for i in range(9))
plt.plot(c6_E, c6_66_u,  'k-', linewidth=1.5)
plt.plot(c6_E, c6_101_u, 'k-', linewidth=1.5)
plt.plot(c6_E, c6_119_u, 'k-', linewidth=1.5)

# CELL 2 OX
c2ox_Ef = -2.41
c2ox = np.loadtxt('c2ox_72_86_126.dat')
c2ox_E, c2ox_dos_u, c2ox_72_u, _, _, c2ox_dos_d, c2ox_72_d, _, _ = tuple(c2ox[:, i] for i in range(9))
plt.plot(c2ox_E, c2ox_72_u, 'r-', linewidth=1.5)

# CELL 3 OX
c3ox_Ef = -1.99
c3ox = np.loadtxt('c3ox_65.dat')
c3ox_E, c3ox_dos_u, c3ox_65_u, c3ox_dos_d, c3ox_65_d = tuple(c3ox[:, i] for i in range(5))
##plt.plot([c3ox_Ef, c3ox_Ef], [-70, 70], 'r--', linewidth =2.)
plt.plot(c3ox_E, c3ox_65_u, 'r-', linewidth=1.5)

# CELL 5 OX
c5ox_Ef = -2.18
c5ox = np.loadtxt('c5ox_65.dat')
c5ox_E, c5ox_dos_u, c5ox_65_u, c5ox_dos_d, c5ox_65_d = tuple(c5ox[:, i] for i in range(5))
##plt.plot([c5ox_Ef, c5ox_Ef], [-70, 70], 'y--', linewidth =2.)
plt.plot(c5ox_E, c5ox_65_u, 'r-', linewidth=1.5)
#
SiBulk = np.loadtxt('state_density_SiBulk.dat')
E_Si, dos_Si = SiBulk[:, 0], SiBulk[:, 1]
plt.plot(E_Si, 10*dos_Si, 'b-', linewidth=2.0, label='bulk Si')
###qz = np.loadtxt('state_density_qz.dat')
##

plt.title('broken dimer defects (spin up)') 
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

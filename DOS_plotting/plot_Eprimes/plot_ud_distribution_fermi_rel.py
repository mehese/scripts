#! /usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np

all_lst = (c1_142_u, c1_144_u, c2_124_u, c2_125_u, c2_134_u, c3_81_u, c3_113_u, c3_128_u, c3_134_u, c3_135_u, c3_147_u, c3_148_u, c4_124_u, c4_125_u, c4_127_u, c4_130_u, c4_136_u, \
           c5_133_u, c5_135_u, c5_137_u,
           c6_125_u, c6_128_u, c6_131_u, c6_135_u, c6_136_u, c6_137_u, c6_144_u, c6_147_u,
           c2ox_84_u, c2ox_128_u, c2ox_136_u, c2ox_138_u, c2ox_148_u,
           c3ox_72_u, c3ox_97_u, c3ox_98_u, c3ox_136_u, c3ox_149_u, c3ox_153_u, c3ox_154_u, 
           c5ox_98_u, c5ox_141_u, c5ox_150_u, c5ox_151_u, c5ox_154_u) = (None,)*45



# CELL 1
c1_Ef = -2.34
c1 = np.loadtxt('c1_142_144.dat')
c1_E, c1_dos_u, c1_142_u, c1_144_u, c1_dos_d, c1_142_d, c1_144_d = tuple(c1[:, i] for i in range(7))
#plt.plot([c1_Ef, c1_Ef], [-70, 70], '-', color = '#662966', linewidth =2.)
plt.plot(c1_E - c1_Ef, c1_142_u, '-', color = '#662966', linewidth=1.5, label='C1')
plt.plot(c1_E - c1_Ef, c1_142_d, '-', color = '#662966', linewidth=1.5)
plt.plot(c1_E - c1_Ef, c1_144_u, '-', color = '#662966', linewidth=1.5)
plt.plot(c1_E - c1_Ef, c1_144_d, '-', color = '#662966', linewidth=1.5)

# CELL 2
c2_Ef = -2.68
c2 = np.loadtxt('c2_57_105_124.dat')
c2_E, c2_dos_u, _, _, c2_124_u, c1_dos_d, _, _, c2_124_d = tuple(c2[:, i] for i in range(9))
c2 = np.loadtxt('c2_125_134.dat')
c2_E, c2_dos_u, c2_125_u, c2_134_u, c1_dos_d, c2_125_d, c2_134_d = tuple(c2[:, i] for i in range(7))
#plt.plot([c2_Ef, c2_Ef], [-70, 70], '-', color = '#FF2966', linewidth =2.)
plt.plot(c2_E - c2_Ef,-c2_124_u, '-', color = '#FF2966', linewidth=1.5, label='C2')
plt.plot(c2_E - c2_Ef, c2_125_u, '-', color = '#FF2966', linewidth=1.5)
plt.plot(c2_E - c2_Ef, c2_134_u, '-', color = '#FF2966', linewidth=1.5)
plt.plot(c2_E - c2_Ef,-c2_124_d, '-', color = '#FF2966', linewidth=1.5)
plt.plot(c2_E - c2_Ef, c2_125_d, '-', color = '#FF2966', linewidth=1.5)
plt.plot(c2_E - c2_Ef, c2_134_d, '-', color = '#FF2966', linewidth=1.5)

## CELL 3
c3_Ef = -2.91
c3 = np.loadtxt('c3_81_113.dat')
c3_E, c3_dos_u, c3_81_u, c3_113_u, c3_dos_d, c3_81_d, c3_113_d = tuple(c3[:, i] for i in range(7))
c3 = np.loadtxt('c3_128_129_130_133.dat')
c3_E, c3_dos_u, c3_128_u, _, _, _, c3_dos_d, c3_128_d, _, _, _ = tuple(c3[:, i] for i in range(11))
c3 = np.loadtxt('c3_134_135_147_148.dat')
c3_E, c3_dos_u, c3_134_u, c3_135_u, c3_147_u, c3_148_u, c3_dos_d, c3_134_d, c3_135_d, c3_147_d, c3_148_d = tuple(c3[:, i] for i in range(11))
#plt.plot([c3_Ef, c3_Ef], [-70, 70], '-', color = '#CC9900', linewidth =2.)
plt.plot(c3_E - c3_Ef, c3_81_u, '-', color = '#CC9900', linewidth=1.5, label='C3')
plt.plot(c3_E - c3_Ef, c3_113_u, '-', color = '#CC9900', linewidth=1.5)
plt.plot(c3_E - c3_Ef, -c3_128_u, '-', color = '#CC9900', linewidth=1.5)
plt.plot(c3_E - c3_Ef, c3_134_u, '-', color = '#CC9900', linewidth=1.5)
plt.plot(c3_E - c3_Ef, c3_135_u, '-', color = '#CC9900', linewidth=1.5)
plt.plot(c3_E - c3_Ef, c3_147_u, '-', color = '#CC9900', linewidth=1.5)
plt.plot(c3_E - c3_Ef, -c3_148_u, '-', color = '#CC9900', linewidth=1.5)
plt.plot(c3_E - c3_Ef, c3_81_d, '-', color = '#CC9900', linewidth=1.5)
plt.plot(c3_E - c3_Ef, c3_113_d, '-', color = '#CC9900', linewidth=1.5)
plt.plot(c3_E - c3_Ef, -c3_128_d, '-', color = '#CC9900', linewidth=1.5)
plt.plot(c3_E - c3_Ef, c3_134_d, '-', color = '#CC9900', linewidth=1.5)
plt.plot(c3_E - c3_Ef, c3_135_d, '-', color = '#CC9900', linewidth=1.5)
plt.plot(c3_E - c3_Ef, c3_147_d, '-', color = '#CC9900', linewidth=1.5)
plt.plot(c3_E - c3_Ef, -c3_148_d, '-', color = '#CC9900', linewidth=1.5)

# CELL 4
c4_Ef = -2.84
c4 = np.loadtxt('c4_124_125_127.dat')
c4_E, c4_dos_u, c4_124_u, c4_125_u, c4_127_u, c4_dos_d, c4_124_d, c4_125_d, c4_127_d = tuple(c4[:, i] for i in range(9))
c4 = np.loadtxt('c4_130_136.dat')
c4_E, c4_dos_u, c4_130_u, c4_136_u, c4_dos_d, c4_130_d, c4_136_d = tuple(c4[:, i] for i in range(7))
#plt.plot([c4_Ef, c4_Ef], [-70, 70], '-', color='#1F7A7A', linewidth =2.)
plt.plot(c4_E - c4_Ef, c4_124_u, '-', color='#1F7A7A', linewidth=1.5, label='C4')
plt.plot(c4_E - c4_Ef, c4_125_u, '-', color='#1F7A7A', linewidth=1.5)
plt.plot(c4_E - c4_Ef, c4_127_u, '-', color='#1F7A7A', linewidth=1.5)
plt.plot(c4_E - c4_Ef, c4_130_u, '-', color='#1F7A7A', linewidth=1.5)
plt.plot(c4_E - c4_Ef, c4_136_u, '-', color='#1F7A7A', linewidth=1.5)
plt.plot(c4_E - c4_Ef, c4_124_d, '-', color='#1F7A7A', linewidth=1.5)
plt.plot(c4_E - c4_Ef, c4_125_d, '-', color='#1F7A7A', linewidth=1.5)
plt.plot(c4_E - c4_Ef, c4_127_d, '-', color='#1F7A7A', linewidth=1.5)
plt.plot(c4_E - c4_Ef, c4_130_d, '-', color='#1F7A7A', linewidth=1.5)
plt.plot(c4_E - c4_Ef, c4_136_d, '-', color='#1F7A7A', linewidth=1.5)

# CELL 5
c5_Ef = -2.18
c5 = np.loadtxt('c5_133_135_137.dat')
c5_E, c5_dos_u, c5_133_u, c5_135_u, c5_137_u, c5_dos_d, c5_133_d, c5_135_d, c5_137_d = tuple(c5[:, i] for i in range(9))
#plt.plot([c5_Ef, c5_Ef], [-70, 70], '-', color='#DB704D', linewidth =2.)
plt.plot(c5_E - c5_Ef, c5_133_u, '-', color='#DB704D', linewidth=1.5, label='C5')
plt.plot(c5_E - c5_Ef, c5_135_u, '-', color='#DB704D', linewidth=1.5)
plt.plot(c5_E - c5_Ef, c5_137_u, '-', color='#DB704D', linewidth=1.5)
plt.plot(c5_E - c5_Ef, c5_133_d, '-', color='#DB704D', linewidth=1.5)
plt.plot(c5_E - c5_Ef, c5_135_d, '-', color='#DB704D', linewidth=1.5)
plt.plot(c5_E - c5_Ef, c5_137_d, '-', color='#DB704D', linewidth=1.5)

# CELL 6
c6_Ef = -2.64
c6 = np.loadtxt('c6_125_128_129_131.dat')
c6_E, c6_dos_u, c6_125_u, c6_128_u, c6_129_u, c6_131_u, c6_dos_d, c6_125_d, c6_128_d, c6_129_d, c6_131_d = tuple(c6[:, i] for i in range(11))
c6 = np.loadtxt('c6_135_136_137_144.dat')
c6_E, c6_dos_u, c6_135_u, c6_136_u, c6_137_u, c6_144_u, c6_dos_d, c6_135_d, c6_136_d, c6_137_d, c6_144_d = tuple(c6[:, i] for i in range(11))
c6 = np.loadtxt('c6_146_147.dat')
c6_E, c6_dos_u, c6_146_u, c6_147_u, c6_dos_d, c6_146_d, c6_147_d = tuple(c6[:, i] for i in range(7))
#plt.plot([c6_Ef, c6_Ef], [-70, 70], '-', color='#669999', linewidth =2.)
plt.plot(c6_E - c6_Ef, c6_125_u, '-', color='#669999', linewidth=1.5, label='C6')
plt.plot(c6_E - c6_Ef, c6_128_u, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_131_u, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_135_u, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_136_u, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_137_u, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_144_u, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_147_u, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_125_d, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_128_d, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_131_d, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_135_d, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_136_d, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_137_d, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_144_d, '-', color='#669999', linewidth=1.5)
plt.plot(c6_E - c6_Ef, c6_147_d, '-', color='#669999', linewidth=1.5)


# CELL 2 OX
c2ox_Ef = -2.41
c2ox = np.loadtxt('c2ox_84_128_136_138.dat')
c2ox_E, c2ox_dos_u, c2ox_84_u, c2ox_128_u, c2ox_136_u, c2ox_138_u, c2ox_dos_d, c2ox_84_d,c2ox_128_d, c2ox_136_d, c2ox_138_d = tuple(c2ox[:, i] for i in range(11))
c2ox = np.loadtxt('c2ox_133_148_150.dat')
c2ox_E, c2ox_dos_u, _, c2ox_148_u, _, c2ox_dos_d, _, c2ox_148_d, _ = tuple(c2ox[:, i] for i in range(9))
#plt.plot([c2_Ef, c2_Ef], [-70, 70], '-', color='#993333', linewidth =2.)
plt.plot(c2ox_E - c2ox_Ef, c2ox_84_u , '-', color='#993333', linewidth = 1.5, label='C2ox')
plt.plot(c2ox_E - c2ox_Ef,-c2ox_128_u, '-', color='#993333', linewidth = 1.5)
plt.plot(c2ox_E - c2ox_Ef,-c2ox_136_u, '-', color='#993333', linewidth = 1.5)
plt.plot(c2ox_E - c2ox_Ef, c2ox_138_u, '-', color='#993333', linewidth = 1.5)
plt.plot(c2ox_E - c2ox_Ef,-c2ox_148_u, '-', color='#993333', linewidth = 1.5)
plt.plot(c2ox_E - c2ox_Ef, c2ox_84_d , '-', color='#993333', linewidth = 1.5)
plt.plot(c2ox_E - c2ox_Ef,-c2ox_128_d, '-', color='#993333', linewidth = 1.5)
plt.plot(c2ox_E - c2ox_Ef,-c2ox_136_d, '-', color='#993333', linewidth = 1.5)
plt.plot(c2ox_E - c2ox_Ef, c2ox_138_d, '-', color='#993333', linewidth = 1.5)
plt.plot(c2ox_E - c2ox_Ef,-c2ox_148_d, '-', color='#993333', linewidth = 1.5)
#
#
# CELL 3 OX
c3ox_Ef = -1.99
c3ox = np.loadtxt('c3ox_72_97_98_136.dat')
c3ox_E, c3ox_dos_u, c3ox_72_u, c3ox_97_u, c3ox_98_u, c3ox_136_u, c3ox_dos_d, c3ox_72_d,c3ox_97_d, c3ox_98_d, c3ox_136_d = tuple(c3ox[:, i] for i in range(11))
c3ox = np.loadtxt('c3ox_149_153.dat')
c3ox_E, c3ox_dos_u, c3ox_149_u, c3ox_153_u, c3ox_dos_d, c3ox_149_d,c3ox_153_d = tuple(c3ox[:, i] for i in range(7))
c3ox = np.loadtxt('c3ox_150_154.dat')
c3ox_E, c3ox_dos_u, _, c3ox_154_u, c3ox_dos_d, _,c3ox_154_d = tuple(c3ox[:, i] for i in range(7))
#plt.plot([c3ox_Ef, c3ox_Ef], [-70, 70], '-', color='#007A00', linewidth =2.)
plt.plot(c3ox_E - c3ox_Ef, c3ox_72_u,  '-', color='#007A00', linewidth = 1.5, label='C3ox')
plt.plot(c3ox_E - c3ox_Ef, c3ox_97_u,  '-', color='#007A00', linewidth = 1.5)
plt.plot(c3ox_E - c3ox_Ef, c3ox_98_u,  '-', color='#007A00', linewidth = 1.5)
plt.plot(c3ox_E - c3ox_Ef,-c3ox_136_u, '-', color='#007A00', linewidth = 1.5)
plt.plot(c3ox_E - c3ox_Ef, c3ox_149_u, '-', color='#007A00', linewidth = 1.5)
plt.plot(c3ox_E - c3ox_Ef, c3ox_153_u, '-', color='#007A00', linewidth = 1.5)
plt.plot(c3ox_E - c3ox_Ef, c3ox_154_u, '-', color='#007A00', linewidth = 1.5)
plt.plot(c3ox_E - c3ox_Ef, c3ox_72_d,  '-', color='#007A00', linewidth = 1.5)
plt.plot(c3ox_E - c3ox_Ef, c3ox_97_d,  '-', color='#007A00', linewidth = 1.5)
plt.plot(c3ox_E - c3ox_Ef, c3ox_98_d,  '-', color='#007A00', linewidth = 1.5)
plt.plot(c3ox_E - c3ox_Ef,-c3ox_136_d, '-', color='#007A00', linewidth = 1.5)
plt.plot(c3ox_E - c3ox_Ef, c3ox_149_d, '-', color='#007A00', linewidth = 1.5)
plt.plot(c3ox_E - c3ox_Ef, c3ox_153_d, '-', color='#007A00', linewidth = 1.5)
plt.plot(c3ox_E - c3ox_Ef, c3ox_154_d, '-', color='#007A00', linewidth = 1.5)
#
# CELL 5 OX
c5ox_Ef = -2.18
c5ox = np.loadtxt('c5ox_78_117_141_98.dat')
c5ox_E, c5ox_dos_u, _, _, c5ox_141_u, c5ox_98_u, c5ox_dos_d, _, _, c5ox_141_d, c5ox_98_d = tuple(c5ox[:, i] for i in range(11))
c5ox = np.loadtxt('c5ox_150_151_154.dat')
c5ox_E, c5ox_dos_u, c5ox_150_u, c5ox_151_u, c5ox_154_u, c5ox_dos_d, c5ox_150_d, c5ox_151_d, c5ox_154_d = tuple(c5ox[:, i] for i in range(9))
#plt.plot([c5ox_Ef, c5ox_Ef], [-70, 70], '-', color='#E60000', linewidth =2.)
plt.plot(c5ox_E - c5ox_Ef, c5ox_98_u, '-', linewidth=1.5, color='#E60000', label='C5ox')
plt.plot(c5ox_E - c5ox_Ef,-c5ox_141_u, '-', linewidth=1.5, color='#E60000')
plt.plot(c5ox_E - c5ox_Ef,-c5ox_150_u, '-', linewidth=1.5, color='#E60000')
plt.plot(c5ox_E - c5ox_Ef,-c5ox_151_u, '-', linewidth=1.5, color='#E60000')
plt.plot(c5ox_E - c5ox_Ef,-c5ox_154_u, '-', linewidth=1.5, color='#E60000')
plt.plot(c5ox_E - c5ox_Ef, c5ox_98_d, '-', linewidth=1.5, color='#E60000')
plt.plot(c5ox_E - c5ox_Ef,-c5ox_141_d, '-', linewidth=1.5, color='#E60000')
plt.plot(c5ox_E - c5ox_Ef,-c5ox_150_d, '-', linewidth=1.5, color='#E60000')
plt.plot(c5ox_E - c5ox_Ef,-c5ox_151_d, '-', linewidth=1.5, color='#E60000')
plt.plot(c5ox_E - c5ox_Ef,-c5ox_154_d, '-', linewidth=1.5, color='#E60000')


#SiBulk = np.loadtxt('state_density_SiBulk.dat')
#E_Si, dos_Si = SiBulk[:, 0], SiBulk[:, 1]
#plt.plot(E_Si, 10*dos_Si, 'b-', linewidth=2.0, label='bulk Si')
#qz = np.loadtxt('state_density_qz.dat')

plt.plot([0, 0], [-70, 70], '-', color='#E60000', linewidth =2.)

#total = c1_142_u + c1_144_u + \
#        c2_124_u + c2_125_u + c2_134_u + \
#        c3_81_u + c3_113_u + c3_128_u + c3_134_u + c3_135_u + c3_147_u + c3_148_u + \
#        c4_124_u + c4_125_u + c4_127_u + c4_130_u + c4_136_u + \
#        c5_133_u + c5_135_u + c5_137_u + \
#        c6_125_u + c6_128_u + c6_131_u + c6_135_u + c6_136_u + c6_137_u + c6_144_u + c6_147_u + \
#        c2ox_84_u + c2ox_128_u + c2ox_136_u + c2ox_138_u + c2ox_148_u + \
#        c3ox_72_u + c3ox_97_u + c3ox_98_u + c3ox_136_u + c3ox_149_u + c3ox_153_u + c3ox_154_u + \
#        c5ox_98_u + c5ox_141_u + c5ox_150_u + c5ox_151_u + c5ox_154_u

#plt.plot(c5ox_E, total, 'g-', linewidth=2., label='total E\'')

plt.title('E\' defects') 
plt.xlabel('Energy (eV)')
plt.xlim([-3, 2.8])
#plt.ylim([-70,70])
plt.gca().tick_params(width=2, labelsize=15)
for tick in plt.gca().xaxis.get_major_ticks()+plt.gca().yaxis.get_major_ticks():
    tick.label1.set_fontweight('bold')
for x in ['top', 'bottom', 'left', 'right']:
    plt.gca().spines[x].set_linewidth(2)
plt.legend(loc=2, fontsize=10)
plt.gcf().set_size_inches(20., 7.)
plt.savefig('test2png.png', dpi=100, bbox_inches='tight')
plt.show()

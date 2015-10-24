#! /usr/bin/python2.7

import sys
sys.path.append('../')
sys.path.append('../../')
from atom_pdos_getter import *
from astools.ReadWrite import ReadStruct
import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator




o = lambda k : k + 3.313

minor_locator = MultipleLocator(0.10)


cells_to_check = ['c1' , 'c2' , 'c3' , 'c4' , 'c5' , 'c6' , 'c2ox', 'c3ox', 'c5ox',
                  'c1p', 'c2p', 'c3p', 'c4p', 'c5p', 'c6p']

# Tuple of (Z_min, Z_max) cartesian coordinates for Si and SiO2 in bulk phase
limits = {
             'c1'  :{'blk': (1.60, 6.90), 'ox': (11.13, 17.30)},
             'c1p' :{'blk': (1.60, 6.90), 'ox': (11.13, 17.30)},
             'c2'  :{'blk': (1.90, 7.22), 'ox': (12.41, 20.00)},
             'c2p' :{'blk': (1.90, 7.22), 'ox': (12.41, 20.00)},
             'c3'  :{'blk': (2.30, 7.30), 'ox': (12.45, 19.45)},
             'c3p' :{'blk': (2.30, 7.30), 'ox': (12.45, 19.45)},
             'c4'  :{'blk': (2.20, 8.30), 'ox': (12.47, 19.27)},
             'c4p' :{'blk': (2.20, 8.30), 'ox': (12.47, 19.27)},
             'c5'  :{'blk': (2.00, 8.40), 'ox': (12.27, 19.25)},
             'c5p' :{'blk': (2.00, 8.40), 'ox': (12.27, 19.25)},
             'c6'  :{'blk': (1.90, 7.60), 'ox': (12.04, 19.52)},
             'c6p' :{'blk': (1.90, 7.60), 'ox': (12.04, 19.52)},
             'c2ox':{'blk': (4.50, 9.60), 'ox': (14.00, 21.50)},
             'c3ox':{'blk': (4.86, 9.00), 'ox': (14.40, 22.00)},
             'c5ox':{'blk': (4.75, 9.80), 'ox': (13.95, 21.80)},
            }


cells_to_check = ['c2'] 

for c in cells_to_check:
    print c
    y_b_u, y_b_d = np.zeros(600), np.zeros(600)
    y_o_u, y_o_d = np.zeros(600), np.zeros(600)
    y_i_u, y_i_d = np.zeros(600), np.zeros(600)

    x, y_u, y_d = get_at_pdos(c, 1, total=True) 

    #plt.plot(x, y_u, 'k-')
    #plt.plot(x, y_d, 'k-')

    s = ReadStruct('../../crystal_files/INPUT_'+c)
    for i, at in enumerate(s.atoms):
        # For atoms in the bulk phase of the Si substrate
        if at.species == 'Si' and limits[c]['blk'][0] < at.z < limits[c]['blk'][1]:
            _, u, d = get_at_pdos(c, i+1) 
            plt.plot(x, u, 'b-')
            plt.plot(x, d, 'b-')
        # For atoms in the bulk phase of the SiO2 layer
        elif at.species == 'O' and limits[c]['ox'][0] < at.z < limits[c]['ox'][1]:
            _, u, d = get_at_pdos(c, i+1) 
            plt.plot(x, u, 'r-')
            plt.plot(x, d, 'r-')

plt.xlabel('Energy [eV]')

plt.gcf().set_size_inches(20., 7.)
plt.savefig(c+'.png', dpi=100, bbox_inches='tight')

plt.show()

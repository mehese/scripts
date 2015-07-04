#! /usr/bin/python2.7
# -*- coding: utf-8 -*-p
from __future__ import print_function

def get_A(i, cell):
    """Returns the block of text containing the output of the out_gtensor files for a
    particular atom. It also creates a numpy matrix with the hyperfine A0 and
    anisotropic Axx matrices
    """
    import numpy as np
    import re

    with open('crystal_files/gtensor_'+cell, 'r') as f:
        Axx = np.zeros((3,3))
        A0  = np.zeros((3,3))
        txt = f.read()

        words = re.search(r'\sPOINT(\s+\w+){6}\n\s+'+str(i)
                +r'(.*\n){20}', txt)
        tens_inf = words.group()
        print(tens_inf)

        # generate ij for Axx components xx, yy, zz, xy, xz, yz
        cd = (i for i in [(0,0), (1, 1), (2, 2), (0, 1), (0,2), (1,2)])
        for val in tens_inf.split('\n')[4].split():
            try:
                v = float(val)
                ij = next(cd)
                Axx[ij] = v
                Axx[ij[::-1]] = v
            except:
                pass
            
        print('Axx tensor is\n', Axx)

        print('Density string:\n')
        # REGEX search for
        # 1 or more spaces, followed by the number given to the function
        # followed by 1-3 digits followed by 3 float
        words = re.search(r'\s+'+str(i)+
                r'\s+\d{1,3}\s+\w{1,2}(\s+[-]?\d{1,2}\.\d{1,8}){3}\s+'+
                r'(?P<density>[-]?\d{1,2}\.\d{1,9}E(\-|\+)\d{2})', txt)
        print(words.group())
        rho_m = float(words.group('density'))
        A0[0,0] = A0[1,1] = A0[2,2] = rho_m
        print('  ρ(m) =', rho_m, 'bohr⁻³')

        return Axx, rho_m
        
if __name__ == "__main__":
    print('Starting...\n')

    get_A(141, 'c5ox')
    #get_A(150, 'c2ox')
    #get_A(151, 'c2ox')
    #get_A(154, 'c2ox')

    print('Done')

#! /usr/bin/python3
# -*- coding: utf-8 -*-p

import numpy as np
from sys import argv
import re

# Returns the block of text containing the output of the out_gtensor files for a
# particular atom. At also creates a numpy matrix with the hyperfine A0 and
# anisotropic Axx matrices

print('Starting...\n')

def get_atom(filename, i):
    with open(filename, 'r') as f:
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
            
        print('Axx tensor is\n', Axx, 2*'\n')

        print('Density string:')
        # REGEX search for
        # 1 or more spaces, followed by the number given to the function
        # followed by 1-3 digits followed by 3 float
        words = re.search(r'\s+'+str(i)+
                r'\s+\d{1,3}\s+\w{1,2}(\s+[-]?\d{1,2}\.\d{1,8}){3}\s+'+
                r'(?P<density>[-]?\d{1,2}\.\d{1,9}E(\-|\+)\d{2})', txt)
        print(words.group())
        rho_m = float(words.group('density'))
        A0[0,0] = A0[1,1] = A0[2,2] = rho_m
        print('Spin density at the nuclear position\n    ρ(m) = ', rho_m, ' bohr⁻³')

        #print('  A0 =\n', A0)
        #print(np.linalg.eig(Axx))

        words = re.search(r'\s+'+str(i)+r'\s+'+str(i)+r'\s+\w{1,2}\s+\d{1,3}\s+'+
                r'[-]?\d{1,2}\.\d{1,7}\s+(?P<mT>[-]?\d{1,2}\.\d{1,9}E(\-|\+)\d{2}).*\n'
                , txt)

        print(words.group())
        AN = float(words.group('mT'))
        print('Hyperfine coupling constant\n\tAN = ', AN, ' mT','\n')
        
        
if __name__ == "__main__":
    for index in argv[2:]:
        print('\n'+30*'='+' ATOM {} '.format(index)+ 30*'='+'\n')
        get_atom(argv[1], index)

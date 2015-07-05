#! /usr/bin/python2.7
# -*- coding: utf-8 -*-p

from astools.ReadWrite import ReadStruct
from astools.analysis  import distance
from astools.operations import expand


def get_A0(i, cell):
    """ Get AN in MT from CRYSTAL cryapi ISO/ANISO output files. i -- atom
    index, cell is an identification string (like c3, c4p, c2ox)
    (int, str) -> float
    """
    import re
    import os
    path = os.path.dirname(os.path.realpath(__file__))
    A0 = None

    try:
        f = open(path+'/crystal_files/gtensor_'+cell, 'r')
    except IOError:
        print 'No file '+path+'crystal_files/gtensor_'+cell+' found :('
        return
    except:
        print r'¯\_(ツ)_/¯ Dunno whut happened'
    
    # A line that has twice the index, 1-2 letters with, atomic mass, nuclear g
    # factor and AN (mT), AN (MHz) and AN (whatever)
    regex = r'^\s+'+str(i)+r'\s+'+str(i)+r'\s+\w{1,3}\s+\d{1,3}\s+'+\
            r'[-]?\d{1,3}\.\d{2,10}\s+(?P<AmT>[-]?\d{1,4}\.\d{2,10}E[-+]\d{2})'

    result = re.search(regex, f.read(), re.M)

    #print result.group()
    A0 = float(result.group('AmT'))
 
    return A0

def get_spin_mom(i, cell):
    """ Given an atom number and a an identification string (like c1, c2ox, c5p
    ...) it opens the corresponding output file, scans through it, and returns
    the spin momentum on that atom at the final SCF step
    (int, str) -> float
    """
    import re
    import os
    path = os.path.dirname(os.path.realpath(__file__))

    try:
        f = open(path+'/crystal_files/OUTPUT_'+cell, 'r')
    except IOError:
        print 'No file '+path+'/crystal_files/OUTPUT_'+cell+' found :('
        return
    except:
        print r'¯\_(ツ)_/¯ Dunno whut happened'
    
    # Stuff that is preceded by a line with TOTAL ATOMIC SPINS and followed by a
    # line with TTTTTTT and starts with some spaces, maybe a minus, and a digit
    regex = r'(?<=^\sTOTAL ATOMIC SPINS  :\n)(^\s{1,6}[-]?\d.*\n)*(?=^\sTT)'
    #result = re.search(regex, f.read(), re.M)

    # Generates an iterator for the matched strings
    result = re.finditer(regex, f.read(), flags=re.M)
    # Get to the final one
    while True:
        try:
            x = next(result)
        except StopIteration:
            break
        except:
            print r'¯\_(ツ)_/¯ Dunno whut happened'

    # return n-th element
    vals = map(float, x.group().replace('\n', '').split())
    f.close()
    if i <= len(vals):
        return vals[i-1]
    else:
        print "i larger than number of values extracted!!!"

def get_similar(at, str_x):
    """ Find equivalent atoms in structures
    (atom, AtomStruct) -> int, Atom

    Given an atom at an index i = index + 1, the routine looks for the closest
    match in str_out.

    WARNING -- DOESN'T CHECK NEAR BOX EDGES, SO IT MIGHT POSE PROBLEMS FOR
    ATOMS NEAR THE BOX BOUNDARIES
    """
    d_min, i_x, at_x = 1e+10, None, None
    for i in range(len(str_x)):
        d_ = distance(at, str_x.atoms[i])
        if (d_ < d_min) and (str_x.atoms[i].species == at.species):
            d_min = d_
            at_x = str_x.atoms[i]
            i_x = i

    return i_x, at_x

if __name__== "__main__":
    from random import randint

    print get_A0(1, 'c5ox')
    print get_A0(11, 'c5ox')

    print 'Testing get_similar 10 times...'
    s = ReadStruct('crystal_files/INPUT_c2')
    s2 = ReadStruct('crystal_files/INPUT_c2p')
    for _ in range(5):
        ii = randint(0, len(s)-1)
        print ii, 
        print s.atoms[ii]
        i, ax = get_similar(s.atoms[ii], s2)
        print i - len([p for p in s2.atoms if p.species=='H'])
        print i, ax

    print get_spin_mom(4, 'c5')

    print '\nDone'

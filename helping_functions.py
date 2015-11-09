#! /usr/bin/python2.7
# -*- coding: utf-8 -*-p

from astools.ReadWrite import ReadStruct
from astools.analysis  import distance, neighbour, dist
from astools.operations import expand


offsets = {
            'c1':{'VBM':-3.20, 'CBM':-2.02, 'Ef':-2.34},
            'c2':{'VBM':-3.46, 'CBM':-1.64, 'Ef':-2.70},
            'c3':{'VBM':-3.97, 'CBM':-2.00, 'Ef':-2.94},
            'c4':{'VBM':-3.31, 'CBM':-2.12, 'Ef':-2.84},
            'c5':{'VBM':-3.52, 'CBM':-1.55, 'Ef':-2.55},
            'c6':{'VBM':-3.49, 'CBM':-1.66, 'Ef':-2.64},
            'c2ox':{'VBM':-3.69, 'CBM':-1.46, 'Ef':-2.67},
            'c3ox':{'VBM':-3.44, 'CBM':-1.60, 'Ef':-2.34},
            'c5ox':{'VBM':-3.67, 'CBM':-1.81, 'Ef':-2.58},
            'hfo2si_c1':  {'VBM': -2.54, 'CBM': -0.62, 'Ef':-1.2}, 
            'hfo2si_c1ox':{'VBM': -2.62, 'CBM': -0.74, 'Ef':-1.15}, 
            'hfo2si_c2ox':{'VBM': -2.48, 'CBM': -0.32, 'Ef':-0.52}, 
            'hfo2si_c3ox':{'VBM': -2.43, 'CBM': -0.04, 'Ef':-0.82}

          }

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

def neighbours_from_file(i, cell):
    """ Given an atom number and a an identification string (like c1, c2ox, c5p
    ...) it opens the corresponding output file, scans through it, and returns
    the printed list of neighbours for the given atom
    (int, str) -> dist list
    """
    import re
    import os
    path = os.path.dirname(os.path.realpath(__file__))

    try:
        f = open(path+'/neighbour_files/OUTPUT_'+cell, 'r')
    except IOError:
        print 'No file '+path+'/neighbour_files/OUTPUT_'+cell+' found :('
        return
    except:
        print r'¯\_(ツ)_/¯ Dunno whut happened'


    nbs = []
    regex = r'^\s+'+str(i)+r'\s+[A-Z]{1,3}\s+\d{1,2}\s+(?P<distance>\d\.\d{3,6})'+\
            r'\s+\d+\.\d+\s+(?P<other_index>\d{1,3})\s+(?P<species>[A-Z]{1,3})\s+[-]?[1,0]((\s|-)[1,0]){2}$'

    result = re.findall(regex, f.read(), flags=re.M)
    for line in result:
        d, ind, species = float(line[0]), int(line[1]), line[2]
        species = species[0]+species[1:].lower()
        elem = dist(species, d)
        nbs.append(elem)

    return nbs
 

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

def get_similar(at, str_x, verbose=False):
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
    if verbose:
        print 'd({}, {}) = {}'.format(at, at_x, d_min)
    return i_x, at_x

if __name__== "__main__":
    from random import randint

    #print neighbours_from_file(16, 'hfo2si_c2ox')


    print get_spin_mom(65, 'c5')

    print '\nDone'

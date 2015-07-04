#! /usr/bin/python2.7
# -*- coding: utf-8 -*-p

from astools.ReadWrite import ReadStruct
from astools.analysis  import distance
from astools.operations import expand

def get_spin_mom(i, cell):
    import re

    try:
        f = open('crystal_files/OUTPUT_'+cell, 'r')
    except IOError:
        print 'No file crystal_files/OUTPUT_'+cell+' found :('
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
    #from random import randint
    #print 'Testing 10 times...'
    #s = ReadStruct('crystal_files/INPUT_c2')
    #s2 = ReadStruct('crystal_files/INPUT_c2p')
    #for _ in range(10):
    #    ii = randint(0, len(s))
    #    i, ax = get_similar(s.atoms[ii], s2)
    #    print i - len([p for p in s2.atoms if p.species=='H'])
    #    print ii, s.atoms[ii]
    #    print i, ax

    print get_spin_mom(1, 'c5')

    print '\nDone'

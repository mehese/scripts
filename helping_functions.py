#! /usr/bin/python 2.7

from astools.ReadWrite import ReadStruct
from astools.operations import expand

def get_similar(index, str_in, str_out):
    """ Find equivalent atoms in structures
    (int, AtomStruct, AtomStruct) -> int, Atom

    Given an atom at an index i = index + 1, the routine looks for the closest
    match in str_out.

    """
    pass

if __name__== "__main__":
    print expand.__doc__
    s = ReadStruct('inputs/INPUT_c2')
    s2 = ReadStruct('inputs/INPUT_c2p')
    get_similar(73, s, s2)
    print 'Done'

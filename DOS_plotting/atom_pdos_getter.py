#! /usr/bin/python2.7

def get_at_pdos(nm, no, passified=False, verbose=False, total=False,
                pdos_dir = '/home/eric/Dropbox/interfaces/PDOS_files/'):

    """Returns E, pdos
    nm -- cell number, eg c2 -- cell 2, c2ox -- cell 2 oxidised
    no -- id number 
    passified -- look for passified cell

    """
    import numpy as np


    file_name = pdos_dir + nm + ('p' if passified else '') + '_' + \
                str(no) + '.dat'
    if verbose:
        print 'Opening...', file_name

    try:
        open(file_name, 'r')
    except IOError:
        print '\nERROR: File {} not found !\n'.format(file_name)
        return
    except:
        print '\n!!!  UNKNOWN ERROR !!!\n'.format(file_name)
        return
        

    dat = np.loadtxt(file_name)
    E, total_dos_u, pdos_u, total_dos_d, pdos_d = tuple(dat[:, i] for i in range(5)) 

    if total:
        return E, total_dos_u, total_dos_d

    return E, pdos_u, pdos_d


if __name__ ==  "__main__":
    import matplotlib.pyplot as plt
    x, y_u, y_d = get_at_pdos('c3', 73, passified=False, verbose=True)
    plt.plot(x, y_u, '-')
    plt.plot(x, y_d, '-')
    x, y_u, y_d = get_at_pdos('c3', 73, passified=False, verbose=True, total=True)
    plt.plot(x, y_u, '-')
    plt.plot(x, y_d, '-')
    #x, y = get_at_pdos('c2ox', 33, verbose=True)
    plt.show()

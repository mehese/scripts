#! /usr/bin/python2.7

# declare Ef dictionary (values given in eV)
Ef = {'c1'  : -2.3426257615,
      'c2'  : -2.6798582799,
      'c3'  : -2.9144629464,
      'c4'  : -2.8464169090,
      'c5'  : -2.1814821940,
      'c6'  : -2.6493136764,
      'c1p' : None,
      'c2p' : -2.4503246978,
      'c3p' : -3.1518898092,
      'c4p' : -2.6477992909,
      'c5p' : -1.8596621865,
      'c6p' : -2.2754045847,
      'c2ox': -2.4185825506,
      'c3ox': -1.9995085485,
      'c5ox': -2.0594598285,
     }

def integrate_dos(x_, y_u, y_d, emin=-3.313, emax=-2.27):
    """Simply returns the integrated DOS between emin and emax
    Default values are bulk Si limits
    """
    import numpy as np

    imin = np.where(emin < x_)[0].item(0)
    imax = np.where(emax > x_)[0].item(-1)

    x_, y_u, y_d = x_[imin:imax], y_u[imin:imax], y_d[imin:imax]

    return np.trapz(y_u, x=x_) + np.trapz(-y_d, x=x_)


def get_at_pdos(nm, no, passified=False, verbose=False, total=False,
                pdos_dir = '/home/eric/Dropbox/interfaces/PDOS_files/'):

    """Returns E, pdos
    nm -- cell number, eg c2 -- cell 2, c2ox -- cell 2 oxidised
    no -- id number 
    passified -- look for passified cell

    """
    import numpy as np

    if (('Si' in nm) or ('si' in nm)) and ('hfo' not in nm):
        dat = np.loadtxt(pdos_dir+'SiBulk.dat')
        E, dos_u, dos_d = dat[:, 0], dat[:, 1], -dat[:, 1]
        return E, dos_u, dos_d 
        

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

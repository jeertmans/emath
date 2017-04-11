import cmath as cm

import matplotlib.pyplot as plt

import sympy as sy

from sympy.abc import x



def cround(c,ndigits=10):

    """

    Uses the builtin round() method to round both real and imaginary values of the complex(es).

    :param c: the complex(es), a 0, 1 or 2D list.

    :param ndigits: the number of decimals -1 before rounding.

    :return: the complex(es) rounded.

    """

    if isinstance(c, tuple) or isinstance(c, list):

        if isinstance(c[0], tuple) or isinstance(c[0], list):

            return [[round(z.real, ndigits) + round(z.imag, ndigits) * 1j for z in c_] for c_ in c]

        else:

            return [round(z.real,ndigits)+round(z.imag,ndigits)*1j for z in c]

    else:

        return round(c.real,ndigits)+round(c.imag,ndigits)*1j



def croots(c,n=1):

    """

    Returns the n nth roots of the complex c (accepts only real values too) in a list.

    :param c: the complex(es), a 0 or 1D list.

    :param n: a non nul integer. Default is 1.

    :return: the root(s) of the complex(es).

    """

    if n==1:

        return c

    if isinstance(c, tuple) or isinstance(c, list):

        return [[cm.rect(pow(abs(z), 1 / n), cm.phase(z) / n + 2 * k * cm.pi / n) for k in range(0, n)] for z in c]

    else:

        r_n = pow(abs(c),1/n)

        phi = cm.phase(c)

        return [cm.rect(r_n,phi/n+2*k*cm.pi/n) for k in range(0,n)]



def cabs(c):

    """

    Apply the abs() builtin method to all the real and imaginary values separately.

    :param c: the complex(es), a 0, 1 or 2D list.

    :return: the complex(es) with only positive values. 

    """

    if isinstance(c,tuple) or isinstance(c,list):

        return [cabs(z) for z in c]

    else:

        return abs(c.real) + abs(c.imag)*1j



def norm(c):

    """

    Apply the abs() builtin method to all the complexes separately.

    :param c: the complex(es), a 0, 1 or 2D list.

    :return: a list or single value with the same shape as c but containing the norm of all complexes. 

    """

    if isinstance(c,tuple) or isinstance(c,list):

        return [abs(z) for z in c]

    else:

        return abs(c)



def cmin(c):

    """

    Give the length of complex with the minimal length among all the complexes.

    :param c: the complex(es), a 0, 1 or 2D list.

    :return: a float corresponding to the minimal length

    """

    if isinstance(c,tuple) or isinstance(c,list):

        return min(norm(c))

    else:

        return c



def cmax(c):

    """

    Give the length of complex with the maximal length among all the complexes.

    :param c: the complex(es), a 0, 1 or 2D list.

    :return: a float corresponding to the maximal length

    """

    if isinstance(c,tuple) or isinstance(c,list):

        return max(norm(c))

    else:

        return c



def show(c,auto_scaling=True):

    """

    Uses matplotlib module to plot all the complexes as vectors with tail = (0,0) and head = (real,imaginary).

    :param c: the complex(es), a 0 or 1D list.

    :param auto_scaling: If True, will set the scaling such that y_scale == x_scale and all the vectors

    will be visible.

    :return: None

    """

    ax = plt.gca()

    ax.quiver([0 for x in c], [0 for x in c], [x.real for x in c], [x.imag for x in c], scale=1, units='xy')

    max_c = cmax(c)

    if auto_scaling:

        ax.set_xlim([-max_c,max_c])

        ax.set_ylim([-max_c,max_c])

    plt.show()



def polynomial(c):

    """

    Uses the module sympy to produce a new polynomial witch has roots c

    :param c: the complex(es), a 0 or 1D list.

    :return: a symbolic polynomial from sympy's module

    """

    if isinstance(c,tuple) or isinstance(c,list):

        sol = 1

        for z in c:

            sol = sol*(x-z)

        return sy.expand(sol)

    else:

        return x-c

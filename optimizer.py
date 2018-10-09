import numpy as np
import scipy.optimize as so
import sys
import argparse

steps = [] #store iterarion steps

def S(x):
    _x = x[0]
    _y = x[1]
    return 2. * _x ** 2 + 3. / 2. * _y ** 2 + _x * _y - _x - 2 * _y + 6


def getIterationSteps(x):
    steps.append(x)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Find the minimum of a given function using 2 methods:")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-BFGS", "--BFGS", action="store_true", help="use BFGS method")
    group.add_argument("-CG", "--CG", action="store_true", help="use Conjugate Gradient method")
    args = parser.parse_args()
    if args.BFGS:
        _method = 'BFGS'
    if args.CG:
        _method = 'CG'

    x = np.random.rand(2)
    ret = so.minimize(S,
                      x,
                      method=_method,
                      callback=getIterationSteps,
                      tol=1e-13)

    print(steps)

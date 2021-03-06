"""
brownian() implements one dimensional Brownian motion (i.e. the Wiener process).
"""

# File: brownian.py
# From SciPy examples: http://scipy-cookbook.readthedocs.io/items/BrownianMotion.html

from math import sqrt
from scipy.stats import norm
import numpy as np


def brownian(x0, n:int, dt, delta, out=None):
    """
    Generate an instance of Brownian motion (i.e. the Wiener process):

        X(t) = X(0) + N(0, delta**2 * t; 0, t)

    where N(a,b; t0, t1) is a normally distributed random variable with mean a and
    variance b.  The parameters t0 and t1 make explicit the statistical
    independence of N on different time intervals; that is, if [t0, t1) and
    [t2, t3) are disjoint intervals, then N(a, b; t0, t1) and N(a, b; t2, t3)
    are independent.

    Written as an iteration scheme,

        X(t + dt) = X(t) + N(0, delta**2 * dt; t, t+dt)


    If `x0` is an array (or array-like), each value in `x0` is treated as
    an initial condition, and the value returned is a numpy array with one
    more dimension than `x0`.

    x0 : float or numpy array (or something that can be converted to a numpy array
         using numpy.asarray(x0)).
        The initial condition(s) (i.e. position(s)) of the Brownian motion.
    n : int
        The number of steps to take.
    dt : float
        The time step.
    delta : float
        delta determines the "speed" of the Brownian motion.  The random variable
        of the position at time t, X(t), has a normal distribution whose mean is
        the position at time t=0 and whose variance is delta**2*t.
    out : numpy array or None
        If `out` is not None, it specifies the array in which to put the
        result.  If `out` is None, a new numpy array is created and returned.

    A numpy array of floats with shape `x0.shape + (n,)`.

    Note that the initial value `x0` is not included in the returned array.
    """

    x0 = np.asarray(x0)

    # For each element of x0, generate a sample of n numbers from a
    # normal distribution.
    r = norm.rvs(size=x0.shape + (n,), scale=delta*sqrt(dt))

    # If `out` was not given, create an output array.
    if out is None:
        out = np.empty(r.shape)

    # This computes the Brownian motion by forming the cumulative sum of
    # the random samples.
    np.cumsum(r, axis=-1, out=out)

    # Add the initial condition.
    out += np.expand_dims(x0, axis=-1)

    return out


# Adapted from the NumPy Geometric Brownian Motion function by Yves Hilpisch:
# https://www.wakari.io/sharing/bundle/yves/Yves_Hilpisch_Python_in_Finance_Talk_NYC?has_login=False
def geometric_brownian(S0, mu, sigma, dt, num_paths: int, num_steps: int):
    """
    :param S0: the initial value
    :param mu: the percentage drift
    :param sigma: the percentage volatility
    :param dt: the time-step (fraction of a year)
    :param num_paths: the number of paths to generate
    :param num_steps: the number of steps to generate
    :return: an array with the paths
    """
    S = S0 * np.exp(np.cumsum((mu - 0.5 * sigma ** 2) * dt
                + sigma * np.sqrt(dt) * np.random.standard_normal((num_steps, num_paths)), axis=0))
    return S.transpose()


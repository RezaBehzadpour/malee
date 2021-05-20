"""`financial_modeling` is a collection of essential financial modeling 
functions, ready to be used for academic and educational 
use cases. 
"""
from __future__ import division, absolute_import, print_function
from math import log, e


def ar(vi, vf, D=0, W=0):
    """The Arithmetic Return is the simplest way of calculating
    the rate of return on an investment. To calculate it,
    you need the amount of growth, which is simply the final value `Vf`
    minus the initial value `Vi`. Then you just divide the amount of growth
    by the initial amount.

    Args:
        vi: Initial value of investment
        vf: Final value of investment
        D: The total deposit made into the investment
        W: Total of any withdrawals

    Returns:
        The arithmetic return of a given investment.

    Example:
        By providing initial and final value of investment
        you can get the percentage return of your investment:

        >>> import financial_modeling as fm
        >>> fm.ar(100, 140)
        0.4
    """
    return (vf - D + W - vi) / vi


def lr(vi, vf, t=1):
    """The logarithmic return is a way of calculating
    the rate of return on an investment. To calculate it
    you need the inital value of the investment `Vi`,
    the final value `Vf` and the number of time periods `t`.
    You then take the natural logarithm of `Vf` divided by `Vi`,
    and divide the result by `t`.

    Args:
        vi: Initial value of investment
        vf: Final value of investment
        t: Number of time periods

    Returns:
        The logarithmic return of a given investment

    Example:
        By providing initial and final value of investment
        you can get the percentage of logarithmic return of
        your investment:

        >>> import financial_modeling as fm
        >>> fm.lr(100, 140)
        0.3364722366212129
    """
    return log(vf / vi, e) / t


def aar(rors):
    """The Arithmetic Average Return is a way of calculating
    an average return for an investment over multiple periods.
    It is simply the average of all the arithmetic returns for
    each period. To calculate it, you add up the individual
    Arithmetic Return values, rarith, for each period, then
    divide by the number of periods `n`.

    Args:
        rors: List of all rate of returns over multiple time periods

    Returns:
        The arithmetic average return of a given investment

    Example:
        Here's how you can calculate the arithmetic average
        return by providing a list of individual returns in
        multiple periods of time:

        >>> import financial_modeling as fm
        >>> fm.aar([.1, -.05, .07])
        0.04
    """
    R = 0
    for ror in rors:
        R += ror
    R /= len(rors)
    return R


def twr(rors):
    """The Time-Weighted Return (also called the
    Geometric Average Return) is a way of calculating
    the rate of return for an investment when there are
    deposits and withdrawals (cash flows) during the period.
    You often want to exclude these cash flows so that we can
    find out how well the underlying investment has performed.

    Args:
        rors: List of all rors over multiple time periods

    Returns:
        The time-weighted return of a given investment

    Example:
        By providing a list of rate of returns you can
        calculate the time-weighted return based on that
        list:

        >>> import financial_modeling as fm
        >>> fm.aar([.10, -.05, .12])
        0.056666666666666664
    """
    Rtw = 1
    for ror in rors:
        Rtw *= 1 + ror
    return Rtw - 1


def an(Rtw, y=1):
    """The time-weighted return expressed as an annual rate,
    then you need to annualize it using this function.

    Args:
        Rtw: Time-weighted return
        y: Number of years for the period

    Returns:
        Time-weighted return expressed as an annual rate

    Example:
        If you want to express your time-weighted return
        as an annual rate, here's how you can do it for 2
        years period:

        >>> import financial_modeling as fm
        >>> fm.an(0.3662, 2)
        0.1688455843266894
    """
    return (1 + Rtw) ** (1 / y) - 1


def pv(Rt, i, t=1):
    """Present value accounts for the current value of a future
    sum of money or stream of cash flows given a specified
    rate of return.

    Args:
        Rt: Return we get at time `t`
        i: Discount rate
        t: Time we get the return

    Returns:
        Present value

    Example:
        Here's a simple example of how you can calculate
        the present value of a given return and time period:

        >>> import financial_modeling as fm
        >>> fm.pv(1030, 0.05, 1)
        980.952380952381
    """
    return Rt / ((1 + i) ** t)


def npv(Rn, i, i0, pe=0):
    """Net present value (NPV) is the difference between
    the present value of cash inflows and the present value
    of cash outflows over a period of time.

    Args:
        Rn: Expected return list
        i: Discount rate
        i0: Initial amount invested
        pe: Profit or expense at the end of investment

    Returns:
        Net present value

    Example:
        Given the expected return list `Rn`, `i` as
        discount rate, and `i0` as initial amount invested
        you can calcuate NPV like this:

        >>> import financial_modeling as fm
        >>> fm.npv([5000, 8000, 12000, 30000], 0.05, 40000)
        7065.266015703324
    """
    npv_sum = 0
    for idx, Ri in enumerate(Rn):
        if Ri == Rn[-1] and pe != 0:
            npv_sum += Ri + pe / ((1 + i) ** (idx + 1))
        else:
            npv_sum += Ri / ((1 + i) ** (idx + 1))
    return npv_sum - i0


def gm(rors):
    """The Geometric Mean is the average of a set of products,
    the calculation of which is commonly used to determine the
    performance results of an investment or portfolio. It is
    technically defined as "the nth root product of n numbers."

    Args:
        rors: List of all rors over multiple time periods

    Returns:
        The Geometric Mean of a list of returns

    Example:
        By providing a list of returns you can calculate
        the Geometric Mean of the given list:

        >>> import financial_modeling as fm
        >>> fm.gm([.14, .06, -.05, .20])
        0.08337520558323552
    """
    total = 1
    n = len(rors)
    for ror in rors:
        total *= 1 + ror
    return total ** (1 / n) - 1

"""
Tool life and machining economy.

Taylor's tool life equation relates cutting speed vc (m/min) and tool life
T (min):

    vc * T**n = C

n is the Taylor exponent (roughly 0.1 to 0.15 for HSS, 0.2 to 0.4 for
carbide) and C is the cutting speed that gives a tool life of 1 minute.

Machining economy (classic Taylor/Gilbert result): the tool life that
minimises cost per part is

    T_econ = (1/n - 1) * (t_ct + C_t / M)

where t_ct is the tool change time (min), C_t the cost of one cutting edge
and M the machine plus operator cost per minute. The tool life that
maximises output (minimum time per part) is

    T_prod = (1/n - 1) * t_ct
"""

import math

from ._validate import positive


def tool_life(vc, C, n):
    """
    Tool life T from Taylor's equation, T = (C / vc)**(1/n).

    Returns:
        float: T in min.
    """
    positive(vc=vc, C=C, n=n)
    return (C / vc) ** (1 / n)


def speed_for_tool_life(T, C, n):
    """
    Cutting speed that gives tool life T, vc = C / T**n.

    Returns:
        float: vc in m/min.
    """
    positive(T=T, C=C, n=n)
    return C / T**n


def fit_taylor(vc1, T1, vc2, T2):
    """
    Taylor constants from two tool life tests.

    Parameters:
        vc1, T1: first test (m/min, min).
        vc2, T2: second test (m/min, min).

    Returns:
        tuple: (n, C)
    """
    positive(vc1=vc1, T1=T1, vc2=vc2, T2=T2)
    if vc1 == vc2 or T1 == T2:
        raise ValueError("The two tests must use different speeds and give different tool lives.")
    n = math.log(vc1 / vc2) / math.log(T2 / T1)
    C = vc1 * T1**n
    return n, C


def economic_tool_life(n, t_ct, C_t, M):
    """
    Tool life for minimum cost per part.

    Parameters:
        n (float): Taylor exponent.
        t_ct (float): Tool change time, min.
        C_t (float): Cost per cutting edge (currency).
        M (float): Machine and operator rate (currency per min).

    Returns:
        float: T in min.
    """
    positive(n=n, t_ct=t_ct, C_t=C_t, M=M)
    if n >= 1:
        raise ValueError("Taylor exponent n must be below 1.")
    return (1 / n - 1) * (t_ct + C_t / M)


def max_production_tool_life(n, t_ct):
    """
    Tool life for minimum time per part (maximum output).

    Returns:
        float: T in min.
    """
    positive(n=n, t_ct=t_ct)
    if n >= 1:
        raise ValueError("Taylor exponent n must be below 1.")
    return (1 / n - 1) * t_ct


def cost_per_part(Tc, T, t_ct, C_t, M, t_other=0.0):
    """
    Cost per part for a single operation.

    cost = M * (t_other + Tc) + (Tc / T) * (M * t_ct + C_t)

    Parameters:
        Tc (float): Cutting time per part, min.
        T (float): Tool life, min.
        t_ct (float): Tool change time, min.
        C_t (float): Cost per cutting edge.
        M (float): Machine and operator rate per min.
        t_other (float): Non-cutting time per part (loading, rapids), min.

    Returns:
        float: Cost per part (same currency as C_t and M).
    """
    positive(Tc=Tc, T=T, M=M)
    return M * (t_other + Tc) + (Tc / T) * (M * t_ct + C_t)

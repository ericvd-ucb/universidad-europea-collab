"""
Drilling formulas (metric).

    vc  = pi * Dc * n / 1000                    m/min
    n   = vc * 1000 / (pi * Dc)                 rpm
    vf  = fn * n                                mm/min
    Q   = vc * Dc * fn / 4                      cm^3/min
    hex = (fn / 2) * sin(kr)                    mm   (two cutting edges)
    Pc  = fn * vc * Dc * kc / (240 * 10^3)      kW
    Mc  = Pc * 30 * 10^3 / (pi * n)             Nm
    Ff  ~ 0.5 * kc * (Dc / 2) * fn * sin(kr)    N
    Tc  = lm / vf                               min

For a twist drill, kr is half the point angle (70 degrees for a 140 degree point).
"""

import math

from ._validate import positive, angle


def cutting_speed(Dc, n):
    """
    Cutting speed vc at the drill periphery.

    Parameters:
        Dc (float): Drill diameter, mm.
        n (float): Spindle speed, rpm.

    Returns:
        float: vc in m/min.
    """
    positive(Dc=Dc, n=n)
    return math.pi * Dc * n / 1000


def spindle_speed(vc, Dc):
    """
    Spindle speed n.

    Parameters:
        vc (float): Cutting speed, m/min.
        Dc (float): Drill diameter, mm.

    Returns:
        float: n in rpm.
    """
    positive(vc=vc, Dc=Dc)
    return vc * 1000 / (math.pi * Dc)


def penetration_rate(fn, n):
    """
    Penetration rate (feed speed) vf.

    Parameters:
        fn (float): Feed per revolution, mm/r.
        n (float): Spindle speed, rpm.

    Returns:
        float: vf in mm/min.
    """
    positive(fn=fn, n=n)
    return fn * n


def metal_removal_rate(vc, Dc, fn):
    """
    Metal removal rate Q for solid drilling.

    Returns:
        float: Q in cm^3/min.
    """
    positive(vc=vc, Dc=Dc, fn=fn)
    return vc * Dc * fn / 4


def chip_thickness(fn, kr=70.0):
    """
    Chip thickness per cutting edge, hex = (fn / 2) * sin(kr).

    The feed per revolution is shared between two edges. Use this as hm
    when calculating kc for drilling.

    Returns:
        float: Chip thickness in mm.
    """
    positive(fn=fn)
    angle("kr", kr)
    return fn / 2 * math.sin(math.radians(kr))


def net_power(fn, vc, Dc, kc):
    """
    Net power Pc.

    Parameters:
        fn (float): Feed per revolution, mm/r.
        vc (float): Cutting speed, m/min.
        Dc (float): Drill diameter, mm.
        kc (float): Specific cutting force, N/mm^2.

    Returns:
        float: Pc in kW.
    """
    positive(fn=fn, vc=vc, Dc=Dc, kc=kc)
    return fn * vc * Dc * kc / (240 * 10**3)


def torque(Pc, n):
    """
    Torque Mc.

    Returns:
        float: Mc in Nm.
    """
    positive(Pc=Pc, n=n)
    return Pc * 30 * 10**3 / (math.pi * n)


def feed_force(kc, Dc, fn, kr=70.0):
    """
    Approximate feed (thrust) force Ff = 0.5 * kc * (Dc / 2) * fn * sin(kr).

    Returns:
        float: Ff in N.
    """
    positive(kc=kc, Dc=Dc, fn=fn)
    angle("kr", kr)
    return 0.5 * kc * (Dc / 2) * fn * math.sin(math.radians(kr))


def machining_time(lm, vf):
    """
    Machining time Tc.

    Parameters:
        lm (float): Hole depth plus approach, mm.
        vf (float): Penetration rate, mm/min.

    Returns:
        float: Tc in min.
    """
    positive(lm=lm, vf=vf)
    return lm / vf

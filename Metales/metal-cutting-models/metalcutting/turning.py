"""
General turning formulas (metric).

    vc  = pi * Dm * n / 1000                  m/min
    n   = vc * 1000 / (pi * Dm)               rpm
    Q   = vc * ap * fn                        cm^3/min
    hex = fn * sin(kr)                        mm
    Pc  = vc * ap * fn * kc / (60 * 10^3)     kW
    Tc  = lm / (fn * n)                       min
    Rmax = fn^2 / (8 * re) * 1000             micrometres (theoretical)
"""

import math

from ._validate import positive, angle


def cutting_speed(Dm, n):
    """
    Cutting speed vc.

    Parameters:
        Dm (float): Machined diameter, mm.
        n (float): Spindle speed, rpm.

    Returns:
        float: vc in m/min.
    """
    positive(Dm=Dm, n=n)
    return math.pi * Dm * n / 1000


def spindle_speed(vc, Dm):
    """
    Spindle speed n.

    Parameters:
        vc (float): Cutting speed, m/min.
        Dm (float): Machined diameter, mm.

    Returns:
        float: n in rpm.
    """
    positive(vc=vc, Dm=Dm)
    return vc * 1000 / (math.pi * Dm)


def feed_speed(fn, n):
    """
    Feed speed vf = fn * n.

    Parameters:
        fn (float): Feed per revolution, mm/r.
        n (float): Spindle speed, rpm.

    Returns:
        float: vf in mm/min.
    """
    positive(fn=fn, n=n)
    return fn * n


def metal_removal_rate(vc, ap, fn):
    """
    Metal removal rate Q.

    Parameters:
        vc (float): Cutting speed, m/min.
        ap (float): Depth of cut, mm.
        fn (float): Feed per revolution, mm/r.

    Returns:
        float: Q in cm^3/min.
    """
    positive(vc=vc, ap=ap, fn=fn)
    return vc * ap * fn


def chip_thickness(fn, kr=90.0):
    """
    Chip thickness in turning, hex = fn * sin(kr).

    For a straight edge in turning the chip thickness is constant along
    the edge, so the average and maximum chip thickness are equal
    (hm = hex). Use this value as hm when calculating kc.

    Parameters:
        fn (float): Feed per revolution, mm/r.
        kr (float): Entering angle, degrees.

    Returns:
        float: Chip thickness in mm.
    """
    positive(fn=fn)
    angle("kr", kr)
    return fn * math.sin(math.radians(kr))


def feed_for_chip_thickness(hex, kr=90.0):
    """
    Feed per revolution that gives a target chip thickness: fn = hex / sin(kr).

    Returns:
        float: fn in mm/r.
    """
    positive(hex=hex)
    angle("kr", kr)
    return hex / math.sin(math.radians(kr))


def net_power(vc, ap, fn, kc):
    """
    Net cutting power Pc.

    Parameters:
        vc (float): Cutting speed, m/min.
        ap (float): Depth of cut, mm.
        fn (float): Feed per revolution, mm/r.
        kc (float): Specific cutting force, N/mm^2.

    Returns:
        float: Pc in kW.
    """
    positive(vc=vc, ap=ap, fn=fn, kc=kc)
    return vc * ap * fn * kc / (60 * 10**3)


def cutting_force(ap, fn, kc):
    """
    Main (tangential) cutting force Fc = kc * ap * fn.

    Returns:
        float: Fc in N.
    """
    positive(ap=ap, fn=fn, kc=kc)
    return kc * ap * fn


def machining_time(lm, fn, n):
    """
    Machining time (period of engagement) Tc.

    Parameters:
        lm (float): Machined length, mm.
        fn (float): Feed per revolution, mm/r.
        n (float): Spindle speed, rpm.

    Returns:
        float: Tc in min.
    """
    positive(lm=lm, fn=fn, n=n)
    return lm / (fn * n)


def surface_roughness_rmax(fn, re):
    """
    Theoretical profile depth Rmax from feed and nose radius.

    Rmax = fn^2 / (8 * re), converted from mm to micrometres.

    Parameters:
        fn (float): Feed per revolution, mm/r.
        re (float): Insert nose radius, mm.

    Returns:
        float: Rmax in micrometres.
    """
    positive(fn=fn, re=re)
    return fn**2 / (8 * re) * 1000


def surface_roughness_ra(fn, re):
    """
    Theoretical arithmetic mean roughness Ra for a round nose.

    For a circular nose profile, Ra = fn^2 / (18 * sqrt(3) * re), which is
    about Rmax / 4. Real surfaces are usually rougher than this ideal value.

    Returns:
        float: Ra in micrometres.
    """
    positive(fn=fn, re=re)
    return fn**2 / (18 * math.sqrt(3) * re) * 1000


def feed_for_roughness_ra(Ra, re):
    """
    Largest feed per revolution that keeps theoretical Ra at or below a target.

    Parameters:
        Ra (float): Target Ra, micrometres.
        re (float): Nose radius, mm.

    Returns:
        float: fn in mm/r.
    """
    positive(Ra=Ra, re=re)
    return math.sqrt(Ra / 1000 * 18 * math.sqrt(3) * re)

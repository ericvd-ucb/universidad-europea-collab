"""
Milling formulas (metric).

    vc = pi * Dcap * n / 1000                    m/min
    n  = vc * 1000 / (pi * Dcap)                 rpm
    vf = fz * n * zc                             mm/min
    fz = vf / (n * zc)                           mm
    fn = vf / n                                  mm/r
    Q  = ap * ae * vf / 1000                     cm^3/min
    Pc = ap * ae * vf * kc / (60 * 10^6)         kW
    Mc = Pc * 30 * 10^3 / (pi * n)               Nm
    Tc = lm / vf                                 min

Chip thickness depends on how the cutter engages the workpiece:

    Side milling (cutter edge on one side of the workpiece):
        hm  = 360 * ae * fz * sin(kr) / (pi * Dcap * arccos(1 - 2*ae/Dcap))
        hex = fz * sin(kr) * 2 * sqrt(ae/Dcap - (ae/Dcap)^2)     if ae < Dcap/2
        hex = fz * sin(kr)                                       if ae >= Dcap/2
        small engagement approximation (ae/Dcap < 0.1):
        hm  ~ fz * sin(kr) * sqrt(ae/Dcap)

    Face milling, workpiece centred under the cutter:
        hm  = 180 * ae * fz * sin(kr) / (pi * Dcap * arcsin(ae/Dcap))
        hex = fz * sin(kr)

    (arccos and arcsin are in degrees, as in the handbook.)
"""

import math

from ._validate import positive, angle


def cutting_speed(Dcap, n):
    """
    Cutting speed vc.

    Parameters:
        Dcap (float): Cutting diameter at depth ap, mm.
        n (float): Spindle speed, rpm.

    Returns:
        float: vc in m/min.
    """
    positive(Dcap=Dcap, n=n)
    return math.pi * Dcap * n / 1000


def spindle_speed(vc, Dcap):
    """
    Spindle speed n.

    Parameters:
        vc (float): Cutting speed, m/min.
        Dcap (float): Cutting diameter at depth ap, mm.

    Returns:
        float: n in rpm.
    """
    positive(vc=vc, Dcap=Dcap)
    return vc * 1000 / (math.pi * Dcap)


def table_feed(fz, n, zc):
    """
    Table feed vf.

    Parameters:
        fz (float): Feed per tooth, mm.
        n (float): Spindle speed, rpm.
        zc (int): Number of effective teeth.

    Returns:
        float: vf in mm/min.
    """
    positive(fz=fz, n=n, zc=zc)
    return fz * n * zc


def feed_per_tooth(vf, n, zc):
    """
    Feed per tooth fz.

    Returns:
        float: fz in mm.
    """
    positive(vf=vf, n=n, zc=zc)
    return vf / (n * zc)


def feed_per_revolution(vf, n):
    """
    Feed per revolution fn.

    Returns:
        float: fn in mm/r.
    """
    positive(vf=vf, n=n)
    return vf / n


def metal_removal_rate(ap, ae, vf):
    """
    Metal removal rate Q.

    Parameters:
        ap (float): Depth of cut, mm.
        ae (float): Working engagement (radial width of cut), mm.
        vf (float): Table feed, mm/min.

    Returns:
        float: Q in cm^3/min.
    """
    positive(ap=ap, ae=ae, vf=vf)
    return ap * ae * vf / 1000


def _check_engagement(ae, Dcap):
    positive(ae=ae, Dcap=Dcap)
    if ae > Dcap:
        raise ValueError(f"ae ({ae}) cannot exceed Dcap ({Dcap}).")


def avg_chip_thickness_side(fz, ae, Dcap, kr=90.0):
    """
    Average chip thickness hm for side (shoulder) milling.

    Parameters:
        fz (float): Feed per tooth, mm.
        ae (float): Working engagement, mm.
        Dcap (float): Cutting diameter, mm.
        kr (float): Entering angle, degrees.

    Returns:
        float: hm in mm.
    """
    positive(fz=fz)
    angle("kr", kr)
    _check_engagement(ae, Dcap)
    arccos_deg = math.degrees(math.acos(1 - 2 * ae / Dcap))
    return 360 * ae * fz * math.sin(math.radians(kr)) / (math.pi * Dcap * arccos_deg)


def avg_chip_thickness_side_approx(fz, ae, Dcap, kr=90.0):
    """
    Approximate hm for small engagements (ae/Dcap < 0.1):
    hm ~ fz * sin(kr) * sqrt(ae / Dcap).

    Returns:
        float: hm in mm.
    """
    positive(fz=fz)
    angle("kr", kr)
    _check_engagement(ae, Dcap)
    return fz * math.sin(math.radians(kr)) * math.sqrt(ae / Dcap)


def max_chip_thickness_side(fz, ae, Dcap, kr=90.0):
    """
    Maximum chip thickness hex for side milling.

    Returns:
        float: hex in mm.
    """
    positive(fz=fz)
    angle("kr", kr)
    _check_engagement(ae, Dcap)
    s = math.sin(math.radians(kr))
    if ae >= Dcap / 2:
        return fz * s
    r = ae / Dcap
    return fz * s * 2 * math.sqrt(r - r**2)


def feed_for_max_chip_thickness_side(hex, ae, Dcap, kr=90.0):
    """
    Feed per tooth needed to reach a target hex in side milling
    (chip thinning compensation).

    Returns:
        float: fz in mm.
    """
    positive(hex=hex)
    return hex / max_chip_thickness_side(1.0, ae, Dcap, kr)


def avg_chip_thickness_face_centred(fz, ae, Dcap, kr=90.0):
    """
    Average chip thickness hm for face milling with the workpiece
    centred under the cutter.

    Parameters:
        fz (float): Feed per tooth, mm.
        ae (float): Working engagement (workpiece width), mm.
        Dcap (float): Cutting diameter, mm.
        kr (float): Entering angle, degrees.

    Returns:
        float: hm in mm.
    """
    positive(fz=fz)
    angle("kr", kr)
    _check_engagement(ae, Dcap)
    arcsin_deg = math.degrees(math.asin(ae / Dcap))
    return 180 * ae * fz * math.sin(math.radians(kr)) / (math.pi * Dcap * arcsin_deg)


def max_chip_thickness_face(fz, kr=90.0):
    """
    Maximum chip thickness for face milling with the cutter centre
    inside the workpiece: hex = fz * sin(kr).

    Returns:
        float: hex in mm.
    """
    positive(fz=fz)
    angle("kr", kr)
    return fz * math.sin(math.radians(kr))


def net_power(ap, ae, vf, kc):
    """
    Net power Pc.

    Parameters:
        ap (float): Depth of cut, mm.
        ae (float): Working engagement, mm.
        vf (float): Table feed, mm/min.
        kc (float): Specific cutting force, N/mm^2.

    Returns:
        float: Pc in kW.
    """
    positive(ap=ap, ae=ae, vf=vf, kc=kc)
    return ap * ae * vf * kc / (60 * 10**6)


def torque(Pc, n):
    """
    Spindle torque Mc.

    Parameters:
        Pc (float): Net power, kW.
        n (float): Spindle speed, rpm.

    Returns:
        float: Mc in Nm.
    """
    positive(Pc=Pc, n=n)
    return Pc * 30 * 10**3 / (math.pi * n)


def machining_time(lm, vf):
    """
    Machining time Tc.

    Parameters:
        lm (float): Machined length (including approach and exit), mm.
        vf (float): Table feed, mm/min.

    Returns:
        float: Tc in min.
    """
    positive(lm=lm, vf=vf)
    return lm / vf

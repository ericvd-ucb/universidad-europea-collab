"""
metalcutting: formulas for turning, milling and drilling.

Symbols follow the Sandvik Coromant Metal Cutting Training Handbook
("Formulas and definitions") so students can map code to the handbook:

    vc   cutting speed              m/min
    n    spindle speed              rpm
    Dm   machined diameter          mm   (turning)
    Dcap cutting diameter at ap     mm   (milling)
    Dc   drill diameter             mm   (drilling)
    fn   feed per revolution        mm/r
    fz   feed per tooth             mm
    zc   number of effective teeth  -
    vf   table feed / penetration   mm/min
    ap   depth of cut               mm
    ae   working engagement         mm   (milling)
    kr   entering angle (kappa_r)   degrees
    hex  maximum chip thickness     mm
    hm   average chip thickness     mm
    kc1  specific cutting force for hm = 1 mm   N/mm^2
    mc   chip thickness exponent    -
    kc   specific cutting force     N/mm^2
    Pc   net power                  kW
    Mc   torque                     Nm
    Q    metal removal rate         cm^3/min
    Tc   machining time             min
    lm   machined length            mm
"""

from . import turning, milling, drilling, material, tool_life

__all__ = ["turning", "milling", "drilling", "material", "tool_life"]

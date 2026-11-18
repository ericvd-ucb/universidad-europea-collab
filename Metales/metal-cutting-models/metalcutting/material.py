"""
Specific cutting force and workpiece material data.

The specific cutting force kc is the force in the cutting direction needed
to remove a chip of area 1 mm^2. It rises as the chip gets thinner:

    kc = kc1 * hm**(-mc) * (1 - gamma0 / 100)

kc1 is the value at hm = 1 mm for a neutral (0 degree) rake angle; the last
factor corrects for the actual rake angle gamma0 (degrees).
"""

from ._validate import positive

# Illustrative values for teaching. They are of the right order of magnitude
# for each ISO material group, but you should replace them with the values
# from the handbook's material table (Coromant Material Classification)
# before using them in graded work.
MATERIALS = {
    "P1 unalloyed steel":          {"kc1": 1500, "mc": 0.25},
    "P2 low-alloy steel":          {"kc1": 1700, "mc": 0.25},
    "P3 high-alloy steel":         {"kc1": 2000, "mc": 0.25},
    "M1 austenitic stainless":     {"kc1": 2000, "mc": 0.21},
    "K1 grey cast iron":           {"kc1": 1100, "mc": 0.28},
    "N1 aluminium alloy":          {"kc1": 500,  "mc": 0.25},
    "S1 nickel-based HRSA":        {"kc1": 2800, "mc": 0.25},
    "H1 hardened steel":           {"kc1": 3000, "mc": 0.25},
}


def get(name):
    """Return (kc1, mc) for a material key in MATERIALS."""
    if name not in MATERIALS:
        raise KeyError(f"Unknown material '{name}'. Options: {list(MATERIALS)}")
    m = MATERIALS[name]
    return m["kc1"], m["mc"]


def specific_cutting_force(kc1, hm, mc, gamma0=0.0):
    """
    Specific cutting force kc.

    Parameters:
        kc1 (float): Specific cutting force at hm = 1 mm, N/mm^2.
        hm (float): Average chip thickness, mm.
        mc (float): Chip thickness exponent (typically 0.2 to 0.3).
        gamma0 (float): Rake angle in degrees. Positive rake lowers kc.

    Returns:
        float: kc in N/mm^2.
    """
    positive(kc1=kc1, hm=hm, mc=mc)
    return kc1 * hm ** (-mc) * (1 - gamma0 / 100)
